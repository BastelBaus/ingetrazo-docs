# Marcos de vista y escala

Un **marco de vista** es una ventana al modelo colocada sobre la hoja. Es el ítem central del compositor.

## Crear un marco

Con la herramienta **Marco** dibuja el rectángulo sobre la hoja (dos clics o arrastre), o **Agregar marco** en el panel. En sus propiedades eliges:

- **Vista**: la cámara actual, una **vista estándar** (planta, frontal, laterales, isométrica…) o cualquiera de tus **escenas guardadas** — una escena «Planta primer piso» con sus capas, su sección y su estilo configurados es tu plano listo.
- **Escala 1:N**: la ecuación sagrada del compositor — *1:100 en un marco de 200 mm de alto muestra exactamente 20 m de modelo*. Siempre, sin aproximaciones. Cambias la escala y el contenido se reencuadra exacto. El combo trae las escalas usuales y acepta cualquier otra.
- **Escalas de ampliación**: para piezas pequeñas el combo trae también **2:1, 5:1 y 10:1**, y acepta que las escribas así. La lámina las rotula como corresponde («ESC. 10:1»), igual que el campo `{escala}` del cajetín.
- **Tamaño del marco** en mm, por arrastre o numérico; **Encuadrar modelo** centra la vista en todo el modelo.
- **Borde impreso** del marco: grosor y color, o ninguno.

## Editar la vista dentro del marco

**Doble clic** sobre un marco entra en edición de vista: el marco se resalta y el mouse trabaja **dentro** de él como en el modelador —arrastre para encuadrar, botón central o `Ctrl`+arrastre para orbitar, rueda para zoom— hasta `Enter`, `Esc` o un clic fuera. Cada gesto es un paso de deshacer y el marco sigue en edición aunque desplaces la lámina. Ese encuadre manual pertenece al origen de vista elegido: si cambias el marco a otra escena o vista estándar, se descarta y el marco parte de la cámara de la escena.

**Girar la vista**: `Mayús`+arrastre gira el dibujo dentro del marco alrededor de su centro, con imantación cada 15°; o escribe el ángulo en **Giro de la vista** del panel (positivo = horario, el mismo ángulo que le pones a la flecha de norte). El marco y todo lo demás se quedan quietos; gira lo que sale de la cámara: el render, las líneas ocultas, la imantación, las cotas ancladas, las marcas de sección y el DXF.

## Estilos de render

| Estilo | Qué muestra |
|---|---|
| **Estilo del modelo** | El modelo tal como se ve en el visor: materiales, texturas, sombreado, sombras. |
| **Estilos guardados** | Cualquier estilo de la biblioteca (Línea oculta, Arquitectónico, Rayos X, los tuyos…), por marco. **Un marco nuevo nace en Arquitectónico**: fondo blanco, aristas y perfiles. |
| **Vectorial (líneas ocultas eliminadas)** | El dibujo que entintaría un dibujante: las **líneas ocultas se eliminan con cálculo exacto**, en vectores reales para el PDF y el DXF. |

Bajo el estilo, la casilla **Fondo del papel** renderiza sobre blanco y sin cielo ni suelo sea cual sea el fondo del estilo: un marco en **Rayos X** (para enseñar el acero) o en Predeterminado ya no trae el gris del modelo a la lámina.

### Plumas y poché del estilo Vector

El estilo Vectorial clasifica cada trazo y lo dibuja con su pluma, como un plano de oficina:

| Clase | Pluma por defecto | Qué es |
|---|---|---|
| **Corte de sección** | 0,50 mm | Donde el plano de sección atraviesa un sólido. |
| **Perfiles** | 0,35 mm | Siluetas y contornos contra el fondo (el grosor de perfil habitual). |
| **Aristas** | 0,18 mm | Las demás aristas, entre dos caras visibles. |

Donde la sección corta un **sólido cerrado**, el marco rellena el corte (el *poché*): **sólido** o **achurado a 45°**, con color y paso de achurado a tu gusto; una superficie abierta queda en blanco. Las plumas y el relleno se ajustan en la sección **Plumas del vectorial** del panel, que solo aparece con este estilo. La exportación DXF reparte las clases en capas `VISTA`, `VISTA-PERFIL` y `VISTA-CORTE` para la tabla de plumas de tu CAD.

## Rótulo de vista

Marca **Rótulo de vista** en el panel del marco y elige el estilo:

- **Numerado, con línea debajo**: burbuja con el **número** de la vista arriba y la **lámina** abajo, título en negrita, «ESC. 1:N» y una línea de base hasta el borde del marco. Con subtítulo opcional («N.P.T. +0.15»).
- **Barra vertical**: una franja a la izquierda del marco con título, subtítulo y escala girados 90°, y la burbuja al pie — el hábito de los planos brasileños.
- **Línea simple**: la línea centrada de siempre.

Título, subtítulo, número y lámina admiten campos dinámicos: `{lamina}` lee el cajetín, `{escala}` la escala de ese marco, `{escena}` el nombre de la escena. Alineación, posición (debajo o encima) y tamaño del texto en el mismo panel. Todo se edita en vivo, sin recalcular la vista.

## Marcas de sección

Marca **Marcas de sección (A–A)** y el marco dibuja la traza de cada plano de sección del modelo que atraviesa su vista: la línea de corte a raya y punto, las flechas hacia el lado que mira la sección y la **letra del plano** en burbujas a ambos extremos. Así la planta dice por dónde va el «Corte A-A». La letra es el símbolo del plano ([Planos de sección](../modelado/secciones.md)); sin símbolo, A, B, C… por orden. Un plano paralelo a la vista no deja marca.

## Extras del marco

- **Anotaciones del modelo**: las cotas y textos con guía dibujados en el modelador salen en el marco, con la altura de texto que elijas.
- **Trazados y progresivas**: las [rutas](../terreno/rutas-perfil.md) trazadas sobre el terreno se dibujan siempre en las vistas (en cian, con sus nodos); con **Progresivas** el marco de planta les pone las marcas de kilometraje (0+000, 0+020…) con el paso que fijes o uno automático — el mismo que usa el perfil de terreno de la lámina, para que coincidan.
- **Cuadrícula de coordenadas**: el grid en metros de modelo sobre la vista (el hábito de los planos con malla), con el paso que elijas.
- **Actualizar vista** re-renderiza el marco desde el modelo actual; **Actualizar vistas** (barra de lámina), todos. Con **Renderizado automático** encendido (barra de estado), los marcos se actualizan solos cuando el modelo cambia — los marcos no son capturas, son ventanas vivas.

!!! tip "El flujo recomendado"
    Prepara **escenas** en el modelador (planta con las capas y la sección correctas, elevaciones frontales) y en el compositor solo colócalas a escala. Cuando el proyecto cambie, las láminas se actualizan solas.
