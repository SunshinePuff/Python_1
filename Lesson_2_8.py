"""8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. 
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""

n = int(input("Сколько будет чисел? Введите значение: "))
d = int(input("Какую цифру считать? Введите значение: "))
count = 0
for i in range(1, n + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10
 
print("Было введено %d цифр %d" % (count, d))