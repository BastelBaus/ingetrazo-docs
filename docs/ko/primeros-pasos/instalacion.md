---
source_blob: 8d10e6482db26581866e62a85881197b1d31646b
---

# 설치

IngeTrazo는 무료 오픈 소스(GPL-3.0)입니다. 계정이 필요 없고, 구독도 없으며, 인터넷 없이 동작합니다. 모든 패키지는 [ingetrazo.com](https://ingetrazo.com/#descargar)과 [GitHub releases](https://github.com/ingelibre/ingetrazo/releases)에 있습니다.

## Windows

1. 설치 프로그램 `ingetrazo-setup-vX.Y.Z.exe`를 내려받습니다.
2. 더블 클릭하고 마법사를 따라갑니다. 설치 프로그램은 `.igz` 파일을 연결하고, `.skp`와 `.dae`의 「연결 프로그램」 메뉴에 IngeTrazo를 추가하며, [AI 브리지](../ia.md)용 `ingetrazo-mcp.exe`도 함께 설치합니다.
3. 아무것도 설치하고 싶지 않다면 `ingetrazo-windows.zip`(포터블 버전)을 내려받아 압축을 풀고 `ingetrazo.exe`를 실행하세요.

!!! note "SmartScreen"
    설치 프로그램에 상용 서명이 없어서, 처음 실행할 때 Windows가 SmartScreen 경고를 띄울 수 있습니다. **추가 정보 ▸ 실행**을 고르세요.

!!! tip "그래픽 카드가 두 개인 노트북"
    내장 그래픽과 외장 그래픽(Intel + NVIDIA/AMD)이 모두 있는 노트북에서는, IngeTrazo가 처음 실행될 때 시스템에 **외장** 그래픽을 요청합니다. 그래도 뷰포트가 느리다면 **도움말 ▸ IngeTrazo 정보**에서 어느 GPU가 그리고 있는지 확인할 수 있습니다. 설정 ▸ 시스템 ▸ 디스플레이 ▸ 그래픽에서 「고성능」으로 직접 지정할 수도 있습니다.

## Linux

=== "Flatpak (권장)"

    **IngeTrazo 저장소에서** 설치하면, 그 뒤로는 `flatpak update`가 새 버전을 가져옵니다. 애플리케이션 메뉴에 등록되고 `.igz`, `.skp`, `.dae`가 연결됩니다(Freedesktop 런타임은 Flathub에서 자동으로 받아 옵니다):

    ```bash
    flatpak remote-add --user --if-not-exists ingetrazo https://ingetrazo.com/ingetrazo.flatpakrepo
    flatpak install --user ingetrazo com.ingetrazo.IngeTrazo
    flatpak run com.ingetrazo.IngeTrazo
    ```

    릴리스에는 더블 클릭으로 설치하는 단일 파일 `IngeTrazo-X.Y.Z-x86_64.flatpak`도 있습니다 — 하지만 번들은 **새 버전을 찾아올 곳이 없어서** 설치한 버전에 머뭅니다.

=== "AppImage"

    `IngeTrazo-X.Y.Z-x86_64.AppImage`를 내려받아 실행 권한을 주고 엽니다(파일 관리자에서 더블 클릭해도 됩니다):

    ```bash
    chmod +x IngeTrazo-*-x86_64.AppImage && ./IngeTrazo-*-x86_64.AppImage
    ```

    FUSE가 필요한데, 거의 모든 배포판에 들어 있습니다.

=== "tar.gz"

    배포판에 FUSE가 없다면 압축을 풀고 실행하세요 — `/opt`에 두는 용도로도 똑같이 쓸 수 있습니다:

    ```bash
    tar -xzf IngeTrazo-*-linux-x86_64.tar.gz && IngeTrazo-*/ingetrazo
    ```

=== "Snap"

    `ingetrazo_X.Y.Z_amd64.snap`이 각 릴리스에 첨부되어 있습니다: `sudo snap install --dangerous ingetrazo_*.snap` (Snap Store 등록은 진행 중입니다).

=== "소스 코드"

    ```bash
    git clone https://github.com/ingelibre/ingetrazo.git
    cd ingetrazo/app
    python3 -m venv venv && venv/bin/pip install -r requirements.txt
    venv/bin/python main.py
    ```

    메뉴 아이콘과 파일 연결은 `scripts/install_desktop.sh`로 합니다. 업데이트는 `git pull`입니다.

패키지에는 Python, Qt, `.skp` 리더, DWG 변환기까지 모두 들어 있습니다. Ubuntu 22.04 이상에서 실행됩니다. 무언가 실패하면 `ingetrazo --check`가 무엇이 빠졌는지 알려 줍니다.

## macOS

IngeTrazo는 macOS에서도 Linux와 같은 단계로 소스 코드에서 실행됩니다. 아직 공식 `.dmg` 패키지는 없습니다.

## 업데이트

- **Windows**: 새 버전을 그 위에 설치하세요. 환경 설정과 파일 연결이 유지됩니다.
- **Linux**: 저장소로 설치했다면 `flatpak update`, AppImage나 tar.gz라면 새 파일을 내려받고, 소스 코드라면 `git pull`.

모델은 디스크에 있는 일반 `.igz` 파일입니다 — 프로그램을 업데이트해도 절대 건드리지 않습니다. 더 새로운 버전으로 저장한 문서도 이전 버전에서 **똑같이 열립니다**(이전 버전이 모르는 부분은 무시합니다). 다만 새 시트는 그것을 만든 버전에서만 온전히 보입니다.

## 이제 열어 볼 차례

[예제](ejemplos.md) — 시트까지 갖춘 실제 문서 네 개 — 가 프로그램이 무엇을 할 수 있는지 가장 빨리 확인하는 방법입니다.
