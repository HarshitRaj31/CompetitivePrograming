#Swap two integers a and b using the XOR operator without using a temporary
#variable.
a=5
b=9
a=a^b
b=a^b
a=a^b
print("After Swaping =",a,b)