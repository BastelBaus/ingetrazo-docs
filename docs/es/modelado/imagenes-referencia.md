# Imágenes de referencia

Un plano escaneado, una foto aérea, un croquis: **Archivo ▸ Importar ▸ Imagen (PNG / JPG)…** la coloca en el modelo como un plano para **calcar encima**.

## Colocar y ajustar

1. Importa la imagen: aparece sobre el plano del suelo, en su propia capa **Images**.
2. **Clic derecho ▸ Tamaño de la imagen…** para darle sus medidas reales en metros — el ancho del plano que escaneaste, el lado de la parcela.
3. **Mover** (`M`), **Rotar** (`Q`) y **Escalar** (`S`) la tratan como cualquier entidad: llévala a su sitio, gírala, escálala tomando dos puntos conocidos.
4. **Clic derecho ▸ Bloquear** cuando esté en su lugar: bloqueada **no acepta clics** (no se selecciona ni se mueve por accidente) pero **sigue dando plano de trabajo e imantación** en sus bordes — el estado de calco.

## Calcar

- Las herramientas de dibujo trabajan **sobre la imagen**: Línea, Rectángulo y Arco caen en su plano, con las inferencias de siempre.
- La imagen es **solo referencia**: no entra a la geometría ni a los metrados ni a los exports 3D; apaga su capa cuando termines.
- Viaja **dentro del `.igz`**, como las texturas: el documento sigue siendo autocontenido.

!!! tip "Planos en DWG/DXF"
    Si el plano está en CAD, no lo calques: **Archivo ▸ Importar ▸ AutoCAD DXF/DWG** lo trae como líneas reales por capa — ver [Importar y exportar](../importar-exportar.md#cad-dxf-y-dwg).
