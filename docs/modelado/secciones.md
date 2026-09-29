# Planos de sección

Un **plano de sección** corta el modelo para mirar adentro — la planta de una casa a la altura de las ventanas, el corte por el eje de una pileta, el acero dentro de una columna. Funciona así: colocas el plano, el modelo se recorta en vivo, y las láminas dibujan el corte con su relleno.

## Colocar un plano

1. **Herramientas ▸ Plano de sección** (también en la barra de herramientas).
2. Mueve el cursor sobre el modelo: el plano se **alinea solo** con la cara que tienes debajo (o con el suelo).
3. Para fijar la orientación sin depender de la cara: las **flechas del teclado** bloquean el eje — `↑` corta horizontal (plano Z), `→` vertical según X, `←` vertical según Y, `↓` vuelve a la cara — y `Mayús` congela la inferencia actual. El plano mira siempre hacia la cámara: colocado delante del modelo, lo que se oculta es lo que está de tu lado.
4. **Clic** para colocarlo. Se te pide un **nombre** y un **símbolo** (la letra que saldrá en las láminas: A, B…). Puedes dejar los que propone: el símbolo es la **siguiente letra libre**, así que los cortes salen A, B, C… y la marca de la lámina se lee «A … A», como manda el dibujo técnico. Si nunca los cambias, marca **«No volver a preguntar»**: los planos nacerán con nombre y símbolo por defecto ([Preferencias ▸ General](../preferencias.md#general) vuelve a encender el cuadro). Colocado el plano, la herramienta **termina** y vuelve a Seleccionar.

Para cambiarlos después, clic derecho sobre el plano de sección ▸ **Nombre y símbolo…**.

El plano recién colocado queda **activo** y corta de inmediato.

## Trabajar con secciones

- **Solo un plano activo por contexto.** Colocar otro lo activa y desactiva el anterior. **Doble clic** sobre un plano alterna si está activo.
- **Mover y girar** el plano con las herramientas Mover (`M`) y Rotar (`Q`): agárralo por su marco. Es la forma de «pasear» un corte por el modelo.
- **Clic derecho** sobre el plano: **Invertir** (corta hacia el otro lado), **Corte activo**, **Alinear vista** (la cámara se pone perpendicular al plano — el encuadre de un corte de plano).
- **`Supr`** lo borra; `Ctrl+Z` lo devuelve.
- El marco de un plano perpendicular a un eje se dibuja **del color de ese eje** (rojo, verde o azul; los oblicuos, gris), así se ve de un vistazo por dónde corta cada uno.
- **Cámara ▸ Planos de sección** muestra u oculta los marcos de los planos; **Cámara ▸ Cortes de sección** enciende o apaga el recorte sin borrar nada.
- Las aristas donde el plano atraviesa un sólido se dibujan **gruesas**, y el estilo puede rellenar el corte (**Relleno de sección**, con su color, en el [editor de estilos](estilos-sombras.md)).
- Las herramientas de dibujo y selección **no alcanzan lo que el corte oculta**: imantas y seleccionas solo lo visible.

## Secciones, escenas y láminas

- Cada **escena** recuerda qué plano estaba activo y si los cortes se veían: una escena «Planta» con el corte horizontal a 1,20 m es tu planta de arquitectura, y otra «Corte A-A» tu sección.
- En el **compositor de láminas**, un marco que muestra esa escena dibuja el corte: en el estilo **Vectorial**, las aristas de corte llevan su pluma gruesa y el sólido cortado se rellena con **poché** (sólido o achurado) — ver [Marcos de vista](../laminas/marcos.md#plumas-y-poche-del-estilo-vector).
- **Marcas de sección**: un marco de planta puede dibujar la traza de cada plano de sección que lo atraviesa, con sus flechas y la letra del plano en burbujas — así la planta dice por dónde va el «Corte A-A» ([anotación en láminas](../laminas/marcos.md#marcas-de-seccion)).
- Los planos se guardan en el `.igz` y se restauran con el documento.

!!! tip "Ver el acero"
    Para revisar armaduras o instalaciones dentro del concreto, combina un plano de sección con **Cámara ▸ Estilo ▸ Rayos X**: el corte muestra la posición exacta y los Rayos X el resto de la armadura a través de las caras. Los [ejemplos](../primeros-pasos/ejemplos.md) del arco y de la luminaria están pensados para eso.
