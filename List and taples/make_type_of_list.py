l = list(map(eval,input().split()))
l1 = list(map(eval,input().split()))
l2 = []

c = len(l)
for i in range (c):
    l3 = []
    l3.append(l[i])
    l3.append(l1[i])
    l2.append(l3)
print(l2)
