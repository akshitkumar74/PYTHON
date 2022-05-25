d = {}
n = int(input())
for i in range (n):
    a = int(input())
    b = int(input())
    d.update({a:b})
print(d)
d1 = {}
n = int(input())
for i in range (n):
    a = int(input())
    b = int(input())
    d.update({a:b})
print(d1)
d2 = {}
for i in (d,d1):
    d2.update(i)
print(d2)
    