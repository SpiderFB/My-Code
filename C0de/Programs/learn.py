print("Hola")
first = 'Arnab'
second = 'Roy'
view1 = first + ' [' + second + '] is good'
view2 = f'{first} [{second}] is good'
print(view1)
print(view2)

# Method is limited for strings specially but function is available for all purpouse

course = 'Learing material'
print(course)
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('l'))  # find method is case sensetive
print(course.find('rial'))
print(course.replace('a', 'u'))
print('Learing' in course)

print(10+3)
print(10-3)
print(10*3)
print(10**3)  # power
print(10/3)
print(10//3)  # integer
print(10 % 3)  # remainder

x = 3.6
print(round(x))
print(abs(-x))

hot = False
cold = False
if hot:
    print("yes")
elif cold:
    print("yes")
else:
    print("no")

price = 20000
rich = True
if rich:
    Payment = 20000 - (20000 * 0.4)
else:
    Payment = 20000 - (20000 * 0.5)
print(f"Payment: {Payment} ₨")

x = 0
while x <= 5:
    print("Not 5")
    x = x+1

for item in [1, 2, 3, 4, 5]:
    print(item)

for item in range(10):
    print(item)

for item in range(1, 10, 2):
    print(item)
# Array is contiguious collection of homogenious data types
# List : Lists are ordered.
# Lists can contain any arbitrary objects.(heterogenious/ all types of data)
# List elements can be accessed by index.(faltu)
# Lists can be nested to arbitrary depth.(nested list)
# Lists are mutable.(changable)
# Lists are dynamic.(size of the list dosen't requied, it allocates dynamically)
# Tuplle is immutable(can not change)
# List and Tuplle may have dudpliacte values but Set can't have
# Set mutable
name = ['zero', 'one', 'two', 'three', 7, 'five']
print(name)
print(name[3])
print(name[2:5])
print(name[2:])
name[3] = "lol"
print(name)

num = [5, 7, 34, 91, 43, 7]  # List
max = num[0]
for number in num:
    if number > max:
        max = number
print(max)
num.append(15)
num.reverse()
print(num.sort(reverse=True))
# del num / To delete the list totally
print(num)
print(34 in num)  # Bollean value in terms of True of False

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
for i in matrix:
    for item in i:
        print(item)

num = (56, 34, 238, 3, 86)  # Tupple
t1 = (5)
print(type(t1))
t1 = (5, 6, 79, 3)
print(type(t1))
t1 = (5,)
print(type(t1))
t1 = [5]
print(type(t1))

# unpackin
list1 = [45, 567, 2]
tuple1 = (55, 96, 32)
a, b, c = list1
print(a)
a, b, c = tuple1
print(a)
# packing
a = 5
b = 6
c = 7
tuple2 = a, b, c
print(tuple2)

info = {
    "Name": "Arnab",
    "Phn": "1234567890",
    "City": "Siliguri",
    "is_verified": True
}
print(info["Name"])
print(info.get("Phn"))  # "get" statement for restlt as "none" with out an error
info["Name"] = "Arnab Roy"  # Replace
print(info.get("Acc", "0987654321"))
info["Gender"] = "Male"  # Add
print(info)

no = input("Number :")
num_dic = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}
for i in no:
    print(((num_dic.get(i, "!")+" ")), end=" ")

msg = input(">")
hold = msg.split(" ")
print(hold)
emoji = {
    ":)": "😀",
    ":(": "🙁",
    ":P": "😋",
    ":*": "😘",
}
for i in hold:
    print(emoji.get(i, i))

# 🔴Function


def who():
    print("who function")


input(">")
who()


def emoji_converter(msg):
    hold = msg.split(" ")
    # print(hold)
    emoji = {
        ":)": "😀",
        ":(": "🙁",
        ":P": "😋",
        ":*": "😘",
    }
    for i in hold:
        print((emoji.get(i, i)+" "), end=" ")


msg = "Hello cutipee :*"
emoji_converter(msg)

try:
    age = int(input('Age > '))
    print("Your age is", +age)
except ValueError:
    print('Not Integer !')
finally:  # It will execute even any error occurs
    print("try again")


class MyClass:
    def add(self):
        print("You added")

    def dele(self):
        print("You delete")


# Obj is the blueprint and obj is the instanece(example)
# To creat an obj / Name of he Class and call it as a function"()"
obj = MyClass()
obj.add()
obj.dele()
obj.a = 5  # attribute
obj.b = 6  # attribute
print(obj.a)
print(obj.a+obj.b)

# 🔴Class


class School:
    def person(self):
        return f"I'm {self.name}, and a {self.position} of class {self.cls}"


std = School()
tech = School()
std.name = "Arnab"
std.position = "Student"
std.cls = 12
tech.name = "Paul"
tech.position = "Teacher"
tech.cls = "8"
print(std.person())
print(tech.person())

# 🔴Constructor


class School:

    def __init__(self, Name, Position, Cls):  # this portion is the constructor
        self.name = Name
        self.position = Position
        self.cls = Cls

    def person(self):
        return f"🔴I'm {self.name}, and a {self.position} of class {self.cls}"


student = School("Arnab", "Student", 12)
teacher = School("Paul", "Teacher", 8)
print(student.person())
print(teacher.person())


# 🔴Inheritance

class Boss:  # parent class
    def human(self):
        return "Boss"


class Male(Boss):  # child class
    def male(self):
        return "It's male"


class Female(Boss):  # child class
    def female(self):
        return "It's female"


m_obj = Male()
f_obj = Female()
print(m_obj.human())
print(f_obj.human())

# both of the childs are now calling the same method as they are inheritaed.

# #🔴Method calling
#
# must be a file of the same name of import
# import mth  # creating an object of the module

# print(mth.add(10, 2))
# print(mth.sub(10, 2))

# #🔴Package  / module -> 1?
#
# import test_package.test_result
# test_package.test_result.result()

# #🔴Package  / module ->2
# from test_package.test_result import result
# result()

# #🔴Package  / module ->3
# from test_package.test_result import result, another_method
# result()

# #🔴Package  / module ->4
# from test_package import test_result # now the (test_result) is obj of (test_package)
# test_result.result()

