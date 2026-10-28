# Rutas, perfil y puntos topográficos

## La herramienta Ruta

**`Y`** activa Ruta (GeoPath): traza alineamientos georreferenciados — el eje de una carretera, un canal, un lindero.

- Clic a clic sobre el mapa, el terreno 3D o tu levantamiento de dron.
- La etiqueta en vivo muestra **longitud, cota y pendiente (%)** de cada tramo.
- Las rutas viven en su propio subsistema: no se mezclan con la geometría del modelo.

## Perfil longitudinal

Con una ruta seleccionada, el **panel de perfil** muestra el perfil longitudinal al instante, muestreado de la mejor superficie disponible (tu vuelo de dron si existe; si no, el DEM):

- **Progresivas** en el eje horizontal, cotas en el vertical.
- Export a **CSV** (para tu hoja de cálculo o diseño geométrico) y a **PNG**.
- **En las láminas**: la herramienta **Perfil** del compositor dibuja el perfil sobre la hoja con escala horizontal y vertical, exageración, progresivas y cotas; y los marcos de planta muestran el trazado con sus **progresivas** (0+000, 0+020…), con el mismo paso que el perfil, para que coincidan. Ver [Marcos de vista](../laminas/marcos.md#extras-del-marco).
- **Herramientas ▸ Perfil del terreno de la selección** saca el perfil de cualquier polilínea seleccionada; con clic derecho sobre una ruta eliges si su superficie es plana, drapeada al relieve o solo la línea, y **Convertir ruta en geometría** la vuelve aristas del modelo.

## Puntos de estación total / GPS

Archivo ▸ Importar ▸ **Puntos topográficos (CSV)**: el clásico `P,N,E,Z,descripción` en UTM.

- Indica la **zona y el hemisferio** al importar (si el proyecto aún no tiene datum, el primer punto lo ancla).
- Los puntos aparecen como marcadores con su número y descripción, y las herramientas de dibujo **enganchan sobre ellos con precisión exacta** — dibujas el lindero uniendo tus puntos reales.

## KML y GeoJSON

Importa alineamientos y polígonos de Google Earth o QGIS: llegan georreferenciados a su posición correcta (los elementos sin altitud propia se posan sobre el plano de referencia del proyecto).
