def CountUpperLower(s):
    u=l=0
    for i in s:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
    print(f"""
UpperCase : {u}
LowerCase : {l}""")

def Palindrome(s):
    if s==s[::-1]:
        #return True
        return "Palindrome"
    else:
        #return False
        return "Not Palindrome"    

def SumEvenOdd(l):
    e=o=0
    for i in l:
        if i%2==0:
            e+=i
        else:
            o+=i
    print(f"""
Sum Of Even : {e}
Sum Of Odd  : {o}""")
    
def CountWords(s):
    n=s.split()
    print(f"Number of Words : {n}")

def SumDigits(n):
    s=str(n)
    a=0
    for i in s:
        a+=int(i)
    return a

def CountVowelsConsonants(s):
    v=c=0
    for i in s:
        if i.lower() in "aeiou":
            v+=1
        elif i.lower() not in "aeiou" and i.isalpha():
            c+=1
    print(f"""
Vowels : {v}
Consonants : {c}""")

def Factorial(n):
    if n<0:
        return "Invalid!"
    elif n==0:
        return 1
    else:
        a=1
        for i in range(1,n+1):
            a*=i
        return a

def Fibbonaci(n):
    l=[0,1,1]
    first=1
    next=1
    for i in range(1,n+1):
        next=next+first
        first=next
        l.appened(next)
    return l

def PrimeCheck(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            break
    else:
        return True
    return False

def ReverseWords(s):
    r=s.split()
    g=''
    for i in r[::-1]:
        g+=i
    return g