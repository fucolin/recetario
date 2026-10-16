# Referencia de trabajo del recetario

Detalle por temas de [la guía principal](../GUIA_DE_TRABAJO.md). Consultar solo los apartados relacionados con la tarea. La autorización, revisión y entrega se rigen por la guía principal.

## Preparar y sincronizar una ficha

Para una ficha nueva, completar este proceso. Para una actualización, actuar sobre las representaciones afectadas:

1. Crear o actualizar la receta maestra en Markdown con YAML, incluidos `tipo_ficha` y `categoria_menu`.
2. Crear o actualizar el JSON completo, incluidos `tipo_ficha` y `categoria_menu`. `pdf_ingredientes` solo es obligatorio para las fichas de tipo `receta`.
3. Crear o actualizar el JSON Schema.org `Recipe`.
4. Para las fichas nuevas, generar una ilustración original ajustada a los ingredientes y al plato, salvo que el usuario aporte una fotografía propia. No buscar imágenes en la web por defecto. Guardar el recurso en `images/`, registrar su origen y mostrar que es una imagen ilustrativa generada con IA, sin atribuir autoría fotográfica ni una licencia Creative Commons inventada. Usar fotografías propias cuando se aporten.
5. Crear o actualizar la página HTML con fotografía, atribución, datos estructurados `Recipe.image`, ingredientes con fondo `#F3F6F1` y botón «Más de [categoría]» con icono SVG de cuadrícula. Solo las fichas de tipo `receta` muestran además el enlace visible al PDF.
6. Solo para `tipo_ficha: receta`, generar el PDF mediante `tools/generar_pdfs.py`: una página A4, sin fotografía, ingredientes sin viñetas y en dos columnas sobre fondo `#F3F6F1`, títulos verdes, pasos numerados, claves y pie. Las preparaciones sencillas y las combinaciones no generan PDF.
7. Actualizar `index.html` y la página visual de `categorias/` correspondiente, sin crear entradas duplicadas y distinguiendo claramente las variantes.
8. Comprobar ingredientes, cantidades, diferencias entre variantes, licencia de la imagen, datos estructurados, enlaces y presentación visual del HTML y del PDF.

## Añadir una receta

Antes de incorporar una ficha nueva mediante «Al recetario» o «Al recetario y GitHub», Codex debe proponer `tipo_ficha` y `categoria_menu` y esperar la confirmación del usuario. Si ambos ya se han confirmado durante la conversación, no vuelve a preguntarlos. Esta confirmación solo se exige para fichas nuevas; no para actualizaciones de fichas existentes, como sustituir una fotografía.

Primero se afina la receta con el usuario. Se pueden preparar archivos y vistas previas durante la revisión; publicar requiere ARG para los cambios en curso. Si faltan datos menores, Codex puede proponerlos, pero debe preservar cualquier decisión expresa del usuario.

## Tipos de ficha

Toda entrada debe declarar uno de estos tres valores en `tipo_ficha`:

- `receta`: ingredientes, preparación numerada paso a paso y claves opcionales.
- `preparacion`: ingredientes y un bloque breve `indicaciones`, sin pasos numerados; puede incluir `consejo` y no genera PDF.
- `combinacion`: solo ingredientes y cantidades; puede incluir `consejo`, pero no pasos ni indicaciones, y no genera PDF.

La etiqueta visible en el índice y en las páginas de categoría será respectivamente `Receta`, `Preparación sencilla` o `Combinación`. En todas las tarjetas, separar los datos de raciones y tiempo de la etiqueta con `&nbsp;`, manteniendo ambos elementos en línea y sin depender de saltos de línea del HTML. No se crean secciones vacías ni instrucciones de relleno. El HTML muestra `Preparación`, `Indicaciones` o ninguna sección de elaboración según corresponda. El campo YAML `pdf`, el botón de impresión y el archivo PDF se omiten en los otros dos tipos.

En Schema.org se mantiene `@type: Recipe` y `recipeIngredient`. `recipeInstructions` solo se incluye cuando existen pasos o indicaciones reales. La importación de una combinación sin instrucciones depende del comportamiento de la aplicación de destino y debe comprobarse con el primer caso.

## Modificar una receta existente

Las recetas de Marisa no añaden «de Marisa» al título. Identificarlas en sus tarjetas del índice y de categorías con un 💚 al principio de la línea de raciones y tiempo, nunca junto al título; el icono lleva nombre accesible «Receta de Marisa». Justo después del bloque del buscador, mostrar una nota discreta: «Las recetas de Marisa, pulidas con mimo durante toda una vida, llevan un 💚». Conservar la autoría, el manuscrito y su transcripción dentro de cada ficha.

