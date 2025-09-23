monthly_usage = int(input())

discount = 0
amount_bill = 0
#Determine discount value
if monthly_usage < 50:
    discount = 0
elif monthly_usage <= 100:
    discount = 0.05
else:
    monthly_usage > 100
    discount = 0.2
    
if discount > 0:
    amount_bill = monthly_usage + (monthly_usage - (discount * monthly_usage))
else:
    amount_bill = monthly_usage

total_pay = amount_bill

print(f"Amount bill to be paid is : {total_pay}")
    