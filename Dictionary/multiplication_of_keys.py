d = {}
n = int(input())
for i in range (n):
    a = int(input())
    b = int(input())
    d.update({a:b})

print(d)
p=1
for i in d:
    p*=i*d[i]
print(p)


