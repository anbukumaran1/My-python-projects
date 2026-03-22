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


class Stack():
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
    


