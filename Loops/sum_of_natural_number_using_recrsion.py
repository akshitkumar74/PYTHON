n = int(input("Enter a natural number : "))
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
print("The sum is " + str(sum(n)))