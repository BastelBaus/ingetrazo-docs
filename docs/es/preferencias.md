# Preferencias

**Ventana ▸ Preferencias…** reúne los ajustes del programa. **Aceptar** guarda; **Cancelar** no toca nada. Casi todo aplica en vivo; el idioma pide reiniciar.

## General

- **Idioma**: español, inglés o portugués de Brasil (también en Ventana ▸ Idioma). Aplica al reiniciar. Un sistema en portugués arranca en portugués la primera vez; lo que aún no está traducido sale en inglés.
- **Resto del modelo al editar**: al entrar a un grupo, lo demás normal, **atenuado** u **oculto**. Lo mismo que Cámara ▸ Resto del modelo al editar.
- **Auto-guardar cada N minutos.** IngeTrazo guarda una copia de seguridad del documento en tu carpeta de datos (nunca junto al archivo: los discos sincronizados en la nube han truncado escrituras ahí). La copia existe solo entre un cambio y el siguiente guardado limpio: si la próxima vez que abras ese documento hay una copia, es que la sesión se interrumpió, y el programa **ofrece recuperarla**. El temporizador no dispara con un botón del ratón apretado.
- **Recuperar una copia auto-guardada descartada…** (en el menú Archivo): si dijiste que no a la recuperación y te arrepientes, las copias descartadas se guardan aparte y desde ahí se abren.
- **Conservar copia de seguridad del guardado anterior (`.igz.bak`)**: antes de escribir, el archivo anterior se copia al lado como `nombre.igz.bak`. Un guardado truncado (corte de luz, disco lleno) nunca se lleva la versión buena.
- **Invertir la rueda del ratón al hacer zoom.**
- **Anti-aliasing (MSAA)**: 0, 2, 4 u 8 muestras. Más muestras, bordes más suaves y más trabajo para la gráfica.
- **Pasos de deshacer**: cuántas operaciones guarda el historial (200 por defecto; 0 = sin límite). Cada paso lleva una instantánea del modelo, así que en un modelo grande el tope es memoria. Aplica al momento.
- **Preguntar nombre y símbolo al colocar un plano de sección**: vuelve a encender el cuadro que aparece al colocar un [plano de sección](modelado/secciones.md) si lo apagaste con «No volver a preguntar».

## Importar

- **Unidad sugerida para OBJ** y **para DXF/DWG**: la respuesta preseleccionada en el diálogo que pregunta la unidad al importar (los diálogos siguen preguntando: las cabeceras CAD suelen mentir, y IngeTrazo además la **sugiere midiendo el dibujo**).
- **Coordenadas**: geográficas (lat/lon) o UTM WGS84, para el panel de terreno.

## Unidades

Las **unidades del documento que tienes abierto** — se guardan con él, no en el programa. Elige la unidad de longitud (metros, centímetros, milímetros, pulgadas, pies, pies y pulgadas, o las fraccionarias `1 1/2"`) y los decimales. Manda en las dos direcciones:

- Un número tecleado **sin unidad** está en ella: `2` son 2 mm en un documento en milímetros; `2m` siempre son 2 m (la unidad explícita gana).
- Todo lo que el programa **muestra** —herramientas, Info de entidad, barra de estado, resumen por materiales— se lee en ella.
- El **estilo de cota** la sigue al cambiarla; su propio panel puede apartarlo después.

Un documento nuevo nace en metros, y los documentos anteriores a la 0.4.9 abren en metros. Cambiar de unidad **no cambia la geometría**, solo cómo se lee y cómo se teclea. En las fraccionarias, **Decimales** fija el denominador más fino: 0 = pulgadas enteras, 1 = 1/4, 2 = 1/16, 3 = 1/32, 4 = 1/64.

## Asistente IA

Las mismas casillas del [Asistente IA](ia.md): proveedor, clave, modelo, URL de Ollama y si se envían capturas del viewport al modelo.

## Lo que el programa recuerda solo

- **Archivo ▸ Abrir recientes**: los últimos diez documentos `.igz` abiertos o guardados, con «Limpiar lista»; los que ya no existen desaparecen solos. Una importación (`.skp`, `.dxf`…) no cuenta como documento reciente.
- **Las carpetas**: cada diálogo de abrir, guardar, importar o exportar arranca en la **última carpeta que elegiste** en cualquiera de ellos (si no hay ninguna, en la del documento abierto; si tampoco, en Documentos).
- **La disposición** de barras de herramientas y paneles.
- **El estilo de cota** de la última cota que editaste en el compositor, y la **plantilla de cajetín** y de **lámina** predeterminadas.
- En Windows, con una laptop de dos gráficas (Intel + NVIDIA/AMD), la primera ejecución pide al sistema la **gráfica dedicada** para IngeTrazo. Si el visor va lento, **Ayuda ▸ Acerca de** dice qué gráfica está dibujando y avisa si es un rasterizador por software.
