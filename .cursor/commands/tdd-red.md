# TDD RED — 실패 테스트 먼저

MagicSquare_xx · Dual-Track TDD · **RED 단계만** 수행한다.  
GREEN / REFACTOR / `src/` 구현은 **이 Command 범위 밖**.

**SSOT:** `.cursorrules`, `docs/PRD.md`  
**Logic Test ID:** `.cursor/skills/magic-square-tdd/reference.md` (D-*)

---

## 필수 선언

응답 **첫 줄**에 반드시 아래 형식으로 선언한다.

```
Phase: RED | Layer: entity|control|boundary | Track: Logic|UI | TestID: D-xx|U-xx
```

| Track | Layer | 테스트 경로 | 파일명 | Test ID |
|-------|-------|------------|--------|---------|
| Logic | entity | `tests/entity/` | `test_d_*.py` | **D-*** |
| Logic | control | `tests/control/` | `test_d_*.py` | **D-*** |
| UI | boundary | `tests/boundary/` | `test_u_*.py` | **U-*** |

---

## 절차

1. **ID 확인** — TestID(D-* / U-*)와 Rule(R-xx), Invariant(INV-xx)를 확정한다. Logic은 `reference.md` D-01~D-10 참조. UI는 U-*를 새로 부여(예: U-01=E001).
2. **범위 고정** — 한 턴 · **한 테스트 파일(또는 한 test 함수 묶음)** · **Track 하나**만.
3. **AAA 테스트 작성** — `tests/` 아래만 수정.
   - **Arrange:** 4×4 격자 fixture, 빈칸 0×2, 1~16 (도메인 계약)
   - **Act:** 테스트 대상 import·호출 (아직 없으면 import 실패가 아닌 **assert 실패**가 목표)
   - **Assert:** 기대 결과 **명시** (docstring에 TestID, R-xx, INV-xx)
4. **pytest 실행** — Track별 명령으로 실행한다.
5. **FAIL 확인** — **FAILED** + **의도한 assert/예외 메시지**. `ImportError`/`ModuleNotFoundError`만으로 RED 완료 **인정 금지**.
6. **보고** — 아래 [보고](#보고) 형식으로 마무리.

---

## pytest 예시 (bash)

프로젝트 루트에서 실행:

```bash
# Logic Track — entity
pytest tests/entity/test_d_<name>.py -v

# Logic Track — control
pytest tests/control/test_d_<name>.py -v

# Logic Track — entity + control
pytest tests/entity tests/control -v

# UI Track — boundary
pytest tests/boundary/test_u_<name>.py -v
```

**RED 성공 기준:** 해당 테스트 **FAILED** (의도한 이유). **PASSED면 RED 실패** — assert·기대값을 재검토.

---

## 보고

RED 완료 시 **한국어**로 아래를 포함한다.

| # | 항목 |
|---|------|
| 1 | **TestID** (D-* / U-*) |
| 2 | **FAIL 요약** — 실패 테스트 함수명 + assert/예외 메시지 한 줄 |
| 3 | **변경 파일** — `tests/` 아래 경로만 (예: `tests/entity/test_d_grid_size.py`) |
| 4 | **다음 GREEN** — 구현할 Layer·함수/클래스 한 줄 |

---

## 금지

| 금지 | 이유 |
|------|------|
| **`src/` 수정·생성** | RED는 테스트만 |
| **Logic Track Domain Mock** — Grid, MagicConstant, Validator, Finder, Solver `patch`/`MagicMock` | Dual-Track Logic 무결성 |
| **assert 완화·삭제**, `@pytest.mark.skip`, `xfail` | 가짜 GREEN |
| **ImportError만 나는 RED** | 구현 없음을 RED로 대체 불가 |
| **Logic 테스트에서 `src/boundary` import** | Track 경계 위반 |
| **UI 테스트에서 entity/control Mock** | boundary는 I/O·CLI만 Mock |
| **한 턴에 RED + GREEN 동시** | Phase 분리 |

---

**다음 Command:** GREEN은 별도 Command(`tdd-green.md`, 미작성) 또는 사용자 지시 시 진행.
