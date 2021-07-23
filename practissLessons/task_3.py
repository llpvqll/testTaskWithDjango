n = 5

power = int(input('Enter some num: '))
res = 0
for item in range(1, power+1):
    res += n ** item

    print(res)
