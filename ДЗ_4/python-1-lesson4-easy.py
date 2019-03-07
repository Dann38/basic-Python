# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
lst1 = [1, 4, 7, 9, 20]
lst2 = [num**2 for num in lst1]
print(lst2)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fructs1 = ["апельсин", "банан", "арбуз", "киви", "яблоко"]
fructs2 = ["апельсин", "банан", "груша", "яблоко"]
common_fructs = list(set(fructs1)&set(fructs2))
print(common_fructs)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
number1 = [3, 98, 209, 489, -890, 333, 577, -3,  48, 89]
number2 = [i for i in number1 if (i%3 == 0) and i>0 and i%4 != 0]
print(number2)