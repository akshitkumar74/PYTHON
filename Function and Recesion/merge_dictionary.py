def merge(dict , dist1):
    return (dist1.update(dict))
dict = {1:2, 3:4, 5:6}
dict1 = {7:8, 9:0, 11:12}

print(merge(dict,dict1))

print(dict1)