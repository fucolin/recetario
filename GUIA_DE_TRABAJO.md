# Guía de trabajo del recetario

Repositorio: `fucolin/recetario`. Web: https://fucolin.github.io/recetario/.
**GitHub es la fuente canónica.** Esta guía recoge las reglas esenciales; el detalle se consulta por temas en [Referencia de trabajo](docs/REFERENCIA_DE_TRABAJO.md).

## Al empezar

1. Leer esta guía y revisar GitHub y el estado local antes de editar. El checkout puede estar atrasado respecto a publicaciones por API; archivos sin seguimiento pueden estar ya publicados. No descartarlos ni subir todo indiscriminadamente.
2. Consultar solo los apartados de referencia relacionados con la tarea; no releer toda la referencia en cada cambio.
3. Preservar los acuerdos del usuario y el estilo de las fichas existentes. Una instrucción actual del usuario prevalece sobre una regla anterior.

## Preparar, mostrar y publicar

- Preparar cambios y vistas previas cuando el usuario lo pide. **Publicar requiere ARG o «Al recetario y GitHub» para los cambios en curso**, sin distinguir mayúsculas. Un ARG anterior no autoriza cambios posteriores. «Dale», «perfecto» o pedir un cambio permiten avanzar en la preparación; no sustituyen ARG. Se aplica también desde el iPhone.
- **Mostrar siempre los cambios antes de publicar.** Cada revisión lleva nombre de archivo y título HTML nuevos y un enlace directo accesible, como los de las fichas. No enlazar al usuario archivos de `build/previews/`: son solo para comprobaciones internas. Excluir todas las copias de revisión de la publicación; la página definitiva conserva su URL.
- Si el usuario ya ha dado ARG para preparar y publicar ese cambio concreto, completar la revisión y publicar sin pedir otra confirmación.
- Publicar solo una lista explícita de archivos afectados. Excluir `build/`, previsualizaciones y temporales. **Los tickets son privados, se guardan aparte y nunca se suben al repositorio.**
- Comprobar datos, sincronización, enlaces y presentación afectados. Reutilizar comprobaciones ya superadas si sus dependencias no cambian; no repetir pruebas ni verificaciones de despliegue sin motivo.
- Al publicar, entregar un resumen y el enlace al commit; no hace falta ZIP.

## Buscadores: web familiar

- Todas las páginas públicas HTML, incluidas categorías, productos y redirecciones, llevan `<meta name="robots" content="noindex, noimageindex">` dentro de `<head>`. Conservarla en plantillas y generadores; no añadir `nofollow` ni bloquear el rastreo con `robots.txt`.
- Antes de publicar, ejecutar `python tools/comprobar_noindex.py` en una copia canónica aislada y comprobar todos los HTML nuevos de la lista explícita. No publicar vistas previas.
- Esto no restringe el acceso por enlace ni hace privado el repositorio. La retirada de resultados depende del rastreador y puede tardar. PDF, imágenes directas y maestros Markdown/JSON no quedan excluidos mediante esta etiqueta HTML. Ver el apartado «Buscadores y alcance» de la referencia.

## Estilo y datos esenciales

