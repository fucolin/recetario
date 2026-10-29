# Continuar en otro chat · Casa Marisa

## 29/10/2026 · Básicos y condimentos · publicación autorizada mediante ARG

Ampliación autorizada de la preparación de ingredientes básicos: añadidos `es_condimento` y `tipo_condimento` en las 31 fichas YAML/JSON, con los cinco grupos de la guía. Valoración por receta, conservando básicos, cantidades, opcionales, sustituciones y originales. Ajo del ajillo, cebolla asada protagonista y albahaca del lago no son condimentos. 272 objetos de ingredientes/opciones clasificados, 134 como condimento; 16 referencias textuales adicionales para aderezos y elecciones agua/caldo, sin alterar el formato previo. Agua nunca clasificada como condimento.

El usuario autoriza publicar con ARG la revisión v2 mostrada y aprobada, sobre el commit de partida `96bd033b32881532311008909d81f7d87f2e515f`. Las selecciones de básicos v1 se conservan. Lista explícita: los 31 maestros Markdown/YAML y sus 31 JSON completos, `GUIA_DE_TRABAJO.md`, `docs/REFERENCIA_DE_TRABAJO.md` y este resumen: 65 archivos. No se publican revisiones, informes, parches, ZIP ni temporales. Los registros anteriores de preparado/sin publicar quedan históricos para este lote.

Verificados YAML/JSON, tipos, referencias y condiciones; cuerpos Markdown, datos culinarios y originales anteriores íntegros; selección básica aprobada conservada. Exportador probado en commit objeto aislado: 31 disponibles y 15 próximas, contrato previo conservado salvo atributos nuevos del ingrediente dentro de `source`. No se han cambiado HTML, PDF, Schema.org, fechas culinarias, imágenes ni menú. El exportador puede transportar anotaciones dentro de `source`, pero eso no acredita interpretación o uso por la app; su integración y las prioridades siguen siendo un trabajo separado. Comprobar después del commit el despliegue y los metadatos servidos; estas verificaciones de preparación no acreditan todavía disponibilidad web. Al incorporar o modificar fichas, aplicar ambos criterios y revisar sus anotaciones.

## 29/10/2026 · Ingredientes básicos · preparado, SIN PUBLICAR

Revisadas las 31 fichas de platos actuales (recetas, preparaciones y combinaciones) sobre el commit de partida `96bd033b32881532311008909d81f7d87f2e515f`. Añadidos `ingredientes_basicos` en sus maestros YAML y JSON completos; 13 fichas incluyen `ingredientes_basicos_opciones` para distinguir alternativas y añadidos opcionales. Criterio por función en cada receta: ajo solo en el ajillo; cebolla cuando es componente protagonista asado, no fondo del sofrito; albahaca protagonista incluida. Listas completas y preparaciones conservadas. Criterio permanente y estructura documentados en las dos guías.

Preparación pendiente de ARG. No afirmar que estos metadatos estén publicados o sean consumidos por la aplicación. No se modifican el catálogo de intercambio, las prioridades de compra, las páginas visibles, Schema.org, PDF, fechas culinarias, imágenes ni menú. Las comprobaciones se entregan con el paquete de revisión; al retomar, contrastar su base con el HEAD y conservar otros cambios antes de publicar.

## 26/10/2026 · Puré/crema y aprovechategui · publicación autorizada

El carrusel omite «Crema» al principio del nombre bajo categoría «Puré» y muestra la crema de aprovechamiento con el apodo «aprovechategui», sin alterar fichas, enlaces ni menú guardado. Incluye categorías comunes a dos platos y caché. Guía, cargador, prueba e incrustación de index.html actualizados; respaldo estático conservado (ya usa aprovechategui). Preview mostrada y publicación autorizada expresamente con «publica». Pruebas del DOM simulado superadas: equivalencia Puré/Crema, apodo con y sin categoría, dos platos, caché y conservación de títulos accesibles/enlaces. Las verificaciones del despliegue son posteriores al commit; no se afirma aquí una revisión visual interactiva.


## Estado vigente contrastado · 25/10/2026

Esta síntesis prevalece sobre las referencias históricas a preparaciones o pendientes de publicación que figuran más abajo. Se conserva íntegro el historial; comprobar de nuevo GitHub antes de trabajar.

Las tres incorporaciones recientes están guardadas en la rama principal:
- **Crema de calabacín**: `crema-calabacin.md` y [ficha](crema-calabacin.html), categoría Purés, receta de Marisa con manuscrito. Commit de incorporación `b65e12cec1010d8a1b01f737a267915335ea91b6`.
- **Gambas al ajillo con pasta**: `gambas-ajillo-pasta.md` y [ficha](gambas-ajillo-pasta.html), categoría Mariscos, receta de Marisa con manuscrito. Commit `10773a2346a02151f175719f7ea76c727d0a339f`. Para dos personas: 100 g de pasta seca preferiblemente integral y 250 g de gambas peladas.
- **Gambas salteadas con trigueros**: `gambas-salteadas-trigueros.md` y [ficha](gambas-salteadas-trigueros.html), categoría Mariscos, inspirada en una sugerencia de menú de Eva. Commit `8e26d9165a092646ecf72332b8d4899f8ea40801`. Conserva las opciones de calabacín y huevo escalfado aparte.

