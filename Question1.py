# A university stores marks obtained by students in an examination in an array.The examination cell wants to identify the maximum sum of marks of marks obtained by students in a contiguous subarray. Write a python program to find the maximum sum of marks obtained by students in a contiguous subarray.
n=int(input("Enter number of students: "))
marks=[]
for i in range(n):
    m=int(input("Enter marks of student"))
    marks.append(m)
current=max_sum=marks[0]

for i in range(1,n):
    current=max(marks[i],current+marks[i])
    max_sum=max(max_sum,current)

print("Maximum sum of marks obtained by students in a contiguous subarray is:",max_sum)


