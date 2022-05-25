d = {}
n = int(input("enter the length : "))
for i in range (n):
    a = int(input("Value of inner keys : "))
    for j in range (n):
        b = int(input())
        c = int(input())
        d.update({a:{b:c}})
print(d)
