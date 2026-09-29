# Herramientas de dibujo

Todas comparten el mismo lenguaje: clic para empezar, las **inferencias** te enganchan a la geometría existente, y el **VCB** acepta la medida exacta por teclado (escribe y Enter, sin hacer clic en ningún campo).

## Líneas y polígonos

| Herramienta | Atajo | Cómo se usa |
|---|---|---|
| **Línea** | `L` | Clic a clic; teclea la longitud para el tramo exacto. Cierra un contorno y la cara se crea sola. |
| **Rectángulo** | `R` | Dos esquinas; teclea `ancho,alto` (ej. `6,4`). **`Ctrl`** alterna a **desde el centro** (centro y una esquina): el sello del lápiz cambia, y el `ancho,alto` tecleado es el tamaño **completo**. Al volver a coger la herramienta arranca desde la esquina. |
| **Rectángulo rotado** | `K` | Primero la base (dos puntos), luego el alto. |
| **Círculo** | `C` | Centro y radio; teclea el radio. |
| **Polígono** | — | Centro y radio; teclea el número de lados (la `G` es Crear componente). |
| **Mano alzada** | — | Arrastra y suelta: una polilínea suavizada que se selecciona entera de un clic, como un círculo; si cierra, crea la cara. |

## Arcos

| Herramienta | Atajo | Cómo se usa |
|---|---|---|
| **Arco** | `A` | Los dos extremos (la cuerda) y luego la comba. Es el arco de 2 puntos. Teclea la comba, o `2r` para el radio. **Redondear una esquina**: empieza sobre una arista, y en la arista vecina, a la misma distancia de la esquina, el arco se vuelve **magenta** (tangente a las dos); doble clic ahí lo dibuja y recorta la esquina, y con el arco magenta **un número tecleado es el radio del redondeo**, manteniendo las tangencias. |
| **Arco 3 puntos** | `J` | Extremo, un punto por el que pasa y el otro extremo. |
| **Arco por centro** | `Mayús+O` | Centro, radio inicial y barrido. |
| **Porción** (Pie) | — | Como Arco por centro, pero cierra el sector con los dos radios y su cara. |

## Derivadas

| Herramienta | Atajo | Cómo se usa |
|---|---|---|
| **Equidistancia (Offset)** | `F` | Copia el contorno de una cara hacia adentro o afuera, a distancia exacta. El clásico para espesores de muro. También funciona con **aristas**: clic sobre una arista suelta y desfasa toda su cadena conectada (abierta o cerrada), o preselecciona las aristas que quieras y haz clic en una de ellas. |
| **Sígueme (Follow me)** | `W` | Extruye un perfil a lo largo de un camino: molduras, tuberías, sardineles. |
| **Texto 3D** | — | Dibujo ▸ Texto 3D: letras con volumen real (fuente, negrita, cursiva, altura y espesor), listas para extruir o pintar. |

### Sígueme, tres maneras

Dibuja el perfil **perpendicular al camino** (lo más fácil: sobre una cara, y borra las aristas que sobren).

1. **Arrastrar por el camino** — activa Sígueme (`W`), haz clic en el perfil y mueve el cursor por el camino tocando sus aristas: el camino se resalta en **rojo** y la extrusión se previsualiza en vivo, con sus ingletes. Clic (o soltar el botón, si arrastraste) al llegar al final; `Esc` empieza de nuevo. Si te saltas tramos de un arco, se siguen las aristas conectadas que hay en medio; si retrocedes, el camino se acorta.
2. **Camino preseleccionado** — selecciona las aristas del camino (un clic en un segmento de círculo toma todo el contorno), activa Sígueme y haz clic en el perfil: se extruye de una vez.
3. **Perímetro de una cara** — selecciona la cara cuyo borde es el camino y haz clic en el perfil; o, mientras arrastras, mantén `Alt` sobre una cara para usar su perímetro. Es el atajo para molduras alrededor de una losa y para **tornear**: un círculo como camino y medio perfil como sección.

## Medidas por teclado: metros, centímetros, pulgadas, pies

