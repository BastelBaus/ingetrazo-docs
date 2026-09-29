# Importar y exportar

## El formato nativo: `.igz`

Abierto y documentado. Sin texturas es JSON legible; con texturas se vuelve un contenedor autocontenido (las imágenes viajan **dentro**, sin rutas de tu máquina). Las composiciones de láminas, capas, escenas, secciones, sombras, BIM y georreferenciación se guardan ahí también. Guardado atómico: un corte de luz no corrompe el archivo, y con la copia `.igz.bak` de [Preferencias](preferencias.md) sobrevive hasta un disco lleno. Un `.igz` de una versión más nueva abre en una anterior (lo desconocido se ignora).

## Importar `.skp` — nativo

![Un `.skp` recién abierto: la geometría, los materiales y las capas originales llegan intactos.](images/importar.jpeg)


**Archivo ▸ Importar ▸ SKP (.skp)…**, o **doble clic** al archivo, o arrástralo a la ventana.

El importador es **propio y de código abierto** (proyecto [OpenSKP](https://github.com/iamahsanmehmood/openskp), al que IngeTrazo contribuye): lee el `.skp` directamente, **sin conversores ni otros programas instalados**, en todas sus eras — desde los formatos antiguos (2013–2020) hasta los actuales.

Lo que llega:

- Geometría completa, **grupos y componentes** (las instancias siguen compartidas: mover una farola no arrastra el resto; los componentes anidados conservan su jerarquía).
- **Materiales y texturas**, incluidos los colorizados, la translucidez, los materiales por lado, las texturas posicionadas y los billboards «siempre de cara».
- **Capas/etiquetas** con su visibilidad, **escenas** (cámara + capas por escena), **cotas lineales** y **textos guía**.
- Verificado con expedientes reales: bounding box exacto y 0,00 % de diferencia de área contra el modelo original.

## CAD: DXF y DWG

**Archivo ▸ Importar ▸ AutoCAD DXF (.dxf)…** o **AutoCAD DWG (.dwg)…** trae un dibujo 2D o 3D de CAD:

- Cada **capa** llega como un grupo etiquetado; las **curvas** (arcos, círculos, polilíneas) como una sola entidad seleccionable de un clic; los **bloques** como componentes con sus instancias; las caras 3D como caras, fusionando las coplanares. Texto y cotas se omiten.
- **La unidad se sugiere midiendo el dibujo** (la cabecera de un DWG suele mentir); el diálogo te deja confirmarla. Las coordenadas UTM lejanas se recentran solas.
- El DWG se convierte con LibreDWG, que viaja dentro del paquete de Linux (en Windows, por ahora, exporta a DXF desde tu CAD).
- Doble clic sobre un `.dxf` o `.dwg` también lo abre.

Para el camino inverso, [exporta la vista de una lámina como DXF](laminas/exportar.md#dxf-hacia-ingecad-autocad).

## Otros formatos

| Formato | Importa | Exporta | Notas |
|---|:-:|:-:|---|
| **COLLADA (.dae)** | ✔ | ✔ | El export incluye la geolocalización — Blender lo abre con el sol de tu sitio para asoleamiento. |
| **OBJ** | ✔ | ✔ | Con materiales (MTL). Al importar se pregunta la unidad. |
| **glTF / GLB** | ✔ | ✔ | Import nativo con texturas y jerarquía; export PBR + geolocalización — el formato de visores web y Blender moderno. |
| **STL** | — | ✔ | Binario, para impresión 3D. Sólidos herméticos garantizados. |
| **IFC 4** | — | ✔ | El puente BIM. Ver [BIM y metrados](bim.md). |
| **DXF (R12)** | ✔ | ✔ | Entra como dibujo CAD; sale como la vista vectorial de una lámina, con una capa por clase de línea. |
| **DWG** | ✔ | — | Vía LibreDWG (Linux). |
| **Imagen** | ✔ | ✔ | Entra como [imagen de referencia](modelado/imagenes-referencia.md) para calcar; sale como captura de alta resolución del viewport. |
| **WebODM/ODM** | ✔ | — | El levantamiento de dron. Ver [Terreno](terreno/dron.md). |
| **CSV topográfico** | ✔ | — | Puntos P,N,E,Z de estación total. Ver [Terreno](terreno/rutas-perfil.md). |
| **KML / GeoJSON** | ✔ | — | Alineamientos y polígonos georreferenciados. |
| **PDF** | — | ✔ | Las láminas, vectoriales. Ver [Exportar PDF](laminas/exportar.md). |

Toda importación es **un paso de deshacer**: `Ctrl+Z` la quita entera.
