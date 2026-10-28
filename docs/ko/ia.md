---
source_blob: e01c1d9807f15ad9c5a84655d7ee1832e0753322
---

# AI로 모델링하기

IngeTrazo에서 인공지능이 대신 모델링하게 하는 방법은 두 가지입니다. 두 방법 모두 AI는 **메시를 직접 건드리지 않습니다**: AI가 *레시피* —회전체, 돌출, 액션 API 위의 Python— 를 쓰면 IngeTrazo의 결정적 엔진이 그것을 실행합니다. 그래서 평소와 같은 보장이 그대로 적용됩니다:

- **AI의 작업 하나가 실행 취소 한 단계입니다.** `Ctrl+Z`로 통째로 없앱니다.
- **코드가 실패하면 문서가 저절로** 이전 상태로 돌아갑니다 — 절대 반쯤 남지 않습니다.
- 모든 레시피는 **밀폐성 검사**를 거칩니다: 만들어지는 솔리드는 측정하고 프린트할 수 있는 진짜 솔리드입니다.
- 만들어지는 것은 평범한 형상입니다: 이름 있는 그룹이라 손으로 편집하고, 칠하고, 치수를 넣고, 시트로 가져갈 수 있습니다.

| | AI 도우미 (앱 안) | MCP 브리지 (외부 에이전트에서) |
|---|---|---|
| 위치 | **확장 기능 ▸ AI 도우미** (`Ctrl+Shift+A`) | **확장 기능 ▸ AI 브리지 (MCP)** + 아무 MCP 클라이언트: Claude Code, Claude Desktop, Cursor, VS Code, Antigravity CLI(Google), Codex CLI… |
| 필요한 것 | 원하는 제공자의 API 키(Groq는 무료 할당량 있음) 또는 로컬 Ollama | 설치된 MCP 클라이언트(자체 계정이나 키 포함) |
| 대화 방식 | IngeTrazo 안에서 채팅, 사진 첨부 가능 | 에이전트에서 대화하면, 에이전트가 열린 앱에 그립니다 |
| 모델을 보는 주체 | 도우미가 뷰포트 캡처를 받음(선택) | 에이전트가 원할 때 캡처를 요청하고 모델을 조회 |

## AI 도우미, 단계별로

![태양광 가로등 위에 열린 AI 도우미: 제공자, 키, 캡처 체크박스, 텍스트 상자에 쓴 요청.](images/asistente-ia.jpeg)

