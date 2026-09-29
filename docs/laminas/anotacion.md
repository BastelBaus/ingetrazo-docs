# Cotas, textos, formas y cajetín

## Cotas sobre la hoja

La herramienta **Cota** del compositor acota sobre el dibujo del marco:

1. **Clic en el primer punto** — sobre un vértice o arista del dibujo aparece el **punto verde**: el snap engancha la geometría real visible del marco.
2. **Clic en el segundo punto** (también en verde).
3. **Mueve y tercer clic** para separar la línea de cota del dibujo — con sus líneas de extensión, como manda el dibujo técnico.

La herramienta **sigue activa** para la cota siguiente; `Esc` (con nada a medias) o el cursor la dejan.

### Cota forzada recta (`Mayús`)

Dos puntos que **no están alineados** dan, por defecto, una cota inclinada: mide la distancia entre ellos, que es lo que pide una cota alineada. Pero muchas veces lo que quieres es **la altura** o **el ancho** entre esos dos puntos, y entonces la cota tiene que salir recta.

**`Mayús`** en cualquier momento del gesto la fuerza recta: elige el eje en el que los dos puntos están más separados, **no mueve los puntos** —cada uno se queda donde enganchó— y la cota mide solo esa parte, con **líneas de referencia de distinta longitud** llegando a cada punto. Es la cota lineal de AutoCAD.

No hace falta acertar con el momento: la elección **se queda** hasta que colocas la cota, y después el desplegable **Dirección** del panel (*Alineada con los dos puntos* / *Forzada horizontal* / *Forzada vertical*) la cambia en cualquier cota ya dibujada, con deshacer.

### Cotas ancladas al modelo

Si ambos puntos engancharon en verde, la cota queda **anclada a los puntos 3D del modelo**:

- La etiqueta muestra la **distancia real 3D exacta** (no una medida de papel multiplicada).
- Si **editas el modelo** (la pared se estira de 6.00 a 6.20 m), la cota se mueve y **se re-mide sola**.
- Si mueves el marco, cambias su escala, su vista o su giro, la cota lo sigue.
- Al seleccionarla, sus manijas son **verdes** (ancladas) o azules (cota libre de papel). Arrastrar a mano un extremo la libera del anclaje (con deshacer).

### Estilo de cota

En sus propiedades: **separación**, **altura de texto**, **decimales**, **unidades** (m, cm, mm, pulgadas, pies, pies-pulgadas y sus fraccionarias), extremos (**flechas**, como manda la norma; trazos oblicuos o ninguno si lo prefieres), grosor, color, fondo del texto y texto manual si quieres reemplazar la medida. El agarre central de la línea permite reacomodar la separación cuando quieras.

**Dónde va el texto**: siempre **encima** de la línea de cota y **alineado con ella** —una cota vertical se lee de abajo arriba, a la izquierda—, como manda la norma ISO (*Posición del texto* no ofrece otra cosa por ahora; *Orientación* conserva «Horizontal» marcada como fuera de norma, por si una cota la lleva y quieres devolverla). La **separación** es la distancia de la línea a la base de las cifras: 0,5 mm en una cota nueva, un cuarto de la altura del texto, lo que se ve en una lámina a norma. *A lo largo de la línea* lo lleva **sobre el centro**, **fuera del inicio** o **fuera del final** (el texto al lado de la cota, a izquierda o derecha). Y **el texto se arrastra con el ratón** agarrándolo por las letras y se queda donde lo dejes, mientras la línea no se mueve; **Devolver el texto a su sitio** deshace el arrastre. **El estilo de la última cota que editaste es el de las nuevas**, y se recuerda entre sesiones — el aspecto (extremos, altura, color, fondo…), no dónde pusiste el texto: cada cota nueva nace con el número **sobre el centro** de su línea.

### Cotas en cadena

La herramienta **Cotas en cadena** (junto a la cota) acota varios tramos seguidos sobre **una sola línea de cota**:

1. Clic en el primer punto y en el segundo.
2. Tercer clic para fijar la separación de la línea.
3. Cada clic siguiente añade el siguiente tramo sobre la misma línea (con un quiebre, el tramo nuevo se acomoda para pasar por la línea de la cadena).
4. Clic sobre el último punto, `Esc` o cambiar de herramienta termina la cadena y apila la **cota total** una fila más afuera (con dos tramos o más; `Ctrl+Z` la quita si sobra).

`Mayús` **fuerza recta la cadena entera**: todos los tramos miden solo su parte horizontal (o vertical) y comparten una única línea de cota, aunque los puntos estén a alturas distintas. La cota total sale forzada igual.

### Cotas desde línea base

La herramienta **Cotas desde línea base** es la hermana de la cadena: se usa igual —dos puntos, la separación, y luego un clic por punto— pero **todas las cotas miden desde el PRIMER punto**, y cada una se apila **una fila más afuera**. Es la acotación acumulada de toda la vida: distancias desde una esquina o desde un eje.

