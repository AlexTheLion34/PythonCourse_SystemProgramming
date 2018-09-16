class Sorting:

    # Массив для ввода значений
    __array = []

    # Заполнение массива из консоли
    def fill_array(self):
        self.__array = list(map(int, input().split()))

    # Пузырьковая сортировка
    def bubble_sort(self):
        counter = 1
        array = self.__array
        while counter < len(array):
            for i in range(len(array) - counter):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
            counter += 1
        print(array)

    # Гномья сортировка
    def gnome_sort(self):
        counter = 1
        array = self.__array
        while counter < len(array):
            if array[counter - 1] <= array[counter]:
                counter += 1
            else:
                array[counter], array[counter - 1] = array[counter - 1], array[counter]
                counter -= 1
                if counter == 0:
                    counter = 1
        print(array)

    # Блочная сортировка
    def bucket_sort(self):
        array = self.__array
        max_element = max(array)
        size = max_element / len(array)
        result = []
        buckets = [[] for _ in range(len(array))]
        for i in range(len(array)):
            index = int(array[i] / size)
            if index != len(array):
                buckets[index].append(array[i])
            else:
                buckets[len(array) - 1].append(array[i])
        for i in range(len(array)):
            buckets[i] = sorted(buckets[i])
        for i in range(len(array)):
            result += buckets[i]
        print(result)

    # Пирамидальная сортировка
    def pyramid_sort(self):
        array = self.__array
        for index in range((len(array) >> 1) - 1, -1, -1):
            self.__shift_down(index, len(array))
        for index in range(len(array) - 1, 0, -1):
            array[0], array[index] = array[index], array[0]
            self.__shift_down(0, index)
        print(array)

    # Добавление элемента в пирамиду
    def __shift_down(self, parent_element, depth):
        array = self.__array
        item = array[parent_element]
        while True:
            child_element = (parent_element << 1) + 1
            if child_element >= depth:
                break
            if child_element + 1 < depth and array[child_element] < array[child_element + 1]:
                child_element += 1
            if item < array[child_element]:
                array[parent_element] = array[child_element]
                parent_element = child_element
            else:
                break
        array[parent_element] = item
