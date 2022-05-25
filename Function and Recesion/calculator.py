def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

n = int(input("Enter for first value : "))
n1 = int(input("Enter for second value : "))

print('''For Additition (a)
For Subtraction (s)
For Multipication (m)
For Divide (d) ''')

you = input("Choice one a/s/m/d : ")

if you == "a":
    print(f"{n} + {n1} = ",add(n,n1))
elif you == "s":
    print(f"{n} - {n1} = ",sub(n,n1))
elif you == "m":
    print(f"{n} x {n1} = ",mul(n,n1))
elif you == "d":
    print(f"{n} / {n1} = ",div(n,n1))
else:
    print("Invalid input")

