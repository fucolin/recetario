# Guía de trabajo del recetario

Este archivo conserva el procedimiento acordado para seguir trabajando en `fucolin/recetario`, incluso desde una conversación nueva.

## Regla principal

GitHub es la fuente canónica. Cuando el usuario diga «Al recetario», Codex lee o descarga el repositorio y entrega los archivos para que el propietario los suba manualmente. Cuando diga «Al recetario y GitHub» o «ARG» (sin distinguir mayúsculas y minúsculas), autoriza a Codex a preparar, comprobar y subir directamente los cambios al repositorio, desde cualquier dispositivo. Al terminar, Codex entrega un resumen y el enlace al commit. Esta excepción también se aplica cuando el usuario indique «Estoy en el iPhone. Al recetario».

En la modalidad de subida directa no es necesario entregar un ZIP; se mantienen todas las comprobaciones y formatos de la receta.

«ARG» es una alternativa abreviada; la frase completa «Al recetario y GitHub» sigue siendo válida.

## Cuando el usuario diga «Al recetario»

Codex debe completar todo este proceso:

1. Crear o actualizar la receta maestra en Markdown con YAML, incluidos `tipo_ficha` y `categoria_menu`.
2. Crear o actualizar el JSON completo, incluidos `tipo_ficha` y `categoria_menu`. `pdf_ingredientes` solo es obligatorio para las fichas de tipo `receta`.
3. Crear o actualizar el JSON Schema.org `Recipe`.
4. Seleccionar una fotografía adecuada con licencia reutilizable, guardarla localmente y documentar su autoría, fuente y licencia, salvo que el usuario proporcione una fotografía propia.
5. Crear o actualizar la página HTML con fotografía, atribución, datos estructurados `Recipe.image`, ingredientes con fondo `#F3F6F1` y botón `👁️ Más de [categoría]`. Solo las fichas de tipo `receta` muestran además el enlace visible al PDF.
6. Solo para `tipo_ficha: receta`, generar el PDF mediante `tools/generar_pdfs.py`: una página A4, sin fotografía, ingredientes sin viñetas y en dos columnas sobre fondo `#F3F6F1`, títulos verdes, pasos numerados, claves y pie. Las preparaciones sencillas y las combinaciones no generan PDF.
7. Actualizar `index.html` y la página visual de `categorias/` correspondiente, sin crear entradas duplicadas y distinguiendo claramente las variantes.
8. Comprobar ingredientes, cantidades, diferencias entre variantes, licencia de la imagen, datos estructurados, enlaces y presentación visual del HTML y del PDF.
9. Entregar los archivos nuevos o modificados según esta regla:
   - Si son uno o dos archivos y pertenecen a la misma carpeta del repositorio, incluir enlaces directos a cada archivo en el mensaje final del chat. No crear un ZIP.
   - Si los archivos pertenecen a carpetas distintas, preparar siempre un ZIP que conserve la estructura de carpetas, aunque solo sean dos.
   - Si son tres o más archivos, preparar un ZIP y abrirlo en el panel derecho de Codex para que el usuario pueda elegir `⋯` → **Descargar una copia**.

## Añadir una receta

Antes de incorporar una ficha nueva mediante «Al recetario» o «Al recetario y GitHub», Codex debe proponer `tipo_ficha` y `categoria_menu` y esperar la confirmación del usuario. Si ambos ya se han confirmado durante la conversación, no vuelve a preguntarlos. Esta confirmación solo se exige para fichas nuevas; no para actualizaciones de fichas existentes, como sustituir una fotografía.

Primero se afina la receta con el usuario. No se incorpora al repositorio hasta que el usuario diga «Al recetario». Si faltan datos menores, Codex puede proponerlos, pero debe preservar cualquier decisión expresa del usuario.

## Buscador del índice

El índice incluye un buscador que filtra las tarjetas y oculta las categorías vacías. Busca en títulos, categorías, ingredientes, pasos, indicaciones, consejos y claves; ignora tildes y mayúsculas, y exige todas las palabras introducidas. Las variantes permanecen agrupadas en una tarjeta y solo se muestran los enlaces de las variantes coincidentes. Los botones superiores conservan sus enlaces internos a las secciones y se presentan encima del buscador, sin un título adicional y con espacio entre ambos bloques.

Al añadir o modificar una ficha, actualizar también los datos integrados en el bloque `search-data` de `index.html`, a partir de su JSON completo. El mapa usa como claves los nombres de sus páginas HTML y como valores texto de los campos anteriores (más subtítulo, etiquetas y variante), sin créditos fotográficos ni URLs. No requiere `ingredientes_clave`, servicios externos ni peticiones de red al buscar. Si JavaScript está desactivado, el índice completo sigue disponible.

