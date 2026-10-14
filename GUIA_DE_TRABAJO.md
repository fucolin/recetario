# Guía de trabajo del recetario

Este archivo conserva el procedimiento acordado para seguir trabajando en `fucolin/recetario`, incluso desde una conversación nueva.

## Regla principal

Codex puede utilizar la conexión de GitHub para leer o descargar el repositorio, pero no debe publicar ni modificar nada directamente en GitHub. Al terminar cada cambio, debe entregar los archivos para que el propietario los suba manualmente, siguiendo la regla de entrega indicada más abajo.

## Cuando el usuario diga «Al recetario»

Codex debe completar todo este proceso:

1. Crear o actualizar la receta maestra en Markdown con YAML.
2. Crear o actualizar el JSON completo, incluidos `categoria_menu` y la lista editorial `pdf_ingredientes`.
3. Crear o actualizar el JSON Schema.org `Recipe`.
4. Seleccionar una fotografía adecuada con licencia reutilizable, guardarla localmente y documentar su autoría, fuente y licencia, salvo que el usuario proporcione una fotografía propia.
5. Crear o actualizar la página HTML con fotografía, atribución, datos estructurados `Recipe.image`, ingredientes con fondo `#F3F6F1`, enlace visible al PDF y botón `👁️ Más de [categoría]` junto al botón de impresión.
6. Generar el PDF mediante `tools/generar_pdfs.py`: una página A4, sin fotografía, ingredientes sin viñetas y en dos columnas sobre fondo `#F3F6F1`, títulos verdes, pasos numerados, claves y pie.
7. Actualizar `index.html` y la página visual de `categorias/` correspondiente, sin crear entradas duplicadas y distinguiendo claramente las variantes.
8. Comprobar ingredientes, cantidades, diferencias entre variantes, licencia de la imagen, datos estructurados, enlaces y presentación visual del HTML y del PDF.
9. Entregar los archivos nuevos o modificados según esta regla:
   - Si son uno o dos archivos, incluir enlaces directos a cada archivo en el mensaje final del chat. No crear un ZIP.
   - Si son tres o más archivos, preparar un ZIP y abrirlo en el panel derecho de Codex para que el usuario pueda elegir `⋯` → **Descargar una copia**.

## Añadir una receta

Primero se afina la receta con el usuario. No se incorpora al repositorio hasta que el usuario diga «Al recetario». Si faltan datos menores, Codex puede proponerlos, pero debe preservar cualquier decisión expresa del usuario.

## Sustituir una fotografía por una foto propia

Cuando el usuario adjunte una fotografía propia, Codex debe:

- Prepararla para la web sin cambiar innecesariamente su encuadre.
- Guardarla dentro de `images/` con un nombre estable.
- Actualizar Markdown/YAML, HTML, JSON y Schema.org `Recipe.image`.
- Retirar la atribución anterior y registrar que la fotografía es propia, sin inventar autor o licencia.
- Mantener el PDF sin fotografía.
- Entregar solamente los archivos afectados.

## Modificar una receta existente

Codex debe actualizar todas las representaciones afectadas para que no queden contradicciones: Markdown/YAML, JSON, Schema.org, HTML y PDF. Si cambia el nombre, la categoría o las variantes, también debe actualizar el índice y comprobar los enlaces.

Si el usuario indica que solo está afinando o probando un cambio, no se preparará la actualización del repositorio hasta que diga «Al recetario».

## Categorías del menú semanal

Cada receta debe pertenecer a una sola `categoria_menu`. La clasificación oficial es:

- Vegetales
- Legumbres
- Pescado azul
- Pescado blanco
- Purés
- Ensaladas
- Huevos
- Mariscos
- Guisos y asados
- Carnes exprés
- Arroces y pastas
- Envueltos y bocados
- Otros

Cuando una receta pueda encajar en varias categorías, se elegirá la que resulte más útil para planificar el menú. Las categorías específicas tienen prioridad: por ejemplo, un guiso de lentejas pertenece a `Legumbres` y una tortilla con verduras pertenece a `Huevos`.

Solo se crea una página dentro de `categorias/` cuando la categoría contiene al menos una receta. Estas páginas muestran tarjetas con fotografía, título, tiempo y raciones.

Las variantes de una misma familia se agrupan siempre en una sola tarjeta, tanto en `index.html` como en su página de categoría. La tarjeta muestra los datos compartidos y enlaces separados con nombres breves, por ejemplo `Versión 300 g` y `Versión 400 g`. No se duplican tarjetas con la misma receta y fotografía.

## Formato canónico de los PDF

Las reglas técnicas están en [`FORMATO_PDF.md`](FORMATO_PDF.md). Todos los PDF deben generarse con la plantilla común; no deben maquetarse manualmente. Las cantidades y el texto de ingredientes que se imprimen proceden de `pdf_ingredientes`.

## Frase para una conversación nueva

Si fuera necesario empezar otro chat, basta con escribir:

> Quiero continuar trabajando en `fucolin/recetario`. Lee `GUIA_DE_TRABAJO.md` y sigue sus instrucciones. No publiques en GitHub: entrégame un ZIP para subirlo manualmente.
