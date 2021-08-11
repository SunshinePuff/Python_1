"""6. В программе генерируется случайное целое число от 0 до 100. 
Пользователь должен его отгадать не более чем за 10 попыток. 
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число."""


from random import random


number = round(random() * 100)
count = 1
print("Компьютер загадал число. Отгадайте его. На это у Вас 10 попыток")
while count <= 10:
    users_answer = int(input(str(count) + '-я попытка: '))
    if users_answer > number:
        print('Меньше')
    elif users_answer < number:
        print('Больше')
    else:
        print('Вы угадали с %d-й попытки' % count)
        break
    count += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано', number)