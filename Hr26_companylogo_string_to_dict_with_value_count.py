from collections import Counter
string='aaabbbdddcc'
string.lower()
ch_count=Counter(string)
#print(ch_count)
dict2=(sorted(ch_count.items(), key=lambda x:x[1],reverse=True))
dict3=dict(dict2 [:3])
#print(dict2)
for x, y in dict3.items():
    print(f"{x} {y}")


from collections import Counter
string=(input())
string.lower()
ch_count=(Counter(string))
ch_count=dict(sorted(ch_count.items()))
#print(ch_count)
dict2=(sorted(ch_count.items(), key=lambda x:x[1],reverse=True))
dict3=dict(dict2 [:3])

#print(dict2)
for x, y in dict3.items():
    print(f"{x} {y}")
