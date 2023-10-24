import wikipedia
import time
print("==========================================WIKIPEDIA SERCHER======================================")
summary=input("Enter the title you want to see summary :")
sentence=int(input("Enter the number of sentence you want :"))
result = wikipedia.summary(summary,sentence)
print(result)
print("========================================THANK YOU FOR USING========================================")
time.sleep(10000)
