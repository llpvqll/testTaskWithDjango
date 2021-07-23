
lst = ['m', 'b', 'a', 'd', 't', '', 'e', '', 'y', '']

for index, value in enumerate(lst):
    if not value:
        lst.pop(index)

print(lst)