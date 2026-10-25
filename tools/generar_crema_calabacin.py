#!/usr/bin/env python3
"""Reconstruye la ficha de crema de calabacín desde el maestro YAML."""
from pathlib import Path
from html import escape as e
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://fucolin.github.io/recetario/'


def main():
    master = ROOT / 'crema-calabacin.md'
    text = master.read_text()
    d = yaml.safe_load(text.split('---', 2)[1])
    ident = d['id']
    schema = {'@context':'https://schema.org', '@type':'Recipe', 'name':d['titulo'], 'description':d['subtitulo'], 'author':{'@type':'Person','name':d['autor']}, 'recipeCategory':d['categoria_menu'], 'recipeYield':'2 raciones', 'totalTime':'PT30M', 'recipeIngredient':d['pdf_ingredientes'], 'recipeInstructions':[{'@type':'HowToStep', 'position':p['orden'], 'name':p['titulo'], 'text':p['instrucciones']} for p in d['pasos']], 'keywords':', '.join(d['etiquetas']), 'image':d['image'], 'url':BASE+ident+'.html', 'dateModified':d['fecha_actualizacion'], 'isBasedOn':{'@type':'CreativeWork', 'name':d['fuente']['titulo_original'], 'author':{'@type':'Person','name':d['autor']}, 'image':BASE+d['original_marisa']['imagen']}}
    (ROOT/(ident+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    (ROOT/(ident+'.schema.json')).write_text(json.dumps(schema,ensure_ascii=False,indent=2)+'\n')
    original = d['original_marisa']
    assert (ROOT/original['imagen']).is_file()
    css = re.search(r'<style>(.*?)</style>', (ROOT/'pollo-guisado-calabacin.html').read_text(), re.S)[1]
    css += '.original-marisa{margin-top:42px}.original-photo{position:relative;display:block}.original-photo img{display:block;width:100%;height:auto;border-radius:10px}.zoom-hint{position:absolute;right:12px;bottom:12px;background:white;color:#245d42;border:1px solid #9db8a5;border-radius:50%;padding:4px 12px;font-size:1.4rem}.original-photo:focus-visible{outline:3px solid #245d42;outline-offset:4px}.original-note{background:#f3f6f1;padding:14px 18px;border-radius:8px}@media print{.original-marisa{display:none}}'
    grid = '<svg class="action-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="3" width="7" height="7" rx="1"></rect><rect x="14" y="3" width="7" height="7" rx="1"></rect><rect x="3" y="14" width="7" height="7" rx="1"></rect><rect x="14" y="14" width="7" height="7" rx="1"></rect></svg>'
    printer = '<svg class="action-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 9V3h12v6M6 18H3V9h18v9h-3M6 14h12v7H6zM17 12h1"></path></svg>'
    h = ['<!doctype html><html lang="es"><head><link rel="icon" type="image/x-icon" href="/recetario/images/iconos/favicon-v1.ico"><link rel="icon" type="image/png" sizes="32x32" href="/recetario/images/iconos/favicon-32-v1.png"><link rel="icon" type="image/png" sizes="16x16" href="/recetario/images/iconos/favicon-16-v1.png"><link rel="apple-touch-icon" href="/recetario/apple-touch-icon.png"><link rel="apple-touch-icon" sizes="76x76" href="/recetario/images/iconos/apple-touch-icon-76-v1.png"><link rel="apple-touch-icon" sizes="180x180" href="/recetario/images/iconos/apple-touch-icon-v1.png"><link rel="manifest" href="/recetario/site.webmanifest"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex, noimageindex">', '<title>'+e(d['titulo'])+' · Casa Marisa</title>', '<meta name="description" content="'+e(d['subtitulo'],quote=True)+'">', '<link rel="canonical" href="'+BASE+ident+'.html">', '<meta property="og:title" content="'+e(d['titulo'],quote=True)+'"><meta property="og:description" content="'+e(d['subtitulo'],quote=True)+'"><meta property="og:image" content="'+d['image']+'"><meta property="og:image:alt" content="'+e(d['image_alt'],quote=True)+'">', '<style>'+css+'</style><script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('</','<\\/')+'</script></head><body><main>', '<nav><a href="index.html">← Índice del recetario</a></nav><h1>'+e(d['titulo'])+'</h1><p class="meta">'+e(d['encabezado']['detalle'])+'</p>', '<p><span role="img" aria-label="Receta de Marisa">💚</span> '+e(d['presentacion'])+'</p>', '<figure class="hero"><img src="'+d['image'].removeprefix(BASE)+'" alt="'+e(d['image_alt'],quote=True)+'" width="1672" height="941"><figcaption>Ilustración generada con IA.</figcaption></figure>', '<p class="actions"><a class="category-link" href="categorias/pures.html">'+grid+'Más de Purés</a><a class="pdf-link" href="'+ident+'.pdf">'+printer+'PDF para imprimir</a></p>', '<h2>Ingredientes</h2><ul class="ingredients">'+''.join('<li>'+e(x)+'</li>' for x in d['pdf_ingredientes'])+'</ul><h2>Preparación</h2>']
    for p in d['pasos']:
        h.append('<section class="step"><strong>'+str(p['orden'])+'. '+e(p['titulo'])+' · '+e(p['duracion_texto'])+'</strong><div>'+e(p['instrucciones'])+'</div></section>')
    h.append('<h2>Claves</h2><p>'+e(d['claves'])+'</p>')
    if d.get('opciones'): h.append('<h2>Opciones</h2>')
    for option in d.get('opciones', []):
        h.append('<p><strong>'+e(option['titulo'])+':</strong> '+e(option['texto'])+'</p>')
    h.append('<section class="original-marisa" aria-labelledby="original-title"><h2 id="original-title">'+e(original['titulo'])+'</h2>')
    h.append('<a class="original-photo" href="'+original['imagen']+'" target="_blank" rel="noopener" aria-label="Ampliar la receta manuscrita de Marisa"><img src="'+original['imagen']+'" alt="'+e(original['imagen_alt'],quote=True)+'" loading="lazy"><span class="zoom-hint" aria-hidden="true">+</span></a><p class="meta">Manuscrito de Marisa.</p>')
    h.append('<h3>Transcripción del manuscrito</h3><p><strong>'+e(original['titulo_manuscrito'])+'</strong></p><ul>'+''.join('<li>'+e(x)+'</li>' for x in original['pasos'])+'</ul><p>'+e(original['nota_pie'])+'</p>')
    h.append('<p class="meta">'+e(original['nota_transcripcion'])+'</p><p class="original-note">'+e(original['actualizacion_familiar'])+'</p></section>')
    h.append('<h2>Fuente</h2><p>'+e(d['fuente']['atribucion'])+'</p><footer>Recetario personal · <a href="'+ident+'.md">Archivo maestro</a></footer></main></body></html>')
    (ROOT/(ident+'.html')).write_text('\n'.join(h)+'\n')
    body = '# '+d['titulo']+'\n\n'+d['encabezado']['detalle']+'\n\n!['+d['image_alt']+']('+d['image'].removeprefix(BASE)+')\n\nIlustración generada con IA.\n\n## Ingredientes\n\n'+'\n'.join('- '+x for x in d['pdf_ingredientes'])+'\n\n## Preparación\n\n'
    body += '\n\n'.join(str(p['orden'])+'. **'+p['titulo']+' · '+p['duracion_texto']+'.** '+p['instrucciones'] for p in d['pasos'])
    body += '\n\n## Claves\n\n'+d['claves']+'\n\n## Fuente\n\n'+d['fuente']['atribucion']+'\n'
    body += '\n## '+original['titulo']+'\n\n!['+original['imagen_alt']+']('+original['imagen']+')\n\n### Transcripción del manuscrito\n\n**'+original['titulo_manuscrito']+'**\n\n'+'\n\n'.join('- '+x for x in original['pasos'])+'\n\n'+original['nota_pie']+'\n\n'+original['nota_transcripcion']+'\n\n'+original['actualizacion_familiar']+'\n'
    master.write_text('---'+text.split('---',2)[1]+'---\n\n'+body)
    print('Crema de calabacín: maestro, JSON, Schema.org y HTML sincronizados.')


if __name__ == '__main__':
    main()
