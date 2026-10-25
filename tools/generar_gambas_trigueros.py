#!/usr/bin/env python3
"""Reconstruye la ficha de gambas salteadas con trigueros desde el maestro YAML."""
from pathlib import Path
from html import escape as e
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://fucolin.github.io/recetario/'


def main():
    master = ROOT / 'gambas-salteadas-trigueros.md'
    text = master.read_text()
    d = yaml.safe_load(text.split('---', 2)[1])
    ident = d['id']
    schema = {'@context':'https://schema.org', '@type':'Recipe', 'name':d['titulo'], 'description':d['subtitulo'], 'recipeCategory':d['categoria_menu'], 'recipeYield':'2 raciones', 'totalTime':'PT20M', 'recipeIngredient':d['pdf_ingredientes'], 'recipeInstructions':[{'@type':'HowToStep', 'position':p['orden'], 'name':p['titulo'], 'text':p['instrucciones']} for p in d['pasos']], 'keywords':', '.join(d['etiquetas']), 'image':d['image'], 'url':BASE+ident+'.html', 'dateModified':d['fecha_actualizacion'], 'isBasedOn':{'@type':'CreativeWork', 'name':d['fuente']['titulo_original']}}
    (ROOT/(ident+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    (ROOT/(ident+'.schema.json')).write_text(json.dumps(schema,ensure_ascii=False,indent=2)+'\n')
    css = re.search(r'<style>(.*?)</style>', (ROOT/'pollo-guisado-calabacin.html').read_text(), re.S)[1]
    grid = '<svg class="action-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="3" width="7" height="7" rx="1"></rect><rect x="14" y="3" width="7" height="7" rx="1"></rect><rect x="3" y="14" width="7" height="7" rx="1"></rect><rect x="14" y="14" width="7" height="7" rx="1"></rect></svg>'
    printer = '<svg class="action-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 9V3h12v6M6 18H3V9h18v9h-3M6 14h12v7H6zM17 12h1"></path></svg>'
    h = ['<!doctype html><html lang="es"><head><link rel="icon" type="image/x-icon" href="/recetario/images/iconos/favicon-v1.ico"><link rel="icon" type="image/png" sizes="32x32" href="/recetario/images/iconos/favicon-32-v1.png"><link rel="icon" type="image/png" sizes="16x16" href="/recetario/images/iconos/favicon-16-v1.png"><link rel="apple-touch-icon" href="/recetario/apple-touch-icon.png"><link rel="apple-touch-icon" sizes="76x76" href="/recetario/images/iconos/apple-touch-icon-76-v1.png"><link rel="apple-touch-icon" sizes="180x180" href="/recetario/images/iconos/apple-touch-icon-v1.png"><link rel="manifest" href="/recetario/site.webmanifest"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex, noimageindex">', '<title>'+e(d['titulo'])+' · Casa Marisa</title>', '<meta name="description" content="'+e(d['subtitulo'],quote=True)+'">', '<link rel="canonical" href="'+BASE+ident+'.html">', '<meta property="og:title" content="'+e(d['titulo'],quote=True)+'"><meta property="og:description" content="'+e(d['subtitulo'],quote=True)+'"><meta property="og:image" content="'+d['image']+'"><meta property="og:image:alt" content="'+e(d['image_alt'],quote=True)+'">', '<style>'+css+'</style><script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('</','<\\/')+'</script></head><body><main>', '<nav><a href="index.html">← Índice del recetario</a></nav><h1>'+e(d['titulo'])+'</h1><p class="meta">'+e(d['encabezado']['detalle'])+'</p>', '<figure class="hero"><img src="'+d['image'].removeprefix(BASE)+'" alt="'+e(d['image_alt'],quote=True)+'" width="1672" height="941"><figcaption>Ilustración generada con IA.</figcaption></figure>', '<p class="actions"><a class="category-link" href="categorias/mariscos.html">'+grid+'Más de Mariscos</a><a class="pdf-link" href="'+ident+'.pdf">'+printer+'PDF para imprimir</a></p>', '<h2>Ingredientes</h2><ul class="ingredients">'+''.join('<li>'+e(x)+'</li>' for x in d['pdf_ingredientes'])+'</ul><h2>Preparación</h2>']
    for p in d['pasos']:
        h.append('<section class="step"><strong>'+str(p['orden'])+'. '+e(p['titulo'])+' · '+e(p['duracion_texto'])+'</strong><div>'+e(p['instrucciones'])+'</div></section>')
    h.append('<h2>Claves</h2><p>'+e(d['claves'])+'</p><h2>Opciones</h2>')
    for option in d['opciones']:
        h.append('<p><strong>'+e(option['titulo'])+':</strong> '+e(option['texto'])+'</p>')
    h.append('<h2>Fuente</h2><p>'+e(d['fuente']['atribucion'])+'</p><footer>Recetario personal · <a href="'+ident+'.md">Archivo maestro</a></footer></main></body></html>')
    (ROOT/(ident+'.html')).write_text('\n'.join(h)+'\n')
    body = '# '+d['titulo']+'\n\n'+d['encabezado']['detalle']+'\n\n!['+d['image_alt']+']('+d['image'].removeprefix(BASE)+')\n\nIlustración generada con IA.\n\n## Ingredientes\n\n'+'\n'.join('- '+x for x in d['pdf_ingredientes'])+'\n\n## Preparación\n\n'
    body += '\n\n'.join(str(p['orden'])+'. **'+p['titulo']+' · '+p['duracion_texto']+'.** '+p['instrucciones'] for p in d['pasos'])
    body += '\n\n## Claves\n\n'+d['claves']+'\n\n## Opciones\n\n'+'\n\n'.join('**'+x['titulo']+':** '+x['texto'] for x in d['opciones'])+'\n\n## Fuente\n\n'+d['fuente']['atribucion']+'\n'
    master.write_text('---'+text.split('---',2)[1]+'---\n\n'+body)
    print('Gambas: maestro, JSON, Schema.org y HTML sincronizados.')


if __name__ == '__main__':
    main()
