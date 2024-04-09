#1.Функция для получения уникальных элементов
def unique_elements(list_of_elements):
    return list(set(list_of_elements))


#2.Функция для получения списка простых чисел
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int( num ** 0.5) + 1):
        if num % i == 0:
            return False
        return True
    
def prime_numbers(min, max):
    primes = []
    for num in range(min, max + 1):
        if is_prime(num):
            primes.append(num)
    return primes


#3. Класс точки в двумерном пространстве
import math 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_point(self, other_point):
        return math.sqrt((self.x - other_point.x)2 + (self.y - other_point.y)**2)

    def get_coordinates(self):
        return (self.x, self.y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y



# 4. Сортировка списка строк по длине
def sort_strings_by_length(strings):
    return sorted(strings, key=len) + sorted(strings, key=len, reverse=True)





