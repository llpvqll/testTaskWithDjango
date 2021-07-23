
lst = [1, 2, 3, 4, 5]
shift = 3
for item in range(shift):
    tmp = lst.pop(0)
    lst.append(tmp)
print(lst)
