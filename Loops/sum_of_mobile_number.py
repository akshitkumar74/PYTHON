n = int(input("Enter Your number : "))
sum=0
while (n!=0):
    sum = sum + int(n%10)
    n = int(n/10)
print("The same of your number :", sum)