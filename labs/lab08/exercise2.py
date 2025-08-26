main_dishes = 25 * 3
appetizers = 12 * 2
drinks = 8 * 4

service_tax = 0.1
delivery_fee = 5


food_bill = main_dishes + appetizers + drinks
total_bill = (food_bill + ( service_tax * food_bill)) + delivery_fee
each_person_amount = total_bill / 6
print(int(each_person_amount))