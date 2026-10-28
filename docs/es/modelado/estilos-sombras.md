# Estilos, sombras y pantalla

Cómo se ve el modelo es una decisión tuya, por documento y por escena: los **estilos** deciden caras, aristas, cielo y fondo; las **sombras** ponen el sol de tu sitio a la hora que elijas; y la pantalla limpia deja solo el modelo.

## Estilos

**Cámara ▸ Estilo** cambia el estilo activo del documento. Los integrados:

| Estilo | Qué muestra |
|---|---|
| **Predeterminado** | Caras con materiales y texturas, aristas, cielo degradado. |
| **Arquitectónico** | Fondo blanco, sin cielo, aristas y perfiles: el aspecto de una lámina. Es el estilo con el que nace todo marco de vista nuevo en el compositor. |
| **Sombreado** | Caras con color, sin texturas. |
| **Línea oculta** | Solo líneas, caras blancas: el dibujo técnico. |
| **Monocromo** | Caras de un solo tono. |
| **Alámbrico** | Solo aristas. |
| **Rayos X** | Todo translúcido, aristas siempre visibles: para mirar adentro (el acero, las tuberías) sin cortar. |

**Cámara ▸ Aristas** y **Cámara ▸ Perfiles** encienden o apagan las aristas y las siluetas gruesas del estilo activo.

### El editor de estilos

El desplegable **Estilos** de la barra de herramientas abre el editor, que edita el estilo activo **en vivo**:

- Modo de cara (sombreado, línea oculta, monocromo, alámbrico, rayos X), aristas, perfiles, cielo y **relleno de sección**.
- Los cuatro colores: frente y dorso de las caras, **cielo** y **suelo** — con un degradado hacia el horizonte. Un color que no se ve en el modo actual sigue siendo editable; la barra de estado dice dónde se verá.
- **Guardar estilo…** lo añade a **tu biblioteca** con nombre (un nombre integrado se rechaza: los presets son fijos). **Eliminar** lo quita.
- Los estilos guardados aparecen en Cámara ▸ Estilo y en el combo de estilo de cada **marco del compositor** — cada marco puede llevar el suyo.
- Cada **escena** recuerda su estilo, y el `.igz` guarda el estilo completo: un documento no depende de tu biblioteca.

## Sombras con el sol de verdad

El desplegable **Sombras** de la barra de herramientas (y **Cámara ▸ Sombras**) enciende sombras calculadas con la **posición real del sol**:

- **Fecha**: día y mes, con un deslizador del año. **Hora**, acotada al día — de amanecer a atardecer del sitio y la fecha, para que el sol nunca esté bajo el horizonte.
- **Oscuridad** de las sombras y **zona horaria** (se deduce de la longitud; puedes fijarla).
- **Sitio**: el datum del proyecto si está [georreferenciado](../terreno/ubicacion.md); si no, Arequipa. **Añadir localización…** abre el localizador y fija el datum.
- El **vidrio con opacidad menor a 70 % no proyecta sombra**; las texturas caladas (mallas, hojas) proyectan su trama; las figuras «cara a la cámara» proyectan su silueta orientada al sol.
- El sol también **sombrea las caras** (las que le dan la espalda se ven más oscuras) y el suelo recibe la sombra como una veladura.
- Los ajustes de sombra se guardan en el documento y **los marcos del compositor renderizan con ellas**: una lámina de asoleamiento sale directa.

!!! note "Precisión"
    El cálculo astronómico está verificado (en el equinoccio el sol sale por el este; en junio, en Arequipa, pasa por el norte a ~50°). Lo que ves es el asoleamiento de tu sitio en esa fecha y hora.

## Pantalla limpia y disposición

- **Ventana ▸ Pantalla limpia** (`Ctrl+0`) oculta barras y paneles y deja solo el viewport; otra vez `Ctrl+0` los devuelve.
- **La disposición se recuerda**: dónde dejaste las barras de herramientas, qué paneles de la bandeja abriste y su tamaño vuelven en la próxima sesión.
- Los paneles **Estilos**, **Sombras** y **Estilo de cota** son desplegables de la barra de herramientas, no ocupan la bandeja derecha.
- **Cámara ▸ Resto del modelo al editar**: al entrar a un grupo, lo demás se muestra normal, **atenuado** (el valor por defecto) u **oculto** (el modo más rápido en modelos pesados). También en Preferencias.

## Exportar una imagen

**Archivo ▸ Exportar ▸ Imagen (PNG / JPG)…** guarda una captura de alta resolución del viewport con el estilo y las sombras actuales — sin indicadores de selección ni marcas de herramienta.
