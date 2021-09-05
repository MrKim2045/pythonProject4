a=int(input())

total=0
while a!=0:
    if a>=25:
        total=total+1
        a-=25
    elif a>=10:
        total+=1
        a-=10
    elif a>=5:
        total+=1
        a-=5
    elif a>=1:
        total+=1
        a-=1
print(total)