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
motif.attrib.update({'x':'486', 'y':'72', 'width':'228', 'height':'152',
    'viewBox':'-17 -9 116 77', 'fill':'none', 'stroke':'#78977e',
    'stroke-width':'1.25', 'stroke-linecap':'round', 'stroke-linejoin':'round'})
for element in motif.iter('use'):
    element.set('{http://www.w3.org/1999/xlink}href', element.get('href'))
    del element.attrib['href']
svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<rect width="1200" height="630" fill="#f5f6f1"/>
<rect x="24" y="24" width="1152" height="582" rx="20" fill="#ffffff" stroke="#d5e5d9"/>
<g transform="translate(0 50)">
MOTIF
<g text-anchor="middle">
<text x="600" y="284" font-family="DejaVu Sans" font-size="21" letter-spacing="5" fill="#245d42">RECETARIO DE</text>
<text x="600" y="369" font-family="DejaVu Serif" font-size="76" letter-spacing="-2" fill="#245d42">Casa Marisa</text>
</g>
<path d="M500 425h200" stroke="#d5e5d9" stroke-width="2"/>
</g>
</svg>'''.replace('MOTIF', ET.tostring(motif, encoding='unicode'))
target = ROOT / 'images/casa-marisa-compartir-20261016-v2'
target.with_suffix('.svg').write_text(svg)
cairosvg.svg2png(bytestring=svg.encode(), write_to=str(target.with_suffix('.png')))
print(target.with_suffix('.png'))
