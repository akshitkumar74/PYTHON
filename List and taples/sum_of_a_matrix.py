n = int(input("Enter the length for first : "))
list = []
for i in range (n):
    list1 = []
    for j in range (n):
        list1.append(int(input()))
    list.append(list1)
for i in range(n):
    for j in range (n):
        print(list[i][j],end=" ")
    print()
n1 = int(input("Enter the length for second : "))
list2 = []
for i in range (n1):
    list3 = []
    for j in range (n1):
        list3.append(int(input()))
    list2.append(list3)
for i in range(n1):
    for j in range (n1):
        print(list2[i][j],end=" ")
    print()
print("Result --->")
for i in range(n):
   for j in range(n):
      print(list2[i][j], end=" ")
   print()                                            
result = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(n):    
    for j in range(len(list[0])): 
        result[i][j] = list[i][j] + list2[i][j] 
print()
for r in result: 
   print(r)