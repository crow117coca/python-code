choice=int(input("are you available in school today?"))
if choice=="y":
    e=input("will you give to exam?")
    if e=="yes":
        print("you are alllowed to the exam")
    else:
        print("your not allowed to the exam")
else:
    print("you not in schoool so you cant take the exam")