import time
print('''
      
░█▀▀▄░▀█▀░░░▒█▀▀█░▒█▀▀▄░█▀▀▄░▒█▀▀▄░▀▀█▀▀░▀█▀░▒█▀▀▄░█▀▀▄░▒█░░░░░░▒█▀▀█░▒█▀▀▄░▒█▀▀▀█░▒█▀▀█░▒█▀▀▄░█▀▀▄░▒█▀▄▀█░▒█▀▀▀█
▒█▄▄█░▒█░░░░▒█▄▄█░▒█▄▄▀▒█▄▄█░▒█░░░░░▒█░░░▒█░░▒█░░░▒█▄▄█░▒█░░░░░░▒█▄▄█░▒█▄▄▀░▒█░░▒█░▒█░▄▄░▒█▄▄▀▒█▄▄█░▒█▒█▒█░░▀▀▀▄▄
▒█░▒█░▄█▄░░░▒█░░░░▒█░▒█▒█░▒█░▒█▄▄▀░░▒█░░░▄█▄░▒█▄▄▀▒█░▒█░▒█▄▄█░░░▒█░░░░▒█░▒█░▒█▄▄▄█░▒█▄▄▀░▒█░▒█▒█░▒█░▒█░░▒█░▒█▄▄▄█
''')
a=True
while a==True:
  print('''
    1.To find average of 3 numbers
    2.To find greatest of 3 numbers
    3.To add elements of 2 lists
    4.Write a program to reverse the digits
    5.To a create a list of integers using for loop and 2 to every elements in a list
    6.To print sum of first 'n' even numbers
    7.To count vowels in given string
    
    ''')
  z=int(input('Enter the corresponding number to access the program : '))
  if z=='1':
    a=float(input("Enter number #1 to find average : "))
    b=float(input("Enter number #2 to find average : "))
    c=float(input("Enter number #3 to find average : "))
    d=(a+b+c)/3
    print("The average of",a,",",b,"&",c,"is",d)
  elif z=='2':
    a=float(input("Enter number #1 to find greatest : "))
    b=float(input("Enter number #2 to find greatest : "))
    c=float(input("Enter number #3 to find greatest : "))
    if (a>=b) and (a>=c):
        larg=a
    elif (b>=a) and (b>=c):
        larg=b
    elif (c>=a) and (c>=b):
        larg=c
    else:
        print("Envalid")
    print("Largest of ",a,"&",b,"&",c,"is",larg)
  elif z=='3':
    a=int(input("Enter the number of items you want to add to list 1 : "))
    b=[]
    for i in range(a):
        c=input("Enter the item you want to add in a list 1 : ")
        b.append(c)
        print(b)
    d=int(input("Enter amount of items you want to add to list 2 : "))
    e=[]
    for i in range(d):
       c=input("Enter the item you want to add in a list 1 : ")
       e.append(c)
       print(e)       
    b.append(e)
    print(b)
  elif z=='4':
    a=int(input("Enter the number to reverse its digits : "))
    print(str(a)[::-1])
  elif z=='5':
    a=int(input("Enter the number of items you want to add to a list : "))
    b=[]
    for i in range(a):
        c=float(input("Enter the item you want to items in a list : "))
        b.append(c)
        print(b)
    res=[x+2 for x in b]
    print(b,"+","2","="+str(res))
  elif z=='6':
    n=int(input("Enter the amount of numbers you want to sum of : "))
    total=0
    sum=(n*(n+1))/2
    print(sum)
  elif z=='7':
    a=input("Enter a string to find vowels in it : ")
    total=0
    for i in str(a):
        if (i=='a') or (i=='e') or (i=='i') or (i=='o') or (i=='u') or (i=='A') or (i=='E') or (i=='I') or (i=='O') or (i=='U'):

            total=total+1
    print("The amount of vowel in '",a,"' are ",total)
  else:
    print("INVALID")
time.sleep(999999999)