La diferencia en una frase: la **cadena** pone los tramos uno tras otro sobre una sola línea; la **línea base** pone las distancias acumuladas, escalonadas. Las dos aceptan `Mayús` para salir rectas, y las dos terminan con clic en el último punto o `Esc`. La cadena apila además su **cota total**; la de línea base no la necesita, porque su última cota ya va de la base al punto más lejano.

#### Continuar desde una cota que ya existe

Como en AutoCAD, **no hace falta volver a dar dos puntos y la separación**: **selecciona una cota** y arma Cadena o Línea base, y la serie **continúa desde ésa** — la cadena desde su segundo punto, la línea base desde el primero —, conservando su línea, su separación y si estaba forzada recta. A partir de ahí es **un clic por punto**.

Sin nada seleccionado, la serie empieza de cero como siempre: dos puntos, la separación y a seguir. *(En AutoCAD `DIMCONTINUE` y `DIMBASELINE` **solo** continúan de una cota existente y nunca piden dos puntos; aquí se dejan las dos formas a propósito.)*

El **escalón** entre filas de una serie desde línea base —el `DIMDLI` de AutoCAD— es un valor que fijas tú en **Estilo de cota ▸ Escalón de línea base** (por defecto 8 mm). Vive en el documento, así que un dibujo conserva el escalón con el que se trazó.

### La línea se prolonga bajo el texto

Cuando el texto va **fuera del inicio o del final** (*A lo largo de la línea* en el panel), la línea de cota **se prolonga hasta cubrirlo**, como manda la normativa: si cambias el texto por uno más largo, la línea crece con él. Si arrastras el texto a mano, la línea se queda donde está — ahí mandas tú.

Los puntos enganchados en verde anclan cada tramo al modelo, como una cota normal.

### Cota angular

La herramienta **Cota angular**: clic en el **vértice**, clic en un punto de cada lado y un cuarto clic para el **radio del arco**. Mide el ángulo real, con su arco, sus flechas y el texto alineado o recto. Los tres primeros clics **enganchan a la geometría** del marco (punto verde), y con **`Mayús`** el brazo cae en un múltiplo exacto de 15°: el primero desde la horizontal de la hoja y el segundo **desde el primer brazo**, así que el ángulo medido sale redondo — 90°, 45°, 30°.

### Cota de radio y de diámetro

La herramienta **Cota de radio**: haz clic **sobre el círculo o el arco** del dibujo y la cota toma el **centro y el radio por sí sola** — como en AutoCAD, no hace falta buscar un centro que el plano no marca; el punto donde haces clic decide por qué lado sale la línea, y al pasar el cursor por el arco ya ves en punteado la cota que va a colocar. Reconoce los círculos y arcos que el marco ve **de frente** (en planta, los horizontales; en una elevación, los verticales) — uno visto de canto es una línea y no tiene radio que acotar. Si haces clic donde no hay ningún arco, ese clic es el **centro** y el siguiente un punto del **arco**. Con **`Ctrl`** en el clic sale de **diámetro** en vez de radio; el desplegable *Tipo* del panel también la cambia después.

Sigue la normativa de acotación:

- La línea **siempre llega al centro**: el radio parte de él y el diámetro lo atraviesa. Una guía que se quede a medio camino no cumple.
- El **símbolo acompaña al valor**: `R` o `Ø`.
- El texto va **encima** de la línea y nunca queda cabeza abajo, esté el radio en el cuadrante que esté.
- Si las letras y las flechas **caben**, van dentro y las flechas apuntan hacia fuera, al arco. Si **no caben**, la línea se prolonga fuera, el texto va sobre esa prolongación y las flechas apuntan **hacia el centro**. *Posición del texto* deja forzarlo (Automática / Dentro / Fuera).
- En un diámetro el número no se pone sobre el centro, que es donde van los ejes: se corre a la mitad **derecha** de la línea, se haya trazado hacia donde se haya trazado (en un diámetro vertical, a la mitad de arriba, que es hacia donde se lee).

Un **arco** se acota igual que un círculo. La **marca de centro** (la crucecita) se puede quitar en el panel, y el agarre del extremo del arco gira y redimensiona la cota.

## Cotas de nivel

La herramienta **Nivel** pone la marca de nivel con un clic sobre un punto de una vista: lee la **altura del punto** y escribe «N.P.T. +0.15» junto al símbolo — triángulo sobre su vértice en secciones y elevaciones, círculo en cuadrantes en plantas (el marco de planta lo elige solo). Anclada al modelo, sigue al punto si la geometría cambia y actualiza la altura; se puede deslizar por la lámina y queda una guía fina hasta el punto.

En una **elevación o una sección** no hace falta ni enganchar: las filas de la hoja SON las alturas del modelo, así que un clic en cualquier sitio del marco ya sabe a qué altura está y escribe esa. Una **planta** mira hacia abajo y no puede decirlo: ahí el nivel sale del punto enganchado, o lo escribes tú.

En sus propiedades: **texto** con `{z}` (o sin él: el nivel se añade al final), **nivel de referencia** (la altura del modelo que se lee como ±0.00), decimales, símbolo, tamaño, largo de la línea de nivel, lado, grosor y color.

