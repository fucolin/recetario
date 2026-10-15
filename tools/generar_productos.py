#!/usr/bin/env python3
"""Genera el catálogo y las fichas de producto desde su Markdown/YAML maestro."""
from pathlib import Path
import html
import json
import yaml
from datetime import date

RAIZ = Path(__file__).resolve().parent.parent
BASE = "https://fucolin.github.io/recetario/"


def e(value):
    return html.escape(str(value), quote=True)


def numero(value):
    return f"{value:g}".replace(".", ",")


def documento(titulo, contenido, css, schema=None):
    datos = ""
    if schema:
        datos = '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False).replace("</", "<\\/") + '</script>'
    return f'<!doctype html>\n<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(titulo)} · Mi recetario</title><link rel="stylesheet" href="{e(css)}">{datos}</head><body><main>{contenido}</main></body></html>\n'


def generar():
    tarjetas = []
    for maestro in sorted((RAIZ / 'productos').glob('*.md')):
        data = yaml.safe_load(maestro.read_text().split('---', 2)[1])
        slug = data['id']
        (maestro.with_suffix('.json')).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
        imagen = data['imagenes'][0]
        etiqueta = data['imagenes'][1]
        nombre = data['nombre']
        marca = data['marca']
        formato = data['formato']
        envase = f"{formato['envase'].capitalize()} de {numero(formato['cantidad'])} {formato['unidad']}"
        composicion = ', '.join(e(i['nombre']) + (f" ({numero(i['porcentaje'])} %)" if 'porcentaje' in i else '') for i in data['ingredientes']) + '.'
        nutricion = data['nutricion_por_100g']
        filas = [('Energía', f"{numero(nutricion['energia_kj'])} kJ / {numero(nutricion['energia_kcal'])} kcal")]
        filas += [(label, numero(nutricion[key]) + ' g') for key, label in [('grasas_g', 'Grasas'), ('saturadas_g', 'De las cuales saturadas'), ('hidratos_g', 'Hidratos de carbono'), ('azucares_g', 'De los cuales azúcares'), ('fibra_g', 'Fibra'), ('proteinas_g', 'Proteínas'), ('sal_g', 'Sal')]]
        precio = data['precio_referencia']
        precio_texto = '<p>Por anotar</p><p class="note">Precio del envase · €/kg · Fecha del precio</p>'
        if precio['importe'] is not None:
            por_kg = precio['importe'] / (formato['cantidad'] / 1000)
            precio_texto = f'<p>{precio["importe"]:.2f} € · {por_kg:.2f} €/kg</p>'.replace('.', ',')
            if precio['fecha']:
                precio_texto += f'<p class="note">Precio consultado: {e(precio["fecha"])}</p>'
        tiendas = '<p>Por anotar</p><p class="note">Tienda · Enlace al producto</p>'
        if data['puntos_venta']:
            tiendas = ''.join('<p>' + (f'<a href="{e(t["url"])}">{e(t["tienda"])}</a>' if t.get('url') else e(t['tienda'])) + '</p>' for t in data['puntos_venta'])
        links_recetas = []
        for receta_id in data['recetas']:
            receta = json.loads((RAIZ / f'{receta_id}.json').read_text())
            links_recetas.append(f'<li><a href="../{e(receta_id)}.html">{e(receta["titulo"])} →</a></li>')
        yuka = data['yuka']
        yuka_texto = '<p>Pendiente de registrar</p><p class="note">Puntuación, observaciones y fecha de consulta.</p>'
        if yuka['puntuacion'] is not None:
            if not 0 <= yuka['puntuacion'] <= 100:
                raise ValueError(f'{slug}: puntuación de Yuka fuera de rango')
            valoracion = f' · {e(yuka["valoracion"])}' if yuka.get('valoracion') else ''
            yuka_texto = f'<p class="yuka-score">{e(yuka["puntuacion"])} / 100{valoracion}</p>'
            if yuka['observaciones']:
                yuka_texto += f'<p>{e(yuka["observaciones"])}</p>'
            for key, label in [('positivos', 'Aspectos positivos según Yuka'), ('negativos', 'Aspectos negativos según Yuka')]:
                if yuka.get(key):
                    yuka_texto += f'<h3>{label}</h3><ul>' + ''.join(f'<li><strong>{e(item["aspecto"])}</strong> · {e(item["valor"])}: {e(item["comentario"])}</li>' for item in yuka[key]) + '</ul>'
            if yuka['fecha_consulta']:
                yuka_texto += f'<p class="note">Consultada: {date.fromisoformat(yuka["fecha_consulta"]).strftime("%d/%m/%Y")}</p>'
            elif yuka.get('fecha_aportacion'):
                yuka_texto += f'<p class="note">Fuente: captura de Yuka aportada el {date.fromisoformat(yuka["fecha_aportacion"]).strftime("%d/%m/%Y")}.</p>'
        schema = {'@context': 'https://schema.org', '@type': 'WebPage', 'name': nombre, 'url': BASE + f'productos/{slug}.html', 'dateModified': data['fecha_actualizacion'], 'mainEntity': {'@type': 'Product', '@id': BASE + f'productos/{slug}.html#producto', 'name': nombre, 'brand': {'@type': 'Brand', 'name': marca}, 'description': data['descripcion'], 'category': data['categoria'], 'image': [BASE + i['archivo'] for i in data['imagenes']], 'weight': {'@type': 'QuantitativeValue', 'value': formato['cantidad'], 'unitCode': 'GRM'}, 'additionalProperty': [{'@type': 'PropertyValue', 'name': label + ' por 100 g', 'value': value} for label, value in filas]}}
        maestro.with_suffix('.schema.json').write_text(json.dumps(schema, ensure_ascii=False, indent=2) + '\n')
        contenido = f'''<nav><a href="../ingredientes-preferidos.html">← Ingredientes preferidos</a></nav>
<header class="product-heading"><figure><a href="../{e(imagen['archivo'])}"><img class="product-photo" src="../{e(imagen['archivo'])}" alt="{e(imagen['alt'])}" width="1080" height="1440"></a><figcaption>Fotografía propia · <a href="../{e(imagen['archivo'])}">Ver envase completo</a></figcaption></figure>
<div><span class="tag">{e(data['categoria'])}</span><h1>{e(nombre)}</h1><p class="meta">{e(marca)} · {e(envase)}</p><p>{e(data['descripcion'])}</p><p class="note">{e(formato['nota'])}</p><div class="purchase"><section><h2>Precio de referencia</h2>{precio_texto}</section><section><h2>Dónde lo compro</h2>{tiendas}</section></div></div></header>
<div class="columns"><div><section><h2>Por qué lo uso</h2>''' + ''.join(f'<p>{e(motivo)}</p>' for motivo in data['por_que_lo_uso']) + f'''</section><section><h2>En mi cocina</h2><p>{e(data['uso_en_cocina'])}</p></section><section><h2>Composición</h2><p class="composition">{composicion}</p></section></div>
<section><h2>Valores por 100 g</h2><table class="nutrition"><caption>Según la etiqueta fotografiada aportada el 14/10/2026.</caption><tbody>''' + ''.join(f'<tr><th scope="row">{e(label)}</th><td>{e(value)}</td></tr>' for label, value in filas) + f'''</tbody></table><a class="label-link" href="../{e(etiqueta['archivo'])}">Ver fotografía de la etiqueta →</a></section></div>
<section class="yuka"><h2>Valoración de Yuka</h2>{yuka_texto}</section><section><h2>Lo uso en</h2><ul class="recipe-links">''' + ''.join(links_recetas) + f'''</ul></section>
<details><summary>Ingredientes y tabla nutricional del envase</summary><figure><img class="label-photo" src="../{e(etiqueta['archivo'])}" alt="{e(etiqueta['alt'])}" width="1080" height="1440" loading="lazy"><figcaption>Fotografía propia proporcionada por el usuario. <a href="../{e(etiqueta['archivo'])}">Abrir a tamaño completo</a>.</figcaption></figure></details>
<footer>Recetario personal · <a href="{e(slug)}.md">Archivo maestro</a> · <a href="../index.html">Índice del recetario</a></footer>'''
        maestro.with_suffix('.html').write_text(documento(nombre, contenido, 'productos.css', schema))
        tarjetas.append(f'''<li><article class="product-summary"><a href="productos/{e(slug)}.html"><img class="product-photo" src="{e(imagen['archivo'])}" alt="{e(imagen['alt'])}" width="1080" height="1440" loading="lazy"></a><div><span class="tag">{e(data['categoria'])}</span><h2><a href="productos/{e(slug)}.html">{e(nombre)}</a></h2><p class="meta">{e(marca)} · {e(envase)}</p><p>{e(data['descripcion'])}</p><p class="note">{'Precio y tienda por anotar' if precio['importe'] is None and not data['puntos_venta'] else 'Ver precio y puntos de venta en la ficha'}</p><a href="productos/{e(slug)}.html">Ver producto →</a></div></article></li>''')
    catalogo = '<nav><a href="index.html">← Índice del recetario</a></nav><h1>Ingredientes preferidos</h1><p class="intro">Los productos que uso y por qué. Dónde comprarlos y su precio de referencia.</p><ul class="product-list">' + ''.join(tarjetas) + '</ul><footer>Recetario personal · <a href="index.html">Volver a las recetas</a></footer>'
    (RAIZ / 'ingredientes-preferidos.html').write_text(documento('Ingredientes preferidos', catalogo, 'productos/productos.css'))
    print(f'{len(tarjetas)} producto(s) y catálogo generados. Sin PDF.')


if __name__ == '__main__':
    generar()
