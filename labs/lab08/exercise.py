# This code proves sequential execution
print("Line 1: This will run")
print("Line 2: This will also run") 
x = 10
print(f"Line 3: x = {x}")
y = x * 2
print(f"Line 4: y = {y}")
print("Line 5: All good so far")

#print(unknown_variable)  # This will cause an error