n = int(input("Enter the number : "))
rem = 0
temp = n
total = 0
while (temp):
    rem = temp % 10
    fact = 1
    while (rem):
        fact = fact*rem
        rem = rem - 1
    total = total + fact 
    temp = temp // 10
if (total == n):
    print("This is a strong number")
else:
    print("This is not a strong number")


