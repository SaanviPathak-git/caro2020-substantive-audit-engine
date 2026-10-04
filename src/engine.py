"""
Core Substantive Audit Engine: All 21 Clauses of CARO 2020
Standards: SA 230 (Audit Documentation), SA 500 (Audit Evidence)
"""

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class ClauseResult:
    clause_num: str
    clause_title: str
    is_applicable: bool
    has_exception: bool
    auditor_finding: str
    annexure_text: str


class CARO2020Engine:
    def __init__(self, client_name: str, engagement_data: Dict[str, Any]):
        self.client = client_name
        self.data = engagement_data
        self.results: List[ClauseResult] = []

    def evaluate_all_clauses(self) -> List[ClauseResult]:
        self.results = [
            self._audit_01_ppe(),
            self._audit_02_inventory_wc(),
            self._audit_03_loans_given(),
            self._audit_04_sec185_186(),
            self._audit_05_deposits(),
            self._audit_06_cost_records(),
            self._audit_07_statutory_dues(),
            self._audit_08_unrecorded_income(),
            self._audit_09_borrowings(),
            self._audit_10_ipo_private_placement(),
            self._audit_11_fraud(),
            self._audit_12_nidhi(),
            self._audit_13_related_party(),
            self._audit_14_internal_audit(),
            self._audit_15_non_cash_directors(),
            self._audit_16_nbfc(),
            self._audit_17_cash_losses(),
            self._audit_18_auditor_resignation(),
            self._audit_19_going_concern(),
            self._audit_20_csr(),
            self._audit_21_consolidation(),
        ]
        return self.results

    def _audit_01_ppe(self):
        title_issues = self.data.get("ppe_title_deed_exceptions", 0)
        reval_pct = self.data.get("ppe_revaluation_pct", 0.0)
        has_exc = (title_issues > 0) or (abs(reval_pct) >= 10.0)
        if not has_exc:
            text = "Clause 3(i): (a) Proper records maintained for PPE. (c) Title deeds of all immovable properties are held in the name of the Company. (d) The Company has not revalued its PPE during the year."
        else:
            text = f"Clause 3(i): Discrepancies noted: {title_issues} title deeds not in company name; Revaluation of {reval_pct}% exceeded 10% threshold."
        return ClauseResult("3(i)", "PPE & Intangibles", True, has_exc, f"Title issues: {title_issues}, Reval: {reval_pct}%", text)

    def _audit_02_inventory_wc(self):
        wc_limit = self.data.get("sanctioned_wc_limit_cr", 0.0)
        bank_diffs = self.data.get("quarterly_bank_variances_count", 0)
        if wc_limit < 5.0:
            return ClauseResult("3(ii)", "Inventory & WC Limits", True, False, "Sanctioned limit < Rs 5 Cr", "Clause 3(ii): Working capital limits do not exceed Rs. 5 crore in aggregate.")
        has_exc = bank_diffs > 0
        text = "Clause 3(ii)(b): Quarterly statements filed with banks agree with books." if not has_exc else f"Clause 3(ii)(b): Discrepancies noted in {bank_diffs} quarterly statements filed with banks compared to books of account."
        return ClauseResult("3(ii)", "Inventory & WC Limits", True, has_exc, f"{bank_diffs} quarterly discrepancies", text)

    def _audit_03_loans_given(self):
        prejudicial = self.data.get("loans_prejudicial_to_interest", False)
        overdue_90 = self.data.get("loans_overdue_over_90_days", False)
        has_exc = prejudicial or overdue_90
        text = "Clause 3(iii): Terms of loans given are not prejudicial to Company's interest; no balances overdue > 90 days." if not has_exc else "Clause 3(iii): Exceptions noted regarding loan terms or overdue balances > 90 days."
        return ClauseResult("3(iii)", "Loans & Guarantees Given", True, has_exc, f"Prejudicial: {prejudicial}, Overdue >90d: {overdue_90}", text)

    def _audit_04_sec185_186(self):
        violations = self.data.get("sec_185_186_violations_count", 0)
        has_exc = violations > 0
        text = "Clause 3(iv): The Company has complied with Sections 185 and 186 of the Act." if not has_exc else f"Clause 3(iv): Non-compliance noted with Sections 185/186 in {violations} instances."
        return ClauseResult("3(iv)", "Compliance with Sec 185 & 186", True, has_exc, f"Violations: {violations}", text)

    def _audit_05_deposits(self):
        accepted = self.data.get("deposits_accepted", False)
        text = "Clause 3(v): The Company has not accepted deposits under Sections 73 to 76." if not accepted else "Clause 3(v): Public deposits accepted during the year."
        return ClauseResult("3(v)", "Public Deposits (Sec 73-76)", accepted, False, "No deposits", text)

    def _audit_06_cost_records(self):
        appl = self.data.get("cost_records_applicable", False)
        maint = self.data.get("cost_records_maintained", True)
        if not appl:
            text = "Clause 3(vi): Maintenance of cost records is not prescribed under Section 148(1)."
        else:
            text = "Clause 3(vi): Cost records under Section 148(1) have been made and maintained." if maint else "Clause 3(vi): Prescribed cost records have not been maintained."
        return ClauseResult("3(vi)", "Cost Audit Records (Sec 148)", appl, (appl and not maint), f"Applicable: {appl}", text)

    def _audit_07_statutory_dues(self):
        arrears_6m = self.data.get("undisputed_dues_over_6m_cr", 0.0)
        disputed = self.data.get("disputed_dues_cr", 0.0)
        has_exc = (arrears_6m > 0) or (disputed > 0)
        text = f"Clause 3(vii): Undisputed arrears > 6 months: Rs {arrears_6m} Cr. Disputed dues pending before forums: Rs {disputed} Cr."
        return ClauseResult("3(vii)", "Statutory Dues (Undisputed & Disputed)", True, has_exc, f"Arrears >6m: {arrears_6m} Cr, Disputed: {disputed} Cr", text)

    def _audit_08_unrecorded_income(self):
        unrec = self.data.get("unrecorded_income_cr", 0.0)
        has_exc = unrec > 0
        text = "Clause 3(viii): No unrecorded transactions surrendered or disclosed in tax assessments." if not has_exc else f"Clause 3(viii): Undisclosed income of Rs {unrec} Cr surrendered in tax assessments."
        return ClauseResult("3(viii)", "Unrecorded Tax Income", True, has_exc, f"Amount: {unrec} Cr", text)

    def _audit_09_borrowings(self):
        defaults = self.data.get("borrowing_defaults_count", 0)
        wilful = self.data.get("wilful_defaulter", False)
        short_for_long = self.data.get("short_term_for_long_term_cr", 0.0)
        has_exc = defaults > 0 or wilful or (short_for_long > 0)
        if not has_exc:
            text = "Clause 3(ix): (a) No defaults in repayment of borrowings. (b) Not declared a wilful defaulter. (d) No short-term funds utilised for long-term purposes."
        else:
            text = f"Clause 3(ix): Repayment defaults: {defaults}; Wilful Defaulter: {wilful}; Short funds used for long: Rs {short_for_long} Cr."
        return ClauseResult("3(ix)", "Borrowings & Fund Diversion", True, has_exc, f"Defaults: {defaults}", text)

    def _audit_10_ipo_private_placement(self):
        raised = self.data.get("ipo_or_private_placement_raised", False)
        text = "Clause 3(x): The Company has not raised moneys by way of initial public offer or preferential allotment." if not raised else "Clause 3(x): Moneys raised through placement were applied for stated end-use."
        return ClauseResult("3(x)", "End-Use of IPO / Pref Placement", raised, False, "No issues", text)

    def _audit_11_fraud(self):
        frauds = self.data.get("fraud_noticed_count", 0)
        whistle = self.data.get("whistleblower_complaints_count", 0)
        has_exc = frauds > 0
        text = f"Clause 3(xi): (a) No fraud on or by Company noticed. (b) Form ADT-4 not filed. (c) Considered {whistle} whistle-blower complaints." if not has_exc else f"Clause 3(xi): {frauds} fraud events noticed during the year."
        return ClauseResult("3(xi)", "Fraud & Whistle-Blower", True, has_exc, f"Frauds: {frauds}, Whistle: {whistle}", text)

    def _audit_12_nidhi(self):
        is_nidhi = self.data.get("is_nidhi_company", False)
        return ClauseResult("3(xii)", "Nidhi Company", is_nidhi, False, "Not applicable", "Clause 3(xii): The Company is not a Nidhi Company.")

    def _audit_13_related_party(self):
        rpt_viol = self.data.get("rpt_violations_count", 0)
        has_exc = rpt_viol > 0
        text = "Clause 3(xiii): Transactions with related parties comply with Sections 177 and 188 of the Act." if not has_exc else f"Clause 3(xiii): Section 177/188 non-compliance in {rpt_viol} transactions."
        return ClauseResult("3(xiii)", "Related Party Transactions", True, has_exc, f"Violations: {rpt_viol}", text)

    def _audit_14_internal_audit(self):
        ia_ok = self.data.get("internal_audit_adequate", True)
        text = "Clause 3(xiv): The Company has an internal audit system commensurate with its size, and reports were considered." if ia_ok else "Clause 3(xiv): Scope of internal audit requires enhancement."
        return ClauseResult("3(xiv)", "Internal Audit System", True, not ia_ok, f"Adequate: {ia_ok}", text)

    def _audit_15_non_cash_directors(self):
        non_cash = self.data.get("sec_192_non_cash_deals", False)
        text = "Clause 3(xv): The Company has not entered into non-cash transactions with directors under Section 192." if not non_cash else "Clause 3(xv): Section 192 non-cash transactions identified."
        return ClauseResult("3(xv)", "Non-Cash Deals with Directors", non_cash, non_cash, f"Non-cash: {non_cash}", text)

    def _audit_16_nbfc(self):
        fin_asset_pct = self.data.get("fin_asset_pct", 10.0)
        fin_inc_pct = self.data.get("fin_income_pct", 5.0)
        is_nbfc = (fin_asset_pct >= 50.0) and (fin_inc_pct >= 50.0)
        text = "Clause 3(xvi): The Company is not required to be registered under Section 45-IA of the RBI Act, 1934." if not is_nbfc else "Clause 3(xvi): Company fulfills 50:50 test and requires RBI registration."
        return ClauseResult("3(xvi)", "RBI Act Sec 45-IA Registration", True, is_nbfc, f"Assets: {fin_asset_pct}%, Income: {fin_inc_pct}%", text)

    def _audit_17_cash_losses(self):
        cy_loss = self.data.get("cash_loss_cy_cr", 0.0)
        py_loss = self.data.get("cash_loss_py_cr", 0.0)
        has_exc = (cy_loss > 0) or (py_loss > 0)
        if not has_exc:
            text = "Clause 3(xvii): The Company has not incurred cash losses in the current financial year or in the immediately preceding financial year."
        else:
            text = f"Clause 3(xvii): The Company has incurred cash losses of Rs {cy_loss:,.2f} Cr in the financial year and Rs {py_loss:,.2f} Cr in the preceding financial year."
        return ClauseResult("3(xvii)", "Cash Losses (CY & PY)", True, has_exc, f"CY: {cy_loss} Cr, PY: {py_loss} Cr", text)

    def _audit_18_auditor_resignation(self):
        resigned = self.data.get("auditor_resigned_during_year", False)
        text = "Clause 3(xviii): There has been no resignation of the statutory auditors during the year." if not resigned else "Clause 3(xviii): Resignation of statutory auditor taken into consideration."
        return ClauseResult("3(xviii)", "Resignation of Statutory Auditors", resigned, False, "No resignation", text)

    def _audit_19_going_concern(self):
        cr = self.data.get("current_ratio", 1.5)
        dscr = self.data.get("dscr", 2.0)
        has_exc = (cr < 1.0) or (dscr < 1.0)
        if not has_exc:
            text = "Clause 3(xix): Based on financial ratios and ageing schedules, no material uncertainty exists regarding meeting liabilities falling due within one year."
        else:
            text = f"Clause 3(xix): Material uncertainty indicated: Current Ratio is {cr:.2f} and DSCR is {dscr:.2f}."
        return ClauseResult("3(xix)", "Going Concern & Debt Service < 1 Yr", True, has_exc, f"CR: {cr:.2f}, DSCR: {dscr:.2f}", text)

    def _audit_20_csr(self):
        unspent_transferred = self.data.get("csr_unspent_transferred", True)
        text = "Clause 3(xx): Unspent CSR amounts have been transferred to Schedule VII Fund or Unspent CSR Account within the prescribed time." if unspent_transferred else "Clause 3(xx): Unspent CSR amounts not transferred within statutory deadline."
        return ClauseResult("3(xx)", "CSR Compliance (Sec 135)", True, not unspent_transferred, f"Transferred: {unspent_transferred}", text)

    def _audit_21_consolidation(self):
        is_standalone = self.data.get("is_standalone", True)
        if is_standalone:
            return ClauseResult("3(xxi)", "Consolidated CARO Qualifications", False, False, "Standalone audit", "Clause 3(xxi): Clause is applicable only to Consolidated Financial Statements.")
        qual_count = self.data.get("component_qualifications_count", 0)
        has_exc = qual_count > 0
        text = "Clause 3(xxi): No qualifications in component CARO reports." if not has_exc else f"Clause 3(xxi): Qualifications noted in {qual_count} component companies."
        return ClauseResult("3(xxi)", "Consolidated CARO Qualifications", True, has_exc, f"Component quals: {qual_count}", text)
