# >>> from collections import Counter
# >>> 
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>> 
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>> 
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]


n=int(input())
size=list(map(int,input().split(" ")))
price2=0
n2=int(input())
for i in range(n2):
   size2, price=list(map(int,input().split(" ")))
   if size2 in size:
      price2+=price
      size.remove(size2)

print(price2)
      

# for i in range(n):
#     if len(size)==n:
#       list2=size 
#       break
# print(list2)
      

# print(list2)
# list2=set(list2)
# print(list2)
# n2=int(input())
# pairs=[]
# for i in range(n2):
#     size2, price=map(int,input().split(" "))
#     pairs.append((size2,price))
# total_price=0
# for item in pairs:

#     if item[0] in list2:
#         total_price += item[1]

# #print(pairs)
# print(total_price)

        

    