Las recetas de Marisa conservan al final de la página «La receta original de Marisa»: la fotografía aportada de su manuscrito, alojada en el repositorio y ampliable al pulsarla, sin recortes, más una transcripción fiel. Guardar ambos en `original_marisa` dentro del maestro YAML y el JSON completo. Los ajustes posteriores van en la receta principal y se explican sin reescribir el original. El PDF habitual sigue siendo una página A4 sin fotografías; el manuscrito se consulta en la web. Primera ficha: `crema-aprovechamiento-marisa`, categoría Purés; regenerar sus representaciones con `python tools/generar_receta_marisa.py`. No atribuir al manuscrito datos aportados después, como la temperatura actual de 90–100 °C o una combinación concreta de verduras.

Codex debe actualizar todas las representaciones afectadas para que no queden contradicciones: Markdown/YAML, JSON, Schema.org, HTML y PDF. Si cambia el nombre, la categoría o las variantes, también debe actualizar el índice y comprobar los enlaces.

Si el usuario solo está afinando o probando, respetar ese alcance: preparar lo necesario para revisar, sin publicar.

## Fecha de actualización

Todas las fichas disponibles incluyen `fecha_actualizacion` como cadena ISO `AAAA-MM-DD` en Markdown/YAML y JSON, y `dateModified` con el mismo valor en Schema.org (archivo y bloque integrado en HTML). Inicialización del registro: 2026-10-15. Al crear o modificar el contenido de una ficha, actualizar la fecha según Europe/Madrid. No cambiarla solo por regenerar un PDF o por cambios globales de presentación.

La fecha se muestra únicamente en el PDF, en el pie `Fecha: DD/MM/AAAA`. No mostrarla en el cuerpo de la web, tarjetas ni índice; conservarla solo en sus metadatos. Las tarjetas «Próximamente» aún no son fichas completas y no necesitan este dato hasta desarrollarse.

## Formato canónico de los PDF

Las reglas técnicas están en [`FORMATO_PDF.md`](../FORMATO_PDF.md). Todos los PDF deben generarse con la plantilla común; no deben maquetarse manualmente. Las cantidades y el texto de ingredientes que se imprimen proceden de `pdf_ingredientes`.

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

## Carrusel semanal y categorías

Si una comida o cena tiene dos platos, dividir su celda en dos columnas con separador vertical: cada tipo en negrita y su ejemplo debajo. No apilar los platos ni colocar un signo más entre bloques. Mantener el carrusel compacto, con menor altura mínima en móvil, sin recortar el texto ni los enlaces.

La portada incorpora el plan semanal debajo del encabezado, SIN el título visible «Mi semana base»: carrusel circular en escritorio y móvil, con tres días completos visibles en escritorio y el día actual de Europe/Madrid centrado inicialmente. En móvil se conserva una tarjeta central con un pequeño avance de las laterales. Botones anterior/Hoy/siguiente, avance de un día y continuidad domingo–lunes en ambos sentidos. Se reordenan los siete nodos originales al terminar el desplazamiento, sin duplicar fichas, enlaces ni identificadores. Mantener centrado el día elegido al redimensionar. Lógica fuente en `tools/semana_base.js`, incrustada por el generador; comprobar con `node tools/comprobar_semana_base.cjs`. Señalar el día actual solo con el color de su cabecera, sin etiqueta «Hoy» en esa celda; mantener `aria-current` para accesibilidad. No mostrar «Más recetas…» ni su enlace interno. Después del carrusel va «Para elegir y comprar» y, a continuación, el catálogo con un título grande «Las recetas» antes de la botonera, el buscador y el listado. Fondo verde suave, sin fotografías ni desplegable. Mantener lunes–domingo y comida/cena alineadas. Los tipos de plato se muestran en negrita SIN enlace; debajo de cada uno, un ejemplo real con enlace a su ficha disponible de la categoría correspondiente. No sustituir un subtipo preciso (tortilla francesa) por otro. Si el usuario ya ha elegido un ejemplo pero aún no existe su ficha, mostrar su nombre como texto sin enlace; «Ejemplo pendiente» solo si no ha elegido ejemplo. «Libre» queda sin ejemplo ni mensaje pendiente. Los ejemplos compuestos pueden declarar `componentes` con enlaces independientes; una guarnición puede enlazar a su propia categoría declarada. No crear recetas ni tarjetas futuras por aparecer en la semana base. Maestro `semana-base.md` con YAML completo (texto, categoría y ejemplo) y espejo `datos/semana-base.json`. Regenerar el bloque delimitado de `index.html` con `python tools/generar_semana_base.py`, que valida categorías y páginas. Preservar los textos personales y los dos componentes de una misma comida o cena. Respetar movimiento reducido y permitir deslizar sin JavaScript, conservando todos los días. No incluir el bloque en filtros ni contadores de recetas; no generar PDF ni tratarlo como ficha Recipe. Es una guía personal de distribución, no un menú fechado ni una evaluación nutricional.

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