**Verificado en archivos en esta revisión:** leídos los tres maestros Markdown/YAML y sus HTML actuales; las páginas incluyen Schema.org, enlace al PDF y `noindex, noimageindex`. `datos/estado-fichas.json` identifica las tres como NUEVA y ya no como próximas. `datos/semana-base.json` enlaza los dos ejemplos de gambas al ajillo con pasta (lunes y sábado). La guía técnica contiene la preferencia de pasta integral, 50 g secos por persona como referencia y la comprobación obligatoria de fichas existentes/próximas antes de desarrollar otra.

**Límites de la comprobación:** guardado en GitHub no equivale a despliegue verificado. No se ha realizado ahora una comprobación HTTP, revisión visual de la web o del PDF ni prueba del menú vivo. No se deduce de estas incorporaciones una actualización de los metadatos o listados privados de Eva. Esas verificaciones quedan pendientes cuando corresponda.

Esta corrección documental actualiza únicamente este resumen; conserva los registros anteriores y no modifica recetas, recursos ni datos del menú. Los apartados detallados de las tres recetas al final del documento ya existían al comenzar esta revisión. Se añade esta síntesis para hacer visible su estado actual.

## 22/10/2026 · Nombres completos de platos

El cargador admite títulos de hasta 300 caracteres, en consonancia con el editor y su servicio de publicación, para conservar nombres largos sin recortarlos. Categorías, enlaces, número de platos/días y controles de validación permanecen iguales. Prueba de aceptación de 300 caracteres y rechazo de 301 conservando la copia válida anterior. No se publica ningún menú ni contenido de Eva desde esta actualización de código. Comprobar despliegue del commit al retomar.

## 22/10/2026 · Aviso bajo Libre

Cuando una comida no contiene platos, el menú público muestra Libre y debajo «⚠️ Respete vd. las cantidades». El aviso se añade al cargador del menú publicado y funciona también desde caché; desaparece al volver a añadir un plato. El respaldo estático y su maestro ya contienen este aviso y se conservan. No se modifica el menú privado ni la copia publicada de datos. Pruebas del DOM simulado para comidas vacías, caché y sustitución por plato; comprobar el despliegue de este commit al retomar. Revisión visual interactiva no disponible.

## 22/10/2026 · Omitir la categoría repetida al comienzo del plato

El cargador del menú público muestra «de boniato» bajo «Tortilla» cuando el título es «Tortilla de boniato». Compara la categoría visible con la primera palabra completa, sin distinguir mayúsculas y con normalización Unicode; conserva nombres sin coincidencia o sin categoría y evita dejar un nombre vacío. Funciona con categorías comunes a dos platos y datos públicos en caché. Títulos originales, enlaces, menú privado y copia publicada permanecen íntegros; el enlace abre la misma ficha y conserva el nombre completo como etiqueta accesible. Cargador incrustado y archivo fuente sincronizados. Pruebas de coincidencias, límites de palabra, mayúsculas, acentos, categorías ocultas, dos platos y caché superadas. Revisión visual interactiva no disponible. Comprobar el despliegue del commit al retomar.

Lista de archivos: `index.html`, `tools/menu_publicado.js`, `tools/comprobar_menu_publicado.cjs`, `GUIA_DE_TRABAJO.md` y este resumen.

Actualizado: 21 de octubre de 2026, Europe/Madrid. Conexión del carrusel al menú publicado desde el editor; documentación de su confirmación y respaldo.

Hito anterior del 19 de octubre: centrado de los botones de menú y compra y su nota, autorizado mediante ARG. Se conserva como antecedente.

## 21/10/2026 · Presentación conjunta de dos platos

Cambio solicitado y autorizado para publicar: cuando dos platos comparten categoría o alguno carece de ella, el carrusel muestra un único bloque, una categoría común si existe y los nombres unidos por « + », conservando cada enlace. Si ambos carecen de categoría, no se inventa ninguna. Dos categorías distintas conservan sus dos columnas. No cambia el menú guardado ni su publicación confirmada.

Archivos de esta modificación: `index.html`, `tools/menu_publicado.js`, `tools/comprobar_menu_publicado.cjs`, `GUIA_DE_TRABAJO.md` y este resumen. Comprobados los cuatro casos de categorías iguales/ausentes, enlaces y nombres sin enlace, cambios entre uno/dos bloques y sincronización del cargador incrustado. Revisión visual interactiva no disponible; comprobar el despliegue del commit al retomar, sin confundir estas pruebas locales con una prueba visual.

## 21/10/2026 · Carrusel conectado a la publicación confirmada

Conexión publicada en el commit `213e81715d906aacd2f832340a247d8e6ffd5e40`, con despliegue de Pages terminado correctamente y cargador comprobado en la portada servida. El carrusel carga el último menú confirmado desde un servicio público aislado del editor. Guardar el menú sigue siendo privado; el botón Publicar menú en la web muestra una revisión y pide confirmación. El servicio recibe solo días/platos/categorías/enlaces resueltos. No contiene compra, despensa, usuarios ni borradores; los nombres libres no tienen enlace y las comidas sin platos muestran Libre. La escritura está protegida en el servidor, sin credenciales en esta web.

