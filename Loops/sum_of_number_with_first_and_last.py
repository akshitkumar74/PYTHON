n = int(input("enter number :"))
b=n%10
while(n!=0):
    a=n%10
    n=n//10
sum=a+b
print(sum)