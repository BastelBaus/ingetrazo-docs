# Materiales, texturas y componentes

## Pintar

**`B`** abre la herramienta Pintar y el panel de **Materiales** de la bandeja:

- Elige un **color** o una **textura** y haz clic sobre caras (o sobre grupos enteros).
- **Pintar un grupo o componente desde fuera** pinta el objeto entero con la regla habitual: el material propio de una cara va por delante del del contenedor, así que **solo las caras con el material por defecto** visten el del grupo (por las dos caras); al explotar, se lo quedan. Dos copias del mismo componente pueden ir de colores distintos, y el material del contenedor viaja en el `.igz`, y se respeta al importar un `.skp`.
- **Gotero**: manteniendo `Alt`, el clic *toma* el material de lo que hay bajo el cursor en lugar de pintarlo (sobre una cara por defecto de un grupo pintado, toma el del grupo) y lo deja como **material activo** en el panel.
- **+ Color…** y **+ Textura…** crean materiales propios (con nombre opcional); puedes traer cualquier imagen PNG/JPG como textura.

### Lo que viene en el programa

- **427 texturas** listas (madera, piedra, ladrillo, pisos, metales, vegetación…), cada una con su **tamaño real** en metros: una baldosa de 30 cm mide 30 cm en tu modelo.
- **213 colores RAL Classic**, con su nombre y su código.
- **Materiales con nombre**: un material tiene identidad, no solo un color. **En el modelo** lista los que ya usas; con clic derecho sobre uno **editas y re-estampas** todas las caras que lo llevan de una vez. El nombre viaja al OBJ, y el [Info del modelo](../extensiones.md) metra los m² por material.

## Texturas

- La proyección es **compatible con el formato `.skp`**: planar por cara, y las texturas de un `.skp` importado llegan con sus pines exactos.
- **El mapa de textura viaja con la geometría**: mover, girar, escalar o pegar una cara texturizada no descoloca su textura.
- Las texturas **viajan dentro del documento** `.igz`: el archivo es autocontenido, lo llevas a otra PC y abre completo.
- Los materiales **translúcidos** (vidrio) y las texturas **caladas** (mallas, celosías, hojas) se ven correctamente en el viewport y proyectan sombra según su trama.

## Caras

- Cada cara tiene **frente y dorso** (el dorso se dibuja azul grisáceo). **Invertir caras** (clic derecho) las voltea — importa para texturizar y para exportar.
- **Aristas suaves**: las superficies curvas (cilindros, arcos extruidos) se muestran continuas; sus aristas de control son «soft» y no ensucian el dibujo. Las que quieras esconder sin borrar: [ocultar aristas](edicion.md#ocultar-aristas).

## Componentes y figuras de escala

El panel **Componentes** de la bandeja coloca modelos listos:

- **Con el programa** vienen 8 modelos (puertas, ventanas, mobiliario) y **6 figuras de escala** — personas de 1,75 m que miran siempre a la cámara, para dar escala a cualquier vista. Se llaman por su nombre de pila; **Sumari** es el de la casa.
- **Más componentes…** (también en **Ayuda ▸ Obtener más modelos y texturas…**) abre la **biblioteca en línea de 1 510 modelos** —muebles, puertas, ventanas, árboles, vehículos, personas— con miniatura, categoría y **tamaño real en cm**. Navegar cuesta kilobytes: solo se descarga el modelo que pulsas, y queda guardado para la próxima vez. Cada uno lleva su licencia y su autor (CC0, CC-BY o Arte Libre).
- Un modelo colocado es un **componente**: se coloca con un clic, Mover (`M`) lo ajusta, y sus copias comparten definición.
- Cada modelo llega **como su archivo lo describe**: eje vertical, tamaño declarado, texturas y grupos de suavizado en su sitio.

!!! tip "Limpieza de la caché de texturas"
    Las imágenes que llegan de archivos `.skp` importados se guardan en una caché del programa (nunca junto a tus archivos). Archivo ▸ Importar ▸ Limpiar caché de texturas importadas… la vacía si necesitas espacio.
