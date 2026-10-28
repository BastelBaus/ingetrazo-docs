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

## Exportar

- **IFC 4**: Archivo ▸ Exportar ▸ IFC. El archivo pasa la validación estándar (`ifcopenshell.validate`) y lo abre cualquier visor o software BIM. Incluye las cantidades (`Qto_*BaseQuantities`).
- **CSV de cantidades**: tu tabla de metrados lista para la hoja de cálculo.

## El puente a IngePresupuestos

El flujo estrella del ecosistema:

1. Etiqueta tu modelo en IngeTrazo.
2. Exporta el **IFC**.
3. En [IngePresupuestos](https://ingepresupuestos.com), importa ese IFC: las partidas llegan con sus **metrados exactos**, listas para el análisis de costos unitarios, el cronograma y el control de obra.

Verificado de punta a punta: los metrados que ves en el panel BIM son los que aterrizan en el presupuesto.