Los números sin sufijo están en la **unidad del documento** (metros salvo que la cambies en [Preferencias ▸ Unidades](../preferencias.md#unidades): en un documento en milímetros, `500` es medio metro). Cada campo puede llevar su propia unidad, así que puedes dibujar la madera o la tubería en pulgadas y las luces en metros dentro del mismo modelo:

| Escribes | Vale |
|---|---|
| `3,2` | 3,20 m |
| `30cm` · `1500mm` | 0,30 m · 1,50 m |
| `2"` · `2in` | 2 pulgadas |
| `1'` · `1ft` | 1 pie |
| `1'6"` | 1 pie 6 pulgadas |
| `3/4"` · `1'3/4"` | fracciones de pulgada |
| `1 1/2"` · `1-1/2"` · `1'6 1/2"` | pulgada y media, pie y seis y media (número mixto) |
| `2";4"` | rectángulo de 2 × 4 pulgadas |
| `3,2;1'6";10cm` | desplazamiento X, Y, Z con unidades mezcladas |

Las comillas y la barra de fracción solo se aceptan después de un número, así que `I` y `F` siguen siendo atajos de herramienta.

**Acotar en pulgadas o pies.** En el estilo de cotas de la bandeja (y en cada cota de lámina, en su panel) elige las unidades: `m`, `cm`, `mm`, `in`, `ft`, `ft-in`, o las fraccionarias `in-frac` (`1 1/2"`) y `ft-in-frac` (`1'6 1/2"`). En las fraccionarias, **Decimales** fija el denominador más fino: 0 = pulgadas enteras, 1 = 1/4, 2 = 1/16, 3 = 1/32, 4 = 1/64.

## El plano de trabajo

Las herramientas dibujan sobre el **plano que estás mirando**: en vista superior dibujas en planta; si empiezas sobre una cara existente, dibujas sobre esa cara. El primer punto sin inferencia queda en el plano de la vista actual — así el trazo nunca "se escapa" a una profundidad inesperada.

**Fijar el plano con las flechas** (círculo, polígono, rectángulo y arcos): antes del primer clic, `→` fija el plano normal a X (el YZ), `←` el normal a Y (el XZ) y `↑` el normal a Z (el XY); la misma flecha otra vez, o `Esc`, lo libera, y una etiqueta del color del eje lo indica. Con el plano fijado, el centro puede caer sobre una cara y la figura sale igualmente en el plano elegido. La figura gasta el bloqueo; tras el primer clic, las flechas vuelven a ser el bloqueo de eje de siempre.

**Perpendicular a una arista con `↓`** (el bloqueo magenta): antes del primer clic, con el cursor sobre una arista, `↓` fija el plano de dibujo perpendicular a esa arista; sobre una cara, paralelo a ella. El anillo del cursor se pinta magenta y `↓` otra vez lo libera. Es la manera de dibujar un tubo sobre un eje inclinado: traza la línea del eje, pulsa `↓` sobre ella, pon el centro del círculo en su extremo, da el radio y aplica Sígueme; el círculo ya sale perpendicular al eje, sin rotarlo después.

!!! tip "Dibujar en vistas estándar"
    Para trabajo de precisión tipo 2D, combina **vista estándar + proyección paralela** (`P`): frontal para fachadas, superior para plantas. Las medidas que ves en pantalla son las reales del plano, sin efecto de perspectiva.

## Inferencias

Los puntos de colores mientras dibujas:

- **Verde** — extremo de arista.
- **Cian** — punto medio.
- **Rojo/verde/azul** — sobre un eje del sistema (X este, Y norte, Z vertical). El **imán de ejes** (un trazo a pocos grados de un eje cae sobre él) lo tienen todas las herramientas que trazan: Línea, Arco, Círculo, Polígono, Rectángulo rotado, Cinta, Transportador, Cota, Texto y Mover.
- **Magenta** — paralela o perpendicular a una arista existente.

Mantén el mouse un instante sobre un punto para "memorizarlo" y proyectar desde él: al alinearte con él por un eje aparece una línea punteada desde el punto (**Desde el punto**).

Y en **otra pared** —perpendicular o la de enfrente—, al pasar a la altura de un punto memorizado el cursor se engancha a una línea punteada que recorre esa pared a esa altura (**A la altura del punto**): así se ponen todas las ventanas de una casa a la misma altura sin líneas guía. Sobre el suelo, bajo un punto alto, lo mismo en planta (**En línea con el punto**).
