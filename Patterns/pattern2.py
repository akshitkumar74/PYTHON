n=int(input())
for i in range (n):
    for j in range (n-i):
        print("*",end="")
    for k in range(2*i):
        print(" ",end="")
    for l in range(n-i):
        print("*",end="")
    print()
       