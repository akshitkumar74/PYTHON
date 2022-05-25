d = {1:[2,3,4],2:[5,6,7]}
sum = 0
for i in d:
    for j in d[i]:
        print(j)
        sum += j
print(sum)