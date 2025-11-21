x = int(input())

if x == 100:
    print('равные числа')
elif x > 50 and x < 100:
    print('больше 50 и меньше 100')
elif x < 50 or x > 0:
    print('от 0 до 50')
else:
    print('число больше 100')
