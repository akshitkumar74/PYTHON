n = int(input())
list = []
for i in range (n):
    list1 = []
    for j in range (n):
        list1.append(int(input()))
    list.append(list1)
for i in range (n):
    for j in range (n):
        print(list[i][j],end=" ")
    print()
print("result ---->")
for i in range (n):
    for j in range (n):
        if (i==j):
            print(list[i][j],end=" ")
    print() 