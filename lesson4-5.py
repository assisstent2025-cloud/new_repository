# сумма чисел от 0 до 100

x = 0
y = 1
while y <= 100:
    x += y
    y += 1
    print(x)

# не четные числа

num = 0
while num < 100:
    num += 1
    if num % 2 == 0:
        continue
    print(num)


# четные числа

num1 = 0
while num1 < 100:
    num1 += 1
    if num1 % 2 != 0:
        continue
    print(num1)


# сумма введенных чисел

n = int(input('ввод первого числа'))
for i in range(n):
    x = int(input('ввод второго числа'))
    n += x
    print('сумма чисел', n)


# вывод четных чисел от 0 до введенного числа

q = int(input("...:"))
print('четные числа до', q)
for i in range(q + 1):
    if i % 2 == 0:
        print(i)



#  числа делящийся на 3

x = int(input('введите число : '))
for i in range(x + 1):
    if i % 3 == 0:
        print('деление на 3 : ', i)
        i += i

