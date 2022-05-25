a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
d = int(input("Enter the fourth number : "))

if (a>b and a>c and a>d):
    print("greatest number is",a)
elif(b>a and b>c and b>d):
    print("greatest number is",b)
elif(c>b and c>d and c>a):
    print("greatest number is",c)
elif(d>a and d>b and d>a):
    print("greatest number is",d)