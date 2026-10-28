# Tu primer modelo

Vamos a levantar una casita de 6 × 4 m con medidas exactas. Es el recorrido esencial: dibujar, extruir, abrir vanos y guardar.

## 1. La planta

1. Activa **Rectángulo** (`R`).
2. Clic en el origen, mueve el mouse y **teclea** `6,4` y Enter. Tienes la planta exacta de 6 × 4 m.

!!! tip "Las inferencias te guían"
    Mientras dibujas verás puntos y líneas de colores: extremos, puntos medios, ejes, paralelas y perpendiculares. Son las **inferencias** — deja que te enganchen y tus líneas caerán exactas sin esfuerzo.

## 2. Levantar los muros

1. Activa **Empujar/Tirar** (`P`).
2. Clic sobre la cara del rectángulo, sube, teclea `2.7` y Enter. La caja mide 2.70 m de alto.

## 3. Abrir la puerta y la ventana

1. Con **Rectángulo** dibuja sobre la fachada el vano de la puerta (por ejemplo `0.9,2.1`).
2. **Empujar/Tirar** sobre ese rectángulo hacia adentro, hasta que la inferencia marque la cara opuesta del muro: el vano queda perforado.
3. Repite con la ventana.

## 4. El techo

1. Dibuja una **Línea** (`L`) por el punto medio de la cara superior, de lado a lado.
2. Con **Mover** (`M`) selecciona esa línea, muévela hacia arriba, teclea la altura de la cumbrera (por ejemplo `1.2`) y Enter. Tienes el techo a dos aguas.

## 5. Pinta y mide

- **Pintar** (`B`) abre los materiales: elige un color o textura y clic sobre cada cara. Con `Alt` tomas el material de una cara existente (gotero).
- **Cota** (`D`): clic en dos puntos y jala la cota — queda anclada al modelo.

## 6. Guarda

`Ctrl+S` guarda el documento como **`.igz`**, el formato nativo y abierto de IngeTrazo. Si el modelo lleva texturas, viajan **dentro** del archivo: puedes llevarlo a otra PC y abre completo. El documento guarda también **la cámara** con la que lo dejaste: al abrirlo ves lo que veías (y **Archivo ▸ Nuevo** vuelve a la vista por defecto). Un `.igz` grande enseña una **barra de progreso** mientras carga; los últimos diez están en **Archivo ▸ Abrir recientes**.

!!! note "Sólidos de verdad"
    IngeTrazo garantiza que las operaciones dejan sólidos **herméticos** (cerrados). Si una operación fuera a romper el volumen, el motor la rechaza en lugar de corromper el modelo — eso es lo que hace confiables el metrado BIM y la impresión 3D.

## ¿Y ahora?

- Todas las herramientas de dibujo, en detalle: **[Herramientas de dibujo](../modelado/dibujo.md)**.
- Etiquetar la casita y sacar sus metrados: **[BIM y metrados](../bim.md)**.
- Ponerle terreno real debajo: **[Ubicación del proyecto](../terreno/ubicacion.md)**.
