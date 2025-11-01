#Solve travelling salesman problem with 5 cities, use brute force methodology
def permutations(cities):
    if len(cities) == 0:
        return [[]]
    result = []
    for i in range(len(cities)):
        rest = cities[:i] + cities[i+1:]
        for p in permutations(rest):
            result.append([cities[i]] + p)
    return result

dist = [
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 6],
    [7, 3, 5, 6, 0]
]

cities = [0, 1, 2, 3, 4]
paths = permutations(cities)
min_cost = float('inf')
best_path = None

for path in paths:
    cost = 0
    for i in range(len(path) - 1):
        cost += dist[path[i]][path[i+1]]
    cost += dist[path[-1]][path[0]] 
    if cost < min_cost:
        min_cost = cost
        best_path = path

print("Best Path:", best_path, "Cost:", min_cost)
