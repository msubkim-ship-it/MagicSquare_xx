---
name: magic-square-tdd
description: MagicSquare_xx Dual-Track TDD·ECB 개발 시 Agent가 따를 절차
---

# MagicSquare Dual-Track TDD Skill

MagicSquare_xx — 4×4 부분 마방진, ECB, Dual-Track TDD 구현·테스트 시 이 Skill을 따른다.

**헌법(SSOT):** `.cursorrules`, `docs/PRD.md`  
**Logic 테스트 ID 목록:** [reference.md](reference.md)

---

## 언제 이 Skill을 켜는가

다음 **하나라도** 해당하면 즉시 이 Skill을 읽고 적용한다.

| 트리거 | 예 |
|--------|-----|
| TDD 사이클 | RED / GREEN / REFACTOR 언급·요청 |
| 레이어 작업 | `src/entity`, `src/control`, `src/boundary` 또는 `tests/*` 작성·수정 |
| Dual-Track | Logic Track / UI Track, `test_d_*` / `test_u_*` |
| 도메인 | 4×4, 빈칸 0×2, 10선, MagicConstant, `int[6]` 출력 |
| 오류 | E001~E007, boundary 검증, 입력 계약 |

**끄는 조건:** 문서만(Mom Test, PRD) 다루거나 git commit/push만 요청할 때 — TDD 절차 생략 가능.

---

## Logic Track vs UI Track

| 항목 | Logic Track | UI Track |
|------|-------------|----------|
| **Layer** | entity, control | boundary |
| **소스** | `src/entity/`, `src/control/` | `src/boundary/` |
| **테스트** | `tests/entity/`, `tests/control/` | `tests/boundary/` |
| **파일명** | `test_d_*.py` | `test_u_*.py` |
| **Test ID** | **D-*** | **U-*** |
| **Mock** | **Domain Mock 금지** | **I/O·CLI Mock 허용** |
| **import** | `src/boundary` import **금지** | `src/entity`·`src/control` Mock **금지** |
| **오류** | 도메인 예외만 (E코드 **금지**) | E001~E007 발생·변환 |

---

## ECB · Mock · E001~E007

### Import (허용 / 금지)

```
boundary → control → entity   (단방향)
```

| | 허용 | 금지 |
|---|------|------|
| entity | — | boundary, control import |
| control | entity | boundary import |
| boundary | control | entity **직접** import (control 경유) |

### Mock (허용 / 금지)

| 대상 | Logic Track | UI Track |
|------|-------------|----------|
| Grid, MagicConstant, Validator, Finder, Solver | **Mock/patch 금지** | **Mock 금지** |
| stdin/stdout, CLI, 파일 I/O, formatter 외부 | 해당 없음 | **Mock 허용** |
| control을 boundary 테스트에서 Mock | — | **금지** (실제 control 호출) |

### E001~E007 (boundary 전용)

| 코드 | 조건 | entity | control | boundary |
|------|------|--------|---------|----------|
| E001 | 격자 ≠ 4×4 | 처리 금지 | 도메인 예외 가능 | **raise/변환** |
| E002 | 빈칸 ≠ 2 | 처리 금지 | 도메인 예외 가능 | **raise/변환** |
| E003 | 범위 위반 | 처리 금지 | 도메인 예외 가능 | **raise/변환** |
| E004 | 중복 | 처리 금지 | 도메인 예외 가능 | **raise/변환** |
| E005 | 타입·형식 | 처리 금지 | — | **raise/변환** |
| E006 | 해 없음 | — | 도메인 예외 | **E006 변환** |
| E007 | 출력 계약 | — | — | **formatter 검증** |

**판정 순서 (R-06):** E001~E005(입력) → 10선/도메인 → 풀이 → 출력(E007)

---

## Phase: RED (5~7단계)

