
lst = [1, 2, 3, 44, 55, 11, 20, 237, 29, 48]
new_lst = []
for item in lst:
    if item % 2 == 0:
        new_lst.append(item)
    elif item == 237:
        break
print(new_lst)