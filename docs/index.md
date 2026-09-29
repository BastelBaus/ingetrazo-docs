# Manual de IngeTrazo

Bienvenido al manual de usuario de **IngeTrazo**, el modelador 3D libre para ingeniería civil y arquitectura: traza como a mano, etiqueta BIM, ubica tu proyecto en el terreno real y saca los planos en PDF — todo en un solo programa, offline y de código abierto.

!!! tip "¿Primera vez con IngeTrazo?"
    Empieza por **[Instalación](primeros-pasos/instalacion.md)** y sigue con **[Tu primer modelo](primeros-pasos/primer-modelo.md)**: en quince minutos levantas una casita con medidas exactas.

## Qué vas a encontrar

<div class="grid cards" markdown>

-   :material-rocket-launch: **Primeros pasos**

    ---

    Instala el programa en Windows o Linux, conoce la interfaz y levanta tu primer modelo con medidas reales.

    [:octicons-arrow-right-24: Empezar](primeros-pasos/instalacion.md)

-   :material-pencil-ruler: **Modelado**

    ---

    Las herramientas de dibujo y edición: empujar/tirar, sígueme, escalar, grupos y componentes, materiales, capas, escenas, secciones, estilos y sombras.

    [:octicons-arrow-right-24: Modelar](modelado/dibujo.md)

-   :material-tag-outline: **BIM y metrados**

    ---

    Etiqueta muros, losas y columnas; obtén cantidades en vivo y exporta IFC 4 para tu presupuesto.

    [:octicons-arrow-right-24: Etiquetar](bim.md)

-   :material-terrain: **Terreno**

    ---

    Mapa satelital, terreno 3D, tu levantamiento de dron y los puntos de la estación total — en UTM WGS84.

    [:octicons-arrow-right-24: Georreferenciar](terreno/ubicacion.md)

-   :material-file-document-outline: **Composición de láminas**

    ---

    Del modelo al plano: vistas a escala exacta con líneas ocultas exactas, cotas ancladas al modelo, niveles, cadenas, llamadas, cajetín con plantillas y PDF vectorial.

    [:octicons-arrow-right-24: Componer](laminas/index.md)

-   :material-swap-horizontal: **Importar y exportar**

    ---

    Abre tus `.skp` (todas las versiones, sin conversores), DXF y DWG; exporta IFC, STL, OBJ, glTF y DXF.

    [:octicons-arrow-right-24: Intercambiar](importar-exportar.md)

-   :material-robot-outline: **Modelar con la IA**

    ---

    El Asistente IA dentro de la app, o Claude dirigiendo IngeTrazo por MCP: describe, adjunta una foto, y la IA escribe la receta que el motor ejecuta.

    [:octicons-arrow-right-24: Modelar con la IA](ia.md)

-   :material-folder-open-outline: **Ejemplos para abrir**

    ---

    Cuatro documentos reales de la plaza de Yanque, tres con su lámina A3 y su PDF: la forma más rápida de ver de qué es capaz el programa.

    [:octicons-arrow-right-24: Abrir los ejemplos](primeros-pasos/ejemplos.md)

</div>

## La idea detrás de IngeTrazo

El nombre es la tesis: **trazar como en la vida real**. Dibujas líneas y rectángulos, empujas una cara y ya tienes un sólido — sin familias rígidas ni capas de complejidad CAD entre tu idea y el modelo. Cuando necesitas semántica, la agregas *encima*: etiquetas la geometría como muro o columna y el programa te da las cantidades y el IFC.

El flujo completo que IngeTrazo cubre junto a su hermano [IngePresupuestos](https://ingepresupuestos.com):

```
Terreno (dron, GPS, satélite) → Trazar encima → Etiquetar BIM → IFC → Presupuesto
                                      ↓
                            Láminas → PDF (planos)
```

## Ayuda y comunidad

- El proyecto vive en [GitHub](https://github.com/ingelibre/ingetrazo): abre un *issue* con tu archivo de ejemplo si algo no funciona.
- Contacto directo: [ing.sumari@gmail.com](mailto:ing.sumari@gmail.com).
