# Formato PDF canónico

Los PDF del recetario se generan con `tools/generar_pdfs.py`. No deben maquetarse a mano.

## Reglas fijas

- Una página A4, sin fotografía. Sin bloque de fuente: la atribución se consulta en la web y se conserva en los archivos maestros.
- Mismo título y línea descriptiva que la página HTML, sin tipo de ficha. Los textos compartidos se conservan en `encabezado.titulo` y `encabezado.detalle` del maestro YAML y JSON; el generador los imprime sin reconstruir raciones, tiempos o variantes.
- Títulos y secciones en verde oscuro.
- Ingredientes sin viñetas y distribuidos en dos columnas.
- Fondo de ingredientes exacto `#F3F6F1`.
- Pasos numerados, bloque `CLAVES` y pie `Fecha: DD/MM/AAAA`.
- Cada JSON debe incluir `pdf_ingredientes`: es la lista editorial exacta que se imprime y evita que una conversión automática altere cantidades o unidades.

Los colores y medidas viven en un solo sitio: las constantes situadas al principio del generador.

## Generar todos los PDF

```bash
python3 -m pip install -r tools/requirements-pdf.txt
python3 tools/generar_pdfs.py
```

Los archivos se crean inicialmente en `build/pdfs`, para que puedan revisarse antes de sustituir los publicados.

Tras revisar los PDF, se pueden generar directamente en la raíz del repositorio:

```bash
python3 tools/generar_pdfs.py --salida .
```

El programa detiene la generación si detecta viñetas, si falta la lista editorial de ingredientes o si el contenido invade el pie de página.

## Enlaces sobre el texto

El campo opcional `enlaces_texto` admite objetos con `texto` y `url`. El generador subraya y enlaza las coincidencias dentro de una línea, por ejemplo «botulismo», sin alterar la plantilla.

## Fecha del pie

El pie obtiene la fecha de `fecha_actualizacion` (cadena ISO `AAAA-MM-DD`) del JSON, nunca de la fecha de generación. Se muestra como `Fecha: DD/MM/AAAA`. El generador exige una fecha válida.
