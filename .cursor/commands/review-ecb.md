# Review ECB — 코드 수정 금지 · 위반만 표로 리포트

MagicSquare_xx · **읽기 전용** ECB·계약 리뷰 Command.

- **코드·테스트 파일 수정 금지** (제안만, 패치·apply 금지)
- **SSOT:** `.cursorrules`, `docs/PRD.md`

---

## 필수 선언

응답 **첫 줄**:

```
Phase: REVIEW | Scope: ECB·계약 | Mode: read-only
```

---

## 절차

1. **범위 확인** — `src/entity`, `src/control`, `src/boundary`, `tests/entity`, `tests/control`, `tests/boundary` (사용자가 지정한 경로 우선).
2. **5개 체크리스트** 순서대로 정적 분석 (grep·import·리터럴·Mock 패턴).
3. **위반만** 아래 표 형식으로 출력. **위반 0건**이면 `위반 없음` 한 줄 + 체크 통과 요약.
4. **수정 코드 제안 금지** — 위치·규칙·심각도만 기록.

---

## 체크리스트 (리뷰 기준)

| # | 항목 | 통과 조건 |
|---|------|-----------|
| 1 | **import 방향** | `boundary→control→entity`만. entity↛control/boundary, control↛boundary, boundary↛entity(직접) |
| 2 | **entity · E001~E005** | entity에 E001~E005 문자열·raise·catch·처리 로직 없음 — 도메인 불변식만 |
| 3 | **int[6] · 1-index** | 출력 `[r1,c1,n1,r2,c2,n2]` 좌표 1-index; 0-index는 entity/control 내부만, boundary formatter에서 변환 |
| 4 | **MagicConstant SSOT** | `34`·`16`·격자 `4`·빈칸 `2` 리터럴이 `entity/constants`(또는 MagicConstant) 외 **산재 금지** |
| 5 | **Logic Track · Domain Mock** | `tests/entity`, `tests/control`에서 Grid/MagicConstant/Validator/Finder/Solver 등 **patch·MagicMock 금지** |

---

## 위반 리포트 표 (필수 형식)

위반이 **1건이라도** 있으면 행을 추가한다. 없으면 표 생략.

| 우선순위 | 체크 | 파일:줄 | 위반 내용 | 규칙 |
|----------|------|---------|-----------|------|
| P0 / P1 / P2 | import / E001~E005 / 1-index / SSOT / Domain Mock | `path/to/file.py:42` | 한 줄 설명 | `.cursorrules` §… |

**우선순위 가이드**

| 등급 | 예 |
|------|-----|
| **P0** | 역방향 import, entity가 E001~E005 처리, Logic Track Domain Mock |
| **P1** | boundary 출력 0-index, `34`/`16` 하드코딩 |
| **P2** | constants 외 매직 넘버, 테스트에서 boundary import |

---

## 분석 힌트 (Agent용 · 실행은 선택)

```bash
# import 방향 (수동 확인)
rg "^from (boundary|control|entity)|^import (boundary|control|entity)" src/

# E001~E005 in entity
rg "E00[1-5]" src/entity/

# 하드코딩 리터럴 (constants 제외)
rg "\b34\b|\b16\b" src/ tests/ --glob "!**/constants*"

# Logic Track Mock
rg "patch|MagicMock|Mock" tests/entity tests/control
```

---

## 보고 (마무리)

| # | 항목 |
|---|------|
| 1 | 검사 범위 (디렉터리·파일 수) |
| 2 | **위반 건수** (P0 / P1 / P2) |
| 3 | 위반 표 (또는 `위반 없음`) |
| 4 | 다음 조치 **한 줄** (예: "P0 2건 — GREEN 전 import 수정") — **코드 diff 없음** |

---

## 금지

| 금지 | 이유 |
|------|------|
| **파일 수정·생성·삭제** | read-only Review |
| **위반 없는데 리팩터 제안** | 범위 초과 |
| **표 없이 장문 설명만** | Command 출력 형식 |
| **git commit / push** | 사용자 명시 요청 시만 |
