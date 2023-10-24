import time

a=int(input("Enter side one of a Triangle:       "))
b=int(input("Enter side Two of a Triangle:       "))
c=int(input("Enter side Three of a Triangle:      "))
h=int(input("Enter a side hieght of pyramid:        "))
l=int(input("Enter the slant height of the pyramid:  "))
print("***********************************************\n")
print("*********HERON FORMULA*************\n")
peri=(a+b+c)
s=peri/2
g=(s*(s - a)*(s - b)*(s - c))**0.5
volume=(1/3*g*h)
area=(g+12*(peri*l))
print("The are of triangle with sides",a,",",b,",",c,"is",g,"\nThe perimeter of triangle is",peri,"\nvolume of pyramid is",volume,"\nThe area of pyramid is",area)
print("***********************************************\n")
time.sleep(10)
