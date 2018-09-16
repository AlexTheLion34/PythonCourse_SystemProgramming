import math


class Probability:

    # Студенты
    __students = ["Никита", "Сережа", "Настя"]

    # Вероятности
    __probabilities = []

    # Событие
    __action = "Оползень"

    # Кол-во дней,за которое происходит событие с вероятностью N
    __num_of_days = 14

    # Кол-во дней, для которого нужно высчитать вероятность
    __num_of_days_check = 200

    # Ввод вероятностей
    def __set_probabilities(self):
        print("Ввеедите вероятность события: " + self.__action + " для каждого студента")
        for student in self.__students:
            print(student + ":")
            self.__probabilities.append(input())
        self.__probabilities = list(map(float, self.__probabilities))

    # Вычисление вероятности
    def count_probability(self):
        self.__set_probabilities()
        p = 1 / 3
        m = (self.__probabilities[0] * self.__num_of_days_check) // self.__num_of_days
        lambda_ = p * self.__num_of_days_check
        result = pow(lambda_, m) * pow(math.e, (lambda_ * -1)) / math.factorial(m)
        print("Вероятность того, что со студентом: " + self.__students[0] + " произойдет событие: " + self.__action)
        print(result)
