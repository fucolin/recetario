# Guía de trabajo del recetario

Repositorio: `fucolin/recetario`. Web: https://fucolin.github.io/recetario/.
**GitHub es la fuente canónica.** Esta guía recoge las reglas esenciales; el detalle se consulta por temas en [Referencia de trabajo](docs/REFERENCIA_DE_TRABAJO.md).

## Al empezar

1. Leer esta guía y revisar GitHub y el estado local antes de editar. El checkout puede estar atrasado respecto a publicaciones por API; archivos sin seguimiento pueden estar ya publicados. No descartarlos ni subir todo indiscriminadamente.
2. Consultar solo los apartados de referencia relacionados con la tarea; no releer toda la referencia en cada cambio.
3. Leer `CONTINUAR_EN_OTRO_CHAT.md` para conocer el estado y los pendientes; contrastarlos con el HEAD de GitHub. El resumen no sustituye las guías ni prevalece sobre el repositorio actual.
4. Preservar los acuerdos del usuario y el estilo de las fichas existentes. Una instrucción actual del usuario prevalece sobre una regla anterior.

## Alcance público de la documentación y de ARG

Estos archivos son documentación pública del recetario: `GUIA_DE_TRABAJO.md`, `docs/REFERENCIA_DE_TRABAJO.md` y `CONTINUAR_EN_OTRO_CHAT.md`. Describen reglas de trabajo, decisiones de presentación, archivos, commits, comprobaciones y pendientes de la web pública.

**ARG («Al recetario y GitHub») autoriza publicar los cambios en curso y las actualizaciones de estos documentos públicos necesarias para describirlos**, dentro de una lista explícita de archivos y conservando los cambios de otras conversaciones. No requiere una segunda confirmación para ese registro. Un ARG anterior no autoriza trabajos posteriores ajenos a ese cambio.

Distinguir por el contenido: mencionar un recurso protegido, conservar un enlace ya aprobado en la web o explicar dónde se realiza un seguimiento no equivale a publicar sus datos. Estas menciones no autorizan revelar credenciales, tokens, correos de acceso, permisos de personas concretas, identificadores o rutas de archivos privados, tickets, originales privados ni el contenido o los estados de compra. Todo ello permanece en la documentación y fuentes privadas correspondientes.

Antes de publicar, comparar la modificación con la última versión remota, revisar tanto los añadidos como el contexto que se conservará y señalar datos concretos si se identifica un riesgo. No afirmar que existe una filtración solo porque una herramienta haya clasificado genéricamente el documento como privado. Que un dato ya esté publicado tampoco demuestra que deba seguir publicado: si aparece información sensible concreta, detener esa parte y proponer su tratamiento.

Una revisión automática puede bloquear una operación pese a estas reglas. No intentar eludirla: completar lo permitido, conservar lo pendiente e informar de la acción rechazada y del motivo literal o su resumen fiel. Estas instrucciones documentan la autorización del usuario; no desactivan controles ni garantizan su aprobación.

## Preparar, mostrar y publicar

- **Evitar repeticiones en el carrusel público:** si la categoría visible coincide con la primera palabra completa del plato, omitir esa palabra del nombre mostrado, sin distinguir mayúsculas. Conservar el nombre íntegro en los datos y el enlace; no recortar nombres sin categoría ni dejar un título vacío. Aplicar también a los dos nombres bajo una categoría común.

- **Puré y crema:** con categoría visible «Puré», tratar la primera palabra completa «Crema» como repetición y omitirla, sin distinguir mayúsculas. Conservar el título completo y el enlace. No aplicar sin categoría ni recortar «Cremas».
- **Apodo en el menú público:** mostrar «Crema de aprovechamiento» como «aprovechategui»; también al identificar su ficha `crema-aprovechamiento-marisa.html`. El apodo tiene prioridad sobre el recorte de categoría. Solo cambia la presentación del carrusel: conservar título íntegro accesible, URL, ficha y datos originales.

