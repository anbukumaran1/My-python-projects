import time

a=[]
b=int(input("Enter the amount of books you want to save : "))

for i in range(b):
    c=input("Enter the name of book or note you want to add : ")
    a.append(c)
    print(a)
    
print("The total book list you have added ",a)

with open('a', 'w') as file:
    file.write(str(a))

