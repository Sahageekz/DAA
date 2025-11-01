# Implement Karatsuba Algorithm for multiplication of 2 long integers

def karatsuba(x, y):
    
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    high1, low1 = divmod(x, 10**half)
    high2, low2 = divmod(y, 10**half)

    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return (z2 * 10**(2 * half)) + ((z1 - z2 - z0) * 10**half) + z0


if __name__ == "__main__":
    num1 = int(input("Enter first long integer: "))
    num2 = int(input("Enter second long integer: "))

    result = karatsuba(num1, num2)

    print(f"\nResult of multiplication using Karatsuba Algorithm:\n{result}")
