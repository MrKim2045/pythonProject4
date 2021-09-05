from math import *
a, k = input(), 0
while a not in ('стоп', 'хватит', 'достаточно'):
    k += 1
    a = input()
print(k)

t = int(input())
while t%7 == 0:
    print(t)
    t = int(input())