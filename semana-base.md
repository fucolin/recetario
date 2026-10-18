---
esquema: recetario-semana-base-1.1
id: semana-base
titulo: Mi semana base
fecha_actualizacion: '2026-10-16'
fuente: Excel semana-base-casa-marisa(2).xlsx aportado por el usuario el 16 de octubre de 2026.
dias:
  - dia: Lunes
    comida:
      - texto: Verduras
        categoria: Vegetales
        ejemplo: {titulo: Menestra guisada, pagina: menestra-guisada.html}
    cena:
      - texto: Picoteo sanote
        categoria: Picoteo y guarniciones
        ejemplo:
          titulo: Barquitas de endivia con requesón + hummus con zanahoria
          componentes:
            - {titulo: Barquitas de endivia con requesón, pagina: barquitas-endivia-requeson.html}
            - {titulo: hummus con zanahoria, pagina: hummus-zanahoria.html}
  - dia: Martes
    comida:
      - texto: Pescado azul
        categoria: Pescado azul
        ejemplo:
          titulo: Salmón + pimientos asados
          componentes:
            - {titulo: Salmón, pagina: null}
            - {titulo: pimientos asados, pagina: pimientos-asados-cebolla-cosori.html, categoria: Picoteo y guarniciones}
    cena:
      - texto: Tortilla
        categoria: Huevos
        ejemplo: {titulo: Tortilla de boniato y espinacas, pagina: tortilla-boniato-espinacas-parmesano.html}
  - dia: Miércoles
    comida:
      - texto: Legumbres
        categoria: Legumbres
        ejemplo: {titulo: Lentejas con calabaza y espinacas, pagina: lentejas-calabaza-espinacas-400g.html}
    cena:
      - texto: Carne exprés
        categoria: Carnes exprés
        ejemplo: {titulo: Pechuga de pavo a la plancha, pagina: pechuga-pavo-plancha.html}
  - dia: Jueves
    comida:
      - texto: Puré
        categoria: Purés
        ejemplo: {titulo: aprovechategui, pagina: crema-aprovechamiento-marisa.html}
      - texto: Pescado blanco
        categoria: Pescado blanco
        ejemplo: {titulo: Lubina a la plancha, pagina: null}
    cena:
      - texto: Revuelto
        categoria: Huevos
        ejemplo: {titulo: de champiñones y trigueros, pagina: revuelto-champinones-trigueros.html}
  - dia: Viernes
    comida:
      - texto: Ensalada
        categoria: Ensaladas
        ejemplo: {titulo: 'de salmón, mango y aguacate', pagina: ensalada-salmon-ahumado-mango-aguacate.html}
    cena:
      - texto: Envuelto/Bocata
        categoria: Envueltos y bocados
        ejemplo:
          titulo: Burrito de frijoles negros + puré aprovechategui
          componentes:
            - {titulo: Burrito de frijoles negros, pagina: burrito-frijoles-negros.html}
            - {titulo: puré aprovechategui, pagina: crema-aprovechamiento-marisa.html, categoria: Purés}
  - dia: Sábado
    comida:
      - texto: Marisco
        categoria: Mariscos
        ejemplo: {titulo: Gambas al ajillo con pasta, pagina: null}
      - texto: Ensalada
        categoria: Ensaladas
        ejemplo: {titulo: de tomate y mozzarella, pagina: null}
    cena:
      - texto: Libre
        categoria: null
        ejemplo: null
        aclaracion: Respete vd. las cantidades
        icono_aclaracion: advertencia
  - dia: Domingo
    comida:
      - texto: Guiso
        categoria: Guisos y asados
        ejemplo: {titulo: Pollo guisado con calabacín, pagina: pollo-guisado-calabacin.html}
    cena:
      - texto: Sopa
        categoria: null
        ejemplo: {titulo: de fideos, pagina: null}
      - texto: Huevos
        categoria: Huevos
        ejemplo: {titulo: Fajita de francesa, pagina: fajita-francesa-pavo.html, categoria: Envueltos y bocados}
---

# Mi semana base

Guía semanal personal acordada con el usuario. Cada día conserva comida y cena; no representa un menú fechado ni una pauta nutricional evaluada.

Se muestra en la portada después del encabezado de Casa Marisa, sin título visible. Carrusel infinito en escritorio y móvil, con tres días visibles en escritorio y el actual centrado inicialmente según Europe/Madrid. El día actual se distingue por el color de su cabecera, sin la palabra «Hoy» dentro de esa celda. Debajo va «Para elegir y comprar», con su título como pestañita en el borde; después, «Las recetas» introduce la botonera, el buscador y el listado. No mostrar el enlace «Más recetas…». Los tipos de plato son texto en negrita sin enlace; debajo aparecen los ejemplos indicados por el usuario, con enlace solo cuando existe la ficha adecuada. Los ejemplos sin ficha se muestran como texto, sin inventar páginas. Los ejemplos compuestos conservan cada componente y sus enlaces por separado. «Ejemplo pendiente» se reserva para un ejemplo aún no elegido. No sustituir tortilla francesa por otra tortilla ni completar la cena libre. No crear fichas ni tarjetas futuras a partir de esta tabla sin petición específica.
