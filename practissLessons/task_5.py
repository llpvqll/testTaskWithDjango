
first_lst = [1, 22, 33, 4, 55, 66, 34, 29, 32, 552]
second_lst = [2, 33, 55, 11, 5, 29, 552, 245, 231]
third_lst = []

for first_item in first_lst:
    if first_item not in second_lst:
        third_lst.append(first_item)

print(third_lst)