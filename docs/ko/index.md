---
source_blob: 845633de4cd292d33bdd63fa2009475a3bc2e3b5
---

# IngeTrazo 사용 설명서

**IngeTrazo** 사용 설명서에 오신 것을 환영합니다. IngeTrazo는 토목 공학과 건축을 위한 무료 3D 모델러입니다. 손으로 그리듯 그리고, BIM 레이블을 붙이고, 프로젝트를 실제 지형 위에 배치하고, 도면을 PDF로 뽑아냅니다 — 이 모든 것을 하나의 프로그램에서, 오프라인으로, 오픈 소스로.

!!! tip "IngeTrazo가 처음이신가요?"
    **[설치](primeros-pasos/instalacion.md)**부터 시작해 **[첫 모델 만들기](primeros-pasos/primer-modelo.md)**로 넘어가세요. 15분이면 정확한 치수로 작은 집 한 채를 세울 수 있습니다.

## 이 설명서에서 다루는 내용

<div class="grid cards" markdown>

-   :material-rocket-launch: **시작하기**

    ---

    Windows나 Linux에 프로그램을 설치하고, 인터페이스를 익히고, 실제 치수로 첫 모델을 세웁니다.

    [:octicons-arrow-right-24: 시작하기](primeros-pasos/instalacion.md)

-   :material-pencil-ruler: **모델링**

    ---

    그리기와 편집 도구: 밀기/끌기, 따라가기, 스케일, 그룹과 컴포넌트, 재질, 레이어, 장면, 단면, 스타일과 그림자.

    [:octicons-arrow-right-24: 모델링하기](modelado/dibujo.md)

-   :material-tag-outline: **BIM과 물량 산출**

    ---

    벽, 슬래브, 기둥에 레이블을 붙이고, 물량을 실시간으로 확인하고, 견적용으로 IFC 4를 내보냅니다.

    [:octicons-arrow-right-24: 레이블 붙이기](bim.md)

-   :material-terrain: **지형**

    ---

    위성 지도, 3D 지형, 드론 측량, 토털 스테이션 측량점 — 모두 UTM WGS84로.

    [:octicons-arrow-right-24: 지리 참조하기](terreno/ubicacion.md)

-   :material-file-document-outline: **시트 구성**

    ---

    모델에서 도면으로: 정확한 축척과 정확한 숨은선 처리를 한 뷰, 모델에 고정된 치수, 레벨, 연속 치수, 상세 표시, 템플릿 표제란, 벡터 PDF.

    [:octicons-arrow-right-24: 구성하기](laminas/index.md)

-   :material-swap-horizontal: **가져오기와 내보내기**

    ---

    `.skp`(모든 버전, 변환기 없이), DXF, DWG를 열고, IFC, STL, OBJ, glTF, DXF로 내보냅니다.

    [:octicons-arrow-right-24: 주고받기](importar-exportar.md)

-   :material-robot-outline: **AI로 모델링하기**

    ---

    앱 안의 AI 도우미, 또는 MCP로 IngeTrazo를 조종하는 Claude: 설명하고 사진을 첨부하면, AI가 레시피를 쓰고 엔진이 그것을 실행합니다.

    [:octicons-arrow-right-24: AI로 모델링하기](ia.md)

-   :material-folder-open-outline: **열어 볼 예제**

    ---

    양케(Yanque) 광장의 실제 문서 네 개. 그중 세 개는 A3 시트와 PDF가 함께 있습니다. 프로그램이 무엇을 할 수 있는지 가장 빨리 확인하는 방법입니다.

    [:octicons-arrow-right-24: 예제 열기](primeros-pasos/ejemplos.md)

</div>

## IngeTrazo의 기본 생각

이름이 곧 핵심입니다: **현실에서처럼 그린다**(*trazar*). 선과 사각형을 그리고, 면을 밀면 솔리드가 됩니다 — 아이디어와 모델 사이에 경직된 패밀리도, CAD의 복잡한 층도 없습니다. 의미 정보가 필요하면 그 *위에* 덧붙입니다: 형상에 벽이나 기둥 레이블을 붙이면 프로그램이 물량과 IFC를 내줍니다.

IngeTrazo가 자매 프로그램 [IngePresupuestos](https://ingepresupuestos.com)와 함께 다루는 전체 흐름:

```
지형 (드론, GPS, 위성) → 위에 그리기 → BIM 레이블 → IFC → 견적
                                 ↓
                         시트 → PDF (도면)
```

## 도움과 커뮤니티

- 프로젝트는 [GitHub](https://github.com/ingelibre/ingetrazo)에 있습니다. 무언가 동작하지 않으면 예제 파일을 첨부해 *issue*를 열어 주세요.
- 직접 연락: [ing.sumari@gmail.com](mailto:ing.sumari@gmail.com).
