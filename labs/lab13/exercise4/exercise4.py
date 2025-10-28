positive_sum = 0
positive_count = 0 

while True :
    number = float(input())
    
    if number == 0:
        break
    elif number < 0 :
        continue
    
    positive_sum += number
    positive_count += 1



print(positive_count)
print(f"{positive_sum:.2f}")
