import time
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def divide(x,y):
    return x/y
def multiply(x,y):
    return x*y
def power(x,y):
    return x**y
def reminder(x,y):
    return x%y
while True:
    try:
        a=float(input("Enter the first number : "))
        b=float(input("Enter the second number : "))
    except Exception:
        print("Something Went Wrong Try Again!")
    except TypeError:
        print("Please Enter a valid number")
    except ValueError:
        print("Please Enter a correct value")
    else:
        print(add(a,b))
        print(sub(a,b))
        print(multiply(a,b))
         
        print(power(a,b))
        print(reminder(a,b))
    try:
        print(divide(a,b))
        print(reminder(a,b))
    except ZeroDivisionError:
        print("Please Enter a valid second number. It can't be zero.")
