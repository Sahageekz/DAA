#Implement Knapsack problem for 6 items, using brute force methodology (Use Combinations)
def combinations(data, r):
    if r == 0:
        return [[]]
    if len(data) < r:
        return []
    include = [[data[0]] + c for c in combinations(data[1:], r - 1)]
    exclude = combinations(data[1:], r)
    return include + exclude

weights = [2, 3, 4, 5, 9, 7]
values = [3, 4, 5, 8, 10, 6]
capacity = 15

n = len(weights)
items = list(range(n))
best_value = 0
best_set = []

for r in range(1, n + 1):
    for combo in combinations(items, r):
        w = sum(weights[i] for i in combo)
        v = sum(values[i] for i in combo)
        if w <= capacity and v > best_value:
            best_value = v
            best_set = combo

print("Best value:", best_value)
print("Items chosen:", best_set)
