import math
balance = int(input("Ваш баланс в начале года ") )
iphone_price = 120000
coffee_price = 50
print(iphone_price)
x =12
zp = int(input("Ежемесячный остаток от зарплаты "))
balance = balance+zp*x

print(balance,"В конце года")
if balance > iphone_price:
  print("УРА! Я могу позволить себе Айфон. ")
else:
  print("Я не смогу позволить себе Айфон. =(((")
  nd=iphone_price - balance
  print("Вам не хватает",iphone_price - balance)
  nw=nd/zp
  math.ceil (nw, )
  print((nw) , "Месяцев нужно работать")
print("Ваш баланс к концу года", balance)
