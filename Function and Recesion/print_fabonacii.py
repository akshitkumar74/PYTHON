n = int(input("Enter the range : "))
def fibonacci():
    a=0
    b=1
    for i in range(n):
        print(b)
        a,b= b,a+b
o = fibonacci()