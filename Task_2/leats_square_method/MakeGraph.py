import openpyxl
import matplotlib.pyplot as plt
import numpy as np


class MakeGraph:

    __wb = openpyxl.load_workbook(filename="/Users/AlexTheLion/Desktop/PythonCourse_SystemProgramming/Task_2/"
                                           "table.xlsx")

    __sheet = __wb.active

    __x_values = []
    __y_values = []

    __sum_x = 0
    __sum_y = 0
    __sum_xy = 0

    __sum_square_x = 0
    __sum_square_y = 0

    __A = 0
    __B = 0

    def __receive_data(self):
        self.__x_values = [v[0].value for v in self.__sheet['A2:A15']]
        self.__y_values = [v[0].value for v in self.__sheet['B2:B15']]

    def sum_x_and_y(self):
        for x in self.__x_values:
            self.__sum_x += x
        for y in self.__y_values:
            self.__sum_y += y
        for i in range(len(self.__x_values)):
            self.__sum_xy += self.__y_values[i] * self.__x_values[i]

    def sum_squares(self):
        for x in self.__x_values:
            self.__sum_square_x += x ** 2
        for y in self.__y_values:
            self.__sum_square_x += y ** 2

    def __approximate(self):
        self.__receive_data()
        self.sum_x_and_y()
        self.sum_squares()
        self.__A = (len(self.__x_values) * self.__sum_xy - (self.__sum_x * self.__sum_y)) / \
                   (len(self.__x_values) * self.__sum_square_x - (self.__sum_x ** 2))
        self.__B = (self.__sum_y - self.__A * self.__sum_x) / len(self.__x_values)

    def make_graph(self):
        self.__approximate()
        x = np.arange(self.__x_values[0], self.__x_values[13], 0.5)
        plt.plot(self.__x_values, self.__y_values, 'go')
        plt.plot(x, self.__A * x + self.__B)
        plt.savefig("/Users/AlexTheLion/Desktop/PythonCourse_SystemProgramming/Task_2/graph.png", dpi=150)
