# caro2020-substantive-audit-engine
Automated Substantive Audit Engine &amp; SA 230 Workpaper Generator for CARO 2020
# CARO 2020 Substantive Audit Engine & SA 230 Workpaper Generator

An automated audit analytics engine covering all **21 clauses of the Companies (Auditor's Report) Order, 2020 (CARO 2020)** under the Companies Act, 2013. Built from an engagement team perspective to evaluate client schedules (PBC), conduct substantive testing, and generate working papers compliant with **SA 230 (Audit Documentation)** and **SA 500 (Audit Evidence)**.

## Audit Scope: All 21 Clauses Implemented

| Clause | Subject Matter | Substantive Procedure |
| :--- | :--- | :--- |
| **3(i)** | PPE & Intangibles | Title deeds verification & revaluations \(\ge 10\%\) aggregate test |
| **3(ii)** | Inventory & Working Capital | Inventory variance \(>10\%\) & quarterly bank returns agreement (\(> ₹5\text{ Cr}\)) |
| **3(iii)**| Loans & Guarantees Given | Terms prejudicial to interest & overdue \(> 90\text{ days}\) |
| **3(iv)** | Sections 185 & 186 | Loans to directors, security, and statutory limit tests |
| **3(v)**  | Deemed Deposits | Compliance with Sections 73 to 76 and RBI directives |
| **3(vi)** | Cost Audit Records | Verification of cost accounts maintenance under Section 148(1) |
| **3(vii)**| Statutory Dues | Undisputed dues \(> 6\text{ months}\) and disputed dues by forum |
| **3(viii)**| Unrecorded Income | Search/survey surrendered income recorded in books |
| **3(ix)** | Borrowings & Repayment | Default matrix, wilful defaulter tag, and short-term fund diversion |
| **3(x)**  | Public Offers / Placements | End-use compliance for IPO/FPO and private placement (Sec 42) |
| **3(xi)** | Fraud & Whistle-Blower | Frauds noticed, Form ADT-4 under Sec 143(12), and whistle-blower logs |
| **3(xii)**| Nidhi Companies | 1:20 Net Owned Funds ratio and 10% unencumbered deposits |
| **3(xiii)**| Related Party Transactions | Compliance with Sections 177 & 188 and Ind AS 24 disclosures |
| **3(xiv)**| Internal Audit System | Adequacy commensurate with scale and review of internal audit reports |
| **3(xv)** | Non-Cash Transactions | Director transactions compliance under Section 192 |
| **3(xvi)**| RBI Registration (Sec 45-IA)| 50:50 Financial Asset / Income test for NBFC status |
| **3(xvii)**| Cash Losses | Cash loss calculation for current and preceding FY |
| **3(xviii)**| Auditor Resignation | Review of issues raised by outgoing statutory auditors |
| **3(xix)**| Going Concern & Liquidity | Financial ratios, ageing realization, and capability to meet debts \(< 1\text{ year}\) |
| **3(xx)** | CSR Compliance | Section 135 unspent amount transfers within statutory deadlines |
| **3(xxi)**| Component Qualifications | CARO qualifications across group entities in consolidation |

## Deliverables Generated
1. **SA 230 Working Paper (`dist/WP_CARO2020_Master_Workpaper.xlsx`):** Audit sign-off header, clause indices, testing thresholds, and exception logs.
2. **Draft CARO Annexure (`dist/Draft_CARO_Annexure_Report.txt`):** Standard reporting text per ICAI Guidance Note incorporating qualified remarks for exceptions.

## How to Run in Google Colab
You can test this repository in Google Colab without installing anything locally:
```python
!git clone https://github.com/SaanviPathak-git/caro-2020-audit-engine.git
%cd caro-2020-audit-engine
!pip install -r requirements.txt
!python main.py
