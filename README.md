# Mi recetario

🌐 **Web publicada:** [https://fucolin.github.io/recetario/](https://fucolin.github.io/recetario/)

El recetario reúne recetas, preparaciones sencillas y combinaciones para organizar el menú semanal. Cada ficha tiene:

- `.md`: fuente maestra, YAML estructurado entre `---` y Markdown legible debajo.
- `.html`: página web autónoma y adaptable a móvil, con fotografía acreditada y JSON-LD Schema.org/Recipe embebido.
- `.schema.json`: exportación interoperable Schema.org/Recipe (no garantiza importación directa en cualquier app).
- `.json`: exportación de datos completos con ingredientes cuantificados y, cuando corresponde, pasos o indicaciones.
- `.pdf`: PDF A4 sin fotografía para las fichas de tipo `receta`; las preparaciones sencillas y las combinaciones no generan PDF.

Los PDF se generan siempre con la plantilla compartida `tools/generar_pdfs.py`. Las reglas de diseño y las instrucciones de uso están en [`FORMATO_PDF.md`](FORMATO_PDF.md); no deben maquetarse manualmente.

El procedimiento completo para añadir recetas, sustituir fotografías y mantener todas las versiones sincronizadas está en [`GUIA_DE_TRABAJO.md`](GUIA_DE_TRABAJO.md).

El recetario admite tres tipos de ficha: recetas con pasos, preparaciones sencillas con indicaciones breves y combinaciones de ingredientes sin elaboración.

Las fotografías se guardan en `images/`; sus autores, fuentes y licencias se documentan en [`IMAGENES_Y_LICENCIAS.md`](IMAGENES_Y_LICENCIAS.md). La URL pública de cada imagen figura en el YAML y en la propiedad `image` de Schema.org para facilitar la importación desde una URL publicada.

Abre `index.html` en un navegador para navegar las recetas. Para publicarlas, sube los HTML a cualquier alojamiento web estático.

Los campos `cantidad_min` y `cantidad_max` expresan rangos; `duracion_min` y `duracion_max_min` están en minutos. Las duraciones de los pasos pueden solaparse, por lo que no deben sumarse para calcular el tiempo total. Los ingredientes al gusto no tienen cantidad numérica. No se han inventado tiempos de preparación separados cuando no constaban en las recetas originales.

**Apps de cocina:** Schema.org/Recipe es un estándar web, no un formato universal de importación. Muchas apps permiten importar recetas desde una URL publicada; otras requieren un formato propio. Los archivos JSON sirven como base para convertir a cada formato cuando elijas la aplicación.


## Ingredientes preferidos

Catálogo independiente: [Ingredientes preferidos](ingredientes-preferidos.html). Fichas de producto en `productos/`, con maestro Markdown/YAML, JSON, HTML y datos estructurados. No generan PDF.

Para actualizar las fichas y el catálogo desde los maestros:

```bash
python tools/generar_productos.py
```
