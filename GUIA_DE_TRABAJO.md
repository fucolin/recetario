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

## Estilo y datos esenciales

- Confirmar `tipo_ficha` y `categoria_menu` antes de incorporar una ficha nueva. No volver a preguntarlos si ya se confirmaron. Cada receta pertenece a una sola categoría.
- Mantener sincronizados Markdown con YAML completo, JSON, Schema.org y HTML. Actualizar PDF, portada, categoría, `datos/estado-fichas.json` y `search-data` según corresponda; no duplicar recetas ni variantes.
- **Ingredientes concisos:** cantidad, unidad e ingrediente; solo aclaraciones breves entre paréntesis cuando sean necesarias. Reparto, corte, uso y momentos de incorporación van en los pasos o en Claves. Conservar el estilo existente.
- Solo `tipo_ficha: receta` genera PDF: una página A4, sin foto, ingredientes en dos columnas sin viñetas sobre `#F3F6F1`, títulos verdes, pasos numerados, claves y fecha al pie. Usar `tools/generar_pdfs.py` y [FORMATO_PDF.md](FORMATO_PDF.md), sin maquetación manual.
- `preparacion` y `combinacion` no llevan PDF. Las fichas de producto usan `tipo_ficha: producto`, van en `productos/` y tampoco generan PDF.
- Fotos de platos en 16:9. En productos, conservar envase y etiqueta legibles con `object-fit: contain`. Documentar procedencia y licencia sin inventarlas; identificar las imágenes generadas con IA.
- Fechar cambios de contenido según Europe/Madrid: `fecha_actualizacion` y `dateModified`. No renovar fecha por presentación o regeneración. Mostrarla solo en el pie del PDF, no en el cuerpo de la web.
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
