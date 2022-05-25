def sum_num(a):
    sum = 0
    for i in str(a):
        sum += int(i)
    return sum
n =int(input("Enter the numbers : "))
print(sum_num(n))
