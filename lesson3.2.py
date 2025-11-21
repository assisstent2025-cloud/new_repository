num_1 = 2
num2 = 4
if num_1 > num2:
    print(False)
elif num_1 == num2:
    print(False)
else:
    print(2)


num1 = 2
num_2 = 4
if num1 > num2 and num1 == num_2:
    print(False)
elif num1 == num2 and not num_1 < num2:
    print(False)
else:
    print(2)
