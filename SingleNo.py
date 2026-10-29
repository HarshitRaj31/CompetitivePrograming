#Given a list of integers in which every element appears twice except one, find the
#element that appears only once.
arr=[1,2,2,3,4]
unique=0
for num in arr:
    unique^=num
print(unique)    