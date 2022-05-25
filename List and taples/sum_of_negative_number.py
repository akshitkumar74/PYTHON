list = []
sum = 0
n = int(input("Enter the length : "))
for i in range (n):
    ele = int(input("Enter the element : "))
    sum = sum + ele
    list.append(ele)

print("list are : ",list)
print("Sum of a list : ",sum)