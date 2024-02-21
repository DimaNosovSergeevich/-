#coding: utf-8
#Задание 1
n = int(input("Введите количество чисел Фибоначи: "))
a,b = 0, 1
count = 0
while a < n:
    print(a)
    a, b = b, a + b

#Задание 2
n = 0
while n <= 20:
    print(n)
    n += 2
n = -1 
while n >= -21:
    if n % 3 == 0:
        print(n)
    n -= 1

#Задание 3
n = int(input())
l = 0
while n > 0:
    n //= 10
    l += 1
print(l)
