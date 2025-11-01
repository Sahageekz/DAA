#Get input from user on 2 matrix and multiply them
def input_matrix(rows, cols):
    print(f"Enter elements for a {rows}x{cols} matrix:")
    mat = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        mat.append(row)
    return mat

def multiply_matrix(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

r1 = int(input("Enter rows for Matrix A: "))
c1 = int(input("Enter cols for Matrix A: "))
r2 = int(input("Enter rows for Matrix B: "))
c2 = int(input("Enter cols for Matrix B: "))

if c1 != r2:
    print("Matrix multiplication not possible!")
else:
    A = input_matrix(r1, c1)
    B = input_matrix(r2, c2)
    print("\nResultant Matrix:")
    result = multiply_matrix(A, B)
    for row in result:
        print(row)
