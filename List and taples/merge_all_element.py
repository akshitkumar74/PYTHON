list = []
n = int(input("enter the length  : "))
for i in range (n):
    ele = int(input("Enter the element of first : "))
    list.append(ele)
print("Element in first list : ",list)

list1 = []
n1 = int(input("enter the length : "))
for i in range (n1):
    ele = int(input("Enter the element of second :"))
    list1.append(ele)
print("Element in second list : ",list)

a = zip(list,list1)
print(set(a))
