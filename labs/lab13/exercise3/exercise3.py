total = 0
valid_count = 0

while True : 
    grade = float(input())
    
    if grade < 0: 
        break
    
    if grade > 100:
        continue
    
    total+= grade
    valid_count +=1
    
if valid_count > 0 :
    average = total / valid_count
else:
    average = 0

# TODO: Your code here

print(valid_count)
print(f"{average:.2f}")
