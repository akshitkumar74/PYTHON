list = []
n = int(input("Enter the length of list : "))
for i in range (n):
    tuple = ()
    for j in range (n):
        y = int(input())
        tuple += y,
    list.append(tuple)
print(list)