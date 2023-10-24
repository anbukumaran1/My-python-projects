print ("***********************************************************WELCOME TO LEAVE LETTER GENARATOR*********************************************")
import time
name=input("Enter your name :")

reason=input("Enter your reason for taking leave :")
days=input("Enter the number of days you took leave :")
when=input("Enter when to when you took leave(date and day) :")
clas=input("Enter your class and section :")
school=input("Enter your school name :")
date=input("Enter todays date")

print("Date:",date,"\n","To,\n","The Class teacher\n\n",school,"\n","Dear Sir/Mam,\n","Subject:","Reason for talking leave\n","I am",name, "a student of", clas,"."," I want to bring to your kind attention that due to",reason, "I am unable to come to school from",when,"\n","I request you to forgive for taking leave on the  the dates mentioned above kindly. I assure you that I will catch up with my studies after coming back. I shall be grateful.\n","Thank you.","Yours faithfully,\n",name)
print("**********************************************************THANK YOU FOR USING OUR PROGRAM**************************************************")
time.sleep(200)