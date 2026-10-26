#!/usr/bin/env python3
"""Genera una instantánea única desde un commit público, sin red ni datos privados.

python tools/sincronizar_recetario.py --source /ruta/recetario --commit SHA \
  --output app/recipe-catalog.json --report docs/sincronizacion-recetario.json
Requiere PyYAML para cotejar los maestros con sus exportaciones JSON.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unicodedata

import yaml

ROOT = Path(__file__).resolve().parents[1]
TYPES = {'receta', 'preparacion', 'combinacion'}
SLUG = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')


def require(ok, message):
    if not ok:
        raise ValueError(message)


def text(value, field):
    require(isinstance(value, str) and bool(value.strip()) and value == value.strip()
            and not any(ord(c) < 32 for c in value), 'Texto inválido: ' + field)
    return value


def number(value):
    require(not isinstance(value, bool) and isinstance(value, (int, float))
            and math.isfinite(value) and value >= 0, 'Cantidad numérica inválida')
    return str(value).replace('.', ',')


def amount(i):
    if i.get('cantidad') is not None:
        q = text(i['cantidad'], 'cantidad textual') if isinstance(i['cantidad'], str) else number(i['cantidad'])
    elif i.get('cantidad_min') is not None:
        q = number(i['cantidad_min'])
        if i.get('cantidad_max') is not None:
            require(i['cantidad_max'] >= i['cantidad_min'], 'Intervalo invertido')
            if i['cantidad_max'] != i['cantidad_min']:
                q += '–' + number(i['cantidad_max'])
    else:
        require(i.get('cantidad_max') is None, 'Máximo sin mínimo')
        q = ''
    return ' '.join(v for v in [q, i.get('unidad') if q else ''] if v)


def ingredient(i, index):
    text(i.get('nombre'), 'ingrediente')
    norm = ''.join(c for c in unicodedata.normalize('NFD', i['nombre'].lower())
                   if unicodedata.category(c) != 'Mn')
    a = i.get('alternativa')
    if isinstance(a, dict):
        alt = ' '.join(v for v in [amount(a), a.get('nombre'),
                      '(' + a['nota'] + ')' if a.get('nota') else ''] if v)
    elif isinstance(a, str):
        alt = a
    else:
        require(a is None, 'Alternativa de tipo desconocido')
        alt = '; '.join(i.get('alternativas', []))
    weight = ''
    if i.get('peso_min_g') is not None:
        weight = 'Peso: ' + number(i['peso_min_g']) + '–' + number(i['peso_max_g']) + ' g'
    elif i.get('peso_aprox_g', i.get('peso_g')) is not None:
        weight = 'Peso aprox.: ' + number(i.get('peso_aprox_g', i.get('peso_g'))) + ' g'
    note = ' · '.join(x for x in [i.get('nota'), i.get('uso'), weight,
          'Equivale a ' + number(i['equivalencia_ml']) + ' ml' if i.get('equivalencia_ml') else ''] if x)
    return dict(index=index, name=i['nombre'], quantity=amount(i), note=note,
                alternative=alt, pantry=bool(re.search(
                    r'\b(aceite|sal|pimienta|pimenton|comino|oregano|tomillo|laurel|curcuma|curry|canela|romero|vinagre|agua)\b', norm)),
                optional=bool(i.get('opcional')) or 'opcional' in i.get('nota', '').lower(),
                group=i.get('grupo', ''), source=i)


def generate(source, commit):
    require(bool(re.fullmatch('[0-9a-f]{40}', commit)), 'Usa un SHA completo')

    def git(*args):
        return subprocess.check_output(['git', '-C', str(source), *args])

    require(git('rev-parse', commit + '^{commit}').decode().strip() == commit, 'Commit desconocido')
    files = set(git('ls-tree', '-r', '--name-only', commit).decode().splitlines())

    def read(name):
        require(name in files, 'Falta archivo: ' + name)
        return git('show', commit + ':' + name).decode()

    rows = []
    ids = set()
    for name in sorted(files):
        if '/' in name or not name.endswith('.json'):
            continue
        d = json.loads(read(name))
        if not isinstance(d, dict) or d.get('tipo_ficha') not in TYPES:
            continue
        ident = text(d.get('id'), 'id')
        require(bool(SLUG.fullmatch(ident)) and name == ident + '.json', 'ID/ruta no coinciden')
        require(ident not in ids, 'ID duplicado: ' + ident)
        require(d.get('esquema') == 'recetario-1.0', 'Esquema desconocido: ' + ident)
        master = read(ident + '.md').split('---', 2)
        require(len(master) == 3 and not master[0].strip(), 'Maestro sin YAML: ' + ident)
        y = yaml.safe_load(master[1])
        for field in ['id', 'titulo', 'categoria_menu', 'tipo_ficha', 'raciones', 'ingredientes']:
            require(y.get(field) == d.get(field), 'Maestro/JSON difieren: ' + ident + ' · ' + field)
        html = read(ident + '.html')
        require('<html' in html.lower() and 'http-equiv="refresh"' not in html.lower(),
                'Ficha ausente o redirección: ' + ident)
        portions = d['raciones']
        lo, hi = portions['min'], portions['max']
        require(lo > 0 and hi >= lo, 'Raciones inválidas: ' + ident)
        servings = number(lo) + ('–' + number(hi) if hi != lo else '')
        servings += ' ración' if lo == hi == 1 else ' raciones'
        if portions.get('nota'):
            servings += ' ' + portions['nota']
        require(isinstance(d['ingredientes'], list) and d['ingredientes'], 'Ficha sin ingredientes: ' + ident)
        rows.append(dict(id=ident, title=text(d.get('titulo'), 'título'),
            category=text(d.get('categoria_menu'), 'categoría'), type=d['tipo_ficha'],
            available=True, url=ident + '.html', portions=portions, servings=servings,
            ingredients=[ingredient(i, n) for n, i in enumerate(d['ingredientes'])]))
        ids.add(ident)
    state = json.loads(read('datos/estado-fichas.json'))
    for p in state['proximas']:
        ident = text(p.get('id'), 'id próximo')
        require(bool(SLUG.fullmatch(ident)) and ident not in ids, 'Próxima duplicada o ya publicada: ' + ident)
        require(ident + '.json' not in files and ident + '.html' not in files,
                'Próxima con archivos de ficha: ' + ident)
        rows.append(dict(id=ident, title=text(p.get('titulo'), 'título próximo'),
            category=text(p.get('categoria_menu'), 'categoría próxima'), type='prevista',
            available=False, url=None, portions=None, servings='', ingredients=[]))
        ids.add(ident)
    require(rows and any(r['available'] for r in rows), 'Catálogo vacío')
    require(set(state['nuevas']) <= {r['id'] for r in rows if r['available']}, 'Novedad sin ficha')
    rows.sort(key=lambda r: r['title'].casefold())
    version = hashlib.sha256(json.dumps(rows, ensure_ascii=False, sort_keys=True,
                                       separators=(',', ':'), allow_nan=False).encode()).hexdigest()
    return dict(schemaVersion=1, sourceRepository='fucolin/recetario', sourceCommit=commit,
                sourceCommitTime=int(git('show', '-s', '--format=%ct', commit).decode()),
                contentVersion=version, recipes=rows)


def changes(previous, current, allow_removed=False):
    before = {r['id']: r for r in previous['recipes']}
    after = {r['id']: r for r in current['recipes']}
    missing = sorted(before.keys() - after.keys())
    require(not missing or allow_removed, 'IDs anteriores desaparecidos; revisar antes de sustituir: ' + ', '.join(missing))
    result = dict(sourceCommit=current['sourceCommit'], contentVersion=current['contentVersion'],
                  available=sum(r['available'] for r in after.values()),
                  upcoming=sum(not r['available'] for r in after.values()), added=[], removed=missing, updated=[])
    for ident, r in after.items():
        if ident not in before:
            result['added'].append(ident)
        else:
            def comparable(row, key):
                value = row.get(key)
                if key == 'ingredients':
                    legacy = any('source' not in i for i in before[ident].get('ingredients', []))
                    return [{k: v for k, v in i.items() if not (legacy and k == 'source')}
                            for i in value or []]
                if key == 'servings':
                    return value or ''
                return value
            fields = [k for k in ['title', 'category', 'type', 'available', 'url', 'servings', 'ingredients']
                      if comparable(before[ident], k) != comparable(r, k)]
            if fields:
                result['updated'].append(dict(id=ident, fields=fields))
    return result


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as out:
            out.write(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--commit', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--previous', type=Path)
    parser.add_argument('--allow-removed', action='store_true')
    args = parser.parse_args()
    try:
        catalog = generate(args.source, args.commit)
        prior_path = args.previous or args.output
        if prior_path.exists():
            prior = json.loads(prior_path.read_text())
        else:
            prior = {'recipes': []}
        report = changes(prior, catalog, args.allow_removed)
        require(args.output.resolve() != args.report.resolve(), 'Informe y catálogo necesitan rutas diferentes')
        write_json(args.report, report)
        write_json(args.output, catalog)
        print(json.dumps({k: v for k, v in report.items() if k not in ['updated']}, ensure_ascii=False))
    except (ValueError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
