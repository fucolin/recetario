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
    return (value if isinstance(value, str) else f"{value:g}").replace(".", ",")


def documento(titulo, contenido, css, schema=None):
    datos = ""
    if schema:
        datos = '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False).replace("</", "<\\/") + '</script>'
    return f'<!doctype html>\n<html lang="es"><head><meta name="robots" content="noindex, noimageindex"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(titulo)} · Mi recetario</title><link rel="stylesheet" href="{e(css)}">{datos}</head><body><main>{contenido}</main></body></html>\n'


def generar():
    tarjetas = []
    for maestro in sorted((RAIZ / 'productos').glob('*.md')):
        data = yaml.safe_load(maestro.read_text().split('---', 2)[1])
        slug = data['id']
        (maestro.with_suffix('.json')).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
        imagen = data['imagenes'][0]
        etiqueta = data['imagenes'][1]
        dimensiones = lambda foto: f'width="{foto.get("ancho", 1080)}" height="{foto.get("alto", 1440)}"'
        fotos_etiqueta = ''.join(f'<figure><img class="label-photo" src="../{e(foto["archivo"])}" alt="{e(foto["alt"])}" {dimensiones(foto)} loading="lazy"><figcaption>Fotografía propia proporcionada por el usuario. <a href="../{e(foto["archivo"])}">Abrir a tamaño completo</a>.</figcaption></figure>' for foto in data['imagenes'][1:])
        fecha_fuente = date.fromisoformat(data['fuente_datos']['fecha_aportacion']).strftime('%d/%m/%Y')
        detalles = data.get('datos_etiqueta', {})
        detalles_html = ''.join(f'<p class="note">{e(texto)}</p>' for texto in ([('Alérgenos: ' + ', '.join(detalles['alergenos']) + '.') ] if detalles.get('alergenos') else []) + ([detalles['conservacion']] if detalles.get('conservacion') else []) + ([detalles['fabricante']] if detalles.get('fabricante') else []))
        if detalles.get('origen_leche'):
            detalles_html += f'<p class="note">{e(detalles["origen_leche"])}</p>'
        if detalles.get('trazas'):
            detalles_html += f'<p class="note">Puede contener trazas de {e(", ".join(detalles["trazas"]))}.</p>'
        referencias_html = ''
        for ref in data.get('referencias_otros_formatos', []):
            fecha_ref = date.fromisoformat(ref['fecha']).strftime('%d/%m/%Y')
            importe_ref = f"{ref['importe']:.2f} € · {ref['precio_por_kg']:.2f} €/kg".replace('.', ',')
            referencias_html += f'<p class="note">Otro formato: {numero(ref["cantidad"])} {e(ref["unidad"])} · {importe_ref} · {e(ref["tienda"])} · {fecha_ref}. {e(ref["nota"])}</p>'
        nombre = data['nombre']
        marca = data['marca']
        formato = data['formato']
        envase = f"{formato['envase'].capitalize()} de {numero(formato['cantidad'])} {formato['unidad']}"
        composicion = ', '.join(e(i['nombre']) + (f" ({numero(i['porcentaje'])} %)" if 'porcentaje' in i else '') for i in data['ingredientes']) + '.' if data['ingredientes'] else 'Lista completa de ingredientes pendiente de aportar.'
        nutricion = data['nutricion_por_100g']
        filas = [('Energía', f"{numero(nutricion['energia_kj'])} kJ / {numero(nutricion['energia_kcal'])} kcal")]
        filas += [(label, (numero(nutricion[key]) + ' g') if nutricion.get(key) is not None else 'No declarada') for key, label in [('grasas_g', 'Grasas'), ('saturadas_g', 'De las cuales saturadas'), ('hidratos_g', 'Hidratos de carbono'), ('azucares_g', 'De los cuales azúcares'), ('fibra_g', 'Fibra'), ('proteinas_g', 'Proteínas'), ('sal_g', 'Sal')]]
        precio = data['precio_referencia']
        escurrido = precio.get('base_calculo') == 'peso_escurrido'
        unidad_precio = '€/kg escurrido' if escurrido else '€/kg'
        precio_texto = '<p>Por anotar</p><p class="note">Precio del envase · €/kg · Fecha del precio</p>'
        resumen_fecha = ''
        if precio['importe'] is not None:
            peso_precio = formato['peso_escurrido_g'] if escurrido else formato['cantidad']
            por_kg = precio['importe'] / (peso_precio / 1000)
            precio_texto = f'<p>{precio["importe"]:.2f} € · {por_kg:.2f} {unidad_precio}</p>'.replace('.', ',')
            if precio['fecha']:
                resumen_fecha = date.fromisoformat(precio['fecha']).strftime('%d/%m/%Y')
        tiendas = '<p>Por anotar</p><p class="note">Tienda · Enlace al producto</p>'
        if data['puntos_venta']:
            tiendas = ''.join('<p>' + (f'<a href="{e(t["url"])}">{e(t["tienda"])}</a>' if t.get('url') else e(t['tienda'])) + '</p>' for t in data['puntos_venta'])
        for ref in data.get('referencias_ticket_pendientes', []):
            fecha_ref = date.fromisoformat(ref['fecha']).strftime('%d/%m/%Y')
            importe_ref = f"{ref['importe']:.2f} €".replace('.', ',')
            referencias_html += f'<p class="note">Ticket de {e(ref["tienda"])} · {fecha_ref} · {importe_ref}. {e(ref["nota"])}</p>'
        if referencias_html:
            precio_texto += referencias_html
        resumen_promociones = []
        for promo in data.get('promociones', []):
            fecha_oferta = date.fromisoformat(promo['fecha_observacion']).strftime('%d/%m/%Y')
            if promo['tipo'] == '3x2':
                total = promo['precio_unitario_base'] * 2
                efectivo = total / 3
                efectivo_kg = efectivo / (formato['cantidad'] / 1000)
                importes = f'{efectivo:.2f} €/lata · {efectivo_kg:.2f} €/kg'.replace('.', ',')
                fecha_promo = '' if fecha_oferta == resumen_fecha else f' ({fecha_oferta})'
                resumen_promociones.append(f'Oferta 3×2{fecha_promo}: aprox. {importes}')
        resumen_precio = ' · '.join(([resumen_fecha] if resumen_fecha else []) + resumen_promociones)
        nota_compra = f'<p class="purchase-note">{e(resumen_precio)}</p>' if resumen_precio else ''
        resumen_compra = 'Precio y tienda por anotar'
        if precio['importe'] is not None:
            resumen_compra = f'{precio["importe"]:.2f} € · {por_kg:.2f} {unidad_precio}'.replace('.', ',')
            if precio.get('tienda'):
                resumen_compra += ' · ' + precio['tienda']
        links_recetas = []
        for receta_id in data['recetas']:
            receta = json.loads((RAIZ / f'{receta_id}.json').read_text())
            links_recetas.append(f'<li><a href="../{e(receta_id)}.html">{e(receta["titulo"])} →</a></li>')
        bloque_recetas = '<section><h2>Lo uso en</h2><ul class="recipe-links">' + ''.join(links_recetas) + '</ul></section>' if links_recetas else ''
        titulo_uso = 'Cómo lo tomo' if data.get('forma_de_consumo') else 'En mi cocina'
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
            if yuka.get('captura'):
                yuka_texto += f'<p class="note"><a href="../{e(yuka["captura"])}">Ver captura de Yuka →</a></p>'
        schema = {'@context': 'https://schema.org', '@type': 'WebPage', 'name': nombre, 'url': BASE + f'productos/{slug}.html', 'dateModified': data['fecha_actualizacion'], 'mainEntity': {'@type': 'Product', '@id': BASE + f'productos/{slug}.html#producto', 'name': nombre, 'brand': {'@type': 'Brand', 'name': marca}, 'description': data['descripcion'], 'category': data['categoria'], 'image': [BASE + i['archivo'] for i in data['imagenes']], 'weight': {'@type': 'QuantitativeValue', 'value': formato['cantidad'], 'unitCode': 'GRM'}, 'additionalProperty': [{'@type': 'PropertyValue', 'name': label + ' por 100 g', 'value': value} for label, value in filas]}}
        maestro.with_suffix('.schema.json').write_text(json.dumps(schema, ensure_ascii=False, indent=2) + '\n')
        contenido = f'''<nav><a href="../productos-preferidos.html">← Productos preferidos</a></nav>
<header class="product-heading"><figure><a href="../{e(imagen['archivo'])}"><img class="product-photo" src="../{e(imagen['archivo'])}" alt="{e(imagen['alt'])}" {dimensiones(imagen)}></a><figcaption>Fotografía propia · <a href="../{e(imagen['archivo'])}">Ver envase completo</a></figcaption></figure>
<div><span class="tag">{e(data['categoria'])}</span><h1>{e(nombre)}</h1><p class="meta">{e(marca)} · {e(envase)}</p><p>{e(data['descripcion'])}</p><p class="note">{e(formato['nota'])}</p><div class="purchase"><section><h2>Precio de referencia</h2>{precio_texto}</section><section><h2>Dónde lo compro</h2>{tiendas}</section>{nota_compra}</div></div></header>
{bloque_recetas}
<div class="columns"><div><section><h2>Por qué lo uso</h2>''' + (''.join(f'<p>{e(motivo)}</p>' for motivo in data['por_que_lo_uso']) or '<p class="note">Pendiente de concretar.</p>') + f'''</section><section><h2>{titulo_uso}</h2><p>{e(data['uso_en_cocina'])}</p></section><section><h2>Composición</h2><p class="composition">{composicion}</p>{detalles_html}</section></div>
<section><h2>Valores por 100 g</h2><table class="nutrition"><caption>Según la etiqueta fotografiada aportada el {fecha_fuente}.</caption><tbody>''' + ''.join(f'<tr><th scope="row">{e(label)}</th><td>{e(value)}</td></tr>' for label, value in filas) + f'''</tbody></table><a class="label-link" href="../{e(etiqueta['archivo'])}">Ver fotografía de la etiqueta →</a></section></div>
<section class="yuka"><h2>Valoración de Yuka</h2>{yuka_texto}</section>
<details><summary>Ingredientes y tabla nutricional del envase</summary>{fotos_etiqueta}</details>
<footer>Recetario personal · <a href="{e(slug)}.md">Archivo maestro</a> · <a href="../index.html">Índice del recetario</a></footer>'''
        maestro.with_suffix('.html').write_text(documento(nombre, contenido, 'productos.css', schema))
        tarjetas.append(f'''<li><article class="product-summary"><a href="productos/{e(slug)}.html"><img class="product-photo" src="{e(imagen['archivo'])}" alt="{e(imagen['alt'])}" {dimensiones(imagen)} loading="lazy"></a><div><span class="tag">{e(data['categoria'])}</span><h2><a href="productos/{e(slug)}.html">{e(nombre)}</a></h2><p class="meta">{e(marca)} · {e(envase)}</p><p>{e(data['descripcion'])}</p><p class="note">{e(resumen_compra)}</p><a href="productos/{e(slug)}.html">Ver producto →</a></div></article></li>''')
    catalogo = '<nav><a href="index.html">← Índice del recetario</a></nav><h1>Productos preferidos</h1><p class="intro">Los productos que uso y por qué. Dónde comprarlos y su precio de referencia.</p><ul class="product-list">' + ''.join(tarjetas) + '</ul><footer>Recetario personal · <a href="index.html">Volver a las recetas</a></footer>'
    (RAIZ / 'productos-preferidos.html').write_text(documento('Productos preferidos', catalogo, 'productos/productos.css'))
    print(f'{len(tarjetas)} producto(s) y catálogo generados. Sin PDF.')


if __name__ == '__main__':
    generar()
