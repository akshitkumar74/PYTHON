def freq(n):
    d = {}
    for i in n:
        if i in d.keys():
            d[i] += 1
        else :
            d[i] = 1
    return d
a = input("Enter the number: ")
print(freq(a))