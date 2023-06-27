# Root of quadratic equation
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if(a >= 0):
    d = ((b**2)-(4*a*c))**(1/2)
    r1 = ((-b)+d)/(2*a)
    r2 = ((-b)-d)/(2*a)
    print(r1)
    print(r2)
else:
    print("WTH check the value of a!")
