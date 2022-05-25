def reverse(n):
    rev = 0
    while (n!=0):
        digit = n % 10
        rev = rev*10+digit
        n  = n//10
    return rev
def rev_str(d):
    str = " "
    for i in d:
        str = i +str
    return str

a =int(input("Enter the number : "))
s =input("Enter the character : ")

print(reverse(a))
print(rev_str(s))
    