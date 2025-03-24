from time import *

def countdown(t):
    print(f"Timer set to {t} seconds .")
    sleep(t)
    print("Time's up!")

t = int(input("Enter the time in seconds: "))
countdown(t)
