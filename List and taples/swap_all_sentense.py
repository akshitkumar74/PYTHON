from posixpath import split


n = input()

x = n.split()
y = " ".join(reversed(x))

print(y)