#Convert an integer to binary equivalent, take a random position, check if the position is 0 or 1 and print true or false accordingly
num = int(input("Enter an integer: "))
binary = bin(num)[2:]
print("Binary equivalent:", binary)
pos = int(input("Enter position to check (0 for last bit): "))

if pos < len(binary):
    bit = binary[-(pos + 1)]
    print("Bit at position", pos, "is", bit)
    print("True" if bit == '1' else "False")
else:
    print("Invalid position!")
