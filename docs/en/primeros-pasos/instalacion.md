---
source_blob: 8d10e6482db26581866e62a85881197b1d31646b
---

# Installation

IngeTrazo is free and open source (GPL-3.0). It asks for no account, has no subscriptions and works without internet. All packages are on [ingetrazo.com](https://ingetrazo.com/#descargar) and in the [GitHub releases](https://github.com/ingelibre/ingetrazo/releases).

## Windows

1. Download the installer `ingetrazo-setup-vX.Y.Z.exe`.
2. Double-click and follow the wizard. The installer associates `.igz` files, adds IngeTrazo to the "Open with" menu of `.skp` and `.dae`, and includes `ingetrazo-mcp.exe` for the [AI bridge](../ia.md).
3. If you would rather not install anything, download `ingetrazo-windows.zip` (portable version): unzip it and run `ingetrazo.exe`.

!!! note "SmartScreen"
    The first time, Windows may show the SmartScreen warning because the installer is not commercially signed. Choose **More info ▸ Run anyway**.

!!! tip "Laptops with two graphics cards"
    On a laptop with integrated and dedicated graphics (Intel + NVIDIA/AMD), IngeTrazo asks the system for the **dedicated** one the first time it starts. If the viewport is still slow, **Help ▸ About** tells you which one is drawing; in Settings ▸ System ▸ Display ▸ Graphics you can pin it by hand to "High performance".

## Linux

=== "Flatpak (recommended)"

    Install it **from the IngeTrazo repository** and from then on `flatpak update` brings you every new version. It shows up in your application menu with `.igz`, `.skp` and `.dae` associated (the Freedesktop runtime is downloaded from Flathub automatically):

    ```bash
    flatpak remote-add --user --if-not-exists ingetrazo https://ingetrazo.com/ingetrazo.flatpakrepo
    flatpak install --user ingetrazo com.ingetrazo.IngeTrazo
    flatpak run com.ingetrazo.IngeTrazo
    ```

    The release also ships a single-file `IngeTrazo-X.Y.Z-x86_64.flatpak` that installs with a double-click — but a bundle **has nowhere to look for new versions**: it stays on the one you installed.

=== "AppImage"

    Download `IngeTrazo-X.Y.Z-x86_64.AppImage`, make it executable and open it (or double-click it in the file manager):

    ```bash
    chmod +x IngeTrazo-*-x86_64.AppImage && ./IngeTrazo-*-x86_64.AppImage
    ```

    It needs FUSE, which almost every distro ships.

=== "tar.gz"

    If your distro has no FUSE, unpack and run — it works just as well for putting it in `/opt`:

    ```bash
    tar -xzf IngeTrazo-*-linux-x86_64.tar.gz && IngeTrazo-*/ingetrazo
    ```

=== "Snap"

    `ingetrazo_X.Y.Z_amd64.snap` is attached to every release: `sudo snap install --dangerous ingetrazo_*.snap` (publication in the Snap Store is in progress).

=== "Source code"

    ```bash
    git clone https://github.com/ingelibre/ingetrazo.git
    cd ingetrazo/app
    python3 -m venv venv && venv/bin/pip install -r requirements.txt
    venv/bin/python main.py
    ```

    For the menu icon and file associations: `scripts/install_desktop.sh`. Updating is `git pull`.

The packages bundle everything: Python, Qt, the `.skp` reader and the DWG converter. They run on Ubuntu 22.04 and later. If something fails, `ingetrazo --check` tells you what is missing.

## macOS

IngeTrazo runs on macOS from source with the same steps as Linux. There is no official `.dmg` package yet.

## Updating

- **Windows**: install the new version over the old one; your preferences and associations are kept.
- **Linux**: `flatpak update` with the repository; with AppImage or tar.gz, download the new one; from source, `git pull`.

Your models are ordinary `.igz` files on your disk — updating the program never touches them. A document saved by a newer version **still opens** in an older one (whatever the old one does not know, it ignores), although new sheets only display completely in the version that made them.

## And now, something to open

The [examples](ejemplos.md) — four real documents with their sheets — are the fastest way to see what the program can do.
