list = []
for i in range (3):
    list1 =[]
    for j in range (3):
      list1.append(int(input()))
    list.append(list1)
for i in range (3):
    for j in range (3):
        print(list[i][j], end=' ')
    print()
for i in range(3):
    for j in range(3):
        if ( i == 3//2 and j == 3//2):
            print(" ",end=" ")
        else:
            print(list[i][j],end=" ")
    print()