## Portada, imagen social y buscador

La caja de búsqueda no lleva un rótulo visible encima. Conservar `aria-label="Buscar recetas"` en el campo y empezar la ayuda inferior con «Busca» en negrita.

La portada se titula «Recetario de Casa Marisa», también en la pestaña del navegador. Su encabezado centrado es un homenaje a la madre del usuario: «Recetario de» pequeño sobre «Casa Marisa» en tipografía de libro, verde, con una ramita SVG original inspirada en la hierba luisa (hojas estrechas y alargadas agrupadas alrededor del tallo). Subtítulo en dos líneas: «Recetas afinadas para comer bien cada día.» / «Ideas de temporada para el menú semanal.». Mantener la adaptación a móvil y permitir que el texto fluya si el usuario amplía la letra.

La ramita lleva pequeñas flores blancas con trazo lila suave y se presenta casi horizontal, inclinada 65 grados respecto a su dibujo inicial. La portada incluye metadatos Open Graph y tarjeta social con URL absoluta, título, descripción e imagen PNG de 1200 × 630. `python tools/generar_imagen_compartir.py` (CairoSVG) genera `images/casa-marisa-compartir-20261016.svg` y `.png` a partir de la ramita de `index.html`. Mantener encabezado e imagen de compartir coherentes; si se cambia la imagen publicada, versionar su nombre y actualizar las URLs para facilitar la renovación de caché. No prometer el aspecto exacto en WhatsApp antes de comprobarlo tras publicar: la presentación final depende de la aplicación. No extender estos metadatos a recetas sin ajustar título, descripción e imagen de cada página.

La imagen social de portada usa ahora `images/casa-marisa-compartir-20261016-v3.png` y su SVG fuente, generados por `tools/generar_imagen_compartir.py`. Mostrar únicamente ramita y nombre del recetario sobre blanco, sin marco ni filete y con margen alrededor; conservar el subtítulo completo en `og:description` y `twitter:description`, además de en el encabezado visible de la web.

El índice incluye un buscador que filtra las tarjetas y oculta las categorías vacías. Busca en títulos, categorías, ingredientes, pasos, indicaciones, consejos y claves; ignora tildes y mayúsculas, y exige todas las palabras introducidas. Las variantes permanecen agrupadas en una tarjeta y solo se muestran los enlaces de las variantes coincidentes. La botonera, encima del buscador, permite seleccionar varias categorías mediante botones con `aria-pressed`. «Todas» va primero y está activo al entrar. Pulsar una categoría activa la selección; otras se suman; pulsarlas otra vez las quita. Sin categorías seleccionadas vuelve a estar activo «Todas». «Todas» reinicia solo las categorías, conserva el texto de búsqueda. Buscar, limpiar texto o pulsar Escape conserva la selección de categorías. Ocultar categorías sin coincidencias en listado y botonera, salvo las seleccionadas, que siguen visibles para poder desmarcarlas. Los botones de otras categorías con coincidencias de texto siguen disponibles aunque no estén seleccionadas. Mantener siempre «Todas» accesible, incluso sin resultados. Sin JavaScript, las categorías conservan sus enlaces internos y se ve el catálogo completo. Comprobar cambios de lógica con `node tools/comprobar_filtros_categorias.cjs`.

Al añadir o modificar una ficha, actualizar también los datos integrados en el bloque `search-data` de `index.html`, a partir de su JSON completo. El mapa usa como claves los nombres de sus páginas HTML y como valores texto de los campos anteriores (más subtítulo, etiquetas y variante), sin créditos fotográficos ni URLs. No requiere `ingredientes_clave`, servicios externos ni peticiones de red al buscar. Si JavaScript está desactivado, el índice completo sigue disponible.

## Productos preferidos

La pestañita «Para elegir y comprar» de la portada se presenta en negativo: fondo verde del recetario y texto blanco.

