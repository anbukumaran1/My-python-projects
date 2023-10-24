import wikipedia

print(""" FUNCTIONS I CAN DO FOR YOU 
1.Search tile 
2.Summary 
3.Essay (short)
4.Full details 
""")


a=int(input("Enter the number of function you want to see : "))
if a== 1:
    c=input("Enter the title you want to search for : ")
    print(wikipedia.search(c))
elif a==2:
    c=input("Enter the title you want to search for : ")
    d=input("Enter the amount of sentence you want  : ")
    print(wikipedia.summary(c, sentences=d))  
elif a==3:
    c=input("Enter the title you want to search for : ")
    print(wikipedia.page(c).content)  
elif a==4:
    c=input("Enter the title you want to search for : ")
    object = wikipedia.page(c)
    print(object.html)  
    print(object.original_title)  
    print(object.links[0:20])  
    
