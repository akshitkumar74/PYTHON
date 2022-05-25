n = int (input("Enter any number : "))
square = n*n
sum = 0
while square > 0:
    rem = square % 10
    sum = sum + rem
    square = square // 10

if (n == sum):
    print("This is a neon number")

else:
    print("This is not a neon number")
