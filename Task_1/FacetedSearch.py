class FacetedSearch:

    # Список всех птиц
    __birdsList = ["Синица", "Голубь", "Воробей", "Сорока",
                   "Дятел", "Иволга", "Кукушка", "Пеночка",
                   "Орел", "Сокол", "Сапсан", "Сплюшка",
                   "Курица", "Павлин", "Пингвин", "Страус", ]

    # Список основных категорий
    __categoriesList = ["Городские", "Лесные", "Хищные", "Нелетающие"]

    # Хранение выбранной пользователем категории
    __selected_category = ""

    # Вывод списка птиц по категориям
    def __print_birds(self):
        count = 0
        for bird in self.__birdsList:
            if count % 4 == 0:
                print("\n" + self.__categoriesList[count // 4] + ":")
            print(bird)
            count += 1
        print()

    # Определение категории
    def start_search(self):
        print("\n" + "Загадайте одну из птиц из предложенного списка: ")
        self.__print_birds()
        for category in self.__categoriesList:
            print("Ваша птица относится к категории - " + category.lower())
            answer = input()
            if answer == "да":
                self.__selected_category = category
                break
        self.__perform_search(self.__selected_category)

    # Выбор конкретной категории и поиск по ней
    def __perform_search(self, category):
        if category == self.__categoriesList[0]:
            self.__search_in_first()
        elif category == self.__categoriesList[1]:
            self.__search_in_second()
        elif category == self.__categoriesList[2]:
            self.__search_in_third()
        else:
            self.__search_in_fourth()

    # Функции для поиска
    # по конкретной группе птиц
    def __search_in_first(self):
        print("Начинается на букву 'C'?")
        answer = input()
        if answer == "да":
            print("Она маленькая?")
            answer = input()
            if answer == "да":
                print("Ваша птица - " + self.__birdsList[0])
            else:
                print("Ваша птица - " + self.__birdsList[3])
        else:
            print("Она маленькая?")
            answer = input()
            if answer == "да":
                print("Ваша птица - " + self.__birdsList[2])
            else:
                print("Ваша птица - " + self.__birdsList[1])

    def __search_in_second(self):
        print("Начинается на гласную букву?")
        answer = input()
        if answer == "да":
            print("Ваша птица - " + self.__birdsList[5])
        else:
            print("Заканчивается на гласную букву?")
            answer = input()
            if answer == "да":
                print("Ваша птица - " + self.__birdsList[4])
            else:
                print("Ваша птица издает звук 'ку-ку'?")
                answer = input()
                if answer == "да":
                    print("Ваша птица - " + self.__birdsList[6])
                else:
                    print("Ваша птица - " + self.__birdsList[7])

    def __search_in_third(self):
        print("Начинается на букву 'C'?")
        answer = input()
        if answer == "нет":
            print("Ваша птица - " + self.__birdsList[8])
        else:
            print("Заканчивается на гласную букву ")
            answer = input()
            if answer == "да":
                print("Ваша птица - " + self.__birdsList[11])
            else:
                print("Существует поезд с таким названием?")
                answer = input()
                if answer == "да":
                    print("Ваша птица - " + self.__birdsList[10])
                else:
                    print("Ваша птица - " + self.__birdsList[9])

    def __search_in_fourth(self):
        print("Начинается на букву 'П'?")
        answer = input()
        if answer == "нет":
            print("Большого размера?")
            answer = input()
            if answer == "да":
                print("Ваша птица - " + self.__birdsList[15])
            else:
                print("Ваша птица - " + self.__birdsList[12])
        else:
            print("Есть большой хвост?")
            answer = input()
            if answer == "да":
                print("Ваша птица - " + self.__birdsList[13])
            else:
                print("Ваша птица - " + self.__birdsList[14])
