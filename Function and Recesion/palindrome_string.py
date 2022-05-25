def pali(a):
    b = a[-1::-1]
    if (b==a):
        print("This string is Palindrome")
    else:
        print("Not palindrome")
    return b
a = input("Enter a string : ")
pali(a)