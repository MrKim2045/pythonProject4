total = 0
max1 = 0
min1 = 9
n =  int(input())
while n > 0:
    total = n % 10
    if total > max1:
        max1 = total
    if total < min1:
        min1 = total
    n = n//10
print('Максимальная цифра равна', max1)
print('Минимальная цифра равна', min1)


