correct_password = "python123"
attempts = 0
login_successful = "Access denied"
attempts_used = 0

while attempts < 3 :
    password = input("Enter password: ")
    attempts += 1
    
    if password == correct_password:
        login_successful = "Access granted"
        attempts_used = attempts
        break
    else:
        print(f"Wrong password. {3 - attempts} attempts remaining.")

print(login_successful)
print(attempts_used)
