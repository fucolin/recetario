# Catálogo de ingredientes y referencias

## Identidad

Cada producto tiene un ID de la forma `cm-ing-000001`, único, inmutable y no reutilizable. Cambiar un nombre o categoría no cambia el ID. El registro compartido contiene ID y nombre; las clasificaciones y estados de uso de aplicaciones consumidoras son independientes. Mantener la secuencia de altas y comprobar la identidad antes de crear un producto. Conservar correspondencias cuando se retire un duplicado.

## Recetas1.1

El nombre de un ingrediente es el texto para cocinar; `catalogo_ref` es su identidad. «Boniato pelado» conserva nombre, cantidad y unidad y enlaza con Boniato. `ingredientes_basicos` enumera IDs existentes; los básicos se deciden por receta. En `ingredientes_basicos_opciones`, `ingredientes` y `sustituye` también usan IDs; cada sustitución debe apuntar a un básico de la receta.

Una línea como sal y pimienta se separa en dos ingredientes. Conservar condiciones y no inventar cantidades. Los pasos y la presentación pueden seguir agrupándolos. Actualizar las referencias por índice de `condimentos_opciones` cuando cambie el orden o número de líneas.

## Alternativas

`alternativas` contiene objetos con nombre, catalogo_ref y atributos de cada rama; `seleccion: "una"` expresa exclusión mutua. No indica que se haya seleccionado una rama. La elección concreta corresponde a la preparación del menú. Si el grupo carece de catalogo_ref propio, sus identidades son las ramas; si tiene referencia propia, esa referencia es el ingrediente base y las ramas sus sustituciones. No se suman las ramas a la base.

«Agua o caldo de pollo» conserva su texto y condición, con dos ramas. El agua no genera necesidad y el caldo solo cuenta si se elige. Una cantidad común pertenece al grupo, no se duplica en las ramas. Los productos preferidos de una rama no se heredan en otra. Las anotaciones de condimentos conservan el papel local y su origen.

## Exportación y compatibilidad

El exportador acepta1.0 y1.1. Para1.0 mantiene la salida previa. Para1.1 valida todas las referencias contra el registro del mismo commit; conserva los IDs en los ingredientes fuente y catalogueMetadata y proyecta shoppingMetadata por nombres para consumidores anteriores. Esta proyección no elige opciones ni migra preparaciones guardadas. El transporte conserva schemaVersion1; las aplicaciones que quieran usar los IDs como identidad propia necesitan integración específica.

Conservar maestros YAML y JSON sincronizados. Estos metadatos no añaden propiedades no estándar a Schema.org ni cambian la presentación culinaria o su fecha. No publicar una ficha1.1 sin registro y exportador compatibles.
