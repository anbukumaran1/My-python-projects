import time
print("""  

░█░░█▀▀░█▀▀▄░█▀▀▀░▀█▀░█░░░░░░█▀▄░▄▀▀▄░█▀▀▄░▄░░░▄░█▀▀░▀█▀░█▀▀░█▀▀▄
░█░░█▀▀░█░▒█░█░▀▄░░█░░█▀▀█░░░█░░░█░░█░█░▒█░░█▄█░░█▀▀░░█░░█▀▀░█▄▄▀
░▀▀░▀▀▀░▀░░▀░▀▀▀▀░░▀░░▀░░▀░░░▀▀▀░░▀▀░░▀░░▀░░░▀░░░▀▀▀░░▀░░▀▀▀░▀░▀▀








""")







print("""
1.Kilo meter 
2.Meter
3.Centimeter
4.Millimeter
5.Miles                  
          """)
ch=int(input("Enter the quantity to convert  : "))
ch1=int(input("Enter the quantity to convert to : "))
if ch ==1 and ch1 ==2:
    c=float(input("Enter the mass in kg to convert to meter : "))
    d=c*1000
    print(d)
if ch ==1 and ch1 ==3:
    c=float(input("Enter the mass in kg to convert to centimeter : "))
    d=c*100000
    print(d)
if ch ==1 and ch1 ==4:
    c=float(input("Enter the mass in kg to convert to millimeter : "))
    d=c*1000000
    print(d)
if ch ==1 and ch1 ==5:
    c=float(input("Enter the mass in kg to convert to miles : "))
    d=c*0.62137119
    print(d)
if ch ==2 and ch1 ==1:
    c=float(input("Enter the mass in meter  to convert to kilometer : "))
    d=c*0.001
    print(d)
if ch ==2 and ch1 ==3:
    c=float(input("Enter the mass in meter  to convert to centiometer : "))
    d=c*100
    print(d)
if ch ==2 and ch1 ==4:
    c=float(input("Enter the mass in meter  to convert to millimeter : "))
    d=c*1000
    print(d)
if ch ==2 and ch1 ==5:
    c=float(input("Enter the mass in meter  to convert to miles : "))
    d=c*0.00062137
    print(d)
if ch ==3 and ch1 ==1:
    c=float(input("Enter the mass in centimeter  to convert to kilometer : "))
    d=c*0.00001
    print(d)
if ch ==3 and ch1 ==2:
    c=float(input("Enter the mass in centimeter  to convert to meter : "))
    d=c*100
    print(d)    
if ch ==3 and ch1 ==4:
    c=float(input("Enter the mass in centimeter  to convert to millimeter : "))
    d=c*10
    print(d)    
if ch ==3 and ch1 ==5:
    c=float(input("Enter the mass in centimeter  to convert to miles : "))
    d=c*0.00000621
    print(d)    
if ch ==4 and ch1 ==1:
    c=float(input("Enter the mass in millimeter  to convert to kilomter : "))
    d=c*0.000001
    print(d) 
if ch ==4 and ch1 ==2:
    c=float(input("Enter the mass in millimeter  to convert to mter : "))
    d=c*0.001
    print(d)   
if ch ==4 and ch1 ==3:
    c=float(input("Enter the mass in millimeter  to convert to centimter : "))
    d=c*0.1
    print(d) 
if ch ==4 and ch1 ==5:
    c=float(input("Enter the mass in millimeter  to convert to miles : "))
    d=c*6.2137E-7
    print(d) 
if ch ==5 and ch1 ==1:
    c=float(input("Enter the mass in miles  to convert to kilometer : "))
    d=c*1.609344
    print(d) 
if ch ==5 and ch1 ==2:
    c=float(input("Enter the mass in miles  to convert to meter : "))
    d=c*1609.344
    print(d) 
if ch ==5 and ch1 ==3:
    c=float(input("Enter the mass in miles  to convert to centimeter : "))
    d=c*160934.4
    print(d) 
if ch ==5 and ch1 ==4:
    c=float(input("Enter the mass in miles  to convert to millimeter : "))
    d=c*1.6093E+6
    print(d) 
