# Terreno 3D

Con la ubicación fijada, activa **Terreno 3D** en el panel Terreno: IngeTrazo descarga el modelo de elevaciones de tu zona (DEM) y **drapea la imagen satelital sobre el relieve real**.

- El relieve cubre el área de captura definida en el localizador.
- La **altitud del origen** se referencia al datum del proyecto, así las cotas que leas son elevaciones reales.
- Es geometría de **referencia visual**: puedes orbitarla, medir sobre ella y trazar encima, pero no entra al motor de sólidos ni al metrado.

## Trazar sobre el terreno

- La herramienta **Ruta** ([ver Rutas y perfil](rutas-perfil.md)) lee la elevación del terreno bajo el cursor y te da el perfil longitudinal del trazo.
- El mapa base plano y el terreno 3D son intercambiables: el mismo sitio, con o sin relieve.

!!! note "El escalón entre fuentes de elevación"
    El DEM global usa altitudes ortométricas (sobre el nivel del mar); un levantamiento de dron sin puntos de control usa altitudes GNSS (elipsoidales). Si ves un pequeño escalón vertical entre el terreno 3D y tu levantamiento, es la diferencia real entre datums verticales — no un error de encaje.

## Superficie de referencia

Cuando hay varias fuentes (DEM, levantamiento de dron), las consultas de elevación usan la **más precisa disponible** en cada punto: tu vuelo manda sobre el DEM satelital de 30 m.
