#Implement Permutation from scratch (do not use inbuilt methods) - For any data type
def get_permutations(data):
    if len(data) == 0:
        return [[]]
    perms = []
    for i in range(len(data)):
        rest = data[:i] + data[i+1:]
        for p in get_permutations(rest):
            perms.append([data[i]] + p)
    return perms

data = [1, 2, 3]
result = get_permutations(data)
print("All permutations:")
for r in result:
    print(r)
