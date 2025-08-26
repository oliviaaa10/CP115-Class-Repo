base_membership = 120
personal_training_sessions = 80
locker_rental = 25
towel_service = 15
one_time_registration_fee = 50

first_month_cost = base_membership + ( personal_training_sessions * 6) + locker_rental + towel_service + one_time_registration_fee
monthly_cost = base_membership + ( personal_training_sessions * 6) + locker_rental + towel_service
annual_cost = first_month_cost + ( monthly_cost * 11)
print(f"First Month Cost = {first_month_cost}")
print(f"Monthly Cost after the first month = {monthly_cost}")
print(f"Annual cost = {annual_cost}")