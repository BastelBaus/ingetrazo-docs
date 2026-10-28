# Ejemplos para abrir

Cuatro documentos reales, dibujados con IngeTrazo para la remodelación de la plaza de Yanque, distrito de Chichas (Arequipa, 2026), por el Ing. Marco Sumari. Los cuatro traen su **lámina A3 lista** y, al lado, el PDF que sale de ella para que compares.

**Descárgalos:** todos juntos en cada release como [`IngeTrazo-ejemplos.zip`](https://github.com/ingelibre/ingetrazo/releases/latest/download/IngeTrazo-ejemplos.zip), o uno a uno desde la carpeta [`examples/`](https://github.com/ingelibre/ingetrazo/tree/main/examples) del repositorio (y desde la sección *Ejemplos* de [ingetrazo.com](https://ingetrazo.com/#ejemplos)). Necesitan IngeTrazo 0.3.15 o posterior.

| Archivo | Qué es | Qué enseña |
|---|---|---|
| `pileta-fuente-yanque.igz` (+ `.pdf`) | La pileta central de la plaza: pedestal octogonal, fuste estriado, dos platos de borde ondulado, vereda con nariz boleada | Componentes repetidos (22 instancias), **sombras con sol real**, plano de sección; lámina con frontal, 3D, planta y corte a 1:40, foto de referencia y cajetín |
| `banca-pergola-yanque.igz` (+ `.pdf`) | Banca de concreto con pérgola de madera | Componentes, cinco **escenas** guardadas; lámina con cuatro vistas, **23 cotas** y 12 etiquetas con guía |
| `luminaria-solar-yanque.igz` (+ `.pdf`) | Poste de alumbrado solar de 4,5 m: dado tronco-cónico, cimiento enterrado con su acero de 3/8", dos reflectores con panel | Modelado por recetas con la [IA](../ia.md), detalle de acero, lámina con cuatro vistas y detalle del dado |
| `arco-yanque.igz` (+ `.pdf`) | Arco de bienvenida «YANQUE» según la lámina estructural E02: concreto, **todo el acero** (zapatas, columnas, arco segmental, viga, tímpano), capiteles de sillar, cuatro farolas ornamentales, letras y escultura | **Rayos X** para ver el acero, planos de sección, imágenes «cara a la cámara», texturas; lámina D04 con frente, lado, planta y 3D a 1:50, detalles de letra y escultura (1:25) y del capitel (1:20), **niveles**, **línea de terreno** y etiquetas con guía |

## Qué mirar en cada uno

- **Abre el documento** (Archivo ▸ Abrir, o doble clic al `.igz`) y recorre las **escenas** del panel Escenas con doble clic: cada una guarda cámara, capas y sección activa.
- **La lámina**: pestaña *Lámina 1* en la barra de estado (o Archivo ▸ Compositor de láminas). Selecciona un marco y mira su panel: escala, estilo, rótulo. Doble clic en un marco para orbitar dentro de él. **Exportar PDF…** y compara con el PDF que viene al lado.
- **El acero del arco y de la luminaria**: Cámara ▸ Estilo ▸ **Rayos X**, o activa el plano de sección del documento (Cámara ▸ Cortes de sección) y muévelo con la herramienta Mover.
- **Los grupos**: todo tiene nombre («Acero columna C1 izq 10 Ø5/8"», «Farola ornamental blanca der adelante»…). Doble clic entra a editar; `Esc` sale.

!!! note "Licencia"
    Los documentos (modelos, láminas y PDF) son del Ing. Marco Sumari Tellez y se publican bajo [Creative Commons Atribución 4.0](https://creativecommons.org/licenses/by/4.0/deed.es): úsalos, modifícalos y compártelos citando la fuente. El código de IngeTrazo sigue bajo la GPL-3.0.
