first = int(float(input('Введите первое ЦЕЛОЕ число: ')))
second = int(float(input('Введите второе ЦЕЛОЕ число: ')))
third = int(float(input('Введите третье ЦЕЛОЕ число: ')))
if first == second == third:
    print("Одинаковых чисел - 3")
elif first == second or first == third or second == third:
    print('Одинаковых чисел - 2')
else:
    print('Одинаковых чисел -0')