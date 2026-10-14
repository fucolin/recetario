# Mi recetario · v2

Cuatro versiones de tres recetas. Cada receta tiene:

- `.md`: fuente maestra, YAML estructurado entre `---` y Markdown legible debajo.
- `.html`: página web autónoma, adaptable a móvil e imprimible, con JSON-LD Schema.org/Recipe embebido.
- `.schema.json`: exportación interoperable Schema.org/Recipe (no garantiza importación directa en cualquier app).
- `.json`: exportación de datos completos con ingredientes cuantificados y pasos cronometrados.
- `.pdf`: PDF A4 original del recetario.

Abre `index.html` en un navegador para navegar las recetas. Para publicarlas, sube los HTML a cualquier alojamiento web estático.

Los campos `cantidad_min` y `cantidad_max` expresan rangos; `duracion_min` y `duracion_max_min` están en minutos. Las duraciones de los pasos pueden solaparse, por lo que no deben sumarse para calcular el tiempo total. Los ingredientes al gusto no tienen cantidad numérica. No se han inventado tiempos de preparación separados cuando no constaban en las recetas originales.

**Apps de cocina:** Schema.org/Recipe es un estándar web, no un formato universal de importación. Muchas apps permiten importar recetas desde una URL publicada; otras requieren un formato propio. Los archivos JSON sirven como base para convertir a cada formato cuando elijas la aplicación.
