f = open("sample.txt","r")
l = [x for x in f.read().split()]
long = l[0]
for i in l[1::]:
    if len(long) < len(i):
        long = i
print(long)