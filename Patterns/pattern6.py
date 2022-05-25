n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    for k in range(n-1-i):
        print(" ",end="")
    for m in range(n-1-i):
        print(" ",end="")
    for l in range(i+1):
        print("*",end="")
    print()
