#!/usr/bin/env python3
"""Genera el calendario de frutas desde su maestro; no toca recetas ni PDF."""
import argparse
import json
import re
from datetime import datetime
from html import escape
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

ROOT = Path(__file__).resolve().parents[1]
MONTHS = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']


def period(values):
    """Agrupa intervalos continuos, incluidos los que cruzan diciembre."""
    values = set(values)
    if not values:
        return '—'
    if len(values) == 12:
        return 'todo el año'
    starts = sorted(n for n in values if (n - 2) % 12 + 1 not in values)
    parts = []
    for start in starts:
        end = start
        while end % 12 + 1 in values:
            end = end % 12 + 1
        a, b = MONTHS[start - 1].lower(), MONTHS[end - 1].lower()
        parts.append(a if start == end else a + '–' + b)
    return ' y '.join(parts)


def month_content(data, n):
    fresh = [f for f in data['frutas'] if n in f['galicia']]
    stored = [f for f in data['frutas'] if n in f.get('conservacion_galicia', [])]
    national = [f for f in data['frutas'] if n in f['espana'] and f not in fresh]
    links = lambda fs: ' · '.join(f'<a href="#fruta-{i}">{escape(f["nombre"])}</a>' for f in fs for i in [data['frutas'].index(f)])
    local = links(fresh) if fresh else 'Sin cosecha local destacada en esta selección.'
    content = f'<div class="choices"><div><h3>Prioriza Galicia</h3><p>{local}</p>'
    if stored:
        content += f'<p class="stored"><span class="tag">De conservación</span> {links(stored)} de la última cosecha, si quedan existencias y se confirma el origen gallego.</p>'
    content += '</div><div><h3>También de temporada en España</h3><p>' + links(national) + '</p></div></div>'
    return content


