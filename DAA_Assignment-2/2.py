#Implement Combinations from scratch (do not use inbuilt methods) - For any data type
def get_combinations(data, r):
    if r == 0:
        return [[]]
    if len(data) < r:
        return []
    include = [[data[0]] + c for c in get_combinations(data[1:], r - 1)]
    exclude = get_combinations(data[1:], r)
    return include + exclude


data = ['A', 'B', 'C']
r = 2
result = get_combinations(data, r)
print(f"All combinations of {r} from {data}:")
for r in result:
    print(r)
