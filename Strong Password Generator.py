#strong password generator

from random import *
from time import *

d={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z",27:"A",28:"B",29:"C",30:"D",31:"E",32:"F",33:"G",34:"H",35:"I",36:"J",37:"K",38:"L",39:"M",40:"N",41:"O",42:"P",43:"Q",44:"R",45:"S",46:"T",47:"U",48:"V",49:"W",50:"X",51:"Y",52:"Z"}

while True:
    print("Press enter to generate a strong password (or any key to exit)")
    a=input(">>>")
    if a=="":
        print("Your strong password is :")
        s=''
        for i in range(1,21):
            r=randint(1,52)
            s+=d[r]

        print(s)


    else:
        break

sleep(10000000)
