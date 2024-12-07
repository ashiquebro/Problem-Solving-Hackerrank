from collections import OrderedDict
n=int(input())

order=OrderedDict()
for item in range(n):
    item,price=input().rsplit(' ', 1)
    price=int(price)
    if item in order:
        order[item]+=price
    else:
        order[item]=price
for item,price in order.items():
    print(item,price)       