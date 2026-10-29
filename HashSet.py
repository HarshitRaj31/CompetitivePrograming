#Given a list of integers, remove duplicate elements while preserving the order of
#their first occurrence.
num=[4,2,3,4,1,6,7]
seen=set()
result=[]
for i in num:
    if num not in seen:
        seen.add(num)
        result.append(num)
print("After removing duplicate ",result)        
