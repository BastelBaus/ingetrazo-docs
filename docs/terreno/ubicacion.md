# Ubicación del proyecto y mapa base

Todo el trabajo de terreno empieza fijando **dónde** está tu proyecto. Eso ancla el sistema de coordenadas y habilita el mapa satelital, el terreno 3D y los datos de campo.

## Fijar la ubicación

En la bandeja, panel **Terreno / Mapa base**:

1. **Buscar ubicación…** abre el localizador: busca el lugar por nombre, usa "Ubicarme", o navega el mapa.
2. Acomoda el mapa hasta que el **pin central esté exactamente sobre tu sitio** — haz zoom sin miedo.
3. Acepta y luego **Ir a ubicación**.

!!! warning "El pin ES el origen de tu modelo"
    El punto que eliges se convierte en el **origen (0,0,0)** del modelo. Dibuja alrededor del origen y tu modelo cae exactamente ahí sobre el satélite — sin tener que moverlo después. El propio mapa lo dice: el pin está rotulado *origen (0,0)*.

    Si el proyecto ya tenía ubicación y eliges otra, IngeTrazo **pregunta antes de mover el origen** (todo lo dibujado conserva sus coordenadas locales y se reubica sobre el mapa).

## Coordenadas: UTM o geográficas

Con el selector **Coordenadas** eliges cómo ver y escribir la posición — y el programa recuerda tu elección:

- **UTM WGS84**: Zona, hemisferio, **Este** y **Norte** — tal como lo reporta tu dron o tu estación total, con las convenciones estándar (falso este 500 km; falso norte 10 000 km en el hemisferio sur).
- **Geográficas**: latitud y longitud en grados decimales.

Ambos marcos están siempre sincronizados por debajo; cambiar de modo no pierde nada. Con el proyecto georreferenciado, la **barra de estado muestra la lectura UTM continua** del cursor.

## El norte: gira el mapa, no el modelo

Un edificio o una plaza se dibuja **a escuadra con los ejes** (el rojo y el verde): así las vistas Frontal, Derecha e Izquierda, los bloqueos de eje y el rectángulo funcionan sin pensar. Pero el sitio rara vez mira al norte. Si giras el modelo para acomodarlo sobre el satélite, pierdes todo eso.

El modelo se queda en sus ejes y **el mapa gira por debajo**. El campo **Norte** del panel dice hacia dónde queda el norte verdadero, en grados en sentido horario desde el eje verde (0° = el eje verde apunta al norte). Al cambiarlo giran el mapa base, el terreno 3D, las rutas y puntos importados y las sombras; el modelo no se mueve.

**¿Ya giraste y arrastraste el modelo sobre el mapa?** Selecciónalo (tiene que ser un solo componente de primer nivel — agrúpalo si hace falta) y pulsa **Enderezar modelo sobre el mapa**: el modelo vuelve a sus propios ejes, el origen pasa a la esquina del modelo y el ángulo del norte queda calculado, de modo que **nada se mueve sobre el mapa**. Las escenas guardadas, las cotas y las láminas ancladas al modelo viajan con él. Es un solo paso de deshacer.

!!! note "Altura"
    Al enderezar, el modelo recupera las alturas con las que se dibujó y el mapa sigue en z = 0 (es el plano de referencia). Si el modelo estaba flotando sobre el mapa, baja a su sitio.

## El mapa base

- **Fuentes**: satélite Esri, OpenStreetMap y las que agregues — cualquier servidor de teselas **XYZ** (tu propio ortofoto servido desde QGIS, por ejemplo) se guarda con nombre y queda para siempre en el menú.
- **Área de captura**: en el localizador puedes dibujar un rectángulo — un cuadrado para un sitio, una franja larga para una carretera.
- **Zoom** controla el detalle de las teselas; las capturas enormes reducen el detalle automáticamente para mantener el programa fluido.
- El mapa es **solo referencia visual**: nunca entra a tu geometría ni a tus metrados, y la captura se guarda con el documento (las teselas se descargan de nuevo al abrir).
