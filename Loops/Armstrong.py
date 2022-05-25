n = int(input("Enter any number : "))
store = 0
t = n 
while (t>0):
    digit = t % 10
    store += digit**3
    t = t // 10

if (n==store):
    print("This number is an Armstrong")
else:
    print("This number is not  an Armstrong")
