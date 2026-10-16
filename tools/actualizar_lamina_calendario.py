#!/usr/bin/env python3
"""Actualiza solo la lámina inicial del calendario según el mes en Galicia."""
from datetime import datetime
from html import escape
import json
from pathlib import Path
import re
from zoneinfo import ZoneInfo

RAIZ = Path(__file__).resolve().parent.parent


def actualizar_html(contenido, mes):
    nombre = mes['nombre'].lower()
    url = escape(mes['archivo_lamina'], quote=True)
    bloque = re.search(r'<!-- LAMINA_ACTUAL_INICIO -->.*?<!-- LAMINA_ACTUAL_FIN -->', contenido, re.S)
    if bloque is None:
        raise ValueError('No se encuentra el bloque de la lámina mensual')
    nuevo = bloque.group(0)
    nuevo = re.sub(r'(id="lamina-(?:enlace|ampliar)" href=")[^"]*', lambda m: m[1] + url, nuevo)
    nuevo = re.sub(r'(id="lamina-imagen" src=")[^"]*', lambda m: m[1] + url, nuevo)
    nuevo = re.sub(r'aria-label="Abrir lámina de [^"]*"', 'aria-label="Abrir lámina de ' + escape(nombre) + ' a tamaño completo (nueva pestaña)"', nuevo)
    nuevo = re.sub(r'alt="Verduras y hortalizas de temporada en [^"]*"', 'alt="Verduras y hortalizas de temporada en ' + escape(nombre) + ' · Codinugal"', nuevo)
    return contenido[:bloque.start()] + nuevo + contenido[bloque.end():]


def main():
    datos = json.loads((RAIZ / 'datos/calendario-verduras-temporada.json').read_text())
    numero = datetime.now(ZoneInfo('Europe/Madrid')).month
    mes = next(m for m in datos['meses'] if m['numero'] == numero)
    pagina = RAIZ / 'calendario-verduras-temporada.html'
    original = pagina.read_text()
    actualizado = actualizar_html(original, mes)
    if actualizado != original:
        pagina.write_text(actualizado)
        print('Lámina inicial actualizada: ' + mes['nombre'])
    else:
        print('La lámina inicial ya corresponde a ' + mes['nombre'].lower())


if __name__ == '__main__':
    main()
