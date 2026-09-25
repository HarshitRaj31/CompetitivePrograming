#Program 3 — Student Name Search
#A university maintains a list of N student names. Given a name to search, determine whether the
#student exists and display their position.
#The program should support:
#1. Case-sensitive search — "Priya" and "priya" are different.
#2. Case-insensitive search — "Priya" and "priya" are considered the same.
n=int(input("Enter Number of Students "))
students=[]
for i in range(n):
    m=input("Enter name of students ")
    students.append(m)
search=input("Enter the name of student ")

for i in range(n):
    if search==students[i]:
       print("Student found")
       break
if students is not search:
   print("Student not found")  

for i in range(n):
    if search.lower()==students[i].lower():
       print("Student found")
       break
if students is not search:
   print("Student not found")  

