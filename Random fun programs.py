import time
print('''
      
░█▀▀▄░▀█▀░░░▒█▀▀█░▒█▀▀▄░█▀▀▄░▒█▀▀▄░▀▀█▀▀░▀█▀░▒█▀▀▄░█▀▀▄░▒█░░░░░░▒█▀▀█░▒█▀▀▄░▒█▀▀▀█░▒█▀▀█░▒█▀▀▄░█▀▀▄░▒█▀▄▀█░▒█▀▀▀█
▒█▄▄█░▒█░░░░▒█▄▄█░▒█▄▄▀▒█▄▄█░▒█░░░░░▒█░░░▒█░░▒█░░░▒█▄▄█░▒█░░░░░░▒█▄▄█░▒█▄▄▀░▒█░░▒█░▒█░▄▄░▒█▄▄▀▒█▄▄█░▒█▒█▒█░░▀▀▀▄▄
▒█░▒█░▄█▄░░░▒█░░░░▒█░▒█▒█░▒█░▒█▄▄▀░░▒█░░░▄█▄░▒█▄▄▀▒█░▒█░▒█▄▄█░░░▒█░░░░▒█░▒█░▒█▄▄▄█░▒█▄▄▀░▒█░▒█▒█░▒█░▒█░░▒█░▒█▄▄▄█
''')
print('''
1.A program to find average of 3 numbers
2.A program to find biggest of 3 numbers
3.A program to add elements of 2 list
4.A program to reverse the digits 
5.To create a list of integers using for loop and add 2 to every element in list
6.To print sum of even numbers upto n
7.To count vowels in a string
''')

choice=int(input("Enter your choice: "))
if choice==1:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    num3=int(input("Enter third number: "))
    average=(num1+num2+num3)/3
    print("Average of 3 numbers is: ",average)
elif choice ==2:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    num3=int(input("Enter third number: "))
    if (num1>=num2) and (num1>=num3):
        print("The biggest number",num1)
    elif (num2>=num1) and (num2>=num3):
        print("The biggest number",num2)
    else:
        print("The biggest number",num3)
elif choice ==3:
    a=[]
    b=[]
    c=int(input("Enter amount of items : "))
    for i in range(c):
        a.append((input("Enter the number you want to add : ")))
        print(a)
    for i in range(c):
        b.append((input("Enter the number you want to add : ")))
        print(b)
    a.extend(b)
    print(a)
elif choice ==4:
    a=int(input("Enter the number you want to reverse : "))
    b=str(a)[::-1]
    print(b)
elif choice ==5:
    a=int(input("Enter the number you want to add : "))
    b=[]
    for i in range(a):
        c=int(input("Enter the number you want to add to list : "))
        b.append(c)
        print(b)
    r=[x+2 for x in b]
    print(r)

elif choice ==6:
    a=int(input("Enter the number you want to add : "))
    r=a*(a+1)
    print(r)
elif choice ==7:
    s=input("Enter the string : ")
    a=0
    for i in s:
        if i in "aeiouAEIOU":
            a=a+1
    print(a)
else:
    print("INVALID choice")
time.sleep(1000000)

