f = open("sample,txt","r")
n = int(input("Enter the number of last would you like to read : "))
s =f.readlines()
[print(x) for x in s[-n:-1]]
print(s[-1])
f.close()