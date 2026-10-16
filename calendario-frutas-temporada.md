---
esquema: recetario-calendario-frutas-1.0
id: calendario-frutas-temporada
titulo: Calendario de frutas de temporada
fecha_actualizacion: '2026-10-16'
criterio: Fruta de España y, cuando sea posible, de temporada en Galicia.
alcance: Selección orientativa de compra, no un inventario de todas las cosechas. Los meses cambian según variedad, zona y campaña. Comprobar siempre el origen real.
fuentes:
  - id: mapa
    nombre: MAPAMA · Calendario de frutas de temporada (2017), página 27
    url: https://diario.madrid.es/cieacasadecampo/wp-content/uploads/sites/61/2021/07/guia_restauracion_web_2017.pdf#page=27
    uso: Base nacional; selección propia a partir de sus meses de temporada y transición. No equivale a fechas exactas de cosecha.
  - id: trops-aguacate
    nombre: TROPS · Campaña nacional del aguacate
    url: https://es.linkedin.com/posts/trops_aguacate-aguacatetrops-activity-7290743466890829827-cvvg
    uso: Ventana preferente diciembre–mayo para aguacate nacional; no agota las variedades ni zonas.
  - id: trops-mango
    nombre: TROPS · Mango nacional
    url: https://www.trops.es/mango/
    uso: Producción nacional agosto–diciembre; meses destacados septiembre–noviembre.
  - id: manzana-galicia
    nombre: USC y CIAM · Colección de cultivares autóctonos gallegos de manzano (2001)
    url: https://frutales.files.wordpress.com/2011/01/maceiras.pdf
    uso: Referencia varietal para una selección de cosecha agosto–octubre; no representa todas las variedades gallegas.
  - id: pera-galicia
    nombre: Plantamus · Peral Urraca Legítima
    url: https://plantamus.com/peral-urraca-legitima-frutal-autoctono-de-galicia-b13f5/
    uso: Recolección a finales de agosto de esta variedad concreta, no de todas las peras gallegas.
  - id: arandano-galicia
    nombre: Berries do Camiño · Plantación de Lugo
    url: https://berriesdocaminho.com/
    uso: Campaña de finales de junio a finales de septiembre en esta explotación.
  - id: cereza-galicia
    nombre: Xunta de Galicia · O home do lume (2013), ficha de la cerdeira
    url: https://mediorural.xunta.gal/sites/default/files/publicacions/2019-10/o_home_do_lume_2013.pdf
    uso: Maduración en mayo y junio; puede variar por localidad y variedad.
  - id: kiwi-galicia
    nombre: Kiwi Atlántico · Recolección
    url: https://kiwiatlantico.com/kiwi-atlantico-en-plena-recoleccion/
    uso: Campaña de noviembre y comienzo de diciembre descrita por el productor.
  - id: kiwi-conservacion
    nombre: Campo Galego · Entrevista al sector del kiwi gallego (2016)
    url: https://www.campogalego.es/?p=28730
    uso: Comercialización de producción española noviembre–junio. Se elige enero–mayo como referencia conservadora de compra tras la cosecha, sujeta a existencias.
