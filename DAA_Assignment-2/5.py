#Implement Knapsack problem for 6 items, using brute force methodology (Use Binary representation to represent items in the sack)
weights = [2, 3, 4, 5, 9, 7]
values = [3, 4, 5, 8, 10, 6]
capacity = 15

n = len(weights)
best_value = 0
best_combo = None

for i in range(1 << n):  # 2^n combinations
    total_weight = total_value = 0
    for j in range(n):
        if i & (1 << j):  # if bit j is set, include item j
            total_weight += weights[j]
            total_value += values[j]
    if total_weight <= capacity and total_value > best_value:
        best_value = total_value
        best_combo = i

print("Best value:", best_value)
print("Selected items:", [j for j in range(n) if best_combo & (1 << j)])
