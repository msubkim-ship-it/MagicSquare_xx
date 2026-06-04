# MagicSquare_xx — RED 단계 TODO (Dual-Track)

**Phase:** RED only · `src/` 수정·GREEN·REFACTOR·skip/xfail 금지  
**SSOT:** `.cursorrules`, `docs/PRD.md`  
**Logic Test ID:** `.cursor/skills/magic-square-tdd/reference.md`

---

## 0. RED 공통 게이트

- [ ] 실패 유형 = **AssertionError** 또는 의도한 예외 (`ImportError`/`ModuleNotFoundError` 단독 RED 불인정)
- [ ] docstring에 TestID · Rule · Invariant 기록
- [ ] RED 턴에 `src/` 수정 없음
- [ ] `@pytest.mark.skip` / `xfail` 없음

| Track | pytest | Mock | E코드 |
|-------|--------|------|-------|
| Logic | `pytest tests/entity tests/control -v` | Domain Mock **금지** | entity E001~E005 **emit 금지** |
| Boundary (UI) | `pytest tests/boundary -v` | stdin/stdout·CLI **허용** | E001~E007 **raise/변환** |

**판정 순서 (R-06):** E001~E005(입력) → 10선/도메인 → 풀이 → 출력(E007)

---

## 1. Boundary Track — UI (`tests/boundary/test_u_*.py`)

> entity/control Mock 금지 · entity 직접 import 금지

### 1-A. 입력 검증 (U-IN-*)

| Test ID | Given | Then | E코드 |
|---------|-------|------|-------|
| U-IN-01 | `grid=None` | E003 / INVALID_NULL | E003 |
| U-IN-02 | `grid=3×4` (TL-01) | E001 / INVALID_SIZE | E001 |
| U-IN-03 | 빈칸 0개 | E002 / INVALID_BLANKS | E002 |
| U-IN-04 | 빈칸 1개 (TL-02) | E002 / INVALID_BLANKS | E002 |
| U-IN-05 | 값 17 포함 | E003 / INVALID_RANGE | E003 |
| U-IN-06 | 비제로 중복 (TL-03) | E004 / INVALID_DUPLICATE | E004 |
| U-IN-07 | 타입 오류 (`str` 격자 등) | E005 / INVALID_TYPE | E005 |

- [ ] **U-IN-01** — `tests/boundary/test_u_input.py`
- [ ] **U-IN-02** — `tests/boundary/test_u_input.py`
- [ ] **U-IN-03** — `tests/boundary/test_u_input.py`
- [ ] **U-IN-04** — `tests/boundary/test_u_input.py`
- [ ] **U-IN-05** — `tests/boundary/test_u_input.py`
- [ ] **U-IN-06** — `tests/boundary/test_u_input.py`
- [ ] **U-IN-07** — `tests/boundary/test_u_input.py`

### 1-B. 출력 계약 (U-OUT-*)

| Test ID | Given | Then |
|---------|-------|------|
| U-OUT-01 | 유효 **G1** → 풀이 성공 | `len(result)==6`, 1-index |
| U-OUT-02 | 출력 필드 순서 | `[r1,c1,n1,r2,c2,n2]` |

- [ ] **U-OUT-01** — `tests/boundary/test_u_output.py`
- [ ] **U-OUT-02** — `tests/boundary/test_u_output.py`

### 1-C. 흐름 (U-FLOW-*)

| Test ID | Given | Then |
|---------|-------|------|
| U-FLOW-01 | **G1** 유효 | control 호출 1회, E코드 없음 |
| U-FLOW-02 | `grid=None` | `execute()` **0회** |
| U-FLOW-03 | E001 격자 | Solver/Finder **미호출** |

- [ ] **U-FLOW-01** — `tests/boundary/test_u_flow.py`
- [ ] **U-FLOW-02** — `tests/boundary/test_u_flow.py`
- [ ] **U-FLOW-03** — `tests/boundary/test_u_flow.py`

### Boundary Fixture

- [ ] `grid_none` — U-IN-01, U-FLOW-02
- [ ] `grid_3x4` — U-IN-02 (TL-01)
- [ ] `grid_zero_blanks` — U-IN-03
- [ ] `grid_one_blank` — U-IN-04 (TL-02)
- [ ] `grid_duplicate` — U-IN-06 (TL-03)
- [ ] `grid_g1` — U-OUT-01, U-FLOW-01

---

## 2. Logic Track — Entity (`tests/entity/test_d_*.py`)

> `boundary`/`control` import 금지 · Domain Mock 금지 · E001~E005 emit 금지

| Test ID | 대상 함수 | Given→Then | Invariant / Rule |
|---------|-----------|------------|------------------|
| D-01 | `is_valid_grid_size()` | 3×4 → `False` | R-01 / INV-01 |
| D-02 | `count_blanks()` | 빈칸 1개 → `1` | R-02 / INV-02 |
| D-03 | `is_in_range()` | `17` → `False` | R-03 / INV-03 |
| D-04 | `has_duplicate()` | 중복 → `True` | R-03 / INV-03 |
| D-05 | `MagicConstant.value` | `sum(1..16)/4` | R-04 / INV-04 |
| D-LOC-01 | `find_blank_coords()` | **G1** → `[(2,2),(3,3)]` | I6 row-major, 1-index |
| D-LOC-02 | `find_blank_coords()` | **G1** → `len==2` | INV-02 |
| D-LOC-03 | `find_blank_coords()` | **G1** → row-major 순서 | I6 |