def render(data, month):
    # Hereda la base visual ya aprobada del calendario de verduras.
    vegetable = (ROOT / 'calendario-verduras-temporada.html').read_text()
    css = re.search(r'<style>(.*?)</style>', vegetable, re.S).group(1)
    css += '.now{background:var(--suave);border-radius:13px;padding:24px;margin:0 0 30px}.now h2{font-size:1.4rem}.month-name{color:#64756a;margin:3px 0 18px}.choices{display:grid;grid-template-columns:1fr 1fr;gap:24px}.choices h3{font-size:1rem;margin:0 0 8px;color:var(--verde)}.choices p{margin:0}.choices a{text-decoration:none;border-bottom:1px dotted #9db8a5}.stored{margin-top:14px!important;font-size:.9rem;color:#52665a}.tag{display:inline-block;font-size:.75rem;border:1px solid #b8cdbb;border-radius:20px;padding:1px 7px;margin-right:3px}.annual{margin-top:34px}.annual h2{margin-bottom:10px}.annual table{width:100%;border-collapse:collapse;text-align:left;font-size:.9rem}.annual th,.annual td{padding:12px 10px;border-bottom:1px solid var(--borde);vertical-align:top}.annual thead{background:var(--suave);color:var(--verde)}.annual th[scope=row]{font-weight:600}.detail{margin-top:26px}.detail summary{cursor:pointer;color:var(--verde);font-weight:600;padding:12px 0}.detail li{margin-bottom:12px}.detail p{color:#64756a;font-size:.9rem}.source-list{padding-left:22px}.source-list li{margin:12px 0}.source-list small{display:block;color:#64756a}@media(max-width:650px){.choices{grid-template-columns:1fr;gap:20px}.now{padding:20px 18px}.annual th,.annual td{padding:10px 6px;font-size:.8rem}.annual th:first-child{width:28%}}'
    schema = {'@context': 'https://schema.org', '@type': 'WebPage', 'name': data['titulo'], 'inLanguage': 'es', 'dateModified': data['fecha_actualizacion'], 'url': 'https://fucolin.github.io/recetario/calendario-frutas-temporada.html', 'citation': [{'@type': 'CreativeWork', 'name': s['nombre'], 'url': s['url']} for s in data['fuentes']]}
    out = ['<!doctype html><html lang="es"><head><meta name="robots" content="noindex, noimageindex"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + escape(data['titulo']) + ' · Mi recetario</title><meta name="description" content="Frutas de temporada para comprar en España, con prioridad a cosechas gallegas documentadas y distinción de fruta conservada."><style>' + css + '</style><script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + '</script></head><body><main>', '<nav class="back"><a href="index.html">← Índice del recetario</a></nav><h1>' + data['titulo'] + '</h1><p class="intro">' + escape(data['criterio']) + '</p><p class="source">Una guía para elegir en la frutería · <a href="#como-usarlo">Cómo usarla y fuentes</a></p>']
    out.append('<nav class="months" aria-label="Meses del calendario">' + ''.join(f'<a href="#{name.lower()}" data-month-link="{n}">{name}</a>' for n, name in enumerate(MONTHS, 1)) + '</nav>')
    out.append('<section class="now" aria-labelledby="este-mes"><h2 id="este-mes">Este mes…</h2><p class="month-name" id="nombre-mes">' + MONTHS[month - 1] + '</p><div id="contenido-mes">' + month_content(data, month) + '</div></section>')
    for n, name in enumerate(MONTHS, 1):
        out.append(f'<section class="month" id="{name.lower()}" data-month="{n}" aria-labelledby="titulo-{n}"><header><h2 id="titulo-{n}">{name}</h2><span class="current" hidden>Este mes</span></header>' + month_content(data, n) + '</section>')
    out.append('<section class="annual" aria-labelledby="resumen"><h2 id="resumen">De un vistazo</h2><p class="note">España: ventana orientativa de compra, incluidos inicios y finales. Galicia: selección de cosechas documentadas. Un guion no significa que no se cultive allí.</p><table><thead><tr><th scope="col">Fruta</th><th scope="col">España</th><th scope="col">Cosecha en Galicia</th></tr></thead><tbody>')
    for i, fruit in enumerate(data['frutas']):
        galicia = period(fruit['galicia'])
        if fruit['nombre'] == 'Pera':
            galicia += ' (Urraca)'
        out.append(f'<tr id="fruta-{i}"><th scope="row">{escape(fruit["nombre"])}</th><td>{period(fruit["espana"])}</td><td>{galicia}</td></tr>')
    out.append('</tbody></table></section><details class="detail"><summary>Matices de cada fruta</summary><ul>')
    sources = {s['id']: s for s in data['fuentes']}
    for fruit in data['frutas']:
        refs = ' · '.join(f'<a href="#fuente-{key}">{escape(sources[key]["nombre"].split(" · ")[0])}</a>' for key in fruit['fuentes'])
        out.append('<li><strong>' + escape(fruit['nombre']) + '.</strong> ' + escape(fruit['nota']) + ' <span class="source">' + refs + '</span></li>')
    out.append('</ul></details><section class="explanation" id="como-usarlo"><h2>Cómo usar este calendario</h2>')
    body = (ROOT / 'calendario-frutas-temporada.md').read_text().split('---', 2)[2]
    out.append('<ul>' + ''.join('<li>' + escape(line[2:]) + '</li>' for line in body.splitlines() if line.startswith('- ')) + '</ul>')
    out.append('<p class="note">La base nacional es de 2017 y se complementa con fuentes de productores. No se presenta como una previsión de la campaña actual. Esta selección gallega inicial no cubre todas las frutas ni todas las comarcas.</p><h2>Fuentes</h2><ul class="source-list">')
    for source in data['fuentes']:
        out.append(f'<li id="fuente-{source["id"]}"><a href="{escape(source["url"], quote=True)}">{escape(source["nombre"])}</a><small>{escape(source["uso"])}</small></li>')
    out.append('</ul></section><aside class="tomato-link"><a href="calendario-verduras-temporada.html"><strong>Calendario de verduras de temporada →</strong><span>La otra mitad de la compra de temporada.</span></a></aside><footer class="site-footer">Recetario personal · <a href="index.html">Volver al índice</a> · <a href="calendario-frutas-temporada.md">Archivo maestro</a></footer></main>')
    # Reutiliza el contenido estático: sin peticiones externas ni fechas fijas.
    out.append('''<script>(()=>{const month=Number(new Intl.DateTimeFormat('es-ES',{month:'numeric',timeZone:'Europe/Madrid'}).format(new Date()));const section=document.querySelector('[data-month="'+month+'"]');const link=document.querySelector('[data-month-link="'+month+'"]');if(section){section.classList.add('is-current');section.querySelector('.current').hidden=false;document.getElementById('nombre-mes').textContent=section.querySelector('h2').textContent;document.getElementById('contenido-mes').replaceChildren(section.querySelector('.choices').cloneNode(true))}if(link)link.setAttribute('aria-current','date')})();</script></body></html>''')
    return '\n'.join(out) + '\n'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--preview', help='Nombre único de la copia de revisión, sin publicarla.')
    args = parser.parse_args()
    data = yaml.safe_load((ROOT / 'calendario-frutas-temporada.md').read_text().split('---', 2)[1])
    for fruit in data['frutas']:
        for key in ['espana', 'galicia', 'conservacion_galicia']:
            values = fruit.get(key, [])
            assert len(values) == len(set(values)) and all(1 <= n <= 12 for n in values)
        assert all(key in {s['id'] for s in data['fuentes']} for key in fruit['fuentes'])
    month = datetime.now(ZoneInfo('Europe/Madrid')).month
    html = render(data, month)
    (ROOT / 'datos/calendario-frutas-temporada.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    (ROOT / 'calendario-frutas-temporada.html').write_text(html)
    if args.preview:
        target = ROOT / 'build/previews' / args.preview
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html.replace('<head>', '<head><base href="../../">', 1))
        print(target)
    print(f'Calendario generado: {len(data["frutas"])} frutas, 12 meses, sin PDF.')


if __name__ == '__main__':
    main()
