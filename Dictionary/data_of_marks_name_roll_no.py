n = int(input("Enter the number of students : "))
d = {}
for i in range (1 ,n+1):
    name = input(f"Enter the name of a student of Roll-No {i} : ")
    marks = int(input(f"Enter the marks of a student of Roll-No {i}: "))
    d.update({i : {'Name':name , 'Marks':marks}})
sum = 0
for i in range (1,n+1):
    sum = sum + d[i]['Marks']
print(sum)
