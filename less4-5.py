#  числа делящийся на 3
x = int(input())
for i in range(x + 1):
    if i % 3 == 0:
        print('деление на 3 : ', i)
        i += i
