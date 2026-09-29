# Composición de láminas

El **compositor de láminas** convierte tu modelo en planos impresos sin salir de IngeTrazo — al estilo del compositor de QGIS: colocas **vistas del modelo a escala exacta** sobre una hoja, las acotas, les pones cajetín, y exportas PDF vectorial.

Se abre desde las **pestañas de la barra de estado** (Modelo | Lámina 1 | … | `+`) — un clic en una lámina la abre; `+` crea una nueva; **Modelo** vuelve al modelador — o desde **Archivo ▸ Compositor de láminas…**.

![El compositor de láminas con la lámina D04 del arco de Yanque: reglas, barra de lámina, lienzo y panel de diseño.](../images/laminas.jpeg)


## La ventana

- **Barra de lámina** (bajo el título, con iconos): **Guardar** el documento (`Ctrl+S`, también desde aquí), **Actualizar vistas**, **Exportar PDF…**, **Exportar imagen…** (PNG o JPG) y **Vista previa de impresión…**.
- **Lienzo central**: la hoja, con sombra y márgenes, entre una **regla** en milímetros arriba y otra a la izquierda (siguen el zoom y marcan la posición del cursor; de ellas se sacan las [guías](#reglas-y-guias)). Zoom con `Ctrl+rueda`, con el combo de la barra de estado (*Ajustar a hoja*, *Ajustar a anchura*, porcentajes — 100 % es el **tamaño real del papel** en tu pantalla) o con las dos herramientas del modelo en la barra izquierda: **Zoom** (arrastra hacia arriba para acercar y hacia abajo para alejar, alrededor del punto donde pulsaste; un clic acerca un paso) y **Zoom ventana** (arrastra un recuadro y la vista se llena con él). **Desplazar** con la rueda, con el botón central o con la herramienta Mano, a cualquier zoom: la hoja nunca se te pierde (una franja queda siempre a la vista).
- **Barra de herramientas izquierda**: seleccionar, mano, pincel de formato, marco de vista, texto, etiqueta con guía, nivel, llamada de detalle, imagen, cajetín, escala gráfica, norte, leyenda, perfil de terreno, línea, flecha, **línea de terreno**, rectángulo, elipse, polígono, cota, cotas en cadena y cota angular. Cada herramienta coloca un ítem y vuelve a Seleccionar; **las cotas se quedan activas** para encadenar una tras otra (`Esc` o el cursor las deja).
- **Panel derecho** (redimensionable, cabe en ~480 px): gestor de láminas, lista de **Elementos** y propiedades del ítem seleccionado. Las secciones que no usas se pliegan.
- **Barra de estado**: las mismas pestañas Modelo | Láminas, la casilla **Renderizado automático**, las coordenadas en mm y el zoom.

## Hojas

- Tamaños **A4 a A0**, horizontal o vertical, con margen configurable y **borde de la lámina** opcional (simple o doble, grosor y color; sale impreso).
- **Varias láminas por documento**: `+` crea, `⧉` duplica (hereda cajetín y márgenes — ideal para mantener el estilo del expediente), `−` elimina, y *Renumerar láminas* actualiza los L-01, L-02… de los cajetines. Lo mismo con **clic derecho sobre una pestaña de lámina** de la barra de estado, en cualquiera de las dos ventanas: *Cambiar nombre*, *Duplicar* (la copia queda justo después), *Eliminar* y *Nueva lámina*.
- **Plantillas de lámina** (botón **Plantillas…**): guarda una lámina —hoja, márgenes, borde, cajetín, marcos vacíos— como plantilla con nombre; crea láminas nuevas desde ella y fija una **por defecto** para todo documento nuevo. Las plantillas son archivos en tu carpeta de usuario (*Abrir la carpeta de plantillas*): se comparten copiándolas.
- Todo se guarda **dentro del `.igz`**, con su propio deshacer: `Ctrl+S` o el botón Guardar de la barra de lámina graban el documento entero, modelo y láminas, y el **autoguardado** de Preferencias también cubre las láminas. Compones una vez; cada revisión del modelo es reabrir y re-exportar — o dejar el **renderizado automático** encendido y verla actualizarse.

## Los ítems

Cada cosa sobre la hoja es un ítem: se mueve arrastrando (con imanes a márgenes, centro, guías y otros ítems) o **con las flechas del teclado** (1 mm; `Mayús` 10 mm; `Alt` 0,1 mm — un paso de deshacer por pulsación), se redimensiona por la esquina (el cursor lo indica), y tiene sus propiedades en el panel. **Doble clic** sobre un texto lo edita en su sitio; sobre un marco entra a editar la vista.

**Seleccionar varios**: arrastra un cuadro desde la hoja vacía — de izquierda a derecha selecciona lo que queda **encerrado** (azul), de derecha a izquierda lo que **toca** (verde a trazos); `Mayús` alterna, `Ctrl` añade, `Mayús+Ctrl` quita. Un clic en la hoja vacía deselecciona.

**Lo que está debajo**: cuando un ítem tapa a otro (un título sobre la etiqueta de escala del marco), `Ctrl+Alt+clic` selecciona el de debajo y, repitiendo, sigue bajando por la pila; o clic derecho ▸ **Seleccionar el ítem de debajo**. La lista **Elementos** del panel siempre llega a todo.

Con **clic derecho** sobre cualquier ítem:

- **Traer al frente / Subir / Bajar / Enviar al fondo** — el orden de apilado (dibuja un rectángulo de fondo, mándalo atrás, y pon todo encima).
- **Bloquear** (`Ctrl+L`) — el ítem queda visible pero **fuera del alcance del mouse**: ni clic ni cuadro lo toman, así las cotas y textos sobre un marco bloqueado se editan sin pescar el marco. La única puerta es la lista **Elementos** del panel: desde ahí se selecciona, se edita y se desbloquea. El candado lo marca.
- **Organizar** — alinear y distribuir la selección (dos o más ítems), **agrupar y desagrupar** (`Ctrl+G`, `Ctrl+Mayús+G`; un grupo se arrastra junto), **duplicar** (`Ctrl+D`). La barra «Organizar» con estos botones está oculta por defecto; clic derecho sobre la barra de herramientas para mostrarla.
- **Copiar estilo / Pegar estilo** (`Ctrl+Mayús+C` / `Ctrl+Mayús+V`) entre ítems del mismo tipo — y el **Pincel de formato** de la barra: clic en el ítem modelo, clic en los destinos, `Esc`.

**Portapapeles**: `Ctrl+C`, `Ctrl+X`, `Ctrl+V` copian ítems dentro de una lámina (el pegado cae 5 mm más abajo y a la derecha) o **entre láminas** (cae en el mismo sitio). Los textos ligados y las cotas ancladas a un marco copiado siguen al marco pegado. **El cajetín también se copia**: pegado en otra lámina ocupa el sitio del suyo.

## Reglas y guías

Como en QGIS: **arrastra desde la regla de arriba** hacia la página y sale una **guía vertical** (línea azul discontinua); desde la de la izquierda, una horizontal. Los ítems se **imantan a las guías** al moverlos o redimensionarlos. Una guía se desliza por su eje; para quitarla, arrástrala de vuelta a la regla o selecciónala y pulsa `Supr`; clic derecho sobre una regla ▸ **Quitar todas las guías**. Se guardan con la lámina y no se imprimen.

Sigue con **[Marcos de vista y escala](marcos.md)** — el corazón del compositor.