1. **선언** — `Phase: RED` / `Layer` / `Track` / `TestID: D-* 또는 U-*` 출력.
2. **범위 고정** — 한 턴·한 테스트 묶음·한 파일(또는 한 describe)만.
3. **ID·Rule 매핑** — docstring에 TestID, Rule(R-xx), Invariant(INV-xx) 기록. Logic은 [reference.md](reference.md) 참조.
4. **실패 테스트 작성** — `test_d_*.py` 또는 `test_u_*.py`에 **assert 필수**. 구현 코드 **작성 금지**.
5. **실행** — Track별 pytest (아래 Test/Review Loop).
6. **RED 확인** — **FAILED** + **의도한 assert 메시지**. ImportError만으로 RED 인정 **금지**.
7. **보고** — 실패 테스트명, 기대 실패 이유, 다음 GREEN 대상 함수/클래스.

---

## Phase: GREEN (5~7단계)

1. **선언** — `Phase: GREEN` / `Layer` / `Track` / 대응 TestID.
2. **최소 범위** — **현재 RED를 통과**시키는 코드만. RED 밖 기능·REFACTOR **금지**.
3. **레이어 준수** — entity → control → boundary 순 권장. 역방향 import **금지**.
4. **SSOT** — `34`·`16`·`4`·`2` 리터럴 산재 금지. `MagicConstant`·constants 모듈 사용.
5. **entity 규칙** — E001~E005 처리·raise·catch **금지**. 도메인 불변식만.
6. **실행** — 해당 Track pytest → **PASSED** 확인.
7. **보고** — 추가/변경 파일, 통과 테스트 목록, 남은 RED(있으면).

---

## Phase: REFACTOR (5~7단계)

1. **선언** — `Phase: REFACTOR` / `Layer` / `Track`.
2. **전제** — 해당 Track pytest **전부 GREEN** 상태에서만 시작.
3. **허용** — 이름·중복 제거·책임 분리·constants 정리. **동작 변경 금지**.
4. **금지** — assert 완화/삭제, skip, xfail, 테스트 삭제, `.cursorrules`/PRD 변경.
5. **실행** — **프로젝트 루트** `pytest` 전체 실행.
6. **종료 조건** — **전체 GREEN**. 실패 시 REFACTOR 중단 → GREEN 복구.
7. **보고** — 리팩터 요약, 전체 pytest 결과, 커버리지(선택).

---

## Test / Review Loop — pytest 실행 시점

```
RED    → Track pytest → FAILED (의도한 assert)
GREEN  → Track pytest → PASSED
REFACTOR → pytest (전체) → ALL PASSED
```

| 시점 | 명령 | 기대 |
|------|------|------|
| RED 직후 | Logic: `pytest tests/entity tests/control -v` | **FAILED** (의도) |
| RED 직후 | UI: `pytest tests/boundary -v` | **FAILED** (의도) |
| GREEN 직후 | 동일 Track `pytest … -v` | **PASSED** |
| REFACTOR 중·후 | `pytest -v` (루트) | **ALL PASSED** |
| 커밋 전(사용자 요청 시) | `pytest -v` | **ALL PASSED** |

**Review Loop 체크 (REFACTOR·완료 보고 시):**

- [ ] TestID ↔ Rule ↔ 파일명 일치
- [ ] Logic Track에 boundary import 없음
- [ ] UI Track에 entity/control Mock 없음
- [ ] MagicConstant SSOT 위반 없음 (`34`/`16` grep)
- [ ] skip / xfail / assert 삭제 없음

---

## 완료 보고 항목 (매 Phase 종료)

에이전트는 Phase 종료 시 **한국어**로 아래를 포함한다.

| # | 항목 |
|---|------|
| 1 | `Phase` / `Layer` / `Track` / `TestID` |
| 2 | 변경 파일 목록 |
| 3 | 실행한 pytest 명령 |
| 4 | 결과 (FAILED n / PASSED n) |
| 5 | Rule(R-xx) · Invariant(INV-xx) 충족 여부 |
| 6 | ECB / Mock / E코드 위반 여부 |
| 7 | 다음 Phase·Track·TestID (한 줄) |

**git commit / push:** 사용자 **명시 요청 시만**.

---

## 추가 참고

- U-* (UI Track) ID는 boundary RED 작성 시 `U-01`부터 순차 부여.
- Golden Master·snapshot 재생성: **사용자 승인 없이 금지**.
- Command 파일(`.cursor/commands/`)은 별도 — 이 Skill만으로 RED/GREEN/REFACTOR 수행.
