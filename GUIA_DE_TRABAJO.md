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

## Fecha de actualización

Todas las fichas disponibles incluyen `fecha_actualizacion` como cadena ISO `AAAA-MM-DD` en Markdown/YAML y JSON, y `dateModified` con el mismo valor en Schema.org (archivo y bloque integrado en HTML). Inicialización del registro: 2026-10-15. Al crear o modificar el contenido de una ficha, actualizar la fecha según Europe/Madrid. No cambiarla solo por regenerar un PDF o por cambios globales de presentación.

La fecha se muestra únicamente en el PDF, en el pie `Fecha: DD/MM/AAAA`. No mostrarla en el cuerpo de la web, tarjetas ni índice; conservarla solo en sus metadatos. Las tarjetas «Próximamente» aún no son fichas completas y no necesitan este dato hasta desarrollarse.

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

`datos/estado-fichas.json` registra las fichas destacadas como «NUEVA» y las tarjetas futuras «PRÓXIMAMENTE». Al incorporar cualquier ficha nueva disponible, añadir siempre su identificador a `nuevas` y mostrar «NUEVA» en sus tarjetas del índice y de la categoría correspondiente. Aplicar también esta regla cuando una ficha «Próximamente» pase a estar disponible. Las novedades no caducan automáticamente: retirarlas cuando lo indique el usuario.

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

## Ingredientes preferidos

El catálogo está en `ingredientes-preferidos.html`, separado de las recetas. El índice enlaza después del buscador con el texto «Y además, un listado de Ingredientes preferidos →» y la descripción «Los productos que uso y por qué. Dónde comprarlos y su precio de referencia.». El enlace permanece visible aunque la búsqueda no encuentre recetas. No tratar productos como categorías del menú ni incluirlos en el contador del buscador de recetas.

Las fichas de producto usan `tipo_ficha: producto` dentro de `productos/`, con Markdown/YAML maestro que estructura todos los datos, JSON completo, HTML y Schema.org WebPage con Product como entidad principal. Generarlas y actualizar el catálogo mediante `python tools/generar_productos.py`; requiere PyYAML, que ya utiliza el flujo del recetario. No generar PDF de este apartado. No añadirlas a los JSON raíz que procesa el generador de PDF de recetas.

Cada producto conserva nombre, marca, envase y cantidad, motivos para usarlo, uso culinario, composición, nutrición por 100 g, fotografías y su origen, precio de referencia (moneda, fecha, tienda, enlace y €/kg o €/l), puntos de venta, valoración de Yuka (nota, observaciones y fecha de consulta), recetas asociadas y fecha de actualización. Los datos no aportados se guardan como null o listas vacías y se muestran como pendientes; nunca inventar precio, tienda, disponibilidad, puntuación o beneficios para la salud. Al calcular precio por unidad, distinguir peso neto de escurrido. Los precios son referencias fechadas y los motivos personales se distinguen de la composición y de la valoración de Yuka. No convertir Yuka en una valoración propia ni en aggregateRating de Schema.org.

Las fotografías propias de producto se guardan en `images/productos/`. Conservar el envase y la etiqueta legibles: usar object-fit:contain sin aplicar el recorte 16:9 de las fotografías de platos. Enlazar la fotografía completa y la etiqueta original. No inventar autor ni licencia de reutilización.

La fecha de actualización de producto se conserva en sus metadatos y cambia al modificar su contenido, no por cambios de presentación. Las fechas de precio y consulta de Yuka son campos independientes y pueden mostrarse donde corresponda.

En las recetas, el ingrediente puede declarar `producto_preferido` con el identificador de producto. Mantener siempre el nombre genérico del ingrediente en el contenido y convertir solo ese nombre en enlace a la ficha de producto; dejar la cantidad y la nota fuera del enlace. No mostrar marcas ni nombres comerciales en la ficha de comida y no añadir líneas auxiliares como «Mi producto: [marca]». La marca se conserva en la ficha de producto y puede aparecer en los metadatos de la referencia Product. Aplicar el mismo enlace en el Markdown maestro y mantener el ingrediente genérico en JSON y Schema.org Recipe.recipeIngredient. El producto enlaza de vuelta a las recetas en las que se utiliza. Añadir o ajustar estos enlaces sin cambiar la receta no requiere regenerar su PDF ni renovar su fecha de contenido.

Al registrar una captura de Yuka, transcribir puntuación, valoración y observaciones positivas y negativas atribuyéndolas explícitamente a Yuka. Conservar sus datos separados de la etiqueta, incluso si agrupa ingredientes de otra manera. Si no consta la fecha de consulta, mantenerla como null y guardar la fecha de aportación de la captura por separado; no inventar la fecha de consulta.
