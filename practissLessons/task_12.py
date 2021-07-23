
lst = [1, 2, 3, 4, 5, 6]

for item in lst:
    count = lst.count(item)
    if count > 1:
        print(True)
        break
else:
    print(False)