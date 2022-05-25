import random

def system(com ,you):
    if com == you:
        return None

    elif com == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    
    elif com == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    
    elif com == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True

print("comp turn : Rock(r) Paper(p) Or Scissor(s)")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'
    
you = input("comp turn : Rock(r) Paper(p) Or Scissor(s) : ")

a = system(comp , you)

print(f"Computer chose : {comp}")
print(f"You chose : {you}")

if a == None:
    print("Game tie !")
elif a:
    print("You Win !")
else:
    print("You Lose !") 

