n = input("Enter a string : ")
print("Your String: ",n)
d = {}
for i in n:
    if i in d.keys():
        d[i] += 1
    else :
        d[i] = 1

print(d)