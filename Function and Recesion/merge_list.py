def merge (list ,list1):
    for i in list1:
        list.append(i)
    print(list)

list = [1,2,3,4]
list1 = [5,6,7,8]

merge (list ,list1)