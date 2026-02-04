import copy
list = [1, 2, 3]
list2 = [4, 5]
list.append(list2)
liste3 = copy.deepcopy(list)
list2.append(6)
print(liste3)