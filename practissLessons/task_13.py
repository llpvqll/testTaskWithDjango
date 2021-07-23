lst = [1, 2, 3, 4, 5, 6, 19, 20, 32, 25, 13, 20]

for item in range(len(lst)):
    if lst[item] == 20:
        lst[item] = 200
        break 
print(lst)
