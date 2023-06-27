# if/else

i = 10
if (i == 10):
    print("Yes")
else:
    print("No")

for i in range(0, 4, +1):
    print("Hello")

for i in range(0, 5, +1):
    for j in range(0, 5, +1):
        print("*", end=" ")
    print("\r")  # Carriage return --(/r) means the courser will go to the next line

a = input("Enter the value : ")

# time.sleep(3)

print(a)

#

n = 10
b = ((n*(n+1))/2)
print(b)

#

a = 5
b = 5.5
c = "Hello"
print(type(a))
print(type(b))
print(type(c))

#

a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # floor division(float)
print(a // b)  # floor division(integer)
print(a ** b)  # Power
print(a**(1/2))

#

sum = 0
for i in range(0, 10, +1):
    sum = sum+i
print(sum)

# Special operator
# Membership  Operator
# in     not in

a = 'Hello'
print('i' in a)
print('i' not in a)

# Identity operator
# is     is not

b = 'Hello'
print('Hello' is b)
print('hello' is b)
print('h' is not b)

# For loop

for i in [1, 2, 3, 5, 'a', 'b', 'c']:
    print(i)

# Nesting loop

for i in range(0, 5, +1):
    for j in range(0, 5, +1):
        print("*", end=" ")
    print("\r")

# While loop

a = 0
while(a <= 10):
    print("*", end=" ")
    a += 1

# Conditional statement

a = int(input("Enter the marks: "))
if (a >= 90):
    print("O")
elif(a >= 80 and a < 90):
    print("E")
elif(a >= 70 and a < 80):
    print("D")
elif(a >= 60 and a < 70):
    print("C")
elif(a >= 50 and a < 60):
    print("B")
else:
    print("Fail")

#

for i in range(0, 11):
    if(i % 2 == 0):
        print(i)

#TypeCasting(Implicit | Explicit)
# Implicit

x = input("Enter : ")
print(x)

# Explicit

x = int(input("Enter: "))
print(x)

#

for i in range(1, 50, +1):
    if(i == 20 and i == 30 and i == 40 and i == 45):
        break
    else:
        val = (i**(1/3))
        print(val)
#

for i in range(0, 11, +1):
    if(i % 2 == 0):
        print(i**3)

# Indexing
# Negetive Indexing

a = ("ok i can understand")
print(a[3])

# Slice operation a[x:Y(n-1)]

print(a[5:8])
print(a[5:8:1])  # have to find out

# String concatination

a = "Hello"
b = "Python"
c = "World"
d = a+b+c
print(d)

#enumerate() and len()

a = "hello"
l = list(enumerate(a))
print(l)
print(len(a))

# Escape sequence(\)

print('this line and \' that line')

#
# a,b=b,a
# List

l1 = [1, 2, 3.5, 'ab', 'bc', 'cd']  # in python list can take all types of data
print(l1)
l2 = [7, 8, 9, 10, l1, ['x', 4, 6.4]]
print(l2)
print(l2[-1])
print(l2[2:5])  # Slice operator(:)
print(l2[::-1])  # Reverse of a list
l2[2] = -5
print(l2)
l1.append("4")
print(l1)
l1.remove("4")  # For direct value remove
l1.pop(1)  # For remove value at a index
print(l1)

# appened(increase),delete, pop, remove in a list(value)

l1.append(17)  # to add only 1 element at the end
print(l1)

#del l1

print(l1.index('ab'))

# Tuple --it's immutable, means can't alter value

t1 = ()
t2 = (1, 2, 3)
t3 = (1, 2, 3, 'a', 'b', 'c')
t4 = (1, 2, 3, t3)
print(t4)

# Dictionary

d1 = {}
d2 = {142: 'abc', 'bcd': 'had', 3: 'it'}
print(d2)
print(d2.popitem())  # to delete the last element
print(d2.setdefault(142))

#Iterate in dictionary

d1 = {1: 'ab', 2: 'cd', 3: 'ef'}
for key, value in d1.items():
    print(key, value)

# Function


def fun():
    print("Hello world")
    print("Hello world")
    print("Hello world")
    print("Hello world")


fun()

#

a = 1
b = 2  # Global


def fun1():
    print("Ye")
    global b
    print("Global: ", b)
    b = 3  # Local
    print("Local: ", b)
    return 1


x = fun1()
print(x)
c = a+b
print(c)

# To return value in a function


def add(a, b):
    s = a+b
    return s


x = add(2, 3)
print(x)

# Argument: The value we provide to the function
# Parameter: The variable in a function is called parameter
# Arbitrary Argument: We  use this when we dont know the total number of arguments


def fun3(*n):
    for i in n:
        print(i)


fun3(4, 5, 4, 7, 8)
