import math
from openpyxl import Workbook
import random


class FillTable:

    table_file_path = "/Users/AlexTheLion/Desktop/PythonCourse_SystemProgramming/Task_2/table.xlsx"

    __wb = Workbook()

    __ws = __wb.active

    __variant = 2

    def __calculate_num_of_coordinates(self):
        return round(math.sqrt(self.__variant) * 10)

    def fill_table(self):
        print("Введите дипазаон координат")
        min_x = input("Минимальный X: ")
        max_x = input("Маскимальный X: ")
        range_y = int(input("Введите разброс для Y: "))
        delta_x = (int(max_x) - int(min_x)) / self.__calculate_num_of_coordinates()
        current_element = float(min_x)
        self.__ws['A1'] = 'X'
        self.__ws['B1'] = 'Y'
        for i in range(self.__calculate_num_of_coordinates()):
            cell_x = 'A' + str(i + 2)
            cell_y = 'B' + str(i + 2)
            self.__ws[cell_x] = current_element
            self.__ws[cell_y] = random.random() * range_y
            current_element += delta_x
        self.__wb.save(self.table_file_path)
