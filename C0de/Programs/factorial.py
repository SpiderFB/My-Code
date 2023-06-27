# Factorial
def fact(n):
    s = 1
    while(n != 0):
        s *= n
        n -= 1
        fact(n)
    return s


x = int(input("Enter value(integer): "))1

y = fact(x)
print("Factorial is: ", +y)
