num_days = int(input())
danger_threshold = float(input())

# TODO: Your code here
# Use input() inside the loop to get each day's temperature

danger_days = 0
average_temp = 0

for temperature in range ( num_days ):
    temperature = input(f"Enter the temperature values {temperature}")

 
print(danger_days)
print(f"{average_temp:.1f}")