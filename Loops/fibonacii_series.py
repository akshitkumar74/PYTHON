num = int(input("Enter the Range Number: "))
First_val = 0
Second_val = 1
for i in range(0, num):
           if(i <= 1):
                      next = i
           else:
                      next = First_val + Second_val
                      First_val = Second_val
                      Second_val = next
           print(next)