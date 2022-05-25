list = []
sum = 0
n = int(input("Enter the length : "))
for i in range (n):
    ele = int(input("Enter the element : "))
    list.append(ele)
    if ele%2 == 0:
        sum = sum + ele
print("List are : ",list)
print("Sum of a list : ",sum)
