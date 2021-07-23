
stroke = 'abcdefgababcd'
needed_symbol = input('Enter symbol: ')
count = 0
for item in stroke:
    if item == needed_symbol:
        count += 1
print(count)