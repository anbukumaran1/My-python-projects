import time
print("====================================================================WELCOME TO STONE PAPER SCISSORS GAME PLS USE CAPS========================================================================================")
item=input("ENTER STONE,PAPER OR SCISSORS      :")
auto=input("ENTER A RANDOM COMPUTER PATH(A,B,C):")
if auto=="A":
   if item=="STONE":
       print("THE COMPUTER CHOSE STONE")
       print(" draw")
   elif item=="PAPER":
       print("THE COMPUTER CHOSE STONE")
       print("YOU WON")
   elif item=="SCISSORS":
       print("THE COMPUTER CHOSE STONE")
       print("YOU LOST TRY AGAIN")
   else:
        print("INVALID")
elif auto=="B":
   if item=="STONE":
       print("THE COMPUTER CHOSE PAPER")
       print("YOU LOST")
   elif item=="PAPER":
       print("THE COMPUTER CHOSE PAPER")
       print("DRAW")
   elif item=="SCISSORS":
       print("THE COMPUTER CHOSE PAPER")
       print("YOU WON")
   else:
        print("INVALID")
elif auto=="C":
   if item=="STONE":
       print("THE COMPUTER CHOSE SCISSORS ")
       print("YOU WON")
   elif item=="PAPER":
        print("THE COMPUTER CHOSE SCISSORS ")
        print("YOU LOST")
   elif item=="SCISSORS":
        print("THE COMPUTER CHOSE SCISSORS ")
        print("DRAW")
   else:
        print("INVALID")
else:
        print("INVALID")

print("*******************************************************************************************THANK YOU FOR PLAYING***********************************************************************************************")
time.sleep(10)
