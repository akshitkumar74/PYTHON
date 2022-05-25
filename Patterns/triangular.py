for i in range(3):
    for j in range (2-i):
        print(" ",end="")
    for k in range(i+1):
        print(k+1,end="")
    for l in range (i,0,-1):
        if(l!=0):
            print(l,end="")
    print()