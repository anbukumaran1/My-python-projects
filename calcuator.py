import time
print("=========================================================================WELCOME TO USSR CALCULATOR===============================================================")

operator=input("Enter a oprator +,-,*,/,//(WHOLE NUMBER DIVION),%(REMINDER DIVISON):")
a=float(input("Enter a one number to oprate                                        :"))
b=float(input("Enter a one number to oprate                                        :"))
if operator=="+":
    print(a,"+",b,"=",a+b)
elif operator=="-":
    print(a,"-",b,"=",a-b)
elif operator=="*":
    print(a,"*",b,"=",a*b)
elif operator=="/":
    print(a,"÷",b,"=",a/b)
elif operator=="//":
    print(a,"÷",b,"=",a//b)
elif operator=="%":
    print(a,"÷",b,"=",a%b)

else:
    print("Ivalid enter a correct operator")
print("==================================================================THANK YOU FOR USING USSR CALCULATOR===============================================================")

time.sleep(10)
