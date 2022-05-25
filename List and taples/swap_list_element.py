list = []
n = int(input("enter the length  : "))
for i in range (n):
    ele = int(input("Enter the element of first : "))
    list.append(ele)
print("Swap For first are : ",list)

# c= b[0:2] + a [2:]
# d = a      +b
list1 = []
n1 = int(input("enter the length  : "))
for i in range (n1):
    ele = int(input("Enter the element of second : "))
    list1.append(ele)
print("Swap For second are : ",list1)

a = list1[-1:] + list[1:4] + list1[0:1]
b = list[-1:] + list1[1:4] + list[0:1]


print("The first Swap list : ",a)
print("The second Swap list : ",b)