score = float(input())

score_count = 0
total_score = 0


while score >= 0 and score <= 100 : 
    total_score += score
    score_count +=1
    score = float(input())
    
if score_count > 0 :
    average_score = total_score / score_count
else: 
    average_score = 0 
    

print(score_count)
print(total_score)
print(f"{average_score:.2f}")
