f = open("sample.txt","r")
n = open("newfile.txt","w+")
data = f.readlines()
for i in range (0,len(data)):
    if (i%2==0):
        n.write(data(i))
n.close()
n = open("newfile.txt","r")
count = n.read()
print(count)
f.close()
n.close()