El HTML conserva el menú estático actual como respaldo; una copia pública válida se conserva también en el navegador. Un fallo, respuesta inválida o versión antigua no vacía ni sustituye el carrusel válido. Se mantienen sus siete nodos/días, centrado, gestos y enlaces. La carga se hace al abrir, recuperar foco y periódicamente. El generador conserva el cargador `tools/menu_publicado.js`; se añade `tools/comprobar_menu_publicado.cjs`. `semana-base.md` y su JSON siguen sincronizados como respaldo estático; el menú vivo publicado procede del nuevo servicio y no requiere commits por cada edición.

Comprobaciones locales: texto/enlaces seguros, dos platos/Libre, validación antes de reemplazar, respaldo estático y caché ante desconexión, ausencia de credenciales y rechazo de versiones antiguas; prueba del carrusel existente conservada. Revisión visual interactiva pendiente por indisponibilidad del navegador. Consultar el HEAD y el despliegue actuales al retomar; este registro no afirma haber pulsado Publicar en nombre del usuario.

## Alcance de este seguimiento público

ARG incluye registrar los cambios autorizados en este resumen y en las guías públicas. Las referencias a recursos protegidos no trasladan sus datos a este repositorio. Aplicar la separación por contenido y la respuesta a bloqueos descritas en [la guía de trabajo](GUIA_DE_TRABAJO.md#alcance-público-de-la-documentación-y-de-arg).

## Mensaje listo para copiar y pegar

```text
Continuamos con Recetario de Casa Marisa, nuestra web familiar de recetas.

Repositorio: fucolin/recetario
Web: https://fucolin.github.io/recetario/

Lee en GitHub GUIA_DE_TRABAJO.md y CONTINUAR_EN_OTRO_CHAT.md. Consulta solo los apartados necesarios de docs/REFERENCIA_DE_TRABAJO.md. GitHub es la fuente canónica: comprueba el HEAD actual y los commits recientes antes de fiarte del estado resumido aquí.

El checkout de una sesión anterior puede estar atrasado, contener archivos ya publicados o haber desaparecido. Revisa su estado sin descartar nada; si no es fiable, prepara una copia aislada del estado actual de GitHub. No publiques indiscriminadamente: utiliza una lista explícita de archivos.

ARG significa preparar, comprobar y publicar directamente los cambios en curso, sin pedir otra confirmación. Sin ARG, prepara y muestra. El ARG de un cambio anterior no autoriza cambios nuevos.

Para las revisiones, usa nombre de archivo y título HTML nuevos y enlaces accesibles. No enlaces build/previews/ ni publiques previsualizaciones o temporales.

Retoma el estado y los pendientes de este archivo, comprobando qué está publicado y qué solo estaba preparado. Aplica el criterio visual de las guías antes de generar imágenes. Al terminar un cambio, actualiza este resumen según la guía para que podamos continuar aunque el chat deje de estar disponible.
```

## Estado publicado y comprobado

- Último cambio de contenido web comprobado en esta sesión: `0366cd0deaf1fa3e83b0284ad20dce990c875aa4`, conservación de la única receta de lentejas de 400 g y redirección desde 300 g. Es un hito de comprobación, no una afirmación sobre el HEAD actual: consultar GitHub al retomar.
- Los HTML llevan `noindex, noimageindex`, incluidas categorías, productos y redirecciones. El comprobador local ha revisado 55 páginas; se ha comprobado también el despliegue de ambas fichas de pollo, PDF nuevo, imagen, portada y categoría. Los generadores lo conservan y existe `tools/comprobar_noindex.py`. No bloqueamos el rastreo ni añadimos `nofollow`. El acceso por enlace y el repositorio siguen públicos; PDF, maestros y recursos directos no quedan excluidos por esta etiqueta HTML. Detalle en «Buscadores y alcance» de la referencia.
- Las cinco fichas importadas de Eva están terminadas y conservan NUEVA: potaje de bacalao, ensaladilla, fajitas de salmón, ensalada de lentejas con salmón y pepino, y fajita de francesa y pavo.
- «Menestra guisada» se incorpora como receta de Marisa, categoría Vegetales, con NUEVA en portada y categoría; sustituye la prevista «Menestra» y enlaza desde la comida del lunes. Sofrito acordado de 10 min (8 de cebolla y 2 de ajo), tabla en escritorio y pasos abiertos en móvil, PDF A4 con tabla. El relato oral se conserva separado; no hay manuscrito.
- Burrito de frijoles negros: `burrito-frijoles-negros.html`; la URL antigua redirige. Cabecera fotorrealista y diagrama de montaje de seis imágenes. El PDF incorpora el diagrama 3+3, sin pies ni numeración de los pasos principales; conservar la excepción de la guía.
- Las fichas de platos y sus tarjetas de categoría tienen las ilustraciones publicadas. Mantener la cocina y el detalle visual acordados; consultar la guía y las imágenes vigentes antes de generar otras.
- En esta publicación autorizada, la leyenda debajo del carrusel se sustituye por «Editar menú», con enlace al menú privado y el estilo de los recursos de compra. Consultar el detalle y el estado de comprobación en Pendientes.

## Relación con el catálogo privado de Eva

El catálogo privado conserva los originales; Casa Marisa publica las adaptaciones autorizadas. Este flujo comprueba la ficha pública y actualiza exclusivamente `casa_marisa` en la ficha privada, partiendo siempre de la última versión guardada y conservando su identidad y los cambios de otros chats. El flujo del catálogo sincroniza después sus 🌿 y enlaces `+`, `++`, `+++` desde esos metadatos, cuando se le solicita. No modificar aquí sus listados ni publicar originales privados.

Conservar todas las versiones públicas de una misma receta de origen, sin duplicar una ficha por cambios en la misma URL. No marcar como publicada una incorporación pendiente de ARG. Consultar «Publicar recetas procedentes del catálogo privado de Eva» en la referencia para el esquema y el procedimiento.

Seguimiento al cambiar de chat: distinguir «web publicada y comprobada», «metadatos privados guardados» y «listados privados sincronizados». No deducir los dos últimos estados del primero. Registrar por título y URL pública cualquier actualización privada pendiente; no incluir rutas, nombres de archivos privados ni identificadores de Biblioteca. En esta tarea se amplía la documentación; no se han actualizado ni auditado exhaustivamente las correspondencias del catálogo. Si se pide una comprobación de novedades, consultar su última versión antes de determinar si hay pendientes.

## Acuerdos documentados

- Ampliación del criterio de imágenes en `GUIA_DE_TRABAJO.md` y `docs/REFERENCIA_DE_TRABAJO.md`: referencias visuales concretas, luz cálida y suave, piedra beige, cerámica clara, encuadres cercanos a tres cuartos, 16:9, fidelidad a cantidades y elaboración, interiores y texturas naturales. Conserva tortillas bajas y melosas y la sincronización de tarjetas, textos alternativos, metadatos y créditos.
- Creación de este archivo y del procedimiento de mantenimiento en la guía principal.
- Ampliación de la relación con el catálogo privado de Eva: reparto de responsabilidades, esquema `casa_marisa`, varias versiones y recuperación de actualizaciones pendientes.
- Archivos de esta actualización: `GUIA_DE_TRABAJO.md`, `docs/REFERENCIA_DE_TRABAJO.md`, `CONTINUAR_EN_OTRO_CHAT.md`.
- El resultado del guardado y del despliegue se comprueba después de publicar; consultar el commit y su ejecución en GitHub al retomar, sin suponer que esta descripción anticipa esa comprobación.

## Pendientes y siguiente paso

Publicación autorizada mediante ARG: centrar los dos botones de menú y compra y la nota inferior tanto en escritorio como en móvil. Conservados fondo blanco, iconos y destinos. Parte del commit comprobado `858dc9a46d08d6cbc845eace388ef30d3171abf3`. Lista explícita: `index.html`, `docs/REFERENCIA_DE_TRABAJO.md` y este resumen. Revisión `portada-botones-centrados-revision-20261019-v7.html`, excluida de publicación. Comprobados estilos y noindex; comprobar el despliegue tras publicar.

Publicación autorizada mediante «Hazlo y ARG»: botones de menú y compra con fondo blanco, borde y radio de 8 px como los controles superiores del carrusel; iconos, nota y destinos conservados. Parte del commit comprobado `44d04565f3e590ad60165ba1160887713c8ce9a8`. Lista explícita: `index.html`, `docs/REFERENCIA_DE_TRABAJO.md` y este resumen. Revisión `portada-botones-blancos-revision-20261019-v6.html`, excluida de publicación. Comprobados estilos y noindex; comprobar despliegue tras publicar.

Publicación autorizada mediante ARG, revisión v5 mostrada y aprobada: los accesos de menú y compra pasan a ser dos botones de navegación, con borde verde, fondo claro, esquinas redondeadas e iconos sin flechas; conservan debajo la nota de acceso privado con candado. Parte de la publicación comprobada `16125f170abb2de64e4239fe8199f2d08a194350`. Lista explícita: `index.html`, `tools/generar_semana_base.py`, `docs/REFERENCIA_DE_TRABAJO.md` y este resumen. Revisión `portada-botones-menu-compra-revision-20261019-v5.html`, excluida de publicación. Comprobados enlaces, generador y noindex; comprobar el despliegue tras publicar.

Publicación autorizada mediante ARG: «Lista de la compra» junto a «Editar menú» debajo del carrusel, con el mismo estilo, sin duplicarlo en «Para elegir y comprar». Checklist junto al enlace de la lista; debajo de ambos, nota compartida «Acceso privado [icono de candado] Iniciar sesión con ChatGPT». Ambos enlaces y la nota se conservan al regenerar. Lista explícita: `index.html`, `tools/generar_semana_base.py`, `docs/REFERENCIA_DE_TRABAJO.md` y este resumen. Revisión v4 mostrada y aprobada; `portada-menu-compra-revision-20261019-v4.html` queda excluida de la publicación. Comprobados enlaces únicos, nota, generador y noindex. El cambio no modifica el menú ni el contenido o estado de las aplicaciones privadas. Comprobar el despliegue después de publicar; la ubicación descrita en el párrafo histórico del primer acceso queda sustituida por esta disposición.

Publicación autorizada mediante **ARGH**: consultado el menú activo guardado en el editor privado. Única diferencia respecto al carrusel: comida del lunes cambia de «Verduras · Menestra guisada» a «Marisco · Gambas al ajillo con pasta». La ficha de gambas sigue próxima, por lo que su nombre se muestra sin enlace y con categoría Mariscos; no crear ficha, PDF ni datos culinarios por este cambio. Resto de días y componentes conservados. Lista explícita: `semana-base.md`, `datos/semana-base.json`, `index.html`, `GUIA_DE_TRABAJO.md`, `docs/REFERENCIA_DE_TRABAJO.md` y este resumen. Revisar el despliegue tras publicar; la revisión local `portada-menu-activo-revision-20261019-v4.html` no se publica. Los accesos de menú y compra del commit `325d4f84d11e104624e325760d0f4047960aeb1c` ya quedaron publicados y comprobados.

Publicación autorizada mediante ARG el 19/10/2026: accesos a la aplicación privada desde la portada. «Editar menú» sustituye la leyenda debajo del carrusel y enlaza a `https://compra-casa-marisa-prueba.snappyseal256.chatgpt.site/menu`; estilo de «Para elegir y comprar»: verde, peso 650, .95rem, icono de edición, flecha y foco visible, sin cursiva. Conservados el centrado móvil y el espacio inferior; generador semanal sincronizado. «Lista de la compra» aparece después de los tres recursos públicos, en una fila propia con filete, candado y descripción «Acceso privado · Iniciar sesión con ChatGPT», enlazada a la raíz del mismo sitio.

Lista explícita: `index.html`, `tools/generar_semana_base.py`, `docs/REFERENCIA_DE_TRABAJO.md` y este resumen. La revisión de portada v3 fue mostrada y aprobada. Comprobados enlaces, generador y noindex; verificar la portada desplegada después de publicar. Datos del menú público, recetas, PDF y estados privados de la compra conservados. No se publican revisiones, contenido de la lista, marcas, correos ni credenciales.

Los detalles de acceso, autorizaciones, funcionamiento y continuidad de la aplicación se conservan en un resumen privado fuera de este repositorio. No copiarlos a las guías ni al seguimiento público. La publicación del menú en el carrusel se realiza únicamente a petición del usuario.

Pendiente aparte, sin incluir en esta publicación: ajuste de texto del producto ElPozo en «En mi cocina», acordado después de `ce18cd860be38bc2e3d6a0d49fe27895306a86de`: mover allí la idea «Me facilita tener a mano una carne que considero bastante saludable para varios tipos de comida improvisada», retirarla del motivo sobre fecha de consumo preferente y conservar el uso de la fajita como enlace en «Lo uso en». Revisión v6 ya mostrada; no asumir que este ARG para los accesos publica también ese ajuste.

Publicación autorizada mediante ARG: producto «Pechuga de pavo asada con madera de haya», ElPozo 1954 Premium Gourmet, envase de 120 g, identificador `pechuga-pavo-elpozo-1954`. Maestro Markdown/YAML, JSON, Schema.org y HTML, entrada en Productos preferidos, fotografías originales completas del envase y etiqueta y captura de Yuka con créditos. Sin PDF. Etiqueta: 95 % de pechuga de pavo, 21,3 g de proteínas y 2,2 g de sal por 100 g; posibles trazas de proteína de leche y soja, refrigeración 0–5 °C y consumo en 2–3 días tras abrir. Yuka: 57/100, Bueno; conserva por separado la declaración «Sin aditivos» del envase y el aditivo de riesgo limitado de Yuka no identificado en la captura.

La ficha de producto conserva sus datos aprobados y enlaza a la fajita de francesa y pavo. Solo el nombre genérico «pavo» enlaza desde los ingredientes de la receta. Cantidades, instrucciones, fecha culinaria y PDF conservados. Este enlace no requiere actualizar el catálogo privado de Eva. Los detalles históricos de compras se retiran de este resumen público con autorización del usuario; consultar los datos aprobados en la ficha y las fuentes privadas cuando corresponda.

Carrusel: cena del domingo bajo «Huevos», texto «Fajita de francesa» enlazado a `fajita-francesa-pavo.html`; conserva Sopa de fideos y la categoría real del ejemplo, Envueltos y bocados. Sincronizados maestro semanal, JSON y portada.

Acuerdos incorporados a las guías: entregar siempre HTML de revisión y PDF cuando exista; capturas solo cuando se soliciten. Al crear productos, revisar los tickets privados actuales y preguntar por qué se compran y en qué platos se usan, salvo que ya conste. Confirmar correspondencias ambiguas antes de atribuir precio o tienda. Tickets y sus identificadores privados fuera del repositorio. El generador de productos admite unidad de promoción «envase» y ocultar «aprox.» en esta ficha, conservando la presentación de los otros productos.

Preparación comprobada: móvil y escritorio, enlaces recíprocos, JSON y Schema.org, datos de precio y promoción, carrusel y noindex en 56 HTML; sin cambios ajenos al regenerar. Revisiones entregadas: producto v4, fajita v1 y portada v2; las copias de revisión y capturas no se publican. ARG recibido; comprobar el despliegue tras esta publicación antes de darlo por verificado. No quedan decisiones del usuario pendientes para este cambio.

Cambio autorizado mediante ARG en esta publicación: doble botón para cambiar entre las dos fichas de pollo. Doble botón de dos segmentos unidos «Versión» después del encabezado y antes de la imagen, con «Olla» y «Cocotte y horno», borde común y sin hueco entre opciones; la actual se muestra en verde con texto blanco y marca de selección, lleva `aria-current="page"` y no enlaza a sí misma. La otra opción es un enlace normal; funciona sin JavaScript y tiene foco visible. Retirado el selector antiguo situado antes de Ingredientes. Acciones unificadas en ambas páginas: «Más de Guisos y asados» seguido de «PDF para imprimir». Datos culinarios, imágenes, PDF y fechas conservados. Cambios sincronizados en ambas páginas HTML, el generador de cocotte y la referencia; este ajuste de navegación no requiere actualizar metadatos privados de Eva. Revisión aprobada por el usuario. Comprobadas ambas fichas en 320/390/1440 px, navegación sin JavaScript, selección de la versión actual y foco de teclado. Verificar el despliegue después de publicar; no quedan cambios pendientes de ARG para este ajuste.

Publicado y comprobado: solo «Lentejas cremosas con calabaza y espinacas» de 400 g; en casa se reservan los botes de 300 g para ensaladas. Tarjeta única directa en portada y Legumbres, sin selector; URL vigente de 400 g conservada y página de 300 g como redirección. Retirada de los maestros Markdown/JSON, Schema.org y PDF de 300 g de la versión actual (histórico recuperable en Git). Título web/PDF de 400 g sin sufijo de variante; cantidades, preparación, imagen y fecha culinaria conservadas. Carrusel del miércoles actualizado para enlazar a 400 g. La ensalada de lentejas de 300 g conserva su receta. Metadatos privados guardados: `casa_marisa` de las lentejas conserva una sola adaptación vigente de 400 g, con título sin sufijo; la redirección antigua no cuenta como otra variante. Se partió del ZIP vigente con control de versión y se comprobó que solo cambia ese campo, conservando ingredientes, elaboración, originales y archivos ajenos. Los listados privados se sincronizan desde su flujo. Preparación comprobada en móvil/escritorio, buscador, redirección y PDF de una página. Despliegue comprobado: ficha, PDF, redirección, portada, categoría y JSON semanal coinciden con la preparación; los recursos maestros y PDF antiguos de 300 g ya no están en la publicación vigente. No quedan cambios web pendientes de ARG para esta tarea. Pendiente del flujo privado: sincronizar los enlaces del índice de lentejas y de la nueva variante de pollo desde los metadatos guardados.

Publicada y comprobada: variante «Pollo guisado con calabacín en cocotte», tipo receta y categoría Guisos y asados, familia `pollo-guisado-calabacin`, identificador `pollo-guisado-calabacin-cocotte`. Cuatro contramuslos o dos cuartos traseros, con hueso y sin piel (800 g–1 kg aprox.); con dos cuartos son dos raciones generosas. Las piezas grandes pueden necesitar más tiempo. 1 h 30–1 h 50 min orientativos. Dorado y sofrito en el fuego; horno tapado a 175 °C (160 °C con ventilador), 40–55 min iniciales orientativos, comprobando ternura y al menos 74 °C sin tocar hueso. Calabacín salteado al final, últimos 10–15 min. Maestro, JSON, Schema.org, HTML, PDF A4, ilustración v2 con dos cuartos traseros y tarjeta común con dos enlaces sincronizados; la versión en olla conserva su URL, ingredientes, preparación y fecha. Botones «Olla» y «Cocotte y horno» con tiempos propios, NUEVA identifica la nueva variante. Acceso entre ambas fichas. El carrusel del domingo ya enlaza a la versión en olla; se conserva. Regenerar la nueva ficha con `tools/generar_pollo_cocotte.py` y el generador común de PDF. La prueba de imagen v1 con cuatro contramuslos queda fuera de la publicación. Revisada con el usuario y comprobada en móvil, escritorio, buscador y PDF de una página. Despliegue y archivos publicados comprobados contra la preparación. Metadatos privados guardados: añadida esta segunda adaptación a `casa_marisa`, conservando la versión en olla, a partir del ZIP vigente y con control de versión. Se ha comprobado que no cambian originales, ingredientes, elaboración ni otros archivos. Listados privados pendientes de sincronización desde el flujo del catálogo; no se han modificado aquí. No quedan cambios web pendientes de ARG para esta variante.

Incorporación autorizada mediante ARG en esta publicación: «Mejillones a la marinera», tipo receta, categoría Mariscos, adaptada del mismo folleto de pictogramas y estuche de vapor de las patatas. Acordados 500 g de mejillones crudos limpios al vacío con concha, 100 g de tomate triturado, 100 g de cebolla, 100 g de pimiento rojo, 30 ml de vino y una cucharada de aceite (15 ml) con las verduras; sal solo al final si hace falta. Tiempo orientativo 20 min, dos raciones como entrante. Cocinar la base 8 min a 800 W hasta tierna y los mejillones 3 min iniciales, con comprobaciones, respeto al envase y tandas adicionales; descartar los que sigan cerrados. Opciones explica el uso de mejillones frescos con limpieza previa. Maestro, JSON, Schema.org, HTML, PDF de una página, ilustración v1 y tarjetas con NUEVA sincronizados; regenerar con `tools/generar_mejillones_marinera.py` y el generador común de PDF. No aparece en el carrusel; conservarlo. Revisados con el usuario y comprobados en móvil, escritorio, buscador y PDF de una página. Verificar el despliegue después de publicar; no quedan cambios pendientes de ARG en esta receta. No hay relación con el catálogo privado de Eva.

«Patatas al vapor sabrosas» publicada y comprobada en el commit citado arriba, con NUEVA en portada y Picoteo y guarniciones. Maestro YAML, JSON, Schema.org, HTML, PDF A4 e ilustración v2 con cebollino sincronizados. Patatas lavadas o patacas novas, media lima al cocinar, laurel retirado al terminar y cebollino al servir; aceite solo en el aliño final, aprovechando el de las sardinillas si acompañan la cena. Alternativas de hierbas en Opciones. Dos raciones de guarnición, unos 15 min. Regenerar con `tools/generar_patatas_vapor.py` y el generador común de PDF. No aparece en el carrusel. La prueba de imagen v1 no se publicó.

Última actualización publicada de «Menestra guisada»: reposo sin llama ni «Sin fuego», solo 3–5 min, y Opciones aclaradas para guarnición o plato principal con huevo cocido y, si no lleva carne ni jamón, bonito en conserva. Maestro, HTML, JSON, buscador y PDF A4 sincronizados junto con sus generadores; versión oral original conservada. Comprobar el HEAD actual de GitHub al retomar.

La ilustración publicada muestra judías verdes planas: `images/menestra-guisada-ilustracion-v2.jpg`, con cabecera, tarjeta de Vegetales, textos alternativos, metadatos y créditos sincronizados. La imagen anterior se conserva como histórico. No hay actualización del catálogo privado de Eva asociada a estos cambios.

Acuerdo permanente: al incorporar cada receta, comprobar si aparece como ejemplo en el carrusel (también dentro de componentes o sin enlace). Enlazarla al publicarla si corresponde y sincronizar `semana-base.md`, `datos/semana-base.json` e `index.html`; no añadir ni sustituir ejemplos no acordados.

Marisa prepara la menestra siguiendo los consejos de la tía Genia, su cuñada. Presentación visible: «💚 Receta oral de Marisa, que prepara siguiendo los consejos de la tía Genia.». Conservar la versión oral y los ajustes separados. El nuevo generador `tools/generar_receta_tabla.py` conserva esta maquetación desde el maestro YAML; el PDF se genera con el programa común.

Al retomar, comprobar el HEAD de GitHub y el resultado del despliegue y de la verificación posterior a este commit: no confundir las comprobaciones de preparación con una publicación ya verificada. Esperar el siguiente encargo del usuario.

## Mantenimiento y recuperación

Actualizar con cada ARG, al cambiar un pendiente importante y antes de cambiar de chat, según «Para continuar en otro hilo» de la guía principal. Mantenerlo breve: los acuerdos permanentes y las instrucciones detalladas pertenecen a las guías.

Este documento puede quedar atrasado si una sesión se interrumpe. Compararlo siempre con el HEAD y los commits recientes. Los archivos temporales preparados sin publicar no son una copia duradera: comprobar su existencia y, si faltan, reconstruirlos a partir de los acuerdos descritos. No incluir información privada en este repositorio público.

## Iconos y aclaración del alcance de ARG · 21/10/2026

Iconos mostrados y aprobados mediante ARG, incorporados en el commit `2e93657dc4bc89c7d69d34feb10833d3c78bc19a`: favicon de hierbaluisa relleno con una flor lila e icono de inicio delineado con tres flores. Enlaces presentes en las 56 páginas públicas y en sus generadores; manifiesto y recursos en `images/iconos/`. Tamaños, rutas, sintaxis de generadores y noindex comprobados localmente. No cambian cabecera, imagen social ni contenido culinario.

La actualización documental quedó inicialmente bloqueada por una clasificación genérica de privacidad. El usuario pidió aclararla y corregir el procedimiento. Se documenta expresamente el alcance de ARG y la distinción entre referencias públicas y datos privados; no se desactivan controles ni se afirma que nunca volverán a bloquear una operación.

En la última comprobación, los recursos aún devolvían 404 en la web y no se había localizado una ejecución de despliegue para ese commit. Código guardado en GitHub; despliegue y aspecto en navegadores/iPhone pendientes. No confundir guardado, despliegue y comprobación de funcionamiento. Las cachés de iconos pueden conservar imágenes anteriores.

## Compatibilidad del icono con iPad no Retina · 21/10/2026

El usuario confirma que el icono funciona en sus otros dispositivos; un iPad no Retina con iOS 9 conserva una miniatura de la página. No se ha demostrado la causa. Cambio autorizado con «dale. ARG»: añadir PNG de 76 × 76 y enlace genérico sin tamaño a `apple-touch-icon.png` (180), conservando el icono actual de 180, favicons y diseño. Sincronizados los 56 HTML y siete generadores; referencia específica actualizada.

Comprobaciones locales: tamaños, formato RGB opaco, enlace genérico y tamaños únicos en head, rutas y noindex; modificación limitada a enlaces y recursos de icono. Publicación y disponibilidad HTTP se verifican después de guardar; prueba en el iPad iOS 9 pendiente. Borrar el acceso antiguo y volver a añadir desde Safari. El éxito en otros dispositivos es una confirmación del usuario, no una prueba ejecutada aquí.

La disponibilidad de los iconos iniciales que figuraba pendiente arriba quedó después comprobada por HTTP (portada, categoría de Legumbres, manifiesto e iconos); esa antigua mención a 404 ya es histórica.



## Gambas salteadas con trigueros · 25/10/2026

Ficha «Gambas salteadas con trigueros», tipo receta, categoría Mariscos. Dos raciones; 250 g de gambas crudas peladas congeladas (peso descongelado y escurrido), 300 g de trigueros, ajo y una cucharada de aceite. Saltear verdura y gambas por separado; reunir al final. Opciones: sustituir por calabacín en bastones de 4–5 cm por 1 cm; huevo escalfado aparte. Inspirada en una sugerencia de menú de Eva, sin atribuirle una receta completa. Maestros, HTML, PDF A4, ilustración y tarjetas NUEVA preparados; se retira su prevista. No corresponde a los ejemplos de gambas al ajillo con pasta del respaldo semanal: se conservan. Revisión mostrada y publicación autorizada mediante ARG. Comprobados YAML/JSON/Schema.org, PDF A4 de una página, noindex y filtros del buscador. Verificar el despliegue tras guardar el commit; no confundir las comprobaciones locales con disponibilidad en la web.

## Gambas al ajillo con pasta · 25/10/2026

Desarrollada la prevista `gambas-ajillo-pasta`, tipo receta y categoría Mariscos. Receta de Marisa, con manuscrito completo ampliable y transcripción diferenciados de la adaptación. Dos raciones: 100 g de pasta seca preferiblemente integral, 250 g de gambas peladas congeladas (peso descongelado y escurrido), dos ajos, una cucharada de aceite y una guindilla pequeña opcional. Cocer según envase y ligar al final con agua de la pasta durante 30–60 s. 20–25 min, con ajillo y gambas mientras cuece la pasta. El manuscrito conserva sus 250 g de pasta, 250 g de gambas, cinco ajos y dos guindillas.

Preparados maestro, JSON, Schema.org, HTML, PDF A4, ilustración y tarjetas NUEVA sin duplicados. Enlazados los dos ejemplos existentes del respaldo semanal (lunes y sábado), sin cambiar el reparto ni el menú vivo publicado. La guía incorpora las reglas acordadas de comprobar próximas antes de desarrollar fichas y preferir pasta integral, con 50 g secos por persona como referencia ajustable. Revisión mostrada y publicación autorizada mediante ARG. Datos, enlaces, manuscrito sin recortes, PDF A4 de una página y pruebas del carrusel, menú publicado, filtros y noindex comprobados. Verificar el despliegue tras guardar; las copias de revisión no se publican.

La crema de calabacín se publica en la incorporación posterior documentada al final de este resumen.

Al regenerar el respaldo se corrigió un error del generador: usar una función de sustitución para conservar literalmente las barras del JavaScript incrustado, sin interpretarlas como escapes de reemplazo. Se conserva el cargador del menú publicado.

## Crema de calabacín · 25/10/2026

Desarrollada la prevista `crema-calabacin`, tipo receta y categoría Purés, como receta de Marisa. Dos raciones: 600 g de calabacín con piel, dos ajos retirados tras dorar, dos quesitos (uno por persona), una cucharada de aceite de oliva, 100 ml de agua inicial y media pastilla de caldo vegetal. 25–30 min. Aceite en lugar de la margarina antigua, según la preparación actual de casa. Maestro, JSON, Schema.org, HTML, PDF A4, ilustración y tarjetas NUEVA preparados. Manuscrito completo ampliable y transcripción separados de la adaptación; no se atribuyen al original las cantidades afinadas o la aclaración de conservar la piel. No aparece como ejemplo en el carrusel: se conserva el respaldo semanal. Regla de comprobar fichas publicadas y próximas antes de desarrollar cualquiera preparada en la guía. Revisión mostrada y publicación autorizada mediante ARG. Integrada sobre el HEAD vigente conservando las dos recetas de gambas y sus enlaces. Comprobaciones locales y disponibilidad tras el despliegue se registran por separado.


## 26/10/2026 · Catálogo estructurado y publicación conjunta

Se incorpora un catálogo de fichas e ingredientes para consumidores del recetario, sin modificar recetas, imágenes ni menú publicado. El generador tools/exportar_catalogo_app.py valida los maestros y exportaciones del mismo commit. El workflow catalogo-app-pages.yml prepara datos/catalogo-app.json y publica páginas y catálogo conjuntamente. Se incluye una instantánea inicial de 31 fichas y 15 próximas generada desde c577350aa825c237279e1f291f98304d3599db35. No contiene datos de compra, menú privado, permisos ni credenciales. Comprobar el despliegue del workflow y la configuración de GitHub Pages antes de considerar activa la generación automática.
