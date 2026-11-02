# BIM y metrados

El BIM de IngeTrazo no es una jaula de familias: **modelas libre y etiquetas**. La etiqueta es metadato sobre la geometría seleccionada — lo etiquetado entra al metrado y al IFC; lo demás es dibujo.

![Una nave industrial con el panel BIM abierto: las columnas seleccionadas se etiquetan como IfcColumn.](images/bim.jpeg)


## Etiquetar

En el panel **BIM** de la bandeja:

1. Selecciona la geometría (el muro que acabas de levantar, la columna, la puerta).
2. Elige la **clase**: muro, losa, columna, viga, puerta, ventana, escalera, baranda, cobertura… (15 clases IFC).
3. **Asignar selección**. Listo — la geometría ya "sabe" lo que es.

!!! tip "Etiquetar al dibujar"
    Activa una clase con el candado de **"Etiquetar al dibujar"** y todo lo que traces desde ese momento asume la clase automáticamente. Además, el empujar/tirar **propaga** la etiqueta: engrosar un muro etiquetado no la pierde.

## Metrado en vivo

El mismo panel muestra las **cantidades al instante**, por clase:

- Muros: **m² netos** de cara (descontando vanos).
- Losas: m² y m³.
- Columnas y vigas: m³ y metros lineales.
- Puertas y ventanas: **unidades** con sus dimensiones.

Los números salen del sólido real — y como el motor garantiza sólidos herméticos, el metrado es confiable por construcción.

## Buscar, filtrar y agrupar

Con muchos objetos, la barra encima de la tabla ayuda a encontrar lo que buscas:

- **Buscador**: escribe parte del nombre, de la clase o de la ruta en el esquema (`*` y `?` funcionan, como en el Navegador).
- **Embudo**: desmarca las clases IFC que no quieres ver — por ejemplo, deja solo los IfcSpace. El embudo se rellena mientras oculta algo.
- **Agrupar**: *por grupo* (cada objeto dentro de los grupos que lo contienen), *por clase IFC* o *por nombre* (cada encabezado con su número de objetos y los totales de metrado y volumen de las filas visibles) o *sin agrupar*.
- **Columnas**: la columna **Ruta en el esquema** dice en qué grupos está cada objeto, por ejemplo «Planta 1/Núcleo». El botón al final del encabezado (o el clic derecho sobre él) muestra u oculta Metrado, Vol m³ y Ruta en el esquema, como en el Navegador.

El agrupamiento, las clases ocultas y las columnas se recuerdan entre sesiones.

## Exportar

- **IFC 4**: Archivo ▸ Exportar ▸ IFC. El archivo pasa la validación estándar (`ifcopenshell.validate`) y lo abre cualquier visor o software BIM. Incluye las cantidades (`Qto_*BaseQuantities`).
- **CSV de cantidades**: tu tabla de metrados lista para la hoja de cálculo. **Exportar todo a CSV** escribe todos los objetos; **Exportar lo mostrado a CSV**, solo los que dejan el buscador y el embudo.

## El puente a IngePresupuestos

El flujo estrella del ecosistema:

1. Etiqueta tu modelo en IngeTrazo.
2. Exporta el **IFC**.
3. En [IngePresupuestos](https://ingepresupuestos.com), importa ese IFC: las partidas llegan con sus **metrados exactos**, listas para el análisis de costos unitarios, el cronograma y el control de obra.

Verificado de punta a punta: los metrados que ves en el panel BIM son los que aterrizan en el presupuesto.
