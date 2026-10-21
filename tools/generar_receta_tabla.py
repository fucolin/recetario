#!/usr/bin/env python3
"""Genera recetas con tabla en escritorio y pasos en móvil desde Markdown/YAML."""
import argparse
from html import escape as e
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://fucolin.github.io/recetario/'
FLAME = '<span class="flame" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="18"><path fill="#b66b36" d="M13 2c1 5-4 6-3 10-2-1-3-2-3-4-3 3-4 6-3 9 1 4 4 6 8 6 5 0 8-3 8-7 0-5-4-8-7-14Z"/><path fill="#f6d4a4" d="M12 12c0 3-3 4-3 6 0 2 1 3 3 3s3-1 3-3c0-2-2-4-3-6Z"/></svg></span>'
GRID = '<svg class="action-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="3" width="7" height="7" rx="1"></rect><rect x="14" y="3" width="7" height="7" rx="1"></rect><rect x="3" y="14" width="7" height="7" rx="1"></rect><rect x="14" y="14" width="7" height="7" rx="1"></rect></svg>'
PRINTER = '<svg class="action-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 9V3h12v6M6 18H3V9h18v9h-3M6 14h12v7H6zM17 12h1"></path></svg>'


def generar(master):
    original_text = master.read_text()
    data = yaml.safe_load(original_text.split('---', 2)[1])
    ident = data['id']
    assert data['preparacion_formato'] == 'tabla-adaptable'
    original = data['original_marisa']
    assert original['tipo'] == 'oral'
    schema = {
        '@context': 'https://schema.org', '@type': 'Recipe',
        'name': data['titulo'], 'description': data['subtitulo'],
        'author': {'@type': 'Person', 'name': data['autor']},
        'recipeCategory': data['categoria_menu'],
        'recipeYield': f'{data["raciones"]["min"]} raciones',
        'totalTime': f'PT{data["tiempo_total_min"]["max"]}M',
        'keywords': ', '.join(data['etiquetas']),
        'recipeIngredient': data['pdf_ingredientes'],
        'recipeInstructions': [{'@type': 'HowToStep', 'position': p['orden'], 'name': p['titulo'], 'text': p['instrucciones']} for p in data['pasos']],
        'image': data['image'], 'url': BASE + ident + '.html',
        'dateModified': data['fecha_actualizacion'],
        'isBasedOn': {'@type': 'CreativeWork', 'name': original['titulo'], 'author': {'@type': 'Person', 'name': data['autor']}, 'description': original['procedencia']},
    }
    (ROOT / (ident + '.json')).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    (ROOT / (ident + '.schema.json')).write_text(json.dumps(schema, ensure_ascii=False, indent=2) + '\n')
    css = (ROOT / 'tools/receta_tabla.css').read_text()
    css += '.oral-original{margin-top:32px}.oral-original summary{color:#245d42;font-weight:650;cursor:pointer}.oral-original[open] summary{margin-bottom:16px}.oral-original ul,.oral-original ol{padding-left:22px}.oral-original li{margin-bottom:8px}'
    h = ['<!doctype html><html lang="es"><head><link rel="icon" type="image/x-icon" href="/recetario/images/iconos/favicon-v1.ico"><link rel="icon" type="image/png" sizes="32x32" href="/recetario/images/iconos/favicon-32-v1.png"><link rel="icon" type="image/png" sizes="16x16" href="/recetario/images/iconos/favicon-16-v1.png"><link rel="apple-touch-icon" sizes="180x180" href="/recetario/images/iconos/apple-touch-icon-v1.png"><link rel="manifest" href="/recetario/site.webmanifest"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex, noimageindex">',
         f'<title>{e(data["titulo"])} · Casa Marisa</title><meta name="description" content="{e(data["subtitulo"], quote=True)}">',
         f'<link rel="canonical" href="{BASE}{ident}.html"><meta property="og:type" content="article"><meta property="og:title" content="{e(data["titulo"],quote=True)}"><meta property="og:description" content="{e(data["subtitulo"],quote=True)}"><meta property="og:url" content="{BASE}{ident}.html"><meta property="og:image" content="{e(data["image"],quote=True)}"><meta property="og:image:alt" content="{e(data["image_alt"],quote=True)}">',
         '<style>' + css + '</style><script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False).replace('</', '<\\/') + '</script></head><body><main>',
         '<nav><a href="index.html">← Índice del recetario</a></nav>',
         f'<h1>{e(data["titulo"])}</h1><p class="meta">{e(data["encabezado"]["detalle"])}</p>',
         '<p><span role="img" aria-label="Receta de Marisa">💚</span> ' + e(data['presentacion_marisa']) + '</p>',
         f'<figure class="hero"><img src="{e(data["image"].removeprefix(BASE),quote=True)}" alt="{e(data["image_alt"],quote=True)}" width="{data["image_width"]}" height="{data["image_height"]}"><figcaption>Ilustración generada con IA.</figcaption></figure>',
         f'<p class="actions"><a class="category-link" href="categorias/vegetales.html">{GRID}Más de Vegetales</a><a class="pdf-link" href="{ident}.pdf">{PRINTER}PDF para imprimir</a></p>',
         '<h2>Ingredientes</h2><ul class="ingredients">' + ''.join('<li>' + e(x) + '</li>' for x in data['pdf_ingredientes']) + '</ul>',
         '<h2 id="preparacion">Preparación</h2><table class="method" aria-labelledby="preparacion"><colgroup><col><col><col></colgroup><thead><tr><th scope="col">Qué haces</th><th scope="col">Fuego y tiempo</th><th scope="col">El punto</th></tr></thead>']
    for p in data['pasos']:
        note = '<span class="detail">' + e(p['nota']) + '</span>' if p.get('nota') else ''
        heat = FLAME + '<span class="heat">' + e(p['fuego']) + '</span>' if p['fuego'] != 'Sin fuego' else ''
        h.append(f'<tbody><tr class="phase"><th colspan="3" scope="rowgroup"><span class="number">{p["orden"]}. </span>{e(p["titulo"])}</th></tr><tr><td class="instruction">{e(p["accion"])}</td><td class="heat-time">{heat}<span class="duration">{e(p["duracion_texto"])}</span>{note}</td><td class="doneness"><em class="until">Hasta que… </em><span class="point-desktop">{e(p["punto"])}</span><span class="point-mobile">{e(p["punto_hasta"])}</span></td></tr></tbody>')
    h.append('</table><h2>Claves</h2>')
    for key in data['claves_detalle']:
        h.append('<p class="key"><strong>' + e(key['titulo']) + '.</strong> ' + e(key['texto']) + '</p>')
    h.append('<h2>Opciones</h2>')
    for option in data['opciones']:
        h.append('<p><strong>' + e(option['titulo']) + ':</strong> ' + e(option['texto']) + '</p>')
    h.append('<details class="oral-original"><summary>' + e(original['titulo']) + '</summary><ul>')
    h.extend('<li>' + e(x) + '</li>' for x in original['ingredientes'])
    h.append('</ul><ol>')
    h.extend('<li>' + e(x) + '</li>' for x in original['pasos'])
    h.append('</ol>')
    h.extend('<p>' + e(x) + '</p>' for x in original['opciones'])
    h.append(f'</details><footer>Receta de Marisa · <a href="{ident}.md">Archivo maestro</a></footer></main></body></html>')
    (ROOT / (ident + '.html')).write_text('\n'.join(h) + '\n')
    body = '\n# ' + data['titulo'] + '\n\n' + data['encabezado']['detalle'] + '\n\n💚 ' + data['presentacion_marisa']
    body += '\n\n![' + data['image_alt'] + '](' + data['image'].removeprefix(BASE) + ')\n\nIlustración generada con IA.\n\n## Ingredientes\n\n'
    body += '\n'.join('- ' + x for x in data['pdf_ingredientes']) + '\n\n## Preparación\n\n| Fase y acción | Fuego y tiempo | El punto |\n| --- | --- | --- |\n'
    body += '\n'.join(f'| **{p["orden"]}. {p["titulo"]}**. {p["accion"]} | ' + (p['fuego'] + ' · ' if p['fuego'] != 'Sin fuego' else '') + f'{p["duracion_texto"]}. {p["nota"]} | {p["punto"]} |' for p in data['pasos'])
    body += '\n\n## Claves\n\n' + '\n\n'.join('**' + x['titulo'] + '.** ' + x['texto'] for x in data['claves_detalle'])
    body += '\n\n## Opciones\n\n' + '\n\n'.join('**' + x['titulo'] + ':** ' + x['texto'] for x in data['opciones'])
    body += '\n\n## ' + original['titulo'] + '\n\n' + original['procedencia'] + '\n\n' + '\n'.join('- ' + x for x in original['ingredientes']) + '\n\n'
    body += '\n'.join(f'{i}. {x}' for i, x in enumerate(original['pasos'], 1)) + '\n\n' + '\n\n'.join(original['opciones']) + '\n'
    master.write_text('---' + original_text.split('---', 2)[1] + '---\n' + body)
    print(ident + ': HTML, JSON, Schema.org y Markdown sincronizados.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('maestro', type=Path)
    args = parser.parse_args()
    generar(args.maestro)