## Etiquetas con guía

La herramienta **Etiqueta**: clic en el punto que señalas (engancha en verde sobre el dibujo) y clic donde va el texto. La guía sigue al punto si mueves el texto; anclada a un marco, se mueve con él. Fuente, tamaño, **negrita, cursiva, subrayado**, color, fondo, punta de flecha y línea a la izquierda o a la derecha en el panel.

## Llamadas de detalle

La herramienta **Llamada** encuadra (rectángulo o círculo a trazos) la parte de una vista que otro dibujo amplía y pone la burbuja **«3 / L-05»** con una guía. La burbuja se arrastra aparte; el encuadre se mueve y redimensiona como cualquier ítem. Dibujada sobre un marco queda ligada a él y se mueve con él. Número, lámina (admite `{lamina}`), forma, tamaño, grosor y color en el panel.

## Formas

Línea, **flecha**, **línea de terreno**, rectángulo (con **radio de esquinas**), elipse y **polígono regular** (3–24 lados). Cada forma con su **color de línea**, grosor, y — para las cerradas — **relleno con color propio**. En línea, flecha y línea de terreno, `Mayús` las fija en horizontal o vertical.

La **línea de terreno** es el suelo de una elevación: la línea y, por debajo, lo que manda la convención de dibujo — **pelos de tierra** a 45°, **banda rayada** o **banda rellena** translúcida (el color de relleno), con largo, separación y alto ajustables en el panel. Admite pendiente y el terreno queda siempre del lado de abajo; para desniveles, un tramo por nivel. Combinada con una cota de **Nivel** («N.T.N. ±0.00») queda dicho todo.

## Texto e imágenes

- **Texto**: bloques con fuente, tamaño en puntos, **negrita, cursiva y subrayado**, color, fondo y alineación. **Doble clic** lo edita **en su sitio**, con la misma letra al mismo tamaño; clic fuera o `Ctrl+Enter` confirma, `Esc` cancela. Un texto puede quedar **ligado a un marco** («se mueve con su marco») y usar campos: `{escala}` lee la escala de ese marco, `{lamina}` y `{proyecto}` el cajetín, `{fecha}` la fecha. **Añadir etiqueta de escala** en el panel del marco pone un texto así, ya escrito.
- **Imagen**: logos, fotos de obra, vistas auxiliares (PNG/JPG). Con **opacidad**, **forma del recorte** (rectángulo, esquinas redondeadas, elipse o círculo), **borde desvanecido** en milímetros, **ajuste** (estirar, cubrir recortando o contener entera) y contorno opcional — una foto en círculo fundida al papel, como en las láminas de presentación.
- **Perfil de terreno**: la herramienta **Perfil** dibuja el perfil longitudinal de un [trazado](../terreno/rutas-perfil.md) sobre la lámina, con escala horizontal y vertical, exageración vertical, progresivas y cotas; muestreado del levantamiento de dron o del DEM, y se actualiza si el trazado cambia.

## Cajetín

El membrete del plano — **el** ítem de una lámina:

- **Campos editables**: la tabla de propiedades permite renombrar, **agregar y quitar filas** (PROYECTO, AUTOR, FECHA, ESCALA, LÁMINA, y los que tu expediente pida: DISTRITO, REGIÓN…). Los valores admiten campos: `{fecha}`, `{lamina}`, `{total}`…
- **1 a 4 columnas** de campos, lado a lado, como los cajetines anchos reales.
- **Diseño**: siete presets de aspecto —esquinas cuadradas, redondeadas o achaflanadas; cuadrícula, banda de cabecera o minimalista; doble borde, relleno de rótulos, colores— que cambian **cómo se ve**, nunca las filas ni el tamaño. Cada detalle es editable aparte: grosores del borde exterior y de las líneas interiores, ancho de la columna de rótulos, colores de rótulo, texto y línea.
- **Plantillas de cajetín** (botón **Plantillas…**): guarda el tuyo —filas, tamaño y aspecto— con nombre, aplícalo a otra lámina y márcalo como **predeterminado**: cada cajetín nuevo nace de él. **Copiar estilo / Pegar estilo** también funciona entre cajetines, y `Ctrl+C` / `Ctrl+V` lleva el cajetín entero a otra lámina (ocupa el sitio del que hubiera).
- **Las filas se reparten el alto según lo que llevan**: un nombre de proyecto largo baja a dos o tres líneas y su fila crece —hasta tres veces su parte— a costa de las filas que no usaban la suya, así todos los valores salen del mismo tamaño; solo si aun así no cabe, la letra se condensa.

## Escala gráfica, norte y leyenda

- **Escala gráfica**: la barra de segmentos blanco/negro con metros — el lector mide incluso sobre una fotocopia. Sigue la escala que le indiques.
- **Flecha de norte**: rotable al norte de tu proyecto.
- **Leyenda de capas**: lista las capas visibles del modelo, con refresco manual.