- **Dos platos en el carrusel:** si comparten categoría o alguno no tiene categoría, mostrar un único bloque con la categoría disponible y ambos nombres unidos por « + », conservando sus enlaces individuales. Si ninguno tiene categoría, mostrar los nombres unidos sin inventar una categoría. Mantener dos columnas cuando las dos categorías sean distintas.
- **Publicación del menú desde el editor:** guardar sigue siendo privado. «Publicar menú en la web» muestra la copia exacta y requiere confirmación; el servidor comprueba la versión y envía solo días, platos, categorías y enlaces a un servicio separado. El carrusel lee únicamente la última copia publicada, sin credenciales, al abrir la página, recuperar foco y periódicamente. Si falla, conserva la copia pública válida de ese navegador o el respaldo estático. La compra, la despensa y el borrador no se exponen. Los nombres libres no llevan enlace y una comida vacía se muestra como Libre.
- **ARGH** conserva su significado de publicar el menú activo, con revisión de versión. La vía ordinaria es el botón del editor, que ya no necesita commits de GitHub por cada cambio de menú. `semana-base.md`, `datos/semana-base.json` y el HTML inicial constituyen el respaldo estático, no una lectura del menú vivo; mantenerlos coherentes si se actualiza expresamente ese respaldo. No sustituir automáticamente el menú por defecto privado al publicar. El generador debe conservar `tools/menu_publicado.js` incrustado y las pruebas `tools/comprobar_menu_publicado.cjs` y `tools/comprobar_semana_base.cjs`.

- Preparar cambios y vistas previas cuando el usuario lo pide. **Publicar requiere ARG o «Al recetario y GitHub» para los cambios en curso**, sin distinguir mayúsculas. Un ARG anterior no autoriza cambios posteriores. «Dale», «perfecto» o pedir un cambio permiten avanzar en la preparación; no sustituyen ARG. Se aplica también desde el iPhone.
- **Mostrar siempre los cambios antes de publicar.** Cada revisión lleva nombre de archivo y título HTML nuevos y un enlace directo accesible, como los de las fichas. No enlazar al usuario archivos de `build/previews/`: son solo para comprobaciones internas. Excluir todas las copias de revisión de la publicación; la página definitiva conserva su URL.
- Entregar por defecto el enlace al HTML de revisión y al PDF si lo hay. No ofrecer ni entregar capturas de móvil o escritorio salvo que el usuario las pida; las capturas internas de comprobación no sustituyen al HTML.
- Si el usuario ya ha dado ARG para preparar y publicar ese cambio concreto, completar la revisión y publicar sin pedir otra confirmación.
- Publicar solo una lista explícita de archivos afectados. Excluir `build/`, previsualizaciones y temporales. **Los tickets son privados, se guardan aparte y nunca se suben al repositorio.**
- Comprobar datos, sincronización, enlaces y presentación afectados. Reutilizar comprobaciones ya superadas si sus dependencias no cambian; no repetir pruebas ni verificaciones de despliegue sin motivo.
- Al publicar, entregar un resumen y el enlace al commit; no hace falta ZIP.

## Buscadores: web familiar

- Todas las páginas públicas HTML, incluidas categorías, productos y redirecciones, llevan `<meta name="robots" content="noindex, noimageindex">` dentro de `<head>`. Conservarla en plantillas y generadores; no añadir `nofollow` ni bloquear el rastreo con `robots.txt`.
- Antes de publicar, ejecutar `python tools/comprobar_noindex.py` en una copia canónica aislada y comprobar todos los HTML nuevos de la lista explícita. No publicar vistas previas.
- Esto no restringe el acceso por enlace ni hace privado el repositorio. La retirada de resultados depende del rastreador y puede tardar. PDF, imágenes directas y maestros Markdown/JSON no quedan excluidos mediante esta etiqueta HTML. Ver el apartado «Buscadores y alcance» de la referencia.

## Estilo y datos esenciales

