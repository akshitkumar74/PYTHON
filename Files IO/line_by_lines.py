f = open("sample.txt","r")
s = f.read()
l = [x for x in s.split("\n")]
print(l)
f.close()