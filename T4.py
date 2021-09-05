n = int(input())
sum = 0
colv = 0
proz = 1
n2 = n
last_d = n %10
while n != 0 :
    last_d1 = n % 10
    sum+=last_d1
    colv+=1
    proz*=last_d1
    n=n//10
sa =sum/colv

n1 = (n2//(10**(colv-1)))

print(sum)
print(colv)
print(proz)
print(sa)
print(n1)
print(n1+last_d)
