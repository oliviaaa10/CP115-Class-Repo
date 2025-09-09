employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

overtime_pay = overtime_hours * 35
total_income = base_salary + overtime_pay

if tax_status == "Single":
    if total_income >= 5000:
        tax_rate = 0.22
    else:
        tax_rate = 0.18
elif tax_status == "Married":
    if total_income >= 6000:
        tax_rate = 0.20
    else:
        tax_rate = 0.15
elif tax_status == "Head":
    if total_income >= 5500:
        tax_rate = 0.25
    else:
        tax_rate = 0.19
else:
    tax_rate = 0.0
    
tax_deduction = total_income * tax_rate
epf_deduction = total_income * 0.11
sosco_deduction = total_income * 0.05
total_deduction = tax_deduction + epf_deduction + sosco_deduction

net_salary = total_income - total_deduction    

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")