#!/usr/bin/env python3
"""Reconstruye la ficha de pollo en cocotte desde el maestro YAML."""
from pathlib import Path
from html import escape as e
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://fucolin.github.io/recetario/'


def main():
    master = ROOT / 'pollo-guisado-calabacin-cocotte.md'
    text = master.read_text()
    d = yaml.safe_load(text.split('---', 2)[1])
    ident = d['id']
    schema = {'@context':'https://schema.org', '@type':'Recipe', 'name':d['titulo'], 'description':d['subtitulo'], 'recipeCategory':d['categoria_menu'], 'recipeYield':'2-3 raciones', 'totalTime':'PT110M', 'recipeIngredient':d['pdf_ingredientes'], 'recipeInstructions':[{'@type':'HowToStep', 'position':p['orden'], 'name':p['titulo'], 'text':p['instrucciones']} for p in d['pasos']], 'keywords':', '.join(d['etiquetas']), 'image':d['image'], 'url':BASE+ident+'.html', 'dateModified':d['fecha_actualizacion'], 'isBasedOn':{'@type':'CreativeWork', 'name':d['fuente']['titulo_original']}}
    schema['author'] = {'@type':'Person', 'name':d['autor']}
    schema['isBasedOn'] = {'@type':'Recipe', 'name':d['fuente']['titulo_original'], 'author':{'@type':'Person','name':'Eva','jobTitle':'Nutricionista'}}
    (ROOT/(ident+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    (ROOT/(ident+'.schema.json')).write_text(json.dumps(schema,ensure_ascii=False,indent=2)+'\n')
    css = re.search(r'<style>(.*?)</style>', (ROOT/'pollo-guisado-calabacin.html').read_text(), re.S)[1]
    grid = '<svg class="action-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="3" width="7" height="7" rx="1"></rect><rect x="14" y="3" width="7" height="7" rx="1"></rect><rect x="3" y="14" width="7" height="7" rx="1"></rect><rect x="14" y="14" width="7" height="7" rx="1"></rect></svg>'
    printer = '<svg class="action-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 9V3h12v6M6 18H3V9h18v9h-3M6 14h12v7H6zM17 12h1"></path></svg>'
    h = ['<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex, noimageindex">', '<title>'+e(d['titulo'])+' · Casa Marisa</title>', '<meta name="description" content="'+e(d['subtitulo'],quote=True)+'">', '<link rel="canonical" href="'+BASE+ident+'.html">', '<meta property="og:title" content="'+e(d['titulo'],quote=True)+'"><meta property="og:description" content="'+e(d['subtitulo'],quote=True)+'"><meta property="og:image" content="'+d['image']+'"><meta property="og:image:alt" content="'+e(d['image_alt'],quote=True)+'">', '<style>'+css+'</style><script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('</','<\\/')+'</script></head><body><main>', '<nav><a href="index.html">← Índice del recetario</a></nav><h1>'+e(d['titulo'])+'</h1><p class="meta">'+e(d['encabezado']['detalle'])+'</p>', '<figure class="hero"><img src="'+d['image'].removeprefix(BASE)+'" alt="'+e(d['image_alt'],quote=True)+'" width="1672" height="941"><figcaption>Ilustración generada con IA.</figcaption></figure>', '<p class="actions"><a class="category-link" href="categorias/guisos-y-asados.html">'+grid+'Más de Guisos y asados</a><a class="pdf-link" href="'+ident+'.pdf">'+printer+'PDF para imprimir</a></p>', '<h2>Ingredientes</h2><ul class="ingredients">'+''.join('<li>'+e(x)+'</li>' for x in d['pdf_ingredientes'])+'</ul><h2>Preparación</h2>']
    variants = '<nav class="recipe-variants" aria-label="Versión de la receta"><span class="variant-label" aria-hidden="true">Versión</span><div class="variant-options">'
    for v in d['variantes']:
        if v['pagina'] == ident+'.html':
            variants += '<span aria-current="page"><span aria-hidden="true">✓</span> '+e(v['titulo'])+'</span>'
        else:
            variants += '<a href="'+e(v['pagina'],quote=True)+'">'+e(v['titulo'])+'</a>'
    variants += '</div></nav>'
    h = [part+variants if '<p class="meta">' in part else part for part in h]
    for p in d['pasos']:
        h.append('<section class="step"><strong>'+str(p['orden'])+'. '+e(p['titulo'])+' · '+e(p['duracion_texto'])+'</strong><div>'+e(p['instrucciones'])+'</div></section>')
    h.append('<h2>Claves</h2><p>'+e(d['claves'])+'</p>')
    for option in d['opciones']:
        h.append('<p><strong>'+e(option['titulo'])+':</strong> '+e(option['texto'])+'</p>')
    h.append('<h2>Fuente</h2><p>'+e(d['fuente']['atribucion'])+'</p><footer>Recetario personal · <a href="'+ident+'.md">Archivo maestro</a></footer></main></body></html>')
    (ROOT/(ident+'.html')).write_text('\n'.join(h)+'\n')
    body = '# '+d['titulo']+'\n\n'+d['encabezado']['detalle']+'\n\n!['+d['image_alt']+']('+d['image'].removeprefix(BASE)+')\n\nIlustración generada con IA.\n\n## Ingredientes\n\n'+'\n'.join('- '+x for x in d['pdf_ingredientes'])+'\n\n## Preparación\n\n'
    body += '\n\n'.join(str(p['orden'])+'. **'+p['titulo']+' · '+p['duracion_texto']+'.** '+p['instrucciones'] for p in d['pasos'])
    body += '\n\n## Claves\n\n'+d['claves']+'\n\n## Opciones\n\n'+'\n\n'.join('**'+x['titulo']+':** '+x['texto'] for x in d['opciones'])+'\n\n## Fuente\n\n'+d['fuente']['atribucion']+'\n'
    body = body.replace('\n\n## Opciones\n\n\n\n## Fuente', '\n\n## Fuente')
    body = body.replace('## Ingredientes', '[Olla](pollo-guisado-calabacin.html) · [Cocotte y horno](pollo-guisado-calabacin-cocotte.html)\n\n## Ingredientes', 1)
    master.write_text('---'+text.split('---',2)[1]+'---\n\n'+body)
    print('Pollo en cocotte: maestro, JSON, Schema.org y HTML sincronizados.')


if __name__ == '__main__':
    main()
