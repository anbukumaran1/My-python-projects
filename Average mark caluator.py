import time
name=input("Enter your name")
clas=input("Enter your class")
hindi=float(input("Enter your hindi mark"))
english=float(input("Enter your english mark"))
science=float(input("Enter your science mark"))
ai=float(input ("Enter your ai mark"))
social=float(input("Enter your social mark"))
maths=float(input("Enter your maths mark"))
print("Hi",name,"Your resuts are below:")
sum=(hindi+english+science+ai+social+maths)
average=sum/5
print("Your average mark is ",average)
time.sleep(100)