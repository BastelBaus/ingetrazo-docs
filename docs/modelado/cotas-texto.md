# Cotas y anotación 3D

Estas son las anotaciones **dentro del modelo 3D**. Para las cotas sobre la hoja impresa, mira [Composición de láminas](../laminas/anotacion.md).

## Cotas

**`D`** activa Cota:

1. Clic en el primer punto (las inferencias enganchan extremos y puntos medios).
2. Clic en el segundo punto.
3. Mueve para separar la línea de cota del modelo y clic para fijarla. Si separas la cota **más allá de un extremo**, en la dirección de un eje, se vuelve **lineal** (mide la proyección sobre ese eje); si la separas en escuadra, queda **alineada** (mide la distancia real). La barra de estado dice cuál es.

La cota queda **anclada a la geometría**: cada extremo que cae sobre un vértice se agarra a él, así que si luego **escalas, mueves o estiras** el dibujo, la cota se va con él y **vuelve a medir** — no se queda flotando con la medida vieja. Un extremo dentro de un componente sigue a la instancia. Si el vértice desaparece (lo borras), el extremo se queda donde estaba. Un extremo puesto en un punto medio o sobre una arista no tiene vértice al que agarrarse y se queda fijo.

Con **Mover** (`M`) sobre una cota, la **línea de cota se desplaza** y las líneas de referencia se estiran desde sus vértices; si la seleccionas junto con la geometría, viaja con ella.

El desplegable **Estilo de cota** de la barra de herramientas controla color, altura de texto, decimales, **unidades** (metros, centímetros, pulgadas, pies, y las fraccionarias `1 1/2"` — ver [medidas por teclado](dibujo.md#medidas-por-teclado-metros-centimetros-pulgadas-pies)) y los **extremos**: flechas (lo que trae un documento nuevo), trazos oblicuos o ninguno — un documento anterior conserva sus trazos. Las cotas se seleccionan, se borran con `Supr` y salen en los [marcos de las láminas](../laminas/marcos.md#extras-del-marco) si activas «Anotaciones del modelo», con los mismos extremos.

### Norma de acotación

Las cotas siguen la norma **ISO / UNE**: el texto va **encima** de la línea de cota, centrado a lo largo de ella, y **la línea no se interrumpe nunca**. El texto se orienta para leerse girando la cabeza a la **izquierda**: una cota vertical se lee de abajo arriba, la dibujes hacia arriba o hacia abajo. Es la única norma disponible por ahora (la alemana/japonesa, con la línea partida y el texto en medio, queda para una versión futura).

En el mismo panel está el **Escalón de línea base**: la separación entre filas de una serie de [cotas desde línea base](../laminas/anotacion.md#cotas-desde-linea-base), el `DIMDLI` de AutoCAD.

## Texto guía

La herramienta **Texto** (`X`) coloca etiquetas con línea guía apuntando a una cara o arista — nombres de ambientes, notas de obra. El texto siempre mira a la cámara; se mueve con su ancla clavada, se edita con doble clic. Cotas y textos guía pueden vivir en una **capa**: apaga «Cotas» y desaparecen de la vista y de las láminas que no las quieren.

## Texto 3D

Dibujo ▸ **Texto 3D** genera letras con geometría real (extruibles, pintables) — para letreros y monumentos, como las letras de una plaza.

## Cinta métrica y transportador

- **Cinta** (`T`): mide y deja **guías** punteadas de construcción. Desde una arista o desde un **eje** del sistema (clic sobre el eje, y vale con el documento vacío: así se sitúa un proyecto «a 20 m y a 5 m del origen» antes de dibujar nada), una guía paralela a la distancia arrastrada o tecleada; desde un **punto con nombre** (extremo, centro, intersección, origen), un **punto guía con su segmento** discontinuo hasta el punto de partida, el «segmento guía» para centrar un círculo o marcar el vuelo de un alero; de punto a punto solo mide (un punto medio no cuenta como punto). Tiene el mismo imán de ejes que la Línea: una medida a pocos grados de un eje cae sobre él, con su color.
- **Transportador** (`Mayús+H`): guías angulares; sus brazos también se imantan a los ejes que están en el plano del disco.
- Las guías no son geometría: no salen en exports ni metrados, y se limpian con Edición ▸ Eliminar guías.
