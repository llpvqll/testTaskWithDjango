
lst = [1, 2, 3, 4, 5]


while True:
    next = input('Enter number: ')
    if next != '':
        lst.pop(0)
        lst.append(next[-1])
    else:
        break
    print(lst)
