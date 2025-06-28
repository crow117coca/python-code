import random

playing = True
number = str(random.randint(10,20))

print("i will genrate a number from 0-9, and you have to gess the digiet 1 at a timr")
print("the game will end when you get 1 hero")
while playing:
    gess=input("give me your best gess! \n")
    if number == gess:
        print("you win")
        print("the number was" ,number)
    break
else:
    print("this isent quit right try agian \n")