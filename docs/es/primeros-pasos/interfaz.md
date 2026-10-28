# La interfaz

La ventana de IngeTrazo tiene cuatro zonas:

- **Viewport 3D** (el centro): aquí vives. Todo se dibuja y se edita directamente sobre el modelo.
- **Barras de herramientas**: dibujo, edición, cámara y anotación, más los desplegables **Estilos**, **Sombras** y **Estilo de cota**. Cada botón muestra su atajo de teclado al pasar el mouse. Se arrastran a donde prefieras y el programa recuerda la disposición.
- **Bandeja lateral** (derecha): Info de entidad, Capas, Escenas, Materiales, Componentes, BIM, Terreno y Puntos topográficos. Se pliega por paneles y se redimensiona.
- **Barra de estado** (abajo): a la izquierda las **pestañas Modelo | Lámina 1 | Lámina 2… | +** —como las pestañas Model/Layout de AutoCAD— para ir del modelo a cada lámina y volver con un clic (`+` crea una lámina nueva); al centro los mensajes de la herramienta activa; a la derecha la herramienta, las coordenadas, el **VCB** (campo de medidas) y — si el proyecto está georreferenciado — la lectura continua de coordenadas UTM.

![La ventana completa: viewport con un modelo en curso y la bandeja lateral con Capas, Escenas y Materiales.](../images/principal.jpeg)


## Navegar el modelo

| Acción | Cómo |
|---|---|
| **Orbitar** | Botón central del mouse (arrastrar), o la herramienta Orbitar (`O`) con el botón izquierdo |
| **Desplazar** | `Shift` + botón central, o la herramienta Desplazar (`H`) |
| **Zoom** | Rueda del mouse (dos dedos en el touchpad); `Z` para zoom por arrastre; Zoom Ventana para encuadrar una región |
| **Encuadrar todo** | Zoom a extensión (`F2`, o en la barra de cámara) |
| **Vistas estándar** | Menú Cámara ▸ Vistas estándar: superior, frontal, lateral, isométrica… |
| **Perspectiva / paralela** | `Mayús+P` alterna la proyección |
| **Pantalla limpia** | `Ctrl+0` esconde barras y paneles; otra vez los devuelve |

!!! tip "El VCB: medidas exactas por teclado"
    Mientras dibujas, **escribe el número y Enter** — no hace falta hacer clic en ningún campo. Una línea de 3.50 m: activa Línea, clic en el origen, orienta, teclea `3.50` y Enter. Funciona en casi todas las herramientas: distancias, radios, ángulos, cantidades de lados, factores de escala. Acepta metros, centímetros, pulgadas y pies ([detalle](../modelado/dibujo.md#medidas-por-teclado-metros-centimetros-pulgadas-pies)).

## El modo oscuro

La interfaz usa tema oscuro siempre, pensado para que el viewport y los paneles no choquen. Cómo se ve el **modelo** (fondo, cielo, aristas, sombras) lo decides tú con los [estilos](../modelado/estilos-sombras.md).

## Idioma y preferencias

Ventana ▸ Idioma cambia entre español, inglés y portugués de Brasil (aplica al reiniciar). **Ventana ▸ Preferencias…** reúne el resto: auto-guardado, copia de seguridad, rueda del ratón, anti-aliasing, pasos de deshacer, las **unidades del documento**, unidades sugeridas al importar y el Asistente IA — ver [Preferencias](../preferencias.md). El manual usa los nombres en español.
