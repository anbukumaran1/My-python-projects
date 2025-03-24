from time import *

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def pow(a,b):
    return a**b
def log(a,b):
    return log(a,b)

while True:
    print("Press Enter access the program")
    a=input(">>>")

    if a!='':
        break
    else:
        print(
            """
 1.Add
 2.Subract
 3.Multiply
 4.Divide
 5.Modulus
 6.Power
 7.Log
           
            """)
        try:

           b=float(input("Enter number 1 : "))
           c=float(input("Enter number 2 : "))
           cho=int(input("Enter your choice : "))
           if cho==1:
               print(add(b,c))
           elif cho==2:
                print(sub(b,c))
           elif cho==3:
                print(mul(b,c))
           elif cho==4:
               print(div(b,c))
           elif cho==5:
               print(mod(b,c))
           elif cho==6:
               print(pow(b,c))
           elif cho==7:
               print(log(b,c))
           else:
               print("Invalid choice")
        except TypeError as t:
            print("Please enter a number ")
            print(t)
        except ZeroDivisionError as z:
            print("Can't divide by zero")
        except ValueError as v:
            print("Please enter a valid number")
        except Exception as e:
            print(e)

sleep(9999999)