---
source_blob: 7e8cbd95eb7c5e9c2452f19b3139010183f90a58
---

# 열어 볼 예제

Marco Sumari 엔지니어가 양케(Yanque) 광장 리모델링(치차스(Chichas) 지구, 아레키파, 2026)을 위해 IngeTrazo로 그린 실제 문서 네 개입니다. 네 개 모두 **완성된 A3 시트**가 들어 있고, 비교할 수 있도록 그 시트에서 뽑은 PDF가 옆에 있습니다.

**내려받기:** 각 릴리스의 [`IngeTrazo-ejemplos.zip`](https://github.com/ingelibre/ingetrazo/releases/latest/download/IngeTrazo-ejemplos.zip)에 모두 들어 있고, 저장소의 [`examples/`](https://github.com/ingelibre/ingetrazo/tree/main/examples) 폴더(그리고 [ingetrazo.com](https://ingetrazo.com/#ejemplos)의 *예제* 섹션)에서 하나씩 받을 수도 있습니다. IngeTrazo 0.3.15 이상이 필요합니다.

| 파일 | 무엇인가 | 무엇을 보여 주나 |
|---|---|---|
| `pileta-fuente-yanque.igz` (+ `.pdf`) | 광장 중앙의 분수: 팔각 받침대, 홈이 파인 기둥, 물결 테두리의 접시 두 개, 둥근 모서리의 보도 | 반복 컴포넌트(인스턴스 22개), **실제 태양 위치의 그림자**, 단면 평면. 1:40 정면·3D·평면·단면, 참조 사진, 표제란이 있는 시트 |
| `banca-pergola-yanque.igz` (+ `.pdf`) | 목재 퍼걸러가 있는 콘크리트 벤치 | 컴포넌트, 저장된 **장면** 다섯 개. 뷰 네 개, **치수 23개**, 지시선 레이블 12개가 있는 시트 |
| `luminaria-solar-yanque.igz` (+ `.pdf`) | 4.5 m 태양광 가로등: 원뿔대 받침, 3/8" 철근이 든 매립 기초, 패널이 달린 투광등 두 개 | [AI](../ia.md) 레시피로 모델링, 철근 상세, 뷰 네 개와 받침 상세가 있는 시트 |
| `arco-yanque.igz` (+ `.pdf`) | 구조 도면 E02를 따른 「YANQUE」 환영 아치: 콘크리트, **모든 철근**(기초, 기둥, 분절 아치, 보, 팀파눔), 시야르(sillar) 석재 주두, 장식 가로등 네 개, 글자와 조각 | 철근을 보는 **X-ray**, 단면 평면, 「정면 고정」 이미지, 텍스처. 1:50 정면·측면·평면·3D, 글자와 조각 상세(1:25), 주두 상세(1:20), **레벨**, **지반선**, 지시선 레이블이 있는 시트 D04 |

## 각 예제에서 볼 것

- **문서를 엽니다**(파일 ▸ 열기, 또는 `.igz`를 더블 클릭). 장면 패널의 **장면**을 더블 클릭해 둘러보세요: 장면마다 카메라, 레이어, 활성 단면이 저장되어 있습니다.
- **시트**: 상태 표시줄의 *시트 1* 탭(또는 파일 ▸ 시트 레이아웃). 프레임을 선택해 그 패널을 보세요: 축척, 스타일, 제목. 프레임을 더블 클릭하면 그 안에서 궤도 회전합니다. **PDF 내보내기…**를 하고 옆에 있는 PDF와 비교해 보세요.
- **아치와 가로등의 철근**: 카메라 ▸ 스타일 ▸ **X-ray**, 또는 문서의 단면 평면을 켜고(카메라 ▸ 단면 절단) 이동 도구로 움직여 보세요.
- **그룹**: 모든 것에 이름이 있습니다(«Acero columna C1 izq 10 Ø5/8"», «Farola ornamental blanca der adelante»…). 더블 클릭하면 편집으로 들어가고, `Esc`로 나옵니다.

!!! note "라이선스"
    문서(모델, 시트, PDF)는 Marco Sumari Tellez 엔지니어의 것이며 [크리에이티브 커먼즈 저작자표시 4.0](https://creativecommons.org/licenses/by/4.0/deed.ko)으로 공개됩니다: 출처를 밝히면 사용, 수정, 공유할 수 있습니다. IngeTrazo 코드는 여전히 GPL-3.0입니다.
