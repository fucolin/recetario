#!/usr/bin/env python3
"""Genera La Piadina di Marisa y prepara su integración sin publicar."""
from pathlib import Path
from html import escape as e
import json,re,yaml

ROOT=Path(__file__).resolve().parents[1]
BASE='https://fucolin.github.io/recetario/'
ID='la-piadina-di-marisa'

def main():
    master=ROOT/(ID+'.md')
    d=yaml.safe_load(master.read_text().split('---',2)[1])
    schema={'@context':'https://schema.org','@type':'Recipe','name':d['titulo'],'description':d['subtitulo'],
        'recipeCategory':d['categoria_menu'],'recipeYield':'2 raciones','totalTime':'PT15M',
        'recipeIngredient':d['pdf_ingredientes'],
        'recipeInstructions':[{'@type':'HowToStep','position':p['orden'],'name':p['titulo'],'text':p['instrucciones']} for p in d['pasos']],
        'keywords':', '.join(d['etiquetas']),'image':d['image'],'url':BASE+ID+'.html','dateModified':d['fecha_actualizacion']}
    (ROOT/(ID+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    (ROOT/(ID+'.schema.json')).write_text(json.dumps(schema,ensure_ascii=False,indent=2)+'\n')
    template=(ROOT/'pan-plano-jamon-queso.html').read_text()
    css=re.search(r'<style>(.*?)</style>',template,re.S)[1]
    icons=re.search(r'<head>(.*?)<meta name="robots"',template,re.S)[1]
    grid=re.search(r'<a class="category-link"[^>]*>(.*?)Más de Envueltos y bocados</a>',template,re.S)[1]
    printer=re.search(r'<a class="pdf-link"[^>]*>(.*?)Descargar receta',template,re.S)[1]
    photo=d['image'].removeprefix(BASE)
    h=['<!doctype html><html lang="es"><head>'+icons,
       '<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex, noimageindex">',
       '<title>'+e(d['titulo'])+' · Casa Marisa</title><meta name="description" content="'+e(d['subtitulo'],quote=True)+'">',
       '<link rel="canonical" href="'+BASE+ID+'.html"><meta property="og:title" content="'+e(d['titulo'],quote=True)+'"><meta property="og:image" content="'+d['image']+'"><meta property="og:image:alt" content="'+e(d['image_alt'],quote=True)+'">',
       '<style>'+css+'</style><script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('</','<\\/')+'</script></head><body><main>',
       '<nav><a href="index.html">← Índice del recetario</a></nav><h1>'+e(d['titulo'])+'</h1><p class="meta">'+e(d['encabezado']['detalle'])+'</p>',
       '<figure class="hero"><img src="'+photo+'" alt="'+e(d['image_alt'],quote=True)+'" width="1672" height="941"><figcaption>Imagen ilustrativa generada con IA; no es una fotografía del plato preparado.</figcaption></figure>',
       '<p class="actions"><a class="category-link" href="categorias/envueltos-y-bocados.html">'+grid+'Más de Envueltos y bocados</a><a class="pdf-link" href="'+ID+'.pdf">'+printer+'PDF para imprimir · A4</a></p>',
       '<h2>Ingredientes</h2><ul class="ingredients">'+''.join('<li>'+e(x)+'</li>' for x in d['pdf_ingredientes'])+'</ul><h2>Preparación</h2>']
    for p in d['pasos']:
        h.append('<section class="step"><strong>'+str(p['orden'])+'. '+e(p['titulo'])+' · '+e(p['duracion_texto'])+'</strong><div>'+e(p['instrucciones'])+'</div></section>')
    h.append('<h2>Claves</h2><p>'+e(d['claves'])+'</p><h2>Opciones</h2>')
    for x in d['opciones']:
        h.append('<p><strong>'+e(x['titulo'])+':</strong> '+e(x['texto'])+'</p>')
    h.append('<h2>Fuente</h2><p>'+e(d['fuente']['atribucion'])+'</p><footer>Recetario de Casa Marisa · <a href="'+ID+'.md">Archivo maestro</a></footer></main></body></html>')
    (ROOT/(ID+'.html')).write_text('\n'.join(h)+'\n')
    body='# '+d['titulo']+'\n\n'+d['encabezado']['detalle']+'\n\n!['+d['image_alt']+']('+photo+')\n\nIlustración generada con IA.\n\n## Ingredientes\n\n'+'\n'.join('- '+x for x in d['pdf_ingredientes'])+'\n\n## Preparación\n\n'
    body+='\n\n'.join(str(p['orden'])+'. **'+p['titulo']+' · '+p['duracion_texto']+'.** '+p['instrucciones'] for p in d['pasos'])
    body+='\n\n## Claves\n\n'+d['claves']+'\n\n## Opciones\n\n'+'\n\n'.join('**'+x['titulo']+':** '+x['texto'] for x in d['opciones'])+'\n\n## Fuente\n\n'+d['fuente']['atribucion']+'\n'
    master.write_text('---\n'+yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=110)+'---\n\n'+body)
    statepath=ROOT/'datos/estado-fichas.json';state=json.loads(statepath.read_text())
    if ID not in state['nuevas']:state['nuevas'].append(ID)
    statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
    home=ROOT/'index.html';text=home.read_text()
    card='<a class="recipe" href="'+ID+'.html"><div class="card-title-row"><strong>'+e(d['titulo'])+'</strong><span class="status-badge is-new">NUEVA</span></div><span>2 raciones · 10-15 min</span>&nbsp;<span class="type-badge">Receta</span></a>'
    if 'href="'+ID+'.html"' not in text:
        marker='<section class="category" id="envueltos-y-bocados"><h2><a href="categorias/envueltos-y-bocados.html">Envueltos y bocados <span>Ver categoría →</span></a></h2><div class="recipes">'
        if marker not in text:raise ValueError('Cambió la sección de Envueltos')
        text=text.replace(marker,marker+card,1)
    def update_search(m):
        index=json.loads(m.group(1))
        index[ID+'.html']=' '.join([d['titulo'],d['subtitulo'],d['categoria_menu'],d['tipo_ficha']]+d['etiquetas']+d['pdf_ingredientes']+[x['instrucciones'] for x in d['pasos']]+[x['texto'] for x in d['opciones']])
        return '<script id="search-data" type="application/json">'+json.dumps(index,ensure_ascii=False,separators=(',',':'))+'</script>'
    text,count=re.subn(r'<script id="search-data" type="application/json">(.*?)</script>',update_search,text,flags=re.S)
    if count!=1:raise ValueError('Buscador no encontrado')
    home.write_text(text)
    category=ROOT/'categorias/envueltos-y-bocados.html';text=category.read_text()
    card='<a class="card" href="../'+ID+'.html"><span class="status-badge is-new">NUEVA</span><img src="../'+photo+'" alt="'+e(d['image_alt'],quote=True)+'"><div class="content"><h2>'+e(d['titulo'])+'</h2><span class="meta">2 raciones · 10-15 min</span>&nbsp;<span class="type-badge">Receta</span></div></a>'
    if 'href="../'+ID+'.html"' not in text:
        text=text.replace('<div class="grid">','<div class="grid">'+card,1)
    category.write_text(text)
    print('Maestro, JSON, Schema.org, HTML, portada, categoría, buscador y estado preparados.')

if __name__=='__main__':main()
