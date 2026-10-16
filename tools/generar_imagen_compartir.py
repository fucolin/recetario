#!/usr/bin/env python3
"""Genera la tarjeta social de portada a partir de su ramita SVG original.

Requiere CairoSVG. No modifica recetas, fechas de contenido ni PDF.
"""
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / 'index.html').read_text()
motif = ET.fromstring(re.search(r'<svg class="sprig".*?</svg>', html, re.S).group())
motif.attrib.clear()
motif.attrib.update({'x':'430', 'y':'25', 'width':'340', 'height':'226',
    'viewBox':'-17 -9 116 77', 'fill':'none', 'stroke':'#78977e',
    'stroke-width':'1.25', 'stroke-linecap':'round', 'stroke-linejoin':'round'})
for element in motif.iter('use'):
    element.set('{http://www.w3.org/1999/xlink}href', element.get('href'))
    del element.attrib['href']
svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<rect width="1200" height="630" fill="#ffffff"/>
<g transform="translate(60 74.7) scale(.9)">
MOTIF
<g text-anchor="middle">
<text x="600" y="321" font-family="DejaVu Sans" font-size="38" letter-spacing="7" fill="#245d42">RECETARIO DE</text>
<text x="600" y="487" font-family="DejaVu Serif" font-size="170" letter-spacing="-4" fill="#245d42">Casa Marisa</text>
</g>
</g>
</svg>'''.replace('MOTIF', ET.tostring(motif, encoding='unicode'))
target = ROOT / 'images/casa-marisa-compartir-20261016-v3'
target.with_suffix('.svg').write_text(svg)
cairosvg.svg2png(bytestring=svg.encode(), write_to=str(target.with_suffix('.png')))
print(target.with_suffix('.png'))
