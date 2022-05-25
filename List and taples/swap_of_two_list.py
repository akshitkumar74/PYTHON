list = []
n = int(input("enter the length  : "))
for i in range (n):
    ele = int(input("Enter the element of first : "))
    list.append(ele)
print("Swap For first are : ",list)
    
list1 = []
n1 = int(input("enter the length  : "))
for i in range (n1):
    ele = int(input("Enter the element of second : "))
    list1.append(ele)
print("Swap For second are : ",list1)

list2=list1
list1=list
list=list2

print("Swap are first : ",list)
print("Swap are second : ",list1)


