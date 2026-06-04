# MagicSquare_xx — 4×4 부분 마방진

> **4×4 부분 마방진에서 10선 조건과 입력 유효성을 무엇부터·어떤 순서로 판정할지 명문화하여, 맞음/틀림과 실패 원인을 헷갈리지 않게 만든다.**

Mom Test → 문제 정의 → Harness · `.cursorrules` → Dual-Track TDD(RED→GREEN→REFACTOR) 순으로 진행하는 실습 프로젝트입니다.

**저장소:** [github.com/msubkim-ship-it/MagicSquare_xx](https://github.com/msubkim-ship-it/MagicSquare_xx)

---

## 목차

1. [프로젝트 개요](#1-프로젝트-개요)
2. [도메인 규칙](#2-도메인-규칙)
3. [문제 정의 (Mom Test)](#3-문제-정의-mom-test)
4. [아키텍처 · Dual-Track TDD](#4-아키텍처--dual-track-tdd)
5. [디렉터리 구조](#5-디렉터리-구조)
6. [개발 환경](#6-개발-환경)
7. [문서 목록](#7-문서-목록)
8. [현재 상태](#8-현재-상태)
9. [다음 단계](#9-다음-단계)

---

## 1. 프로젝트 개요

| 항목 | 내용 |
|------|------|
| **도메인** | 4×4 Magic Square (마방진), 빈칸 `0` × 2, 1~16 |
| **방법론** | Mom Test → Rule/PRD → ECB + Dual-Track TDD |
| **페르소나** | 4×4 부분 마방진을 손·코드로 다루는 학습자 |
| **현재 단계** | **G1 Golden Master** Logic+Boundary GREEN PASS (29 tests) |

### 예시 격자

```
 16   3   2  13
  5  10  11   0
  9   6   0  12
  4  15  14   1
```

- 빈칸(`0`) **2개** → 1~16 중 누락 숫자를 채움
- **10선**(행 4 + 열 4 + 대각 2) 합 = **34** (`MagicConstant` SSOT)
- 출력: `int[6]` = `[r1, c1, n1, r2, c2, n2]` (좌표 **1-index**)

---

## 2. 도메인 규칙

| Rule | 내용 |
|------|------|
| **R-01** | 격자 **4×4** |
| **R-02** | 빈칸(`0`) **정확히 2개** |
| **R-03** | `0` 제외 **1~16**, 중복 없음 |
| **R-04** | Magic Constant = **(1+…+16)/4** — `34`·`16` 리터럴 산재 금지 |
| **R-05** | **10선** 합 = Magic Constant |
| **R-06** | **판정 순서:** 입력(R-01~03) → 10선(R-05) → 풀이 |

### Boundary 오류 코드 (E001~E007)

| 코드 | 조건 |
|------|------|
| E001 | 격자 ≠ 4×4 |
| E002 | 빈칸 개수 ≠ 2 |
| E003 | 값 범위 위반 (1~16 밖) |
| E004 | 비제로 값 중복 |
| E005 | 입력 타입·형식 오류 |
| E006 | 유효 입력, 해 없음 |
| E007 | 출력·포맷 계약 위반 |

> E001~E007은 **boundary** 전용. **entity**는 E001~E005 처리 금지.

상세: [`docs/PRD.md`](docs/PRD.md) · [`.cursorrules`](.cursorrules)

---

## 3. 문제 정의 (Mom Test)

### 표면 문제 (하지 않을 것)

> "4×4 마방진에서 빈칸 2개를 채우는 **프로그램**을 만든다."

### 진짜 문제

> 손으로 풀 때는 여러 행·열(·대각선) 조건을 동시에 추적·판정하기 어렵고, 코드로 옮기면 입력·타입·문제 출제 오류 가능성까지 겹쳐 **무엇이 맞고 틀린지, 무엇부터 확인해야 하는지** 판단하기 전에 헷갈린다.

상세: [`Report/01.MagicSquare_ProblemDefinition_Report.md`](Report/01.MagicSquare_ProblemDefinition_Report.md)

---

## 4. 아키텍처 · Dual-Track TDD

### ECB (단방향 의존)

```
boundary → control → entity
```

| Layer | 경로 | 책임 |
|-------|------|------|
| **entity** | `src/entity/` | Grid, MagicConstant, 도메인 불변식 |
| **control** | `src/control/` | Validator, Finder, Solver |
| **boundary** | `src/boundary/` | 입력 파싱, E001~E007, 출력 포맷 |

### Dual-Track

| Track | 테스트 경로 | Mock | 테스트 ID |
|-------|------------|------|-----------|
| **Logic** | `tests/entity/`, `tests/control/` | Domain Mock **금지** | `D-*` · `test_d_*.py` |
| **UI** | `tests/boundary/` | Mock **허용** | `U-*` · `test_u_*.py` |

TDD: **RED → GREEN → REFACTOR** (skip · xfail · assert 완화 금지)

RED Test ID·진행 체크: [`docs/TODO_RED.md`](docs/TODO_RED.md) · Logic ID 상세: [`.cursor/skills/magic-square-tdd/reference.md`](.cursor/skills/magic-square-tdd/reference.md)

---

## 5. 디렉터리 구조

```
MagicSquare_xx/
├── README.md
├── .cursorrules
├── pyproject.toml
├── .gitignore
├── .cursor/
│   ├── skills/magic-square-tdd/   ← SKILL.md, reference.md (D-*)
│   └── commands/
│       ├── tdd-red.md
│       └── review-ecb.md
├── docs/
│   ├── PRD.md
│   └── TODO_RED.md              ← Dual-Track RED 체크리스트
├── Report/
│   ├── 01.MagicSquare_ProblemDefinition_Report.md
│   ├── 01.mom_test_interview_report.md
│   ├── 02.project_introduction_report.md
│   ├── 03.work_progress_report.md   ← 작업 진행 통합
│   ├── 04.red_design_session_report.md ← RED 설계 세션
│   ├── 05.red_skeleton_session_report.md ← RED 스켈레톤 (D-LOC-01)
│   ├── 06.green_minimal_session_report.md ← GREEN D-LOC-01
│   └── 07.golden_master_session_report.md ← G1 Golden Master GREEN
├── Prompting/
│   ├── 01~02  Mom Test 프롬프트
│   ├── 03.work_progress_transcript.md
│   ├── 04.red_design_transcript.md
│   ├── 05.red_skeleton_transcript.md
│   ├── 06.green_minimal_transcript.md
│   └── 07.golden_master_transcript.md
├── src/entity|control|boundary/
└── tests/entity|control|boundary/
```

---

## 6. 개발 환경

**요구:** Python 3.10+

```bash
git clone https://github.com/msubkim-ship-it/MagicSquare_xx.git
cd MagicSquare_xx
pip install -e ".[dev]"
pytest                              # 전체
pytest tests/entity -v              # Logic — entity
pytest tests/control -v             # Logic — control
pytest tests/boundary -v            # UI — boundary
```

현재: **29 tests** — G1 Golden Master 경로 GREEN PASSED

```powershell
python -m pytest tests/ -v
python -m pytest tests/control/test_d_solver_combination.py::test_d_sol_01_step_a_success -v
python -m pytest tests/boundary/test_u_output.py -v
```

**G1 solution (Step A):** `[2, 2, 10, 3, 3, 7]` — 빈칸 (2,2)·(3,3), 누락 7·10

브랜치: `main` · `staging` · `spec` · `red`

---

## 7. 문서 목록

| 문서 | 설명 |
|------|------|
| [`.cursorrules`](.cursorrules) | 도메인 · ECB · Dual-Track · TDD · AI 행동 규칙 |
| [`docs/PRD.md`](docs/PRD.md) | Rule, R-G-I-O, 입출력 계약, DoD |
| [`docs/TODO_RED.md`](docs/TODO_RED.md) | **Dual-Track RED 체크리스트** (U-* · D-*) |
| [`Report/01.MagicSquare_ProblemDefinition_Report.md`](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test + Rule/Command/Test Loop |
| [`Report/01.mom_test_interview_report.md`](Report/01.mom_test_interview_report.md) | Mom Test 인터뷰 원본 |
| [`Report/02.project_introduction_report.md`](Report/02.project_introduction_report.md) | 프로젝트 소개 · ECB 초안 |
| [`Prompting/01.mom_test_step1_interview.md`](Prompting/01.mom_test_step1_interview.md) | Mom Test 인터뷰 프롬프트 |
| [`Prompting/02.mom_test_workbook_template.md`](Prompting/02.mom_test_workbook_template.md) | Mom Test 워크북 템플릿 (→ Report/01 문제 정의) |

### Report ↔ Prompting (번호·이름 짝)

| # | Report | Prompting |
|---|--------|-----------|
| 01 | `01.mom_test_interview_report.md` | `01.mom_test_step1_interview.md` |
| 01 | `01.MagicSquare_ProblemDefinition_Report.md` | `02.mom_test_workbook_template.md` |
| 02 | `02.project_introduction_report.md` | — |
| 03 | `03.work_progress_report.md` | `03.work_progress_transcript.md` |
| 04 | `04.red_design_session_report.md` | `04.red_design_transcript.md` |
| 05 | `05.red_skeleton_session_report.md` | `05.red_skeleton_transcript.md` |
| 06 | `06.green_minimal_session_report.md` | `06.green_minimal_transcript.md` |
| 07 | `07.golden_master_session_report.md` | `07.golden_master_transcript.md` |
| [`.cursor/skills/magic-square-tdd/SKILL.md`](.cursor/skills/magic-square-tdd/SKILL.md) | Dual-Track TDD 절차 |
| [`.cursor/commands/tdd-red.md`](.cursor/commands/tdd-red.md) | RED Command |
| [`.cursor/commands/review-ecb.md`](.cursor/commands/review-ecb.md) | ECB 리뷰 Command (read-only) |
| [`Report/03.work_progress_report.md`](Report/03.work_progress_report.md) | 작업 진행 보고서 (통합) |
| [`Report/04.red_design_session_report.md`](Report/04.red_design_session_report.md) | **RED 설계 세션** — D-LOC-01 · TODO_RED |
| [`Report/05.red_skeleton_session_report.md`](Report/05.red_skeleton_session_report.md) | **RED 스켈레톤** — D-LOC-01 pytest RED |
| [`Report/06.green_minimal_session_report.md`](Report/06.green_minimal_session_report.md) | **GREEN minimal** — `find_blank_coords` |
| [`Report/07.golden_master_session_report.md`](Report/07.golden_master_session_report.md) | **G1 Golden Master** — 29 tests GREEN |
| [`Prompting/03.work_progress_transcript.md`](Prompting/03.work_progress_transcript.md) | 작업 진행 Transcript (통합 요약) |
| [`Prompting/04.red_design_transcript.md`](Prompting/04.red_design_transcript.md) | RED 설계 Transcript |
| [`Prompting/05.red_skeleton_transcript.md`](Prompting/05.red_skeleton_transcript.md) | RED 스켈레톤 Transcript |
| [`Prompting/06.green_minimal_transcript.md`](Prompting/06.green_minimal_transcript.md) | GREEN minimal Transcript |
| [`Prompting/07.golden_master_transcript.md`](Prompting/07.golden_master_transcript.md) | G1 Golden Master Transcript |

---

## 8. 현재 상태

| 영역 | 상태 |
|------|------|
| Mom Test · 문제 정의 · PRD | ✅ |
| pytest Harness | ✅ |
| `.cursorrules` | ✅ 초안 |
| Skill · Commands (`tdd-red`, `review-ecb`) | ✅ |
| [`Report/03`](Report/03.work_progress_report.md) 작업 보고서 | ✅ |
| [`docs/TODO_RED.md`](docs/TODO_RED.md) RED 설계·체크리스트 | ✅ |
| RED D-LOC-01 스켈레톤 | ✅ |
| G1 Golden — Logic entity (D-LOC, D-01~05) | ✅ |
| G1 Golden — Logic control (D-06~10, D-MIS, D-SOL) | ✅ |
| G1 Golden — Boundary (U-IN, U-OUT, U-FLOW) | ✅ |
| REFACTOR · SSOT 통합 (`GRID_SIZE` 등) | ⬜ |

상세 타임라인: [`Report/03.work_progress_report.md`](Report/03.work_progress_report.md)

---

## 9. 다음 단계

진행 순서는 [`docs/TODO_RED.md`](docs/TODO_RED.md) §5 참조.

1. REFACTOR — `boundary`/`entity` constants 통합, 호출 카운터 정리
2. `.cursorrules` v0.2 (리뷰 P0 반영)
3. 추가 시나리오 RED (TL-02~04 boundary·control 회귀 강화)

---

## 라이선스 / 기여

교육용 실습 프로젝트. 기여·이슈는 저장소 정책에 따릅니다.
