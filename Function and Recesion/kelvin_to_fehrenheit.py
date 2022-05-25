def feh(kal):
    return kal*(9/5)-459.67

c = int(input("Enter the value of kalvin : "))

f = feh(c)
print("The value in fehrenhiet : "+ str(f))