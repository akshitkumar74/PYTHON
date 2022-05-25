f = open("system.txt","r")
txt = f.read()
count = 0
vowels = ['a','e','i','o','u']
for i in txt:
    if i in vowels:
        count += 1
print(count)