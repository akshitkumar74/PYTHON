list = []
for i in range (3):
    list1 = []
    for j in range (3):
        list1.append(int(input()))
    list.append(list1)
for i in range (3):
    for j in range (3):
        print(list[i][j], end=' ')
    print()
print("Result ---->")
for i in range (3):
    for j in range (3-i):
        print(list[i][j], end=' ')
    print()
        
