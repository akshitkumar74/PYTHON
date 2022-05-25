d = {}
n = int(input())
for i in range (n):
    a = int(input())
    b = int(input())
    d.update({a:b})
print(d)
print(sum(d))
    