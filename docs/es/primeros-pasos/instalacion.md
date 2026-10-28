# Instalación

IngeTrazo es gratuito y de código abierto (GPL-3.0). No pide cuenta, no tiene suscripciones y funciona sin internet. Todos los paquetes están en [ingetrazo.com](https://ingetrazo.com/#descargar) y en los [releases de GitHub](https://github.com/ingelibre/ingetrazo/releases).

## Windows

1. Descarga el instalador `ingetrazo-setup-vX.Y.Z.exe`.
2. Doble clic y sigue el asistente. El instalador asocia los archivos `.igz` y agrega IngeTrazo al menú «Abrir con» de `.skp` y `.dae`, e incluye `ingetrazo-mcp.exe` para el [puente IA](../ia.md).
3. Si prefieres no instalar nada, descarga `ingetrazo-windows.zip` (versión portable): descomprime y ejecuta `ingetrazo.exe`.

!!! note "SmartScreen"
    La primera vez Windows puede mostrar el aviso de SmartScreen porque el instalador no está firmado comercialmente. Elige **Más información ▸ Ejecutar de todas formas**.

!!! tip "Laptops con dos gráficas"
    En una laptop con gráfica integrada y dedicada (Intel + NVIDIA/AMD), IngeTrazo pide al sistema la **dedicada** la primera vez que arranca. Si aun así el visor va lento, **Ayuda ▸ Acerca de** dice quién está dibujando; en Configuración ▸ Sistema ▸ Pantalla ▸ Gráficos puedes fijarlo a mano en «Alto rendimiento».

## Linux

=== "Flatpak (recomendado)"

    Instálalo **desde el repositorio de IngeTrazo** y a partir de ahí `flatpak update` te trae cada versión nueva. Queda en tu menú de aplicaciones con los `.igz`, `.skp` y `.dae` asociados (el entorno Freedesktop baja solo de Flathub):

    ```bash
    flatpak remote-add --user --if-not-exists ingetrazo https://ingetrazo.com/ingetrazo.flatpakrepo
    flatpak install --user ingetrazo com.ingetrazo.IngeTrazo
    flatpak run com.ingetrazo.IngeTrazo
    ```

    El release también trae un `IngeTrazo-X.Y.Z-x86_64.flatpak` de un solo archivo que se instala con doble clic — pero un bundle **no tiene de dónde buscar versiones nuevas**: se queda en la que instalaste.

=== "AppImage"

    Descarga `IngeTrazo-X.Y.Z-x86_64.AppImage`, dale permiso de ejecución y ábrelo (o doble clic desde el gestor de archivos):

    ```bash
    chmod +x IngeTrazo-*-x86_64.AppImage && ./IngeTrazo-*-x86_64.AppImage
    ```

    Necesita FUSE, que casi toda distro trae.

=== "tar.gz"

    Si tu distro no tiene FUSE, descomprime y ejecuta — sirve igual para dejarlo en `/opt`:

    ```bash
    tar -xzf IngeTrazo-*-linux-x86_64.tar.gz && IngeTrazo-*/ingetrazo
    ```

=== "Snap"

    `ingetrazo_X.Y.Z_amd64.snap` está adjunto a cada release: `sudo snap install --dangerous ingetrazo_*.snap` (la publicación en la Snap Store está en trámite).

=== "Código fuente"

    ```bash
    git clone https://github.com/ingelibre/ingetrazo.git
    cd ingetrazo/app
    python3 -m venv venv && venv/bin/pip install -r requirements.txt
    venv/bin/python main.py
    ```

    Para el ícono en el menú y la asociación de archivos: `scripts/install_desktop.sh`. Actualizar es `git pull`.

Los paquetes traen todo adentro: Python, Qt, el lector de `.skp` y el conversor de DWG. Corren en Ubuntu 22.04 y posteriores. Si algo falla, `ingetrazo --check` dice qué falta.

## macOS

IngeTrazo corre en macOS desde el código fuente con los mismos pasos que Linux. No hay todavía paquete `.dmg` oficial.

## Actualizar

- **Windows**: instala la versión nueva encima; conserva tus preferencias y asociaciones.
- **Linux**: `flatpak update` con el repositorio; con AppImage o tar.gz, descarga el nuevo; desde el código, `git pull`.

Tus modelos son archivos `.igz` normales en tu disco — actualizar el programa nunca los toca. Un documento guardado por una versión más nueva **abre igual** en una anterior (lo que la vieja no conoce, lo ignora), aunque las láminas nuevas se ven completas solo en la versión que las hizo.

## Y ahora, algo para abrir

Los [ejemplos](ejemplos.md) — cuatro documentos reales con sus láminas — son la forma más rápida de ver de qué es capaz el programa.
