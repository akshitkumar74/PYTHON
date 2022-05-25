f = open("system.txt","r")
count = 0
data = f.readlines()
for i in data:
    count += 1
print(count)