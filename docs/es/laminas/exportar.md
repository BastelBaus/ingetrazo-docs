# Exportar PDF, imagen y DXF

Todo está en la **barra de lámina**, bajo el título de la ventana del compositor: vista previa, PDF e imagen; el DXF, en el menú del marco.

## Vista previa de impresión

**Vista previa de impresión…** muestra la lámina tal como saldrá: tamaño real, grosores de línea, sin manijas ni imanes. Es el lugar para revisar antes de exportar.

## PDF de una lámina

**Exportar PDF…** escribe la lámina actual con métrica física exacta: el A3 sale A3, la escala 1:100 **mide** 1:100 sobre el papel impreso. El PDF es **vectorial** — las líneas del estilo Vectorial son curvas reales con sus tres plumas y su poché, no píxeles: se imprime nítido a cualquier tamaño. Nada de la pantalla se cuela: ni la selección del modelo, ni las manijas, ni los imanes.

## PNG o JPG de una lámina

**Exportar imagen…** escribe la lámina actual como **PNG o JPG**: eliges el archivo y luego la resolución en puntos por pulgada (200 por defecto; se recuerda la última). La imagen sale al tamaño exacto del papel —un A3 apaisado a 200 ppp son 3307 × 2339 píxeles—, con fondo blanco y el mismo pintor que el PDF, lista para un informe, un correo o una presentación.

## El atlas: todas las láminas en un PDF

**Exportar todas las láminas (PDF)…** genera un solo archivo con cada lámina del documento en su propia página (cada una con su tamaño de papel) — el juego de planos completo del expediente en un clic.

## DXF hacia IngeCAD / AutoCAD

Con un marco seleccionado, **Exportar vista como DXF…** escribe el dibujo vectorial de esa vista (las líneas visibles exactas, en metros de modelo, con el giro de la vista aplicado) como DXF R12 — lo abre [IngeCAD](https://ingecad.org), AutoCAD, LibreCAD o QGIS. Las clases de línea van en capas separadas —`VISTA`, `VISTA-PERFIL`, `VISTA-CORTE`— para tu tabla de plumas. Es el puente para quien remata detalles 2D en su CAD de siempre.

!!! tip "Antes de exportar"
    - **Actualiza los marcos** si editaste el modelo con el compositor abierto (o deja el renderizado automático encendido).
    - Revisa a **zoom 100 %** (tamaño real del papel) o en la vista previa: los grosores de línea y tamaños de texto se ven exactamente como saldrán impresos.
    - Los cuatro [ejemplos](../primeros-pasos/ejemplos.md) traen el PDF de su lámina al lado, por si quieres comparar.