- Confirmar `tipo_ficha` y `categoria_menu` antes de incorporar una ficha nueva. No volver a preguntarlos si ya se confirmaron. Cada receta pertenece a una sola categoría.
- Mantener sincronizados Markdown con YAML completo, JSON, Schema.org y HTML. Actualizar PDF, portada, categoría, `datos/estado-fichas.json` y `search-data` según corresponda; no duplicar recetas ni variantes.
- Encabezados de fichas: bajo el título, una línea con descripción breve, técnica o utensilio cuando aporte información, raciones y tiempo. No incluir el tipo de ficha ni copiar los distintivos de las tarjetas. Los PDF llevan el mismo título y línea descriptiva que la web, a partir de `encabezado` en YAML/JSON. La fuente se muestra en la web y se conserva en los archivos maestros; los PDF no llevan imagen ni bloque de fuente. Conservar el tipo en metadatos y tarjetas.
- **Ingredientes concisos:** cantidad, unidad e ingrediente; solo aclaraciones breves entre paréntesis cuando sean necesarias. Reparto, corte, uso y momentos de incorporación van en los pasos o en Claves. Conservar el estilo existente. El texto visible se dirige a quien cocina: incluir solo información relevante para ese lector; no trasladar notas internas, decisiones de edición ni explicaciones de nuestro proceso. La atribución de fuentes debe ser sencilla.
- Solo `tipo_ficha: receta` genera PDF: una página A4, sin foto, ingredientes en dos columnas sin viñetas sobre `#F3F6F1`, títulos verdes, pasos numerados, claves y fecha al pie. Usar `tools/generar_pdfs.py` y [FORMATO_PDF.md](FORMATO_PDF.md), sin maquetación manual.
- `preparacion` y `combinacion` no llevan PDF. Las fichas de producto usan `tipo_ficha: producto`, van en `productos/` y tampoco generan PDF.
- En las fichas nuevas, generar siempre una ilustración ajustada a sus ingredientes, salvo que el usuario aporte una foto propia; no buscar fotografías en la web por defecto. Identificarla como generada con IA. Imágenes de platos en 16:9. En productos, conservar envase y etiqueta legibles con `object-fit: contain`. Documentar procedencia y licencia sin inventarlas; identificar las imágenes generadas con IA.
- Tortillas de casa en las ilustraciones: bajas, poco cuajadas y melosas; ingredientes bien mezclados con el huevo. En la de boniato, láminas finas algo doradas y espinacas integradas, sin capas regulares.
- Ilustraciones de platos: estilo fotorrealista coherente, como fotografiadas en la misma cocina (luz natural cálida, vajilla sencilla clara y superficie neutra). Revisar ingredientes, cortes, textura y técnica de la ficha antes de generar; no añadir guarniciones ajenas.
- Al cambiar la imagen de una ficha, actualizar también la imagen y el texto alternativo de su tarjeta en la categoría y en cualquier otro listado que la muestre; comprobar que ninguna tarjeta siga usando la imagen anterior.
- Fechar cambios de contenido según Europe/Madrid: `fecha_actualizacion` y `dateModified`. No renovar fecha por presentación o regeneración. Mostrarla solo en el pie del PDF, no en el cuerpo de la web.
- Recetas de Eva: procedencia en metadatos (`origen_receta: eva-nutricionista`, autor y fuente); 🌿 accesible «Receta de Eva, nutricionista» al principio de raciones/tiempo en tarjetas. En Fuente: «🌿 Adaptada de una receta de Eva, la nutricionista». Afinar con raciones ajustadas, aceite medido y añadidos moderados. Importar una cada vez: terminar, mostrar y esperar ARG antes de publicar y empezar la siguiente. Generar la ilustración después de acordar ingredientes y preparación; conservar los originales en el catálogo privado. En los archivos públicos, incluir la atribución a Eva sin rutas, nombres ni referencias internas al catálogo privado o sus PDF. Tras publicar, guardar la URL pública en los metadatos del catálogo privado, conservando su versión más reciente y sin añadir marcas visibles desde este flujo.
- Recetas de Marisa: título sin «de Marisa», 💚 al principio de raciones/tiempo y manuscrito ampliable con transcripción fiel. Los ajustes no alteran el original.
- Una ficha nueva lleva «NUEVA» en portada y categoría; retirarla solo cuando lo pida el usuario. Al desarrollar una prevista, sustituir «PRÓXIMAMENTE» y eliminar su entrada provisional.

## Consultar según la tarea

| Tarea | Apartado o archivo |
| --- | --- |
| Recetas: creación, tipos, modificaciones, Marisa, fechas y fotos | [Referencia de recetas](docs/REFERENCIA_DE_TRABAJO.md#preparar-y-sincronizar-una-ficha) |
| Carrusel, clasificación y variantes | [Carrusel y categorías](docs/REFERENCIA_DE_TRABAJO.md#carrusel-semanal-y-categorías) |
| Contenido del carrusel | `semana-base.md` → `datos/semana-base.json` e `index.html`; `tools/generar_semana_base.py`; prueba `tools/comprobar_semana_base.cjs` |
| Novedades y previstas | [Novedades y próximas fichas](docs/REFERENCIA_DE_TRABAJO.md#novedades-y-próximas-fichas) |
| Portada, logo, imagen social y filtros | [Portada y buscador](docs/REFERENCIA_DE_TRABAJO.md#portada-imagen-social-y-buscador); prueba `tools/comprobar_filtros_categorias.cjs` |
| Productos, etiquetas, Yuka y precios | [Productos preferidos](docs/REFERENCIA_DE_TRABAJO.md#productos-preferidos); `tools/generar_productos.py` |
| Verduras y tomate | [Calendario de verduras](docs/REFERENCIA_DE_TRABAJO.md#calendario-de-verduras-de-temporada) |
| Frutas | [Calendario de frutas](docs/REFERENCIA_DE_TRABAJO.md#calendario-de-frutas-de-temporada) |

## Entrega manual: «Al recetario» sin ARG

Preparar y comprobar los archivos para que el usuario los suba. Si son uno o dos y están en la misma carpeta, entregar enlaces directos sin ZIP. Si están en carpetas distintas, o son tres o más, entregar un ZIP que conserve la estructura y permita descargarlo.

## Para continuar en otro hilo

> Continuamos con Recetario de Casa Marisa, repositorio `fucolin/recetario`. Lee `GUIA_DE_TRABAJO.md` y consulta solo la referencia necesaria. GitHub es la fuente canónica. Muéstrame los cambios con nombre y título nuevos; publica solo cuando diga ARG.

## Excepción acordada: diagrama de burritos

El PDF de burritos incorpora seis imágenes numeradas en dos filas de tres, sin pies de imagen. Sus pasos principales no se numeran; la web conserva las indicaciones bajo cada imagen. Se mantiene una página A4 y el encabezado común. Configuración en `pdf_diagrama` y `pdf_numerar_pasos` del maestro; usar el generador común.
