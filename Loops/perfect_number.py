n = int(input("Enter the number : "))
sum = 0
i = 1

while (n>i):
    if(n%i==0):
        sum = sum +i
    i = i +1 
if (sum == n):
    print("This is a Perfect number")

else:
    print("This is not a Perfect number")
