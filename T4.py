a = int(input())
b = int(input())
sum, bigsum, num, bignum =0, 0, 0, 0
for i in range (a, b + 1):
    for j in range (1, i+1):
        if i//j == i/j:
            sum+=j
            num = i
    if sum> bigsum:
        bignum = num
        bigsum = sum
    if sum ==bigsum:
        bignum= max(num, bignum)
        bigsum=sum
    num, sum =0,0
print(bignum, bigsum)






