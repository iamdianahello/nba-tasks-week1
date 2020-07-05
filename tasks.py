import keyword

# создай список с целыми числами произвольных значений произвольной длины,
numbers = [1, 11, 111, 2, 22, 222, 3, 33, 333]

# отсортируй его по возрастанию и убыванию, запиши результат в отдельные переменные
little_to_big = sorted(numbers)
big_to_little = sorted(numbers, reverse=True)

# даны два списка с числами, нужно вернуть список, который состоит из общих чисел
a = [1, 4, 5, 7, 23, 36, 67, 78, 99, 134, 142, 150]
b = [3, 5, 6, 19, 67, 77, 123, 134, 172, 323, 434]
common_list  = a + b

# напиши функцию, которая складывает сумму двух чисел, переданных ей на вход
def math_sum(num1, num2):
    sum = num1 + num2

# напиши функцию, которая возвращает тип данных, переданный ей на вход, и возвращает его на русском языке (пример: "строка")
def define_type(object):
    return type(object)

# напиши функцию, которая принимает на вход любое количество чисел и говорит, есть ли среди них четное
def even_detector(nums_list):
    bool_even_detected = False
    count = 0
    while count < len(nums_list):
        if nums_list[count] % 2 == 0:
            bool_even_detected = True
            break
        count +=1
    print(bool_even_detected)
    return bool_even_detected

# используй тернарный оператор, чтобы вызвать функцию, если возраст больше 21 года, в противном случае верни сообщение "мы не продаем алкоголь несовершеннолетним"
age = 17

def sell_alcohol():
    return True if age > 21 else print('мы не продаем алкоголь несовершеннолетним')


sell_alcohol()

# загрузи список ключевых слова из модуля keyword, преобразуй его в строку со словами, разделенными запятой
keyword.kwlist
key_string = ",".join(keyword.kwlist)

# напиши функцию, которая проверит, является ли строка ключевым словом, используй модуль keyword
# не забудь сначала изучить этот модуль с помощью dir, чтобы узнать, есть ли там полезные методы
def detect_keyword(word):
    return keyword.iskeyword(word)

# посчитайте, сколько раз символ встречается в строке, функция принимает на вход символ и строку
def symbol_count(symbol, str):
    count = 0
    symbols_in_str = 0
    while count < len(str):
        if symbol == str[count]:
            symbols_in_str +=1
        count +=1
    return symbols_in_str


symbol_count('a', "radasa")