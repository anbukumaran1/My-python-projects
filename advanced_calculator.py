import math
import time
print("""
░▒█▀▀▀█░▒█░▒█░▒█▀▀█░▒█▀▀▀░▒█▀▀▄░░░▒█▀▀▄░█▀▀▄░▒█░░░░▒█▀▀▄░▒█░▒█░▒█░░░░█▀▀▄░▀▀█▀▀░▒█▀▀▀█░▒█▀▀▄
░░▀▀▀▄▄░▒█░▒█░▒█▄▄█░▒█▀▀▀░▒█▄▄▀░░░▒█░░░▒█▄▄█░▒█░░░░▒█░░░░▒█░▒█░▒█░░░▒█▄▄█░░▒█░░░▒█░░▒█░▒█▄▄▀
░▒█▄▄▄█░░▀▄▄▀░▒█░░░░▒█▄▄▄░▒█░▒█░░░▒█▄▄▀▒█░▒█░▒█▄▄█░▒█▄▄▀░░▀▄▄▀░▒█▄▄█▒█░▒█░░▒█░░░▒█▄▄▄█░▒█░▒█
""")
print("""
1.Calculator 
2.Convertor
""")
def add():
    a=float(input("Enter the first number : "))
    b=float(input("Enter the second number : "))
    print(a,'+',b,'=',a+b)
def sub():
    a=float(input("Enter the first number : "))
    b=float(input("Enter the second number : "))
    print(a,'-',b,'=',a-b)
def mutiply():
    a=float(input("Enter the first number : "))
    b=float(input("Enter the second number : "))
    print(a,'x',b,'=',a*b)
def da():
    a=float(input("Enter the first number : "))
    b=float(input("Enter the second number : "))
    print(a,'/',b,'=',a//b)
def db():
    a=float(input("Enter the first number : "))
    b=float(input("Enter the second number : "))
    print(a,'/',b,'=',a/b)
def dc():
    a=float(input("Enter the first number : "))
    b=float(input("Enter the second number : "))
    print(a,'/',b,'=',a%b)
def sq():
    a=float(input("Enter the  number you want to square : "))   
    print(a,"^2","=",a**2)
def root():
    a=float(input("Enter the  number you want to square root : "))   
    print(a,"^0.5","=",a**0.5)
def proot():
    a=float(input("Enter the first number : "))
    b=float(input("Enter the second number : "))
    print(a,'^',b,'=',a**b)
def log10():
    log = float(input("Enter the number to find log base 10 : "))
    print("The log base 10 of ",log, "is",math.log10(log))
def loge():
    log = float(input("Enter the number to find log base e : "))
    print("The log base e of ",log, "is",math.log(log))
def sin():
    log = float(input("Enter the number to find sine : "))
    print("The sine of ",log, "is",math.sin(log))
def cos():
    log = float(input("Enter the number to find cos : "))
    print("The cosine of ",log, "is",math.cos(log))
def tan():
    log = float(input("Enter the number to find sine : "))
    print("The tangent of ",log, "is",math.tan(log))
def asin():
    log = float(input("Enter the number to find asine : "))
    print("The sine of ",log, "is",math.asin(log))
def acos():
    log = float(input("Enter the number to find acos : "))
    print("The acosine of ",log, "is",math.acos(log))
def atan():
    log = float(input("Enter the number to find atan : "))
    print("The atangent of ",log, "is",math.atan(log))
    
a=int(input("Enter the number of the program you want to use : "))
if a==1:
    print("""
         1.Standard Calculator
         2.Scientific Calculations""")
    b=int(input("Enter the number of program you want to use :" ))
    if b==1:
        print("""
1.Addition
2.Subraction
3.Multiplication
4.Division : (a)Integer division (b)Decimal (c)Remainder
5.square
6.Square root
7.Power
8.Power root
 """)
        c=int(input("Enter the number of program you want to use :"))
        if c==1:
            add()
        if c==2:
            sub()
        if c==3:
            mutiply()
        if c=='4a':
            da()
        if c=='4b':
            db()
        if c=='4c':
            dc()
        if c==5:
            sq()
        if c==6:
            root()
        if c==7:
            proot()
        else:
            print("Invalid")
    if b==2:
        print("""
1.Log base 10
2.Log base e (natural log )
3.Sine
4.Cosine
5.Tangent
6.Asine
7.Acosine
8.Atangent
""")
        d=int(input("Enter the number of program you want to use :"))
        if d==1:
            log10()
        if d==2:
            loge()
        if d==3:
            sin()
        if d==4:
            cos()
        if d==5:
            tan()
        if d==6:
            asin()
        if d==7:
            acos()
        if d==8:
            atan()
        else:
            print("Invalid")
    else:
        print("Invalid")

time.sleep(10000000)