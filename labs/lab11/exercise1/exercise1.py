num_rounds = int(input())

# TODO: Your code here
# Use input() inside the loop to get each round's score

total_score = 0
rounds_processed = 0

for round_score in range ( num_rounds ):
    round_score = input(f"Enter the game scores for this round {round_score}")
    if round_score > 100:
        round_score += round_score * 0.2
    total_score += round_score
    rounds_processed += 1
        


print(f"{final_score:.1f}")
print(rounds_processed)