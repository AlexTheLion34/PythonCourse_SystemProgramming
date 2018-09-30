from least_square_method.FillTable import *
import openpyxl


class MakeTable:

    __wb = openpyxl.load_workbook(filename=FillTable.table_file_path)

    __sheet = __wb.active

    __matrix = [[]]

    __result = [[]]

    __n = 0

    def __make_matrix_n_x_n(self):
        n = int(input("Введите размерность матрицы nXn: "))
        self.__matrix = [[int(random.random() * 30) for _ in range(n)] for _ in range(n)]

    def put_matrix_in_table(self):
        self.__make_matrix_n_x_n()
        array = self.__matrix
        count = 0
        while count < 10:
            i = random.randint(0, len(array) - 1)
            j = random.randint(0, len(array) - 1)
            cell = self.__matrix[i][j]
            if cell != -100:
                self.__matrix[i][j] = -100
                count += 1
        for i in range(len(array)):
            for j in range(len(array)):
                self.__sheet.cell(row=i + 2, column=j + 5).value = self.__matrix[i][j]
        self.__wb.save(FillTable.table_file_path)


