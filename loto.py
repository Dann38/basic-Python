
import random
import re


class Cart:

    def __init__(self, name="Компьютер"):
        """
        :param name: Имя игрока
        str1: Список значений
        str2: Первая строчка в карточке
        str3: Вторая строчка в карточке
        str4: Третья строчка в карточке
        number: Список значений, для того, чтоб их вычеркивать и проверять
        остались ли в карточке ещё незачеркнутые значения
        """
        self.name = name
        self.str1, self.str2, self.str3, self.str4 = num_cart()
        self.number = self.str1.copy()

    def print_cart(self):
        """
        :return: Выводит на экран карточку из 3-х строк, имени и
        рамки
        """
        print(f"============={self.name}=============")

        print(f'|{"|".join(self.str2)}|')
        print(f'|{"|".join(self.str3)}|')
        print(f'|{"|".join(self.str4)}|')

        print(f"============={'=' * len(self.name)}=============")


def num_cart():
    """
    :return:4 списка
    1-й: 15 неповторяющихся чисел от 1- 90
    2-4-е: список состоящий из 9 элементов(5 чисел в порядке возрастания, и 4-х
    рандомно расположенных пробелов)
    """
    str1 = []
    # создаем список из 15 неповторяющихся значений 1-90
    for i in range(15):
        a = 1
        while True:
            num = random.randint(1, 91)
            for j in str1:
                if j == num:
                    a = 0
                    continue
            if a == 0:
                a = 1
                continue
            break
        str1.append(num)
    str1.sort()

    # Превращаем числа в строки, к однозначным добавляем пробел(для красоты)
    for i in range(len(str1)):
        str1[i] = str(str1[i])
        if len(str1[i]) == 1:
            str1[i] += ' '

    # делим список на 3 части
    str2 = str1[:5]
    str3 = str1[5:10]
    str4 = str1[10:]

    # добавляем в списки произвольные пробелы
    for i in range(4):
        str4.insert(random.randint(0, 5), "  ")
    for i in range(4):
        str2.insert(random.randint(0, 5), "  ")
    for i in range(4):
        str3.insert(random.randint(0, 5), "  ")

    # выводим результат
    return str1, str2, str3, str4


def replacement(list_, object_, value):
    """
    :param list_: Список в котором будет происходить замена
    :param object_: Заменяемый объект
    :param value: Замена
    :return: Меняет значение в списки на новое
    """
    num = list_.index(object_)
    list_.remove(object_)
    list_.insert(num, value)


def start():
    """
    :return: Процесс игры в лото.
    """
    print("""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

============================
|  |  |9 |43|62|  |  |74|90|
|2 |  |27|  |  |75|78|  |82|
|  |41|56|63|  |76|  |  |86| 
============================

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.    
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
======================================================================= 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

  
    """)

    you = Cart(input("Введите ваше имя:"))
    comp = Cart()

    # Создаю список бочонков
    barrels = [str(i) for i in range(1, 91)]

    # Игровое действие, работает пока есть числа в обоих карточках
    # и игрок не ошибся при ответе
    while True:

        # проверка: зачеркнуты или нет все значения в карточках
        if len(you.number) == 0:
            print("++++++++++++++++++++++++"
                  "Поздравляю, вы выйграли"
                  "++++++++++++++++++++++++"
                  )
            break
        elif len(comp.number) == 0:
            print("Вы проиграли!")
            break

        # Вывод карточек, боченка, кол-во боченков и вопроса
        you.print_cart()
        comp.print_cart()
        a = barrels.pop(random.randint(0, len(barrels)-1))
        print(f"{a} (осталось {len(barrels)})")
        answer = input("Зачеркнуть цифру? (y/n)")

        # Проверка на правильный ввод
        while True:
            if re.match("^[yn]{1}$", answer) == None:
                answer = input("Зачеркнуть цифру? (y/n)")
            else:
                break

        if answer == "n":
            # если в карточке было число а вы сказали, что его нет, то вы проиграли
            if a in you.str1:
                print("Вы проиграли!")
                break
        elif answer == "y":
            # если в карточке нет числа, то вы проиграли
            # иначе оно вычеркивается
            try:
                # добовляет к однозначным числам пробел, чтобы число прошло проверку
                if len(a) == 1:
                    a += ' '
                # проверяет в каком из списков находится данное число
                num = you.str1.index(a)+1
                you.number.remove(a)
                if num <= 5:
                    replacement(you.str2, a, "X ")
                elif num <= 10:
                    replacement(you.str3, a, "X ")
                elif num <= 15:
                    replacement(you.str4, a, "X ")
            except ValueError:
                print("Вы проиграли!")
                break

        # вычеркивает числа у компьютера
        if a in comp.str1:
            num = comp.str1.index(a) + 1
            comp.number.remove(a)
            if num <= 5:
                replacement(comp.str2, a, "X ")
            elif num <= 10:
                replacement(comp.str3, a, "X ")
            else:
                replacement(comp.str4, a, "X ")
# начало игры
start()