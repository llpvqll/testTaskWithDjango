
user_nam = input('Enter some numbers, splited by coma: ')

lst = []
user_nam = str(user_nam)
for item in user_nam:
    if item == ',':
        continue
    else:
        lst.append(item)
print(lst)