- [ ] **D-LOC-01** — `tests/entity/test_d_loc_01.py` ← **현재 착수**
- [ ] **D-LOC-02** — `tests/entity/test_d_loc_01.py`
- [ ] **D-LOC-03** — `tests/entity/test_d_loc_01.py`
- [ ] **D-01** — `tests/entity/test_d_grid_size.py`
- [ ] **D-02** — `tests/entity/test_d_blank_count.py`
- [ ] **D-03** — `tests/entity/test_d_cell_range.py`
- [ ] **D-04** — `tests/entity/test_d_no_duplicate.py`
- [ ] **D-05** — `tests/entity/test_d_magic_constant.py`

**G1 (1-index 빈칸 (2,2), (3,3)):**

```text
 16   3   2  13
  5   0  11   8
  9   6   0  12
  4  15  14   1
```

- [ ] `grid_g1` fixture — D-LOC-01~03
- [ ] `grid_3x4` — D-01
- [ ] `grid_one_blank` — D-02

---

## 3. Logic Track — Control (`tests/control/test_d_*.py`)

> `boundary` import 금지 · Domain Mock 금지

| Test ID | 대상 함수 | Given→Then | Invariant / Rule |
|---------|-----------|------------|------------------|
| D-06 | `sum_lines()` | **G0** → 10선 = MagicConstant | R-05 / INV-05 |
| D-06b | `sum_lines()` | TL-04 격자 → 대각 FAIL | R-05 |
| D-07 | `find_blanks()` | **G1** → `[(2,2),(3,3)]` | R-02, I6 |
| D-MIS-01 | `find_not_exist_nums()` | **G1** → `[7, 10]` 오름차순 | I7, I11 |
| D-VAL-01 | `is_magic_square()` | **G0** 완전 → `True` | R-01~05 |
| D-VAL-02 | `is_magic_square()` | TL-04 → `False` | INV-05 |
| D-SOL-01 | `solution()` | **G1** Step A 성공 | I8 |
| D-SOL-02 | `solution()` | **G1** → `int[6]` 1-index | I6, I8 |
| D-10 | `is_valid_magic_square()` | 채운 G1 → 10선 PASS | INV-05 |

- [ ] **D-06** — `tests/control/test_d_line_sums.py`
- [ ] **D-06b** — `tests/control/test_d_line_sums.py`
- [ ] **D-07** — `tests/control/test_d_find_blanks.py`
- [ ] **D-MIS-01** — `tests/control/test_d_missing_numbers.py`
- [ ] **D-VAL-01** — `tests/control/test_d_valid_magic_square.py`
- [ ] **D-VAL-02** — `tests/control/test_d_valid_magic_square.py`
- [ ] **D-SOL-01** — `tests/control/test_d_solver_combination.py`
- [ ] **D-SOL-02** — `tests/control/test_d_solver_combination.py`
- [ ] **D-10** — `tests/control/test_d_valid_magic_square.py`

### Control Fixture

- [ ] `grid_g0` — 완전 마방진 (D-06, D-VAL-01)
- [ ] `grid_g1` — 부분 격자 (D-07, D-MIS-01, D-SOL-*)
- [ ] `grid_tl04` — 행만 34, 대각 불일치 (D-06b, D-VAL-02)

---

## 4. C2C 추적 (PRD / TL ↔ Test ID)

| PRD / TL | Boundary | Logic |
|----------|----------|-------|
| TL-01 3×4 | U-IN-02 | D-01 |
| TL-02 빈칸 ≠2 | U-IN-04 | D-02 |
| TL-03 중복 | U-IN-06 | D-04 |
| TL-04 대각 FAIL | — | D-06b, D-VAL-02 |
| TL-05 10선 PASS | U-OUT-01 | D-VAL-01, D-10 |
| S-02 find_blanks | — | D-LOC-01~03, D-07 |
| §7.3 solution | U-OUT-01~02 | D-MIS-01, D-SOL-01~02 |

---

## 5. RED 진행 순서 (권장)

1. - [ ] Logic **D-LOC-01~03** — `tests/entity/test_d_loc_01.py`
2. - [ ] Logic **D-01~05** — `tests/entity/test_d_*.py`
3. - [ ] Logic **D-MIS-01, D-VAL-01** — `tests/control/`
4. - [ ] Logic **D-SOL-01~02, D-10** — `tests/control/`
5. - [ ] Boundary **U-IN-01~07** — `tests/boundary/test_u_input.py`
6. - [ ] Boundary **U-FLOW-01~03** — `tests/boundary/test_u_flow.py`
7. - [ ] Boundary **U-OUT-01~02** — `tests/boundary/test_u_output.py`

---

## 6. RED 완료 보고 (각 묶음마다)

- [ ] Phase / Layer / Track / TestID 선언
- [ ] 변경 파일 = `tests/` 만
- [ ] pytest 명령 + **FAILED** (의도한 assert)
- [ ] ECB / Mock / E코드 위반 없음
- [ ] 다음 GREEN 대상 함수 한 줄

---

*갱신: RED 테스트 작성·통과 시 해당 `- [ ]` → `- [x]` 로 표시.*
