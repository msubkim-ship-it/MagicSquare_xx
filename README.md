# MagicSquare_xx — 4×4 부분 마방진

> **4×4 부분 마방진에서 10선 조건과 입력 유효성을 무엇부터·어떤 순서로 판정할지 명문화하여, 맞음/틀림과 실패 원인을 헷갈리지 않게 만든다.**

Mom Test → 문제 정의 → Rule/Command/Test Loop → (후속) ECB 구현 순으로 진행하는 실습 프로젝트입니다.

---

## 목차

1. [프로젝트 개요](#1-프로젝트-개요)
2. [도메인 규칙](#2-도메인-규칙)
3. [문제 정의 (Mom Test)](#3-문제-정의-mom-test)
4. [디렉터리 구조](#4-디렉터리-구조)
5. [문서 목록](#5-문서-목록)
6. [현재 상태](#6-현재-상태)
7. [다음 단계](#7-다음-단계)

---

## 1. 프로젝트 개요

| 항목 | 내용 |
|------|------|
| **도메인** | 4×4 Magic Square (마방진), 빈칸 2개 |
| **방법론** | Mom Test → Invariant/Rule → Test Loop → ECB |
| **페르소나** | 4×4 부분 마방진을 손·코드로 다루는 학습자 |
| **현재 단계** | 문제 정의 · PRD v0.1 (설계 문서) |

### 예시 격자

```
 16   3   2  13
  5  10  11   0
  9   6   0  12
  4  15  14   1
```

- 빈칸(`0`) **2개** → 1~16 중 누락 숫자를 채움
- **10선**(행 4 + 열 4 + 대각 2) 합 = **34**

---

## 2. 도메인 규칙

| Rule | 내용 |
|------|------|
| **R-01** | 격자 **4×4** |
| **R-02** | 빈칸(`0`) **정확히 2개** |
| **R-03** | `0` 제외 **1~16**, 중복 없음 |
| **R-04** | Magic Constant = **(1+…+16)/4 = 34** (하드코딩 금지) |
| **R-05** | **10선** 합 = Magic Constant |
| **R-06** | **판정 순서:** 입력(R-01~03) → 10선(R-05) → 풀이 |

상세: [`docs/PRD.md`](docs/PRD.md) §4

---

## 3. 문제 정의 (Mom Test)

### 표면 문제 (하지 않을 것)

> "4×4 마방진에서 빈칸 2개를 채우는 **프로그램**을 만든다."

### 진짜 문제

> 손으로 풀 때는 여러 행·열(·대각선) 조건을 동시에 추적·판정하기 어렵고, 코드로 옮기면 입력·타입·문제 출제 오류 가능성까지 겹쳐 **무엇이 맞고 틀린지, 무엇부터 확인해야 하는지** 판단하기 전에 헷갈린다.

상세: [`Report/01.MagicSquare_ProblemDefinition_Report.md`](Report/01.MagicSquare_ProblemDefinition_Report.md)

---

## 4. 디렉터리 구조

```
MagicSquare_xx/
├── README.md                 ← 이 파일
├── docs/
│   └── PRD.md                ← 제품 요구사항 (v0.1)
├── Report/
│   ├── 01.MagicSquare_ProblemDefinition_Report.md
│   ├── 01.mom_test_interview_report.md
│   └── 02.project_introduction_report.md
└── Prompt/
    ├── 01.mom_test_step1_interview.md
    └── 02.mom_test_workbook_template.md
```

> 구현 코드(`entity/`, `control/`, `boundary/`, `tests/`)는 후속 세션에서 추가 예정.

---

## 5. 문서 목록

| 문서 | 설명 |
|------|------|
| [`docs/PRD.md`](docs/PRD.md) | Rule, R-G-I-O, 입출력 계약, DoD |
| [`Report/01.MagicSquare_ProblemDefinition_Report.md`](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test + Rule/Command/Test Loop 통합 |
| [`Report/01.mom_test_interview_report.md`](Report/01.mom_test_interview_report.md) | Mom Test 인터뷰 원본 |
| [`Report/02.project_introduction_report.md`](Report/02.project_introduction_report.md) | 프로젝트 소개 · ECB 초안 |
| [`Prompt/01.mom_test_step1_interview.md`](Prompt/01.mom_test_step1_interview.md) | Mom Test 인터뷰 프롬프트 |
| [`Prompt/02.mom_test_workbook_template.md`](Prompt/02.mom_test_workbook_template.md) | Mom Test 워크북 템플릿 |

---

## 6. 현재 상태

| 영역 | 상태 |
|------|------|
| Mom Test 인터뷰 | ✅ 완료 (채점 8/10) |
| 문제 정의 보고서 | ✅ |
| PRD v0.1 | ✅ |
| Rule / Command / Test Loop | ✅ 문서화 |
| ECB 구현 | ⬜ 미착수 |
| pytest / RED 테스트 | ⬜ 미착수 |

---

## 7. 다음 단계

1. Mom Test Q10 보완 — *"입력이 이상할 때 뭘 먼저 확인했어?"*
2. Test Loop TL-01~05 RED 케이스 작성
3. Skill(S-01~03) 인터페이스 → pytest
4. ECB 레이어 구현 (Entity → Control → Boundary)

---

## 라이선스 / 기여

교육용 실습 프로젝트. 기여·이슈는 저장소 정책에 따릅니다.
