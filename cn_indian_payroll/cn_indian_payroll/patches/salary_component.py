import frappe

def execute():


    data=[

        
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  "condition": "",
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 1,
  "custom_is_part_of_ctc": 1,
  "custom_is_part_of_gross_pay": 1,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 1,
  "description": "Basic",
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "(base * 0.35)/12\n\n    ",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 1,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:04:28.123783",
  "name": "Basic",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 0,
  "salary_component": "Basic",
  "salary_component_abbr": "B",
  "statistical_component": 0,
  "type": "Earning",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 1,
  "custom_is_part_of_ctc": 1,
  "custom_is_part_of_gross_pay": 1,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "3",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 1,
  "description": "House Rent Allowance",
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "((base/12 *.35) * 1 if base <= 515000\n else (base/12 *.35 * 0.5 if base/12 *.35 < 20000 and base <= 1000000 \n       else 20000 if base/12 *.35 >= 20000 and base <= 1000000 \n       else 25000 if 1000001 < base <= 1700000\n       else (base/12 *.35) * 0.5 if 1700001 < base <= 99999999 \n       else base/12 *.35))",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 1,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:04:56.119015",
  "name": "House Rent Allowance",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 1,
  "salary_component": "House Rent Allowance",
  "salary_component_abbr": "HRA",
  "statistical_component": 0,
  "type": "Earning",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 1,
  "custom_is_part_of_ctc": 1,
  "custom_is_part_of_gross_pay": 1,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "7",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 1,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "custom_uniform_allowance_value/12 if custom_is_uniform_allowance  else 0",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 1,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:05:36.149341",
  "name": "Uniform",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 0,
  "salary_component": "Uniform",
  "salary_component_abbr": "UFM",
  "statistical_component": 0,
  "type": "Earning",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 1,
  "custom_is_part_of_ctc": 1,
  "custom_is_part_of_gross_pay": 1,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "9",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 1,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "custom_medical_allowance_value/12 if custom_is_medical_allowance else 0",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 1,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:06:27.330768",
  "name": "Medical",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 0,
  "salary_component": "Medical",
  "salary_component_abbr": "M",
  "statistical_component": 0,
  "type": "Earning",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 1,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 1,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "13",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 1,
  
  "disabled": 0,
  "do_not_include_in_total": 1,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "2000 if custom_is_food_coupon and income_tax_slab==\"Old Regime\" else 0",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 1,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:07:00.360762",
  "name": "Food Coupon",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 0,
  "salary_component": "Food Coupon",
  "salary_component_abbr": "FC",
  "statistical_component": 0,
  "type": "Earning",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 1,
  "custom_is_part_of_ctc": 1,
  "custom_is_part_of_gross_pay": 1,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "20",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 1,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "((base * 0.35)/12 * custom_nps_percentage)/100 if custom_is_nps else 0",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 1,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:07:31.426078",
  "name": "NPS",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 0,
  "salary_component": "NPS",
  "salary_component_abbr": "NPS",
  "statistical_component": 0,
  "type": "Earning",
  "component_type":"NPS",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 0,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 1,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "((base * 0.35)/12 * custom_nps_percentage)/100 if custom_is_nps else 0",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 0,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:07:48.116596",
  "name": "NPS (Deduction)",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 0,
  "salary_component": "NPS (Deduction)",
  "salary_component_abbr": "NPSDE",
  "statistical_component": 0,
  "type": "Deduction",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 1,
  "custom_is_part_of_ctc": 1,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 1,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "(base * 0.35)/12 * .12 if custom_is_epf else 0",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 0,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:08:19.793054",
  "name": "Employee Provident Fund",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 0,
  "salary_component": "Employee Provident Fund",
  "salary_component_abbr": "PF",
  "statistical_component": 0,
  "type": "Deduction",
  "component_type":"EPF",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 0,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 0,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "(B+FC+H+M+UFM+TWA+HRA)*0.75/100 if custom_is_esic==1 else 0",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 0,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:08:45.213651",
  "name": "ESIC",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 1,
  "salary_component": "ESIC",
  "salary_component_abbr": "ESIC",
  "statistical_component": 0,
  "type": "Deduction",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 0,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 1,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 0,
  
  "disabled": 0,
  "do_not_include_in_total": 1,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "custom_car_perquisite_as_per_rules if custom_car_perquisite_as_per_rules>0 else 0",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 1,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:09:15.636746",
  "name": "Car Perquisite",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 1,
  "salary_component": "Car Perquisite",
  "salary_component_abbr": "CP",
  "statistical_component": 0,
  "type": "Earning",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 0,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 1,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 0,
  
  "disabled": 0,
  "do_not_include_in_total": 1,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "custom_driver_perquisite_as_per_rules if custom_driver_provided_by_company==1 else 0",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 1,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:09:34.707034",
  "name": "Driver Perquisite",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 0,
  "salary_component": "Driver Perquisite",
  "salary_component_abbr": "DP",
  "statistical_component": 0,
  "type": "Earning",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 0,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 0,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "(0 if base/12 <= 5999 and custom_state == \"Gujarat\" else \r\n80 if 6000 <= base/12 <= 8999 and custom_state == \"Gujarat\" else \r\n150 if 9000 <= base/12 <= 11999 and custom_state == \"Gujarat\" else\r\n200 if custom_state == \"Gujarat\" else 0)",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 0,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:10:01.810208",
  "name": "Professional Tax (Gujarat)",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 1,
  "salary_component": "Professional Tax (Gujarat)",
  "salary_component_abbr": "PT_GU",
  "statistical_component": 0,
  "type": "Deduction",
  "component_type":"Professional Tax",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 0,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 0,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "(0 if ((gender == 'Male' and base <= 7500) or (gender == 'Female' and base <= 25000)) else \r\n175 if (gender == 'Male' and 7500 < base  <= 10000) else \r\n200 if ((gender == 'Male' and base > 10000) or (gender == 'Female' and base  > 25000)) else \r\n300 if (getdate(start_date).month == 2 and ((gender == 'Male' and base> 10000) or (gender == 'Female' and base > 25000))) else 0\r\n)if custom_state == \"Maharashtra\" else 0",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 0,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:10:27.243490",
  "name": "Professional Tax (Maharashtra)",
  
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 1,
  "salary_component": "Professional Tax (Maharashtra)",
  "salary_component_abbr": "PT_MAH",
  "statistical_component": 0,
  "type": "Deduction",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 0,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 0,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "(0 if base / 12 <= 15000 and custom_state == \"Telangana\" else\r\n150 if 15001 <= base / 12 <= 20000 and custom_state == \"Telangana\" else\r\n200 if base / 12 > 20000 and custom_state == \"Telangana\" else\r\n0)\r\n",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 0,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:11:09.723491",
  "name": "Professional Tax (Telangana)",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 1,
  "salary_component": "Professional Tax (Telangana)",
  "salary_component_abbr": "PT_TELA",
  "statistical_component": 0,
  "type": "Deduction",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 0,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 0,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "(0 if base / 12 <= 21000 and custom_state == \"Tamil Nadu\" else\n135 if 21001 <= base / 12 <= 30000 and custom_state == \"Tamil Nadu\" else\n315 if 30001 <= base / 12 <= 45000 and custom_state == \"Tamil Nadu\" else\n690 if 45001 <= base / 12 <= 60000 and custom_state == \"Tamil Nadu\" else\n1025 if 60001 <= base / 12 <= 75000 and custom_state == \"Tamil Nadu\" else\n1250 if base / 12 > 75000 and custom_state == \"Tamil Nadu\" else\n0)",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 0,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:11:24.855623",
  "name": "Professional Tax (Tamilnadu)",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 1,
  "salary_component": "Professional Tax (Tamilnadu)",
  "salary_component_abbr": "PT_TAM_N",
  "statistical_component": 0,
  "type": "Deduction",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 0,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 0,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "(0 if base/12 <= 11999  else\n120 if 12000 <= base/12 <= 17999  else\n180 if 18000 <= base/12 <= 29999  else\n300 if 30000 <= base/12 <= 44999  else\n450 if 45000 <= base/12 <= 59999  else\n600 if 60000 <= base/12 <= 74999  else\n750 if 75000 <= base/12 <= 99999  else\n1000 if 100000 <= base/12 <= 124999 else\n1250) if custom_state == \"Kerala\" else 0\n\n",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 0,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:11:40.154971",
  "name": "Professional Tax (Kerala)",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 1,
  "salary_component": "Professional Tax (Kerala)",
  "salary_component_abbr": "PT_KER",
  "statistical_component": 0,
  "type": "Deduction",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 0,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 0,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "0 if custom_state == \"Delhi\" else 0\n",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 0,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:12:00.248665",
  "name": "Professional Tax (Delhi)",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 1,
  "salary_component": "Professional Tax (Delhi)",
  "salary_component_abbr": "PT_DEL",
  "statistical_component": 0,
  "type": "Deduction",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 0,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 0,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "(0 if base/12 < 15000 else\n150 if 15000 <= base/12 < 20000 else\n200) if custom_state==\"Andra Pradesh\" else 0",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 0,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:12:16.308997",
  "name": "Professional Tax (Andra Pradesh)",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 1,
  "salary_component": "Professional Tax (Andra Pradesh)",
  "salary_component_abbr": "PT_AN",
  "statistical_component": 0,
  "type": "Deduction",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 0,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 0,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "(0 if base/12 <= 15000 and custom_state == \"Karnataka\" else\n200 if custom_state == \"Karnataka\" else 0)\n             \n",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 0,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:12:34.837640",
  "name": "Professional Tax (Karnata)",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 1,
  "salary_component": "Professional Tax (Karnata)",
  "salary_component_abbr": "PT_KAR",
  "statistical_component": 0,
  "type": "Deduction",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 1,
  
  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",
  
  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 0,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,
  
  
  
  "custom_perquisite": 0,
  
  "custom_sequence": "1",
  
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 0,
  
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,
  "formula": "(0 if base/12 <= 10000 and custom_state == \"West Bengal\" else \n110 if 10001 <= base/12 <= 15000 and custom_state == \"West Bengal\" else \n130 if 15001 <= base/12 <= 25000 and custom_state == \"West Bengal\" else \n150 if 25001 <= base/12 <= 40000 and custom_state == \"West Bengal\" else \n200 if custom_state == \"West Bengal\" else 0)\n",
  "is_flexible_benefit": 0,
  "is_income_tax_component": 0,
  "is_tax_applicable": 0,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-13 16:12:52.456863",
  "name": "Professional Tax (West Bengal)",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 1,
  "salary_component": "Professional Tax (West Bengal)",
  "salary_component_abbr": "PT_WES",
  "statistical_component": 0,
  "type": "Deduction",
  "variable_based_on_taxable_salary": 0
 },
 {
  "accounts": [],
  "amount": 0.0,
  "amount_based_on_formula": 0,
  "component_type": "",

  "create_separate_payment_entry_against_benefit_claim": 0,
  "custom_accrual_paid_on": "Payroll",

  "custom_is_accrual": 0,
  "custom_is_allowance": 0,
  "custom_is_arrear": 0,
  "custom_is_food_coupon": 0,
  "custom_is_nps": 0,
  "custom_is_part_of_appraisal": 0,
  "custom_is_part_of_ctc": 0,
  "custom_is_part_of_gross_pay": 0,
  "custom_is_reimbursement": 0,

  "custom_perquisite": 0,
  "custom_regime": "",
  "custom_sequence": "1",
  "custom_tax_exemption_applicable_based_on_regime": 0,
  "deduct_full_tax_on_selected_payroll_date": 0,
  "depends_on_payment_days": 0,
  "description": "Income Tax",
  "disabled": 0,
  "do_not_include_in_total": 0,
  "docstatus": 0,
  "doctype": "Salary Component",
  "exempted_from_income_tax": 0,

  "is_flexible_benefit": 0,
  "is_income_tax_component": 1,
  "is_tax_applicable": 0,
  "max_benefit_amount": 0.0,
  "modified": "2024-11-14 10:25:36.899877",
  "name": "Income Tax",
  "only_tax_impact": 0,
  "pay_against_benefit_claim": 0,
  "remove_if_zero_valued": 1,
  "round_to_the_nearest_integer": 1,
  "salary_component": "Income Tax",
  "salary_component_abbr": "IT",
  "statistical_component": 0,
  "type": "Deduction",
  "variable_based_on_taxable_salary": 1
 }

    
    ]

    for i in data:
        insert_record(i)

def insert_record(i):

    
    if frappe.db.exists("Salary Component", i["name"]):
        get_doc=frappe.get_doc("Salary Component",i["name"])

        if get_doc.type=="Earning":
            if get_doc.custom_is_part_of_gross_pay==0:
                get_doc.custom_is_part_of_gross_pay=1
            if get_doc.custom_is_part_of_ctc==0:
                get_doc.custom_is_part_of_ctc=1
            if get_doc.custom_is_part_of_appraisal==0:
                get_doc.custom_is_part_of_appraisal=1

        get_doc.save()

    else:
        doc=frappe.new_doc("Salary Component")
        doc.update(i)
        doc.save()

       