## Formato común de las fotografías

Todas las fotografías de las fichas y de las tarjetas de categorías se muestran en horizontal con relación de aspecto **16:9**, tanto en ordenador como en móvil. Usar `width: 100%`, `height: auto`, `aspect-ratio: 16 / 9` y `object-fit: cover`, sin alturas fijas ni alturas mínimas que alteren esa proporción. El encuadre se centra por defecto; puede ajustarse para preservar el plato o los ingredientes principales. Las imágenes originales se conservan y la presentación aplica el recorte. Para las próximas fotografías propias, el usuario puede encuadrar directamente en 16:9 desde el móvil.

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
- Picoteo y guarniciones
- Otros

Cuando una receta pueda encajar en varias categorías, se elegirá la que resulte más útil para planificar el menú. Las categorías específicas tienen prioridad: por ejemplo, un guiso de lentejas pertenece a `Legumbres` y una tortilla con verduras pertenece a `Huevos`.

`Vegetales` se reserva para platos completos cuyo elemento principal sean las verduras, como menestra, ensaladilla o pisto. Los picoteos, acompañamientos y guarniciones vegetales pertenecen a la categoría específica que mejor describa su uso; por ejemplo, `Picoteo y guarniciones`.

Se crea una página dentro de `categorias/` cuando la categoría contiene al menos una ficha disponible o una tarjeta «Próximamente» expresamente solicitada por el usuario. Estas páginas muestran tarjetas con fotografía, título, tiempo y raciones.

Las variantes de una misma familia se agrupan siempre en una sola tarjeta, tanto en `index.html` como en su página de categoría. La tarjeta muestra los datos compartidos y enlaces separados con nombres breves, por ejemplo `Versión 300 g` y `Versión 400 g`. No se duplican tarjetas con la misma receta y fotografía.

## Novedades y próximas fichas

`datos/estado-fichas.json` registra las fichas que el usuario quiere destacar como «NUEVA» y las tarjetas futuras «PRÓXIMAMENTE». Mostrar los estados en el índice y en la categoría correspondiente. Las novedades no caducan automáticamente: retirar o cambiar la selección cuando lo indique el usuario.

Las próximas fichas se representan como tarjetas sin enlace ni foco de teclado, con aspecto diferenciado y el texto «Ficha aún no disponible». No inventar tiempos, raciones, ingredientes, fotografía o tipo de ficha. No crear todavía Markdown, JSON de receta, Schema.org o PDF. La categoría de estas tarjetas es provisional y se confirma junto con el tipo al desarrollar cada ficha.

El buscador incluye las tarjetas próximas por título y categoría, pero distingue en el contador las fichas disponibles de las previstas. Al publicarse una próxima ficha, sustituir su tarjeta provisional y retirar su entrada de `proximas` para evitar duplicados.

## Tipos de ficha

Toda entrada debe declarar uno de estos tres valores en `tipo_ficha`:

- `receta`: ingredientes, preparación numerada paso a paso y claves opcionales.
- `preparacion`: ingredientes y un bloque breve `indicaciones`, sin pasos numerados; puede incluir `consejo` y no genera PDF.
- `combinacion`: solo ingredientes y cantidades; puede incluir `consejo`, pero no pasos ni indicaciones, y no genera PDF.

La etiqueta visible en el índice y en las páginas de categoría será respectivamente `Receta`, `Preparación sencilla` o `Combinación`. En todas las tarjetas, separar los datos de raciones y tiempo de la etiqueta con `&nbsp;`, manteniendo ambos elementos en línea y sin depender de saltos de línea del HTML. No se crean secciones vacías ni instrucciones de relleno. El HTML muestra `Preparación`, `Indicaciones` o ninguna sección de elaboración según corresponda. El campo YAML `pdf`, el botón de impresión y el archivo PDF se omiten en los otros dos tipos.

En Schema.org se mantiene `@type: Recipe` y `recipeIngredient`. `recipeInstructions` solo se incluye cuando existen pasos o indicaciones reales. La importación de una combinación sin instrucciones depende del comportamiento de la aplicación de destino y debe comprobarse con el primer caso.

## Formato canónico de los PDF

Las reglas técnicas están en [`FORMATO_PDF.md`](FORMATO_PDF.md). Todos los PDF deben generarse con la plantilla común; no deben maquetarse manualmente. Las cantidades y el texto de ingredientes que se imprimen proceden de `pdf_ingredientes`.

## Frase para una conversación nueva

Si fuera necesario empezar otro chat, basta con escribir:

> Quiero continuar trabajando en `fucolin/recetario`. Lee `GUIA_DE_TRABAJO.md` y sigue sus instrucciones. No publiques en GitHub: entrégame un ZIP para subirlo manualmente.
