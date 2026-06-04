# Product Requirements Document (PRD)

**프로젝트:** MagicSquare_xx  
**버전:** 0.1 (초안)  
**작성일:** 2026-06-04  
**기반:** Mom Test · MagicSquare_xx 세션 3 워크북  
**참조:** `Report/01.MagicSquare_ProblemDefinition_Report.md`

---

## 목차

1. [제품 개요](#1-제품-개요)
2. [문제 정의 (Mom Test)](#2-문제-정의-mom-test)
3. [목표 및 범위](#3-목표-및-범위)
4. [도메인 규칙 (Rule / Invariants)](#4-도메인-규칙-rule--invariants)
5. [R-G-I-O 계약](#5-r-g-i-o-계약)
6. [기능 요구사항 (세션 3)](#6-기능-요구사항-세션-3)
7. [입출력 계약](#7-입출력-계약)
8. [아키텍처 개요 (ECB)](#8-아키텍처-개요-ecb)
9. [완료 기준 (Definition of Done)](#9-완료-기준-definition-of-done)
10. [제약 및 금지 사항](#10-제약-및-금지-사항)
11. [참조 문서](#11-참조-문서)

---

## 1. 제품 개요

MagicSquare_xx는 **4×4 부분 마방진**을 소재로, **10선(행 4 + 열 4 + 대각 2) 합 34** 조건과 **입력 유효성**을 **판정 순서**까지 포함해 명문화하는 실습 프로젝트이다.

### 1.1 한 줄 정의 (Mom Test 기반, 솔루션 최소화)

> **4×4 부분 마방진에서 10선 조건과 입력 유효성을 무엇부터·어떤 순서로 판정할지 명문화하여, 맞음/틀림과 실패 원인을 헷갈리지 않게 만든다.**

### 1.2 도메인 한눈에 보기

```
격자     : 4×4 (16셀)
숫자     : 1 ~ 16 (중복 없음)
빈칸     : 0 — 정확히 2개
Magic C. : 34 (= 136 ÷ 4)
검증     : 10선 (행4 + 열4 + 대각2)
```

---

## 2. 문제 정의 (Mom Test)

### 2.1 페르소나

4×4 부분 마방진(빈칸 2개, 1~16, 합 34)을 **손으로/코드로** 다루는 **학습자**.

### 2.2 표면 문제 (하지 않을 정의)

> "4×4 마방진에서 빈칸 2개를 채우는 **프로그램**을 만든다."

### 2.3 진짜 문제 (한 문장)

> 손으로 풀 때는 여러 행·열(·대각선) 조건을 동시에 추적·판정하기 어렵고, 코드로 옮기면 입력·타입·문제 출제 오류 가능성까지 겹쳐 **무엇이 맞고 틀린지, 무엇부터 확인해야 하는지** 판단하기 전에 헷갈린다.

### 2.4 Mom Test 증거

| # | 인용 |
|---|------|
| E-1 | "여러 행열의 합을 적지 않고 외우고 있는 것이 헷갈렸어." |
| E-2 | "코드로 다룰 때에는 여러 경우의 수를 고려해보느라 훨씬 헷갈렸어." |
| E-3 | "변수 타입이 달라서 오류가 난다거나, 문제가 잘못 출제될 수 있는 가능성" |

---

## 3. 목표 및 범위

### 3.1 목표 (Goal)

| # | 목표 | Mom Test 연결 |
|---|------|---------------|
| G-1 | **10선** 합 34 판정을 외우지 않고 재현 가능하게 한다 | E-1 |
| G-2 | **입력 검증 → 10선 검증** 순서를 고정한다 | E-2, 진짜 문제 |
| G-3 | 잘못된 입력·출제가 **즉시 실패**하고 원인 라벨을 준다 | E-3 |

### 3.2 이번 버전 범위 (세션 3)

| 포함 | 미포함 |
|------|--------|
| Rule R-01 ~ R-06 | 완성형 Solver 구현 |
| Command C-01 ~ C-05 | GUI / PyQt |
| Skill S-01 ~ S-03 (인터페이스) | Dual-Track TDD 전체 |
| Test Loop TL-01 ~ TL-05 | REFACTOR · 배포 |

---

## 4. 도메인 규칙 (Rule / Invariants)

| ID | Rule / Invariant | 설명 |
|----|------------------|------|
| **R-01 / INV-01** | 격자 **4×4** | 16셀 고정 |
| **R-02 / INV-02** | 빈칸(`0`) **정확히 2개** | |
| **R-03 / INV-03** | `0` 제외 **1~16, 중복 없음** | |
| **R-04 / INV-04** | Magic Constant = **sum(1..16)/4** | 하드코딩 `34` 금지 |
| **R-05 / INV-05** | **10선** 합 = Magic Constant | 행4+열4+대각2 |
| **R-06** | **판정 순서:** INV-01~03 → INV-05 → *(풀이)* | |

### 4.1 실패 라벨 (Command C-03)

| ID | 조건 | 라벨 |
|----|------|------|
| **ERR-01** | 격자 ≠ 4×4 | `InvalidGridSize` |
| **ERR-02** | 빈칸 ≠ 2 | `InvalidBlankCount` |
| **ERR-03** | 범위·중복 위반 | `InvalidCellValue` / `DuplicateValue` |

---

## 5. R-G-I-O 계약

| | 정의 |
|---|------|
| **Role** | 4×4 부분 마방진 학습자 — 규칙을 **명문화·검증**하는 주체 |
| **Goal** | 유효 입력 판정 → 10선 합 판정 → *(후속)* 풀이 |
| **Input** | `int[4][4]`, `0`×2, 나머지 1~16 unique |
| **Output** | `{ status, failed_rule?, coordinates? }` — status: `VALID_INPUT` \| `VALID_MAGIC_SQUARE` \| `FAIL` |

---

## 6. 기능 요구사항 (세션 3)

### 6.1 Skill (최소 인터페이스)

| ID | Skill | 입력 | 출력 | Rule |
|----|-------|------|------|------|
| **S-01** | `sum_lines(grid)` | `int[4][4]` | 10개 합 `list[int]` | R-05 |
| **S-02** | `find_blanks(grid)` | `int[4][4]` | 2개 `(row,col)` row-major | R-02 |
| **S-03** | `label_failure(grid)` | `int[4][4]` | `ERR-xx` 또는 `OK` | R-01~03 |

### 6.2 Test Loop 시나리오

| ID | Given | Then |
|----|-------|------|
| **TL-01** | 3×4 격자 | R-01 FAIL, ERR-01 |
| **TL-02** | 빈칸 1개 | R-02 FAIL, ERR-02 |
| **TL-03** | 중복 값 | R-03 FAIL, ERR-03 |
| **TL-04** | 행만 34, 대각 불일치 | R-05 FAIL |
| **TL-05** | 유효 + 10선 34 | R-05 PASS |

---

## 7. 입출력 계약

### 7.1 입력 (Precondition)

```text
grid: int[4][4]
  - len(grid) == 4, all len(row) == 4
  - count(0) == 2
  - forall v != 0: 1 <= v <= 16
  - nonzero values unique
```

### 7.2 출력 (Postcondition — 세션 3)

```text
판정 결과:
  - VALID_INPUT    : R-01~03 PASS
  - VALID_MAGIC_SQUARE : R-01~05 PASS (채워진 격자)
  - FAIL           : failed_rule + err_label
```

### 7.3 출력 (Postcondition — 후속 세션)

```text
solution: int[6] = [r1, c1, n1, r2, c2, n2]  # 1-index
  - (r1,c1), (r2,c2) = blank positions
  - n1, n2 = missing numbers from {1..16}
  - filled grid satisfies R-05
```

---

## 8. 아키텍처 개요 (ECB)

```
Boundary          Control              Entity
─────────         ────────             ──────
InputHandler  →   SquareValidator  →   MagicSquare
GridUI            MissingFinder        Cell
ResultDisplay     Solver               SolveResult
```

| PR | 주 책임 계층 |
|----|-------------|
| PR-01, PR-02 | Control — 10선 검증 |
| PR-03 | Boundary — 입력 파싱·1차 검증 |

> 세션 3 PRD 범위: ECB **구현** 전 **Rule·Contract·Test Loop** 확정.

---

## 9. 완료 기준 (Definition of Done)

| ID | 기준 | Mom Test / Rule |
|----|------|-----------------|
| **DOD-01** | R-01~06 문서화·추적 가능 | SC-01 |
| **DOD-02** | TL-01~05 RED 케이스 정의 | SC-02 |
| **DOD-03** | ERR-01~03 실패 라벨 명명 | SC-03 |
| **DOD-04** | `34` 하드코딩 0건 (R-04) | — |
| **DOD-05** | 표면 문제 N-01~05 "하지 않음" 합의 | §10 |

---

## 10. 제약 및 금지 사항

| # | 금지 | 이유 |
|---|------|------|
| N-01 | 솔버·GUI **선구현** | 표면 문제 |
| N-02 | 10선 중 **일부만** 검증 | PR-02, E-1 |
| N-03 | TDD/ECB/GUI를 **v0.1 산출물**로 | 세션 3 범위 |
| N-04 | Magic Constant **하드코딩** | R-04 |
| N-05 | Rule·Test **구현 후** 작성 | E-2 |

---

## 11. 참조 문서

| 문서 | 내용 |
|------|------|
| `Report/01.MagicSquare_ProblemDefinition_Report.md` | Mom Test · Rule · Command · Test Loop |
| `Report/01.mom_test_interview_report.md` | Mom Test 인터뷰 원본 |
| `Report/02.project_introduction_report.md` | 프로젝트 소개 · ECB 초안 |
| `Prompt/01.mom_test_step1_interview.md` | Mom Test 인터뷰 프롬프트 |
| `Prompt/02.mom_test_workbook_template.md` | Mom Test 워크북 템플릿 |

---

*다음 버전(v0.2): Invariant 전체(INV-06~), Solver US, pytest RED 구현*