- **Condimentos por receta:** en los objetos de ingredientes actuales, indicar `es_condimento` y, solo cuando sea `true`, `tipo_condimento` con uno de los cinco grupos acordados. Valorar la función en cada ficha: ajo del ajillo y albahaca protagonista son básicos, no condimentos. Conservar alternativas y opcionales. Las opciones textuales y las mezclas de agua/caldo se anotan por referencia sin alterar su formato original. Ver [estructura y grupos](docs/REFERENCIA_DE_TRABAJO.md#condimentos-por-receta).

- **Ingredientes básicos:** todas las fichas de platos (`receta`, `preparacion` y `combinacion`) llevan `ingredientes_basicos` en YAML y JSON: nombres sencillos, sin cantidades, de los ingredientes que definen la preparación. Ajo, cebolla y otras bases aromáticas solo se incluyen cuando tienen protagonismo (ajo en un ajillo, cebolla asada como parte del plato); no por formar parte del sofrito. No equivale a prioridad de compra. Alternativas y añadidos básicos opcionales se separan en `ingredientes_basicos_opciones`, con sus condiciones. Ver [criterio y estructura](docs/REFERENCIA_DE_TRABAJO.md#ingredientes-básicos).

- Pasta: usar preferiblemente pasta integral y 50 g en seco por persona como cantidad de referencia, salvo ajuste acordado para una receta concreta. Para las gambas al ajillo con pasta, conservar 100 g de pasta seca preferiblemente integral y 250 g de gambas peladas para dos personas; el manuscrito de Marisa conserva sus 250 g de pasta originales.

- Antes de desarrollar cualquier ficha, comprobar en `datos/estado-fichas.json`, portada y categoría si ya existe publicada o en «Próximamente», también con nombres equivalentes. Comunicar la coincidencia y reutilizar su identificador; al publicarla, sustituir la prevista sin duplicados. Hacer esta comprobación siempre, aunque el usuario no mencione las próximas.

- Confirmar `tipo_ficha` y `categoria_menu` antes de incorporar una ficha nueva. No volver a preguntarlos si ya se confirmaron. Cada receta pertenece a una sola categoría.
- Al incorporar cualquier receta nueva, comprobar siempre si ya aparece como ejemplo en el carrusel semanal, incluidos los componentes de ejemplos compuestos. Si corresponde, enlazar su ficha definitiva al publicarla y sincronizar `semana-base.md`, `datos/semana-base.json` y el bloque de `index.html`; regenerar y comprobar el carrusel. Si no aparece, no añadirla ni sustituir otro ejemplo sin acuerdo del usuario.
- Mantener sincronizados Markdown con YAML completo, JSON, Schema.org y HTML. Actualizar PDF, portada, categoría, `datos/estado-fichas.json` y `search-data` según corresponda; no duplicar recetas ni variantes.
- Encabezados de fichas: bajo el título, una línea con descripción breve, técnica o utensilio cuando aporte información, raciones y tiempo. No incluir el tipo de ficha ni copiar los distintivos de las tarjetas. Los PDF llevan el mismo título y línea descriptiva que la web, a partir de `encabezado` en YAML/JSON. La fuente se muestra en la web y se conserva en los archivos maestros; los PDF no llevan imagen ni bloque de fuente. Conservar el tipo en metadatos y tarjetas.
- **Ingredientes concisos:** cantidad, unidad e ingrediente; solo aclaraciones breves entre paréntesis cuando sean necesarias. Reparto, corte, uso y momentos de incorporación van en los pasos o en Claves. Conservar el estilo existente. El texto visible se dirige a quien cocina: incluir solo información relevante para ese lector; no trasladar notas internas, decisiones de edición ni explicaciones de nuestro proceso. La atribución de fuentes debe ser sencilla.
- Solo `tipo_ficha: receta` genera PDF: una página A4, sin foto, ingredientes en dos columnas sin viñetas sobre `#F3F6F1`, títulos verdes, pasos numerados, claves y fecha al pie. Usar `tools/generar_pdfs.py` y [FORMATO_PDF.md](FORMATO_PDF.md), sin maquetación manual.
- `preparacion` y `combinacion` no llevan PDF. Las fichas de producto usan `tipo_ficha: producto`, van en `productos/` y tampoco generan PDF.
- Al crear una ficha de producto, consultar siempre los tickets privados guardados para buscar precio, fecha y lugar de compra. Contrastar denominación, marca y formato; si la correspondencia no es inequívoca, señalar la posible coincidencia y pedir confirmación antes de atribuirla al producto. No dar esos datos por ausentes sin revisar los tickets ni publicar los originales o sus identificadores privados.
- Preguntar siempre por qué compra ese producto y en qué platos lo utiliza, salvo que ya lo haya explicado. Recoger sus motivos como experiencia personal y enlazar las recetas que confirme.
- En las fichas nuevas, generar siempre una ilustración ajustada a sus ingredientes, salvo que el usuario aporte una foto propia; no buscar fotografías en la web por defecto. Identificarla como generada con IA. Imágenes de platos en 16:9. En productos, conservar envase y etiqueta legibles con `object-fit: contain`. Documentar procedencia y licencia sin inventarlas; identificar las imágenes generadas con IA.
- Tortillas de casa en las ilustraciones: bajas, poco cuajadas y melosas; ingredientes bien mezclados con el huevo. En la de boniato, láminas finas algo doradas y espinacas integradas, sin capas regulares.
- Ilustraciones de platos: mantener el estilo y nivel de detalle de las publicadas, tomando como referencias visuales la cabecera del burrito de frijoles negros y las últimas ensaladas, guisos y tortillas. Misma cocina: luz natural cálida y suave, encimera de piedra beige, cerámica clara, encuadre cercano normalmente a tres cuartos, horizontal 16:9 y pocos accesorios. Leer ingredientes, cantidades, elaboración y claves antes de generar; representar cortes, proporciones, dorado, humedad e interior creíbles, sin añadidos ajenos. Aplicar el [criterio visual completo](docs/REFERENCIA_DE_TRABAJO.md#ilustraciones-de-casa-marisa).
- Al cambiar la imagen de una ficha, actualizar también su tarjeta de categoría y cualquier otro listado, los textos alternativos, metadatos y créditos afectados; comprobar que ninguna referencia siga usando la imagen anterior. Identificarla como ilustración generada con IA y mostrar siempre el resultado antes de publicar, según el flujo de ARG.
- Fechar cambios de contenido según Europe/Madrid: `fecha_actualizacion` y `dateModified`. No renovar fecha por presentación o regeneración. Mostrarla solo en el pie del PDF, no en el cuerpo de la web.
- Recetas de Eva: procedencia en metadatos (`origen_receta: eva-nutricionista`, autor y fuente); 🌿 accesible «Receta de Eva, nutricionista» al principio de raciones/tiempo en tarjetas. En Fuente: «🌿 Adaptada de una receta de Eva, la nutricionista». Afinar con raciones ajustadas, aceite medido y añadidos moderados. Importar una cada vez: terminar, mostrar y esperar ARG antes de publicar y empezar la siguiente. Generar la ilustración después de acordar ingredientes y preparación; conservar los originales en el catálogo privado. En los archivos públicos, incluir la atribución a Eva sin rutas, nombres ni referencias internas al catálogo privado o sus PDF. Tras publicar, guardar la URL pública en los metadatos del catálogo privado, conservando su versión más reciente y sin añadir marcas visibles desde este flujo.
- Recetas de Marisa: título sin «de Marisa» y 💚 al principio de raciones/tiempo en las tarjetas; en la ficha, presentación con 💚 bajo el encabezado. Conservar el original: manuscrito ampliable con transcripción fiel cuando exista, o relato oral identificado como tal, sin inventar un documento escrito. Los ajustes no alteran el original.
- Una ficha nueva lleva «NUEVA» en portada y categoría; retirarla solo cuando lo pida el usuario. Al desarrollar una prevista, sustituir «PRÓXIMAMENTE» y eliminar su entrada provisional.

## Consultar según la tarea

| Tarea | Apartado o archivo |
| --- | --- |
| Recetas: creación, tipos, modificaciones, Marisa, fechas y fotos | [Referencia de recetas](docs/REFERENCIA_DE_TRABAJO.md#preparar-y-sincronizar-una-ficha) |
| Relación con el catálogo privado de Eva y seguimiento | [Publicar recetas de Eva](docs/REFERENCIA_DE_TRABAJO.md#publicar-recetas-procedentes-del-catálogo-privado-de-eva) |
| Ilustraciones: estilo, referencias y revisión | [Ilustraciones de Casa Marisa](docs/REFERENCIA_DE_TRABAJO.md#ilustraciones-de-casa-marisa) |
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

Mantener [CONTINUAR_EN_OTRO_CHAT.md](CONTINUAR_EN_OTRO_CHAT.md) en la raíz: contiene un mensaje listo para copiar, estado comprobado, cambios preparados y siguientes pasos. En un chat nuevo basta con pegar ese mensaje o pedir que se lea el archivo actual de GitHub.

- Actualizarlo con cada publicación autorizada mediante ARG, cuando cambie un pendiente importante y antes de cambiar de chat. No depende de una tarea por calendario.
- Preparar su actualización en la misma lista explícita de archivos que el cambio; publicar juntos los cambios y su resumen. Sin ARG, conservarlo como propuesta local y mostrarlo. Documentar los acuerdos permanentes en las guías y enlazarlos desde el resumen.
- Distinguir lo publicado, lo comprobado y lo preparado sin publicar. Tras desplegar, comprobar los cambios afectados y comunicar el resultado; no afirmar en el archivo una comprobación que todavía no se ha realizado. Si falla el despliegue o la comprobación, registrar la incidencia en el seguimiento del cambio; cualquier actualización remota sigue el alcance de ARG.
- No intentar escribir el SHA del propio commit dentro del archivo: obtener el HEAD actual de GitHub al retomar. Puede citarse un commit anterior como hito comprobado, identificándolo así. No generar commits sucesivos solo para actualizar un SHA o una hora.
- El repositorio es público: no incluir tickets, datos personales, rutas de archivos privados ni contenido del catálogo privado. El checkout temporal puede desaparecer; no usarlo como única copia de trabajo pendiente.
- Guardar el acceso, permisos, alojamiento, estados e instrucciones operativas de las aplicaciones familiares en un resumen privado, separado de este seguimiento público. Aquí solo se documentan los acuerdos y resultados de la web pública; no copiar el resumen privado a GitHub.

Si la sesión se interrumpe antes de actualizar el resumen, comparar sus afirmaciones con los commits recientes y las guías actuales. Un estado «preparado» solo en el chat o en una carpeta temporal no garantiza que sus archivos sigan disponibles; comprobarlo y reconstruirlo desde los acuerdos documentados si hace falta.

> Continuamos con Recetario de Casa Marisa, repositorio `fucolin/recetario`. Lee en GitHub `GUIA_DE_TRABAJO.md` y `CONTINUAR_EN_OTRO_CHAT.md`, y consulta solo la referencia necesaria. Contrasta el resumen con el HEAD actual. GitHub es la fuente canónica. Muéstrame los cambios con nombre y título nuevos; publica solo cuando diga ARG.

## Excepción acordada: diagrama de burritos

El PDF de burritos incorpora seis imágenes numeradas en dos filas de tres, sin pies de imagen. Sus pasos principales no se numeran; la web conserva las indicaciones bajo cada imagen. Se mantiene una página A4 y el encabezado común. Configuración en `pdf_diagrama` y `pdf_numerar_pasos` del maestro; usar el generador común.

## Excepción acordada: menestra y preparación en tabla

«Menestra guisada» presenta la preparación en tres columnas en escritorio y como pasos abiertos en móvil: título numerado y filete, fuego en cursiva con icono de llama y tiempo, acción y «Hasta que…». El PDF mantiene la tabla en una página A4. Fuente estructurada en `pasos`, con `preparacion_formato: tabla-adaptable` y `pdf_preparacion_tabla: true`; regenerar con `tools/generar_receta_tabla.py menestra-guisada.md` y el generador común de PDF. No extender esta excepción a otras recetas sin acuerdo.


