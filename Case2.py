#Program 2 — Hospital Emergency Monitoring
#A hospital records the number of patients arriving in its emergency department during N consecutive
#hours. Determine:
#1. The maximum number of patients and the hour when it occurred.
#2. The minimum number of patients.
#3. The peak hour.
#4. The number of hours whose patient count is above the average.

patients=[]
n=int(input("Enter number of hours "))

for i in range(n):
     m=int(input("Enter number of patients "))
     patients.append(m)

maximum=patients[0]
minimum=patients[0]
max_hour=0
hours=0
for i in range(n):
    if patients[i]>maximum:
       maximum=patients[i]
       max_hour=i
       print("Patients",maximum,"in hours",max_hour)

    if patients[i]<minimum:
           minimum=patients[i]
           print("Patients",minimum)

average=int(sum(patients)//n) 
print("Peak hours are",average)
for i in patients:
     if i>average:
          hours=+1
print("Number of hours",hours)              