El catálogo está en `productos-preferidos.html`, separado de las recetas. El índice enlaza justo debajo del carrusel, antes del catálogo de recetas, en un recuadro de tres recursos, con el título «Para elegir y comprar» encajado en el borde superior como una pestañita decorativa, sin comportamiento de botón. El enlace se llama «Productos preferidos», precedido por un icono de cesta de la compra, y lleva la descripción «Por qué los uso. Dónde comprarlos y su precio de referencia». Los otros dos enlaces son «Verduras de temporada» y «Frutas de temporada», cada uno precedido por un icono de calendario. Usar iconos SVG de línea con estilo uniforme. Presentar los tres en columnas en escritorio, con separadores verticales; en móvil, lista apilada con separadores horizontales. Conservar las flechas en columna propia para que no salten solas a otra línea. El bloque permanece visible aunque la búsqueda no encuentre recetas. No tratar estos recursos como categorías del menú ni incluirlos en el contador del buscador de recetas.

Las fichas de producto usan `tipo_ficha: producto` dentro de `productos/`, con Markdown/YAML maestro que estructura todos los datos, JSON completo, HTML y Schema.org WebPage con Product como entidad principal. Generarlas y actualizar el catálogo mediante `python tools/generar_productos.py`; requiere PyYAML, que ya utiliza el flujo del recetario. No generar PDF de este apartado. No añadirlas a los JSON raíz que procesa el generador de PDF de recetas.

Cada producto conserva nombre, marca, envase y cantidad, motivos para usarlo, uso culinario, composición, nutrición por 100 g, fotografías y su origen, precio de referencia (moneda, fecha, tienda, enlace y €/kg o €/l), puntos de venta, valoración de Yuka (nota, observaciones y fecha de consulta), recetas asociadas y fecha de actualización. Los datos no aportados se guardan como null o listas vacías y se muestran como pendientes; nunca inventar precio, tienda, disponibilidad, puntuación o beneficios para la salud. Al calcular precio por unidad, distinguir peso neto de escurrido. Los precios son referencias fechadas y los motivos personales se distinguen de la composición y de la valoración de Yuka. No convertir Yuka en una valoración propia ni en aggregateRating de Schema.org.

Las fotografías propias de producto se guardan en `images/productos/`. Conservar el envase y la etiqueta legibles: usar object-fit:contain sin aplicar el recorte 16:9 de las fotografías de platos. Enlazar la fotografía completa y la etiqueta original. No inventar autor ni licencia de reutilización.

La fecha de actualización de producto se conserva en sus metadatos y cambia al modificar su contenido, no por cambios de presentación. Las fechas de precio y consulta de Yuka son campos independientes y pueden mostrarse donde corresponda.

En las recetas, el ingrediente puede declarar `producto_preferido` con el identificador de producto. Mantener siempre el nombre genérico del ingrediente en el contenido y convertir solo ese nombre en enlace a la ficha de producto; dejar la cantidad y la nota fuera del enlace. No mostrar marcas ni nombres comerciales en la ficha de comida y no añadir líneas auxiliares como «Mi producto: [marca]». La marca se conserva en la ficha de producto y puede aparecer en los metadatos de la referencia Product. Aplicar el mismo enlace en el Markdown maestro y mantener el ingrediente genérico en JSON y Schema.org Recipe.recipeIngredient. El producto enlaza de vuelta a las recetas en las que se utiliza. Añadir o ajustar estos enlaces sin cambiar la receta no requiere regenerar su PDF ni renovar su fecha de contenido.

Al registrar una captura de Yuka, transcribir puntuación, valoración y observaciones positivas y negativas atribuyéndolas explícitamente a Yuka. Conservar sus datos separados de la etiqueta, incluso si agrupa ingredientes de otra manera. Si no consta la fecha de consulta, mantenerla como null y guardar la fecha de aportación de la captura por separado; no inventar la fecha de consulta.

Registrar las promociones comunicadas por el usuario por separado del precio habitual, con tienda, fecha de observación, condiciones y cálculo del precio efectivo. Mostrar las promociones pasadas como históricas, sin inferir que siguen vigentes ni inventar fechas de fin. Identificar si el precio es aportado por el usuario o consultado en una tienda.

## Calendario de verduras de temporada

