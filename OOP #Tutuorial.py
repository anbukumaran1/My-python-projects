# # class HI():
# #     def __init__(self):
# #         pass
# #     def Hello(self):
# #         print("Hey")

# # l=HI()
# # print(type(l))
# # l.Hello()

# class Stack():
#     def __init__(self,l):
#         self=list(l)
#     def Push(self,obj):
#         self.appened(obj)
#     def Pop(self):
#         if self==[]:
#             return "UnderFlowError"
#         else:
#             item=list(self)
#             item2=item.pop()
#             self=item
#             return item2
#     def Display(self):
#         if self==[]:
#             print(self)
#         else:
#             for i in self[::-1]:
#                 print(i)
#     def Peek(self):
#         return self[-1]

# # s=Stack([1,2,3,4])
# # print(type(s))
# # r=s.Pop()
# # print(r)

# class stack():
#     def __init__(self):
#         self.items = []
#     def Push(self,item):
#         self.items.append(item)
#     def Pop(self):
#         if self==[]:
#             return "UnderFlowError"
#         else:
#             item=self.items.pop()
#             return item
#     def Display(self):
#         for i in self.items[::-1]:
#             print(i)
#     def Peek(self):
#         return self.items[-1]


# s=stack()
# s.Push(1)
# s.Push(2)
# s.Display()


class Stack(): #Intro
    Sample_Stack= [1,2,3,4,5,6,7]
    def __init__(self,l):
        self.items=list(l)
    def Push(self,object):
        self.items.append(object)
    def Display(self):
        if len(self.items)==1:
            print(self.items)
        elif len(self.items)==0:
            print(self.items)
        else:
            for i in self.items[::-1]:
                print(i)
    def Peek(self):
        return self.items[-1]
    def Pop(self):
        assert self.items!=[], "UnderFlowError"
        a=self.items.pop()
        return a
     # def Pop(self):
    #     if self.items!=[]:
    #         a=self.items.pop()
    #         return a
    #     else:
    #         #return "UnderFlowError"
    #         assert self.items!=[] , "UnderFlowError : Cant Remove the object as the stack is empty"
    
class Student(): #Class and instaance variavle
    class_year = 2024
    num_stu = 0#class variable can be used anywhere like with any class objecrt
    def __init__(self,name,section):
        self.name = name
        self.section = section #intanse varible can be only used on that paritcualr ibject of class
        Student.num_stu += 1

# student1= Student("ABC","B")
# stduent2= Student("XYZ","A")
# student3= Student ("PQR","X")

# print(student1.name)
# print(student1.num_stu)

#############INHERITANCE#####################

####SIMPLE
class animal():
    is_sleeping=False
    def __init__(self,name,is_alive=True):
        self.name = name
        self.is_alive = is_alive
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        if self.is_sleeping==False:
            print(f"{self.name} is sleeping")
            self.is_sleeping = True
        else:
            print(f"{self.name} is already sleeping")
    def wake(self):
        if self. is_sleeping:
            print(f"{self.name} is now awake")
            self. is_sleeping=False
        else:
            print(f"{self.name} is already awake")


class Dog(animal): #now the dog class inherits all the funcations and methods and attributes of the animal class
    pass

# s=Dog("Shesar")
# print(s.name)
# s.eat()
# s.sleep()
# s.sleep()

######MULTIPLE INHERITANCE

class Prey():
    def Flee(self):
        print(f"THis is Fleeing")

class Predator():
    def Hunt(self):
        print("TH is hunting")

class Fish(Prey,Predator): #Here the Fish can the functiona and methods of both Prey and Predator
    pass


#####ABSTRACT CLASS : These classes can only act as a parent class and cant be called or used on its own 

from abc import ABC,abstractmethod #needed to create absvate class

class vehicle(ABC): #makes this an abscrate class

    @abstractmethod #makes the method abscrate ie cant be called standanlone can be only using child class
    def go(self):
        pass #we must not define them now we must only define them in the child class

    @abstractmethod
    def stop(self):
        pass

class Car(vehicle):    #both the go and stop must 100% be there in the child class as well 
    def go(self):
        print("The car has started")
    def stop(self):
        print("The car has stoped")


#####SUPER FUNCTIONS : Allows us to extend the functionaly of inherite methods


class Circles():
    num_side = "inf"
    def __init__(self,color,filled,radius):
        self.color = color
        self.filled = bool(filled)
        self.radius = radius
class Square():
    num_side = 4
    def __init__(self,color,filled,side):
        self.color = color
        self.filled = filled
        self.side = side
class Triangle():
    num_side = 3
    def __init__(self,color,filled,base,height):
        self.color = color
        self.filled = filled
        self.base = base
        self.height = height

class Shape():
    def __init__(self,color,filled):
        self.color = color
        self.filled = bool(filled) 
    def Describe(self):
        print(f"IT is {self.color} in color and it {"filled" if self.filled else "Not Filled"}")

class Circles1(Shape):
    num_side = "inf"
    def __init__(self,color,filled,radius):
        super().__init__(color,filled) #we can replace that redundant code with a super function
        self.radius = radius 
    def Describe(self):  #now the function at the child level is executed and it called method over writing 
        print(f"The Area is {3.14*self.radius**2} cm^2") #only the code at the child level is extecuted and not the parent code
class Square1(Shape):
    num_side = 4
    def __init__(self,color,filled,side):
        super().__init__(color,filled)
        self.side = side
    def Describe(self):
        super().Describe() #Now the code of the parent as well as the child is executed
        print(f"The Area is {self.side**2} cm^2")

class Triangle1(Shape):
    num_side = 3
    def __init__(self,color,filled,base,height):
        super().__init__(color,filled)
        self.base = base
        self.height = height