frutas:
  - {nombre: Aguacate, espana: [12, 1, 2, 3, 4, 5], galicia: [], fuentes: [trops-aguacate], nota: Ventana preferente nacional; otras variedades pueden ampliar la campaña.}
  - {nombre: Albaricoque, espana: [4, 5, 6, 7, 8, 9], galicia: [], fuentes: [mapa], nota: Abril y septiembre son meses de transición.}
  - {nombre: Arándano, espana: [6, 7, 8, 9], galicia: [6, 7, 8, 9], fuentes: [arandano-galicia], nota: Selección centrada en la campaña gallega; no cubre toda la producción española. Finales de junio a finales de septiembre en la explotación consultada.}
  - {nombre: Caqui, espana: [9, 10, 11, 12, 1], galicia: [], fuentes: [mapa], nota: Septiembre y enero son meses de transición.}
  - {nombre: Cereza, espana: [4, 5, 6, 7], galicia: [5, 6], fuentes: [mapa, cereza-galicia], nota: Abril es transición nacional; la referencia gallega sitúa la maduración en mayo–junio.}
  - {nombre: Chirimoya, espana: [9, 10, 11, 12, 1], galicia: [], fuentes: [mapa], nota: Septiembre y enero son meses de transición.}
  - {nombre: Ciruela, espana: [5, 6, 7, 8, 9], galicia: [], fuentes: [mapa], nota: Mayo y septiembre son meses de transición.}
  - {nombre: Frambuesa, espana: [5, 6, 7, 8, 9], galicia: [], fuentes: [mapa], nota: Mayo y septiembre son meses de transición; sin ventana gallega específica en esta versión.}
  - {nombre: Fresa y fresón, espana: [1, 2, 3, 4, 5, 6], galicia: [], fuentes: [mapa], nota: Enero y junio son transición en la referencia nacional; cultivos locales pueden tener otras fechas.}
  - {nombre: Granada, espana: [8, 9, 10, 11], galicia: [], fuentes: [mapa], nota: Agosto es transición.}
  - {nombre: Higo, espana: [6, 7, 8, 9, 10], galicia: [], fuentes: [mapa], nota: Junio y octubre son transición en la fuente; no se separan brevas e higos.}
  - {nombre: Kiwi, espana: [11, 12, 1, 2, 3, 4, 5, 6], galicia: [11, 12], conservacion_galicia: [1, 2, 3, 4, 5], fuentes: [kiwi-galicia, kiwi-conservacion], nota: Ventana comercial española noviembre–junio según la referencia sectorial; el final depende de existencias. Cosecha gallega de referencia en noviembre y comienzo de diciembre. En invierno y primavera puede venderse fruta conservada; confirmar origen.}
  - {nombre: Limón, espana: [10, 11, 12, 1, 2, 3, 4, 5, 6], galicia: [], fuentes: [mapa], nota: Ventana del calendario base; las variedades y zonas pueden ampliarla.}
  - {nombre: Mandarina, espana: [10, 11, 12, 1, 2, 3, 4], galicia: [], fuentes: [mapa], nota: Octubre y abril son transición.}
  - {nombre: Mango, espana: [8, 9, 10, 11, 12], galicia: [], fuentes: [trops-mango], nota: Priorizar septiembre–noviembre; agosto y diciembre dependen de variedades y campaña.}
  - {nombre: Manzana, espana: [7, 8, 9, 10, 11, 12, 1, 2], galicia: [8, 9, 10], fuentes: [mapa, manzana-galicia], nota: Selección de cosecha gallega agosto–octubre según variedades documentadas. Su venta posterior puede proceder de conservación. Hay variedades fuera de esta selección.}
  - {nombre: Melocotón y nectarina, espana: [4, 5, 6, 7, 8, 9, 10], galicia: [], fuentes: [mapa], nota: Abril y octubre son transición.}
  - {nombre: Melón, espana: [5, 6, 7, 8, 9, 10], galicia: [], fuentes: [mapa], nota: Mayo y octubre son transición.}
  - {nombre: Naranja, espana: [10, 11, 12, 1, 2, 3, 4, 5], galicia: [], fuentes: [mapa], nota: Octubre y mayo son transición; variedades tardías pueden ampliar la campaña.}
  - {nombre: Níspero, espana: [3, 4, 5, 6], galicia: [], fuentes: [mapa], nota: Marzo y junio son transición.}
  - {nombre: Paraguayo, espana: [6, 7, 8, 9], galicia: [], fuentes: [mapa], nota: Junio y septiembre son transición.}
  - {nombre: Pera, espana: [6, 7, 8, 9, 10, 11, 12], galicia: [8], fuentes: [mapa, pera-galicia], nota: La prioridad gallega se refiere a Urraca Legítima a finales de agosto. No se extrapola a todas las variedades. La venta de pera también puede incluir conservación.}
  - {nombre: Plátano de Canarias, espana: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], galicia: [], fuentes: [mapa], nota: Producción española todo el año; comprobar la indicación de origen Canarias.}
  - {nombre: Pomelo, espana: [11, 12, 1, 2, 3, 4, 5], galicia: [], fuentes: [mapa], nota: Noviembre y mayo son transición.}
  - {nombre: Sandía, espana: [5, 6, 7, 8, 9], galicia: [], fuentes: [mapa], nota: Mayo y septiembre son transición.}
  - {nombre: Uva de mesa, espana: [8, 9, 10, 11, 12], galicia: [], fuentes: [mapa], nota: Agosto es transición. La uva de mesa no se confunde con las fechas de vendimia de uva para vino.}
---

# Calendario de frutas de temporada

Fruta de España y, cuando sea posible, de temporada en Galicia.

## Cómo usarlo

- Primero comprobar el país de origen; después, buscar procedencia gallega cuando encaje con la cosecha local.
- La columna España es una ventana orientativa de compra que incluye inicios y finales de campaña, no un calendario estricto de recolección ni una promesa de disponibilidad.
- La selección gallega recoge cosechas concretas documentadas. Que una fruta no esté marcada no significa que no se cultive en Galicia.
- La fruta conservada tras la cosecha se distingue de la recién recogida. Manzanas, peras y kiwis pueden seguir siendo de origen español fuera de los meses indicados.
- La marca del distribuidor o el lugar de envasado no sustituyen al origen del fruto. Preguntar en la frutería cuando el cartel solo diga España.
- No se incluyen frutos secos ni fruta desecada. No hay clasificaciones nutricionales ni recomendaciones de marcas.

Las fuentes y las notas de cada fruta están en los metadatos. La base nacional de 2017 se complementa con información de productores; es una referencia inicial que podremos afinar con la oferta real de nuestras tiendas.
