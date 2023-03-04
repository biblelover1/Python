

def Sum(a, b):
    if b == 0:
        return 1
    return a + Sum(1, b - 1)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(Sum(a, b))