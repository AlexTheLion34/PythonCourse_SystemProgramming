from FacetedSearch import *
from Numbers import *
from Sorting import *
from Probability import *


class Test:

    @staticmethod
    def test():
        fs = FacetedSearch()
        num = Numbers()
        srt = Sorting()
        prb = Probability()
        print("Тест первого задания: ")
        fs.start_search()
        print("----------------------")
        print("Тест второго задания: ")
        num.perform_distribution()
        print("----------------------")
        print("Тест третьего задания: ")
        srt.fill_array()
        print("Пузырьковая сортировка:")
        srt.bubble_sort()
        print("Гномья сортировка:")
        srt.gnome_sort()
        print("Блочная сортировка:")
        srt.bucket_sort()
        print("Пирамидальная сортировка:")
        srt.pyramid_sort()
        print("----------------------")
        print("Тест четвертого задания: ")
        prb.count_probability()


Test.test()
