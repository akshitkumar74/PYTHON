n = int(input("Enter any number : "))

temp = False

if(n>1):
    for i in range (2 , n):
        if(n%i==0):
            temp = True
            break

if (temp):
    print("This is not a Prime Number")

else:
    print("This is a Prime Number")
