def convert(s):
    str1 = " "
    return (str1.join(s))
n = int(input("Enter the length for first : "))
list = []
for i in range (n):
    list.append(input())
print(convert(list))
list1=[]
for i in list:
    if i not in list1:
        list1.append(i)
print("Remove element : ",convert(list1))
