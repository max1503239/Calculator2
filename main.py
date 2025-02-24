import math
a = int(input("Введите , пожалуйста , число:"))
b = input("Введите операцию:")
c = int(input("Введите , пожалуйста , второе число:"))
if b == '%':
    print(a%c)
if b == '**':
    print(a**c)
if b == '√':
    print(math.sqrt(a))
a = int(input())
def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n