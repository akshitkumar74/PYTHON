def ab(n):
    if n>18:
        return True
    else:
        return False
lst = []
n = int(input("Range : "))
for i in range (n):
    lst.append(int(input()))
print(lst)

print(list(filter(ab,lst)))


