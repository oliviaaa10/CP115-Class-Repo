price = float(input())
item_count = 0
total_cost = 0


while price >-1: 
    total_cost += price
    item_count += 1
    price = float(input())

print(item_count)
print(f"{total_cost:.2f}")
            