def name(s):
    ls = s.split()
    ln = len(ls)
    s = ""
    for i in ls:
        if (ls.index(i)!=ln-1):
            s += i[0:1] + " "
        else:
            s +=i
    return(s)

n = input()
print(name(n))