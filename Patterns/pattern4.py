n = int(input())
for i in range (n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i+0):
        print("*",end="")
    for l in range(i+1):
        print("*",end="")
    print()