1. **확장 기능 ▸ AI 도우미**(또는 `Ctrl+Shift+A`). 모델 위에 떠 있는 대화 상자가 열립니다.
2. **제공자.** 하나를 고르거나 *자동*으로 둡니다: 키의 접두사로 저절로 알아냅니다(`sk-ant-`는 Anthropic, `gsk_`는 Groq, `AIza`는 Gemini…). 제공자마다 **자기 키와 모델을 기억합니다**: 한 곳의 할당량이 떨어지면 두 번 클릭으로 다른 곳으로 바꿉니다.

    | 제공자 | 키 | 이미지 인식 | 메모 |
    |---|---|:-:|---|
    | **Groq** | [console.groq.com/keys](https://console.groq.com/keys) | — | 무료 할당량이 넉넉하고 매우 빠름. 기본 모델 `openai/gpt-oss-120b`. |
    | **Google Gemini** | [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) | ✔ | 무료 할당량. 기본 `gemini-2.5-flash`. |
    | **Anthropic (Claude)** | console.anthropic.com | ✔ | 유료. |
    | **OpenAI** | platform.openai.com | ✔ | 유료. 기본 `gpt-4o`. |
    | **OpenRouter** | openrouter.ai | ✔ | 여러 모델을 한곳에서. |
    | **DeepSeek** | platform.deepseek.com | — | 저렴. |
    | **Ollama** | *(키 없음)* | 모델에 따라 | **내 컴퓨터에서, 인터넷 없이.** Ollama를 설치하고 키는 비워 둡니다. 기본 URL은 `http://localhost:11434`. |

3. **API 키.** 입력란에 붙여 넣습니다. 키는 사용자 프로필에 저장되며 문서에는 절대 저장되지 않습니다. 입력란 아래 링크가 키를 받는 페이지로 데려갑니다. **키가 없으면 응답도 없습니다**(Groq는 무료지만 키가 필요): 비워 두거나 제공자가 거부하면, 도우미가 날것의 401 오류 대신 키를 받는 링크와 함께 분명하게 알려 줍니다.
4. **모델.** 비우면 제공자의 기본 모델. **모델 목록**은 내 키로 실제로 쓸 수 있는 모델을 보여 주고, **연결 테스트**는 시작하기 전에 키를 검증합니다.
5. **뷰포트 캡처를 모델에 보내기.** 이미지를 *보는* 제공자(Claude, GPT, Gemini)라면, 도우미가 단계마다 만든 결과의 이미지를 받아 보고 스스로 고칩니다. 시각 기능이 없는 모델이라도 체크박스는 해가 없습니다: 이미지를 보내지 않을 뿐입니다.
6. **요청을 쓰고 Enter.** 치수와 함께: *«지름 4 m, 높이 0.6 m, 테두리 20 cm인 원형 분수를 그려 줘»*. 도우미가 답하고, 실행할 레시피를 보여 주고, 결과가 모델에 나타납니다. 대화를 이어 가며 고치세요: *«20 cm 더 높게»*, *«석재로 칠해 줘»*.
7. **사진…**으로 이미지(실물 사진, 스케치, 도면 캡처)를 첨부하면 모델이 **보이는 것을 재구성합니다**. 같은 메시지에 실제 치수를 함께 주세요 — 사진은 모양을, 치수는 여러분이 알려 줍니다.

!!! tip "잘 나오게 요청하는 법"
    - **메시지 하나에 부재 하나**, 치수와 함께: «높이 4.5 m 기둥, 3" 파이프»가 «공원 전체»보다 잘 됩니다.
    - **반복하지 말고 고치세요**: 도우미는 맥락과 만든 그룹을 기억합니다. «팔이 너무 길어, 60 cm로 해 줘»는 있는 것을 편집합니다.
    - 응답이 잘리면 도우미가 감지해 **스스로 이어서 요청합니다**. 단계 한도를 넘으면 알려 주며, «계속»이라고 하면 멈춘 곳부터 이어 갑니다.
    - 모델 창이 활성인 상태에서 **Ctrl+Z**는 마지막 레시피 전체를 되돌립니다.

!!! note "무엇이 어디에 저장되나"
    키와 제공자는 사용자 환경 설정에 저장됩니다(**창 ▸ 환경 설정 ▸ AI 도우미**에서도 편집 가능). `.igz` 문서에는 결과 형상만 저장됩니다: 키를 노출하지 않고 공유할 수 있습니다.

## MCP 브리지, 단계별로

![Ubuntu 데스크톱 전체: 왼쪽 터미널의 Claude Code가 브리지로 방금 그린 의자 네 개 딸린 식탁의 치수를 나열하고, 오른쪽 IngeTrazo가 모델과 연결 명령이 적힌 AI 브리지 (MCP) 대화 상자를 보여 줍니다.](images/mcp-claude.jpeg)

[Model Context Protocol](https://modelcontextprotocol.io)은 Claude 전용이 아닌 **개방형 표준**입니다: MCP를 쓰는 에이전트라면 —Claude Code, Claude Desktop, Cursor, Copilot이 있는 VS Code, Windsurf, Google의 Antigravity CLI, Codex CLI…— 누구든 **앱이 열린 상태에서 실시간으로** IngeTrazo를 조작할 수 있습니다: 그리고, 조회하고, 모델을 보며, 그 작업 하나하나가 실행 취소 한 단계입니다. IngeTrazo는 모델을 고르지도, 비용을 내지도 않습니다: 그건 클라이언트가 정합니다.

1. **브리지 켜기**: **확장 기능 ▸ AI 브리지 (MCP)**. IngeTrazo가 로컬 서버(`127.0.0.1` 전용, 포트 4763)를 띄우고, 내 시스템에 맞는 정확한 명령 줄과 **복사** 버튼이 있는 창을 엽니다. 같은 메뉴로 끕니다.
2. **클라이언트 연결** — 한 번만:

    === "Claude Code (터미널)"

        ```bash
        # Windows (설치 프로그램 또는 zip)
        claude mcp add ingetrazo -- "C:\Program Files\IngeTrazo\ingetrazo-mcp.exe"
        # Linux: AppImage, tar.gz, Flatpak 또는 snap
        claude mcp add ingetrazo -- <IngeTrazo 실행 파일> --mcp
        # 소스 코드에서
        claude mcp add ingetrazo -- python3 /경로/app/scripts/ingetrazo_mcp.py
        ```

        Python을 설치할 필요가 없습니다: 패키지에 MCP 서버가 들어 있습니다(Windows는 `ingetrazo-mcp.exe`, Linux는 `ingetrazo --mcp`).

    === "Claude Desktop"

        설정 파일(Windows는 `%APPDATA%\Claude\claude_desktop_config.json`, Linux는 `~/.config/Claude/claude_desktop_config.json`)에 다음을 붙여 넣고 Claude Desktop을 다시 시작합니다:

        ```json
        {
          "mcpServers": {
            "ingetrazo": {
              "command": "C:\\Program Files\\IngeTrazo\\ingetrazo-mcp.exe",
              "args": []
            }
          }
        }
        ```

    === "기타 MCP 클라이언트"

        모두 위의 **같은** `mcpServers` 블록(또는 그에 해당하는 것)을 각자의 파일에서 받습니다:

        | 클라이언트 | 붙여 넣을 곳 |
        |---|---|
        | Cursor | `~/.cursor/mcp.json` (또는 Settings ▸ MCP ▸ *Add new server*) |
        | VS Code (Copilot) | 프로젝트의 `.vscode/mcp.json`, `mcpServers` 대신 `servers` 키 사용 |
        | Windsurf | `~/.codeium/windsurf/mcp_config.json` |
        | Antigravity CLI (Google) | `~/.gemini/config/mcp_config.json` (또는 프로젝트 폴더의 `.agents/mcp_config.json`). Gemini CLI의 후속 제품입니다: Google은 2026-06-18에 Google 계정으로 Gemini CLI를 무료로 쓰는 길을 닫았고, 그 계정으로는 더 이상 들어갈 수 없습니다. Antigravity에는 주간 한도가 있는 **무료 Individual 플랜**이 있습니다. `curl -fsSL https://antigravity.google/cli/install.sh \| bash`로 설치하고 명령은 `agy`입니다. |
        | Codex CLI | `~/.codex/config.toml`의 `[mcp_servers.ingetrazo]` 섹션, `command`와 `args` |

        모두 `command`는 `--mcp`를 붙인 IngeTrazo 실행 파일(Windows에서는 `ingetrazo-mcp.exe`)이며, 브리지 창에 표시된 그대로입니다.

3. IngeTrazo를 열고 브리지를 켠 채로 **요청하세요**: *«1.60 × 0.90 식탁과 나무 의자 네 개를 디자인해 줘»*, *«시트 E02의 아치를 철근까지 모두 그려 줘»*, *«어떻게 됐는지 보여 줘»*. 에이전트가 레시피를 쓰고, 실행하고, 캡처로 스스로 검토한 뒤, 한 일을 알려 줍니다. 여러분은 앱에서 결과를 실시간으로 보며 동료에게 하듯 고칩니다: *«의자들이 너무 붙어 있어»*.

에이전트가 할 수 있는 일:

| 도구 | 하는 일 |
|---|---|
| `run_python` | 열린 문서 위에서 Python을 실행합니다. `scene`, `selection`, `groups`, `QVector3D`… 그리고 생성자 `revolve(프로파일)`과 `extrude(윤곽, z0, z1)`: 한 줄 → 매끄럽고 방향이 맞는 솔리드 그룹 하나. 호출당 실행 취소 하나이며, 실패하면 아무것도 바뀌지 않습니다. |
| `query_model` | 개수, 그룹과 컴포넌트 이름, 재질, 레이어, 경계 상자. |
| `screenshot` | 실제 뷰포트를 렌더링합니다: 에이전트가 보고 반복합니다. |
| `undo` / `redo` | 평소의 기록. |

!!! tip "에이전트가 응답하지 않으면"
    IngeTrazo가 **브리지가 켜진 채로** 열려 있는지(확장 기능 메뉴에 *listening*으로 표시), 명령의 경로가 존재하는지, 그리고 클라이언트에서 `ingetrazo` 서버가 오류 없이 연결되어 있는지(Claude Desktop: Settings ▸ Developer ▸ MCP) 확인하세요. 서버는 한 번에 클라이언트 하나만 받으며, 내 컴퓨터 밖에서는 절대 수신하지 않습니다.

## 이렇게 만든 것들

IngeTrazo에 함께 들어 있는 [예제](primeros-pasos/ejemplos.md)는 상당 부분 MCP 브리지로 그렸습니다: 태양광 가로등(기둥, 원뿔대 받침, 기초와 철근), 철근·가로등·글자·조각까지 갖춘 양케 환영 아치, 기초가 있는 농부상 받침대. 열어서 그룹을 보세요: 블랙박스가 아니라 실행된 레시피입니다.

!!! info "다른 모델러는 이것을 구독으로 팝니다"
    IngeTrazo에서 AI는 자유입니다: 원하는 키(또는 로컬 모델)를 쓰고, 아무것도 IngeTrazo 서버를 거치지 않습니다. AI 없이도 프로그램은 똑같이, 인터넷 없이 동작합니다.
