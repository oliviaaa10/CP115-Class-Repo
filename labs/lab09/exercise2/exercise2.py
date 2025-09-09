employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()


if tax_status == "Single":
    if base_salary >= 5000:
        tax_rate = 0.22
    else:
        tax_rate = 0.18
elif tax_status == "Married":
    if base_salary >= 6000:
        tax_rate = 0.20
    else:
        tax_rate = 0.15
else:
    if base_salary >= 5500:
        tax_rate = 0.25
    else:
        tax_rate = 0.19
        
overtime_pay = overtime_hours * 35
total_income = base_salary + overtime_pay
net_salary = total_income * ( 1 - tax_rate ) * ( 1 - 0.115 )

print(employee_name)
print(f"{tax_rate * 100:.0f}%")
print(f"{net_salary:.2f}")