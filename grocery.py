import time
print("=============================================Welcome to smart shoppe====================================================")
budget=float(input("Enter the amount of money you want to spend on shopping :"))
if budget =>2000:
    print("You have a good amount of money in hands you can order anything you want")
    a=int(input("Enter your amount of grocery item :"))
                  
    
    n=[]
    for i in range(a):
          s=input("Enter your grocery item :")
          n.append(s)
          print("Your grocery list is :",n)
elif budget =<1000:
    print("Spend your money with little care")
     
    a=int(input("Enter your amount of grocery item :"))
  
    n=[]
    for i in range(a):
          s=input("Enter your grocery item :")
          n.append(s)
          print("Your grocery list is :",n)
elif budget =< 500:
    print("Spend your money carefully")
     
    a=int(input("Enter your amount of grocery item :"))
  
    n=[]
    for i in range(a):
          s=input("Enter your grocery item :")
          n.append(s)
          print("Your grocery list is :",n)
elif budget =<100:
    print("Spend your money extremly carefully")
     
    a=int(input("Enter your amount of grocery item :"))
  
    n=[]
    for i in range(a):
          s=input("Enter your grocery item :")
          n.append(s)
          print("Your grocery list is :",n)
print("============================================Thank you for using smart shoppe==============================================")



time.sleep(1000)
