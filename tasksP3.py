# Напишите программу-симулятор пирожка с «сюрпризом», - которая бы при запуске отображала один из пяти различных «Сюрпризов», выбранный случайным образом.
""" import random
# начальные значения
surprise = random.choice('abcde')
# вывод результата
print('Вам попался пирожо с сюрпризом! Сюрприз:', surprise) """

# Напишите программу, которая бы «Подбрасывала» условную монету 100 раз и сообщала, сколько раз выпал орел, а сколько - решка.
""" import random
# начальные значения
throw = 1
eagle = 0
tails = 0
# начинаем бросать монету 100 раз
while throw <= 100:
    mean = random.randint(1,2)
    # если выпала 1 - плюсуем к орлам
    if mean == 1:
        eagle += 1
    # есди выпала 2 - плюсуем к решкам    
    else:
        tails += 1
    throw += 1
# выводим результат
print('Орел выпал', eagle, 'раз,', 'решка выпала', tails, 'раз') """

# Измените программу «Отгадай число» таким образом, чтобы у игрока было ограниченное количество попы­ток. 
# Если игрок не укладывается в заданное чисnо (и проигрывает), то программа должна выводить сколь возможно суровый текст.
""" import random

print( "\tДобро пожаловать в игру 'Отгадай число'!")
print("\nЯ загадал натуральное число из диапазона от 1 до 100.") 
print("Постарайтесь отгадать его за 7 попыток.\n")

# начальные значения
the_number = random.randint(1,101)
guess = int(input('Ваше предположение: '))
tries = 1

# цикл отгадывания
while guess != the_number and tries < 7:
    if guess > the_number:
        print('Меньше...')
    else:
        print('Больше...')
    guess = int(input('Ваше предположение: '))
    tries += 1
if guess == the_number:
    print("\n\nBaм удалось отгадать число! Зто в самом деле", the_number) 
    print("Bы затратили на отгадывание всего лишь ", tries, " попыток!\n")
else:
    print("\n\nВы с треском проиграли!!!!!")
input("\n\nНажмите Enter, чтобы выйти.") """

# А вот задача посложнее. Напишите на псевдокоде алгоритм игры, в которой случайное число от 1 до 100 за­гадывает человек, а отгадывает компьютер. 
# Прежде чем приступать к решению, задумайтесь над тем, какой должна быть оптимальная стратегия опадывания. 
# Если алгоритм на псевдокоде будет удачным, попробуйте реализовать игру на Pythoп.

# псевдокод:
# программа спрашивает у человека число
# человек вводит число, введенное число записывается в переменную 
# запускается цикл с угадыванием числа: компьютер пробует отгадать число с помощью рандома, если компьютер не угадал число, 
# то программа подсказывает больше загаданное число или меньше, далее в качестве аргумента рандом принимает прошлую попытку компьютера и пробует отгадать уже исходя из нее 
# игра продолжается до победного

""" import random
# просим человека ввести число
numhum = int(input('Введите число от 1 до 100, которое программа попробует отгадать: '))
# программа выбирает число
numprog = random.randint(1,100)
tries = 1
# запускаем цикл угадывания
while numhum != numprog:
    print(numprog)
    if numprog < numhum:
        print('Предположение программы: \nЗагаданное число больше...')
        numprog = random.randint(numprog,100)
    else:
        print('Предположение программы: \nЗагаданное число меньше...')
        numprog = random.randint(1,numprog)
    tries += 1
print("\n\nПрограмме удалось отгадать число! Зто в самом деле", numprog) 
print("Программа затратила на отгадывание всего лишь ", tries, " попыток!\n") """