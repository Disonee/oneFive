
#ЗАДАНИЕ 6

from tkinter import N


def print_hello_world():
    print("Привет, мир!")

def print_name(name):
    print(name)

def calculate_discriminant(a, b, c):
    D = b**2 - 4*a*c
    return D

def ask_user_info():
    name = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    return name, age

def get_russian_alphabet_letter(numero):
    russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if 1 <= numero <= 33:
        return russian_alphabet[numero - 1]
    else:
        print("Указано не правильное число!")

# Пример использования функций
print_hello_world()
print_name("Валентин")
D = calculate_discriminant(1, 5, 6)
print("Дискриминант равен:", D)
name, age = ask_user_info()
print("Пользователь указал:")
print("Имя:", name)
print("Возраст:", age)
letter = get_russian_alphabet_letter(7)
print("Буква русского алфавита под номером 7:", letter)
print("\n")




#ЗАДАНИЕ 7 

full_name = "Иванов Иван Иванович"

# Печать длины строки
print("Длина строки с ФИО:", len(full_name))

# Печать результата конкатенации
concatenated_name = full_name + " Программист"
print("Результат конкатенации:", concatenated_name)

# Печать только имени
name_only = full_name.split()[1]
print("Только имя:", name_only)

# Печать ФИО в верхнем регистре
uppercase_full_name = full_name.upper()
print("ФИО в верхнем регистре:", uppercase_full_name)

# Разбиение строки по пробелу
name_parts = full_name.split()
print("Разбиение строки по пробелу:", name_parts)
print("\n")



#ЗАДАНИЕ 8


# создаем список из 7 элементов разных типов 
my_list = [None, 42, 3.14, "Hello, world!", [1, 2, 3], (4, 5, 6), {"name": "Alice", "age": 30}] 
 
# печатаем тип каждого элемента 
for elem in my_list: 
    print(type(elem)) 
 
# удаляем последний элемент 
my_list.pop() 
 
# создаем список из букв ФИО 
full_name = "John Doe" 
letters = list(full_name) 
 
# создаем строковую переменную с ФИО из списка букв 
full_name_back = ''.join(letters) 
 
# печатаем порядковый номер и соответствующий символ в ФИО 
for i, letter in enumerate(full_name): 
    print(i+1, letter) 
 
# печатаем количество символов "а" в ФИО 
a_count = letters.count('a') 
print("Количество символов 'а' в ФИО:", a_count)
print ("\n")




#ЗАДАНИЕ 9


# Создаем пустой список 
odd_numbers = [] 
 
# Используем цикл для генерации нечетных чисел от 1 до 100 и добавления их в список. А двойка отвечает за то что каждый второй элемень будет пропущен)
for i in range(1, 101, 2): 
    odd_numbers.append(i) 
 
# Печатаем список 
print(odd_numbers)

print ("\n")






#ЗАДАНИЕ 10






def safe_division(a, b): 
    """ 
    Функция для деления двух чисел, исключающая деление на 0. 
    """ 
    if b == 0: 
        print("Ошибка: деление на ноль!") 
        return None 
    else: 
        return a / b 
 
# Пример использования функции 
a = 10 
b = 0 
result = safe_division(a, b) 
if result: 
    print("Результат:", result)
