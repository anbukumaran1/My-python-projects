from time import *
from random import *

print("=================================BOGO SORTER===========================")

def bogo(li):
    for i in range(len(li)):
        r=randint(0,len(li)-1)
        li[i],li[r]=li[r],li[i]
    return li

lis=eval(input("Enter a list to sort : "))
n="Searching for Match"

while True:

    sl=bogo(lis)
    if sl==sorted(lis):
        print(f"Match found  : {sl}")
    else:
        n = n + '.'
        print(n)
        sleep(0.25)

sleep(99999)
