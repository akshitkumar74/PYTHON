def maximum(n1,n2,n3):
    if (n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3

m = maximum(2,6,9)
print("The maximum number is " + str(m) )