# Capas, escenas y organización

## Capas

El panel **Capas** de la bandeja organiza la visibilidad del modelo (la lista crece hasta 12 filas y de ahí en adelante se desplaza ella sola, igual que la de Componentes):

- **+ Capa** crea una; el selector de cada entidad (o el panel Info de entidad) la asigna.
- El **ojo** muestra/oculta todo lo que vive en la capa — muebles, referencias, instalaciones.
- Al importar un `.skp`, sus capas/etiquetas llegan con su visibilidad original.
- Eliminar una capa no borra su geometría: pasa a la capa por defecto.

!!! note "Capas = visibilidad, no aislamiento"
    Las capas controlan qué se ve; la geometría en capas distintas **sí se toca** si comparte espacio. Para aislar geometría usa **grupos**.

## Escenas

El panel **Escenas** guarda vistas con nombre:

- **+ Escena** captura la cámara actual **y** qué capas están ocultas.
- **Doble clic** en una escena la restaura.
- Las escenas se guardan en el `.igz`, llegan desde los `.skp` importados, y son las **fuentes de vista** del [compositor de láminas](../laminas/marcos.md): una escena "Planta" bien preparada es tu plano de planta.

## Info de entidad

El panel **Info** muestra y edita lo esencial de la selección: longitud de una arista, área de una cara, capa, material, y los metadatos BIM si los tiene.

## Escenas: qué recuerdan

Además de la cámara y las capas, cada escena guarda el **estilo** activo, el **plano de sección** activo y si los cortes se ven, y la **hora del sol** de las sombras. `F2` renombra la escena (o la capa) seleccionada en su lista; **Actualizar** la re-captura desde la vista actual.

## Estilo visual, secciones y sombras

- Los **estilos** (Predeterminado, Arquitectónico, Línea oculta, Rayos X… y los tuyos), las **sombras con el sol real** y la pantalla limpia tienen su página: [Estilos, sombras y pantalla](estilos-sombras.md).
- Los **planos de sección** cortan el modelo para mirar adentro: [Planos de sección](secciones.md).
- Un plano escaneado o una foto para calcar: [Imágenes de referencia](imagenes-referencia.md).
- **Culling de caras**: los dorsos se pintan azul grisáceo para detectar caras volteadas de un vistazo.
- Archivo ▸ Exportar ▸ **Imagen** guarda una captura de alta resolución del viewport.

## Componentes: editas uno, cambian todos

Las copias de un componente (Ctrl+C / Ctrl+V, o Mover con Ctrl) comparten una misma definición:

- **Doble clic en cualquier copia** la abre para editar. Dibuja, empuja, borra dentro; al salir (Esc o clic afuera), el cambio pasa a **todas** las copias. Toda la edición se deshace en un solo paso de Ctrl+Z.
- **Empujar/Tirar sobre una copia desde fuera** también edita la definición: las demás copias reciben el mismo empuje.
- **Para cambiar una sola copia**, antes de editarla usa clic derecho ▸ **Hacer único**: esa copia se desliga y las demás siguen compartiendo la definición.
- Mirar dentro de un componente y salir sin tocar nada no cambia nada.
- **Crear componente…** (`G`) convierte la selección en una definición con nombre; **Unir grupos** funde varios grupos en uno; **Explotar** (`Ctrl+Mayús+G`) disuelve un nivel.
- Los componentes importados de `.skp` con **subgrupos** conservan su jerarquía: se mueven y copian como un solo objeto y su archivo no engorda. Editar dentro de uno de esos lo desarma en ese documento (lo habitual al editar un componente anidado).
