from collections import defaultdict


class Numbers:

    # Словарь для хранения чисел по категориям
    __numbers_by_categories = defaultdict(list)

    def __set_categories(self):
        self.__numbers_by_categories.setdefault("Натуральные", [])
        self.__numbers_by_categories.setdefault("Целые", [])
        self.__numbers_by_categories.setdefault("Вещественные", [])
        self.__numbers_by_categories.setdefault("Комплексные", [])
        self.__numbers_by_categories.setdefault("Четные", [])
        self.__numbers_by_categories.setdefault("Нечетные", [])
        self.__numbers_by_categories.setdefault("Простые", [])

    # Распределение чисел по категориям
    def perform_distribution(self):
        numbers_string = input()
        for num in numbers_string.split(','):
            self.__numbers_by_categories["Комплексные"].append(num)
            self.__check_natural(num)
            self.__check_integer(num)
            self.__check_real(num)
            self.__check_even(num)
            self.__check_prime(num)

        self.__print_numbers()

    # Проверка на натуральное
    def __check_natural(self, num):
        try:
            if int(num) >= 0:
                self.__numbers_by_categories["Натуральные"].append(num)
        except ValueError:
            if len(num) > 2 and num[-2] == '.' and num[-1] == '0' and num[0] != '-':
                self.__numbers_by_categories["Натуральные"].append(num)

    # Проверка на целое (1.0 - тоже целое)
    def __check_integer(self, num):
        try:
            int(num)
            self.__numbers_by_categories["Целые"].append(num)
        except ValueError:
            if len(num) > 2 and num[-2] == '.' and num[-1] == '0':
                self.__numbers_by_categories["Целые"].append(num)

    # Проверка на вещественное
    def __check_real(self, num):
        if 'i' in num or '+' in num:
            pass
        else:
            self.__numbers_by_categories["Вещественные"].append(num)

    # Проверка на четность
    def __check_even(self, num):
        try:
            if int(num) % 2 == 0:
                self.__numbers_by_categories["Четные"].append(num)
            else:
                self.__numbers_by_categories["Нечетные"].append(num)
        except ValueError:
            if len(num) >= 2 and num[-2] == '.' and num[-1] == '0':
                if int(num[:-2]) % 2 == 0:
                    self.__numbers_by_categories["Четные"].append(num)
                else:
                    self.__numbers_by_categories["Нечетные"].append(num)

    # Проверка на простое
    def __check_prime(self, num):
        new_num = 0
        if "+" in num or "i" in num:
            return
        try:
            new_num = int(num)
        except ValueError:
            if len(num) >= 2 and num[-2] == '.' and num[-1] == '0':
                new_num = int(num[:-2])
        if new_num <= 0:
            return
        i = 2
        j = 0
        while i ** 2 <= abs(new_num) and j != 1:
            if new_num % i == 0:
                j = 1
            i += 1
        if j != 1:
            self.__numbers_by_categories["Простые"].append(num)

    # Вывод словаря
    def __print_numbers(self):
        for key in self.__numbers_by_categories.keys():
            print(key + ": " + str(self.__numbers_by_categories[key]))
