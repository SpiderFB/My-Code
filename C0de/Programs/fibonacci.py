# a = 0
# b = 1
# c = a + b
# print (a)
# print (b)
# for i in range(1, 10):
#     print (c)
#     a = b
#     b = c
#     c = a + b

def fibonacci(n):
    l = [0, 1]
    for i in range(2, n+1):
        h = l[-1] + l[-2]
        l.append(h)
    return l


print(fibonacci(15))