Página de referencia: `calendario-verduras-temporada.html`, enlazada desde el índice fuera de las tarjetas y del buscador de recetas. Maestro Markdown/YAML: `calendario-verduras-temporada.md`; datos estructurados idénticos en `datos/calendario-verduras-temporada.json`. Mantener los tres sincronizados. Fuente: las doce láminas de Codinugal, con enlace general; los originales mensuales se conservan como URLs en los datos. No mostrar enlaces a la lámina dentro de cada sección mensual. La agrupación es propia. Conservar la advertencia: el origen gallego de la entidad no garantiza cosecha local gallega al aire libre. No inventar plena temporada/inicio/final, ni incorporar patata o boniato sin otra fuente. No generar PDF ni tratar esta página como una receta o categoría del menú. El mes actual se destaca según Europe/Madrid sin ocultar los demás. Tras la botonera, mostrar su lámina con enlace para abrirla a tamaño completo en una nueva pestaña. Mantener la nota de alcance dentro de «Cómo usar este calendario», al final. JavaScript elige la lámina al cargar; `python tools/actualizar_lamina_calendario.py` renueva la imagen inicial para navegación sin JavaScript y la subida mensual autorizada a GitHub. No renovar la fecha de contenido por este cambio de presentación.

El bloque de la lámina se titula «Este mes…», sin pie; la propia imagen es el enlace de ampliación y lleva una lupa superpuesta. Guardar las doce láminas originales en `images/calendario-verduras/`. Tanto `src` como el enlace ampliado usan el campo `archivo_lamina` (mismo servidor); `fuente_lamina` conserva la procedencia original solo como metadato. No renovar la fecha de contenido por cambios visuales o mensuales. Para las revisiones, entregar una copia de vista previa con nombre único para evitar versiones en caché; no publicar esas copias.

Tras el bloque «Este mes…», mostrar una tabla con una única cabecera «Mis verduras favoritas» (colspan=2), sin título exterior ni encabezados individuales de columna: verduras presentes en las fichas disponibles (incluida lechuga como alternativa), sin champiñones ni advertencias adicionales en ese bloque. Los datos están en `verduras_favoritas` del maestro y JSON del calendario. Unificar singular/plural y variedades de tomate y pimiento. Presentar intervalos continuos que crucen el año como «diciembre–julio», no «enero–julio y diciembre»; lo mismo para «septiembre–julio» y «mayo–enero». Revisar esta lista al añadir recetas.

«La cuestión del tomate» (`la-cuestion-del-tomate.html`) es una página de referencia enlazada desde el calendario, tras la tabla de verduras favoritas. Conserva las propuestas culinarias acordadas, sin convertirlas en recetas completas ni atribuirlas a Codinugal. Maestro `la-cuestion-del-tomate.md`, datos idénticos en `datos/la-cuestion-del-tomate.json`; sin PDF ni cambios automáticos en recetas existentes.

La categoría Ensaladas muestra también el mismo recuadro «La cuestión del tomate», tras la introducción y antes de sus tarjetas. Mantener su diseño y texto iguales al recuadro del calendario, ajustando solo la ruta relativa del enlace.

## Calendario de frutas de temporada

Referencia `calendario-frutas-temporada.html`, maestro Markdown/YAML homónimo y JSON idéntico en `datos/`. Regenerar con `python tools/generar_calendario_frutas.py`. Enlazar desde el índice fuera del buscador y del contador de recetas. No generar PDF. Prioridad: origen España y cosecha gallega cuando exista referencia documentada. Mantener fuentes por fruta; distinguir ventanas de compra españolas de cosechas locales y fruta de conservación. Una lista gallega vacía no implica ausencia de cultivo. No extrapolar una variedad a todas las variedades, la vendimia a uva de mesa ni la marca a origen. Agrupar intervalos que crucen el año (diciembre–mayo). «Este mes…» se adapta al mes Europe/Madrid con JavaScript y conserva contenido inicial sin él; no precisa publicación mensual para funcionar. Regenerar el contenido inicial si se revisa la página, sin renovar fecha por mero formato o cambio de mes. No extender la automatización del calendario de verduras a esta página sin autorización. Para revisión usar `--preview` con un nombre único; no publicar copias de `build/previews/`.

## Iconos de los botones de las fichas

Los botones de PDF y «Más de [categoría]» usan SVG de línea, del mismo estilo que los recursos de portada: `viewBox="0 0 24 24"`, sin relleno, trazo `currentColor` de 1.8 y extremos/uniones redondeados. Impresora para PDF y cuadrícula para categoría. Tamaño 1 em y margen derecho .4 em. Los SVG son decorativos (`aria-hidden="true"`, `focusable="false"`); conservar el texto visible de cada botón. No usar emojis en estos botones. Este cambio de presentación no renueva las fechas de contenido ni los PDF.
