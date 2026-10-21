#!/usr/bin/env python3
"""Genera la ficha con el original de Marisa a partir de su maestro YAML."""
import json
import re
from html import escape as e
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://fucolin.github.io/recetario/'

def main():
    master = ROOT / 'crema-aprovechamiento-marisa.md'
    data = yaml.safe_load(master.read_text().split('---', 2)[1])
    ident = data['id']
    original = data['original_marisa']
    assert (ROOT / original['imagen']).is_file()
    (ROOT / f'{ident}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    schema = {
        '@context': 'https://schema.org', '@type': 'Recipe',
        'name': data['titulo'], 'description': data['subtitulo'],
        'author': {'@type': 'Person', 'name': data['autor']},
        'recipeCategory': data['categoria_menu'], 'recipeYield': '4 raciones aproximadamente',
        'totalTime': 'PT50M', 'keywords': ', '.join(data['etiquetas']),
        'recipeIngredient': data['pdf_ingredientes'],
        'recipeInstructions': [{'@type': 'HowToStep', 'position': p['orden'], 'name': p['titulo'], 'text': p['instrucciones']} for p in data['pasos']],
        'image': data['image'], 'url': BASE + ident + '.html',
        'dateModified': data['fecha_actualizacion'],
        'isBasedOn': {'@type': 'CreativeWork', 'name': original['titulo_manuscrito'], 'author': {'@type': 'Person', 'name': data['autor']}, 'image': BASE + original['imagen']},
    }
    (ROOT / f'{ident}.schema.json').write_text(json.dumps(schema, ensure_ascii=False, indent=2) + '\n')
    css = re.search(r'<style>(.*?)</style>', (ROOT / 'pollo-satisfryer.html').read_text(), re.S)[1]
    css += '.action-icon{width:1em;height:1em;vertical-align:-.1em;margin-right:.4em;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}.original-marisa{margin-top:42px}.original-photo{position:relative;display:block}.original-photo img{display:block;width:100%;height:auto;border-radius:10px}.zoom-hint{position:absolute;right:12px;bottom:12px;background:white;color:#245d42;border:1px solid #9db8a5;border-radius:50%;padding:4px 12px;font-size:1.4rem}.original-photo:focus-visible{outline:3px solid #245d42;outline-offset:4px}.original-note{background:#f3f6f1;padding:14px 18px;border-radius:8px}.example{border-left:3px solid #9db8a5;padding-left:18px} @media print{.original-marisa{display:none}}'
    h = ['<!doctype html><html lang="es"><head><link rel="icon" type="image/x-icon" href="/recetario/images/iconos/favicon-v1.ico"><link rel="icon" type="image/png" sizes="32x32" href="/recetario/images/iconos/favicon-32-v1.png"><link rel="icon" type="image/png" sizes="16x16" href="/recetario/images/iconos/favicon-16-v1.png"><link rel="apple-touch-icon" sizes="180x180" href="/recetario/images/iconos/apple-touch-icon-v1.png"><link rel="manifest" href="/recetario/site.webmanifest"><meta name="robots" content="noindex, noimageindex"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>{e(data["titulo"])} · Casa Marisa</title><meta name="description" content="{e(data["subtitulo"],quote=True)}">',
         '<style>' + css + '</style><script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False).replace('</', '<\\/') + '</script></head><body><main>',
         '<nav><a href="index.html">← Índice del recetario</a></nav>',
         f'<h1>{e(data["encabezado"]["titulo"])}</h1><p class="meta">{e(data["encabezado"]["detalle"])}</p>',
         '<p><span role="img" aria-label="Receta de Marisa">💚</span> La crema que Marisa prepara con las verduras que tiene por casa. Con puerro como base y una mezcla que cambia cada vez.</p>',
         f'<figure class="hero"><img src="{e(data["image"].removeprefix(BASE),quote=True)}" alt="{e(data["image_alt"],quote=True)}" width="1672" height="941"><figcaption>Ilustración generada con IA.</figcaption></figure>',
         f'<p class="actions"><a class="category-link" href="categorias/pures.html"><svg class="action-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="3" width="7" height="7" rx="1"></rect><rect x="14" y="3" width="7" height="7" rx="1"></rect><rect x="3" y="14" width="7" height="7" rx="1"></rect><rect x="14" y="14" width="7" height="7" rx="1"></rect></svg>Más de Purés</a><a class="pdf-link" href="{ident}.pdf"><svg class="action-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 9V3h12v6M6 18H3V9h18v9h-3M6 14h12v7H6zM17 12h1"></path></svg>PDF para imprimir</a></p>',
         '<h2>Ingredientes</h2><ul class="ingredients">']
    items = ['200 g de puerro limpio', '40 g de aceite de oliva, para el sofrito', '500-600 g de verduras variadas preparadas, además del puerro', '500-600 g de agua o caldo de pollo', 'Sal al gusto; probar antes si el caldo ya lleva sal']
    h += ['<li>' + e(x) + '</li>' for x in items]
    h += ['</ul><h2>Preparación en Thermomix</h2><ol>']
    for p in data['pasos']:
        h += [f'<li><strong>{e(p["titulo"])} · {e(p["duracion_texto"])}</strong><p>{e(p["instrucciones"])}</p></li>']
    h += ['</ol><h2>Claves</h2><p>' + e(data['claves']).replace('Una mezcla de Marisa', '<strong>Una mezcla de Marisa</strong>') + '</p><p>' + e(data['tiempo_nota']) + '</p>',
          '<section class="original-marisa" aria-labelledby="original-title"><h2 id="original-title">' + e(original['titulo']) + '</h2>',
          f'<a class="original-photo" href="{original["imagen"]}" target="_blank" rel="noopener" aria-label="Ampliar la receta manuscrita de Marisa"><img src="{original["imagen"]}" alt="{e(original["imagen_alt"],quote=True)}" loading="lazy"><span class="zoom-hint" aria-hidden="true">+</span></a>',
          '<p class="meta">Manuscrito de Marisa.</p>',
          '<h3>Transcripción del manuscrito</h3><p><strong>' + e(original['titulo_manuscrito']) + '</strong></p><ul>']
    h += ['<li>' + e(x) + '</li>' for x in original['ingredientes']]
    h += ['</ul><ol>'] + ['<li>' + e(x) + '</li>' for x in original['pasos']]
    h += ['</ol><p class="original-note">' + e(original['nota_transcripcion']) + '</p></section>',
          f'<footer>Receta de Marisa · <a href="{ident}.md">Archivo maestro</a></footer></main></body></html>']
    (ROOT / f'{ident}.html').write_text('\n'.join(h) + '\n')
    body = '\n# ' + data['titulo'] + '\n\n' + data['subtitulo'] + '\n\n## Ingredientes\n\n'
    body = body.replace('\n\n## Ingredientes', '\n\n![' + data['image_alt'] + '](' + data['image'].removeprefix(BASE) + ')\n\nIlustración generada con IA.\n\n## Ingredientes', 1)
    body += '\n'.join('- ' + x for x in items) + '\n\n## Preparación\n\n'
    body += '\n'.join(f'{p["orden"]}. **{p["titulo"]} · {p["duracion_texto"]}.** {p["instrucciones"]}' for p in data['pasos'])
    body += '\n\n## Claves\n\n' + data['claves'].replace('Una mezcla de Marisa', '**Una mezcla de Marisa**') + '\n\n## ' + original['titulo'] + '\n\n'
    body += f'![{original["imagen_alt"]}]({original["imagen"]})\n\n### Transcripción del manuscrito\n\n'
    body += '**' + original['titulo_manuscrito'] + '**\n\n' + '\n'.join('- ' + x for x in original['ingredientes']) + '\n\n'
    body += '\n'.join(f'{i}. {x}' for i, x in enumerate(original['pasos'], 1)) + '\n\n' + original['nota_transcripcion'] + '\n'
    master.write_text('---' + master.read_text().split('---', 2)[1] + '---\n' + body)
    print('Ficha de Marisa generada; original conservado sin modificaciones.')

if __name__ == '__main__':
    main()
