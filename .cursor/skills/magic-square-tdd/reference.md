# Logic Track — D-* Test ID (reference)

| ID | 초점 | Rule / INV | 파일(예정) |
|----|------|------------|------------|
| **D-01** | 격자 4×4 | R-01 / INV-01 | `tests/entity/test_d_grid_size.py` |
| **D-02** | 빈칸 0 정확히 2개 | R-02 / INV-02 | `tests/entity/test_d_blank_count.py` |
| **D-03** | 값 범위 1~16 | R-03 / INV-03 | `tests/entity/test_d_cell_range.py` |
| **D-04** | 비제로 중복 없음 | R-03 / INV-03 | `tests/entity/test_d_no_duplicate.py` |
| **D-05** | MagicConstant 유도 (34 하드코딩 금지) | R-04 / INV-04 | `tests/entity/test_d_magic_constant.py` |
| **D-06** | 10선 합 = MagicConstant | R-05 / INV-05 | `tests/control/test_d_line_sums.py` |
| **D-07** | 빈칸 좌표 row-major 2개 | R-02 | `tests/control/test_d_find_blanks.py` |
| **D-08** | 누락 숫자 2개 (오름차순) | INV-03 | `tests/control/test_d_missing_numbers.py` |
| **D-09** | 두 조합 시도 (정방향→역순) | R-05 | `tests/control/test_d_solver_combination.py` |
| **D-10** | 출력 전 10선 유효 마방진 | R-05 / INV-05 | `tests/control/test_d_valid_magic_square.py` |

> TL-01~03 → boundary(U-*) + entity(D-01~04). TL-04~05 → D-06, D-10.
