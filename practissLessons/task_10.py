
a = 130
b = 123450

if a > b:
    biggest = a
    smallest = b
else:
    biggest = b
    smallest = a

for item in range(smallest, 0, -1):
    if biggest % item == 0:
        print(item)
        break