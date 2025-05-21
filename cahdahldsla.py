choice=input("enter your word:")
char=input("which letter")
i=0
count=0
while(i<len(choice)):
    if(choice[i] == char):
        count = count + 1
    i=i+1
print("the total number of times",char,"has occored =",count)