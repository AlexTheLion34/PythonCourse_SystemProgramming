from openpyxl import Workbook
from openpyxl.styles import Alignment
import matplotlib.pyplot as plt


import math


def make_table():
    table_file_path = "/Users/AlexTheLion/Desktop/PythonCourse_SystemProgramming/Task_5/systems/systems.xlsx"
    wb = Workbook()
    ws = wb.active
    system_names = ['Линейная', 'Динамическая', 'Любая']
    cells = ['A', 'B', 'C', 'D', 'E', 'F']
    linear = [(5, 10), (10, 20), (20, 40), (40, 80), (80, 160)]
    dynamic = [(10, math.sin(10) + 1), (20, math.sin(20) + 1), (40, math.sin(40) + 1),
               (80, math.sin(80) + 1), (160, math.sin(160) + 1)]
    anything = [(5, math.sin(10) + 1), (10, math.sin(20) + 1), (20, math.sin(40) + 1),
                (40, math.sin(80) + 1), (80, math.sin(160) + 1)]
    ws.merge_cells('A1:B1')
    ws.merge_cells('C1:D1')
    ws.merge_cells('E1:F1')

    counter = 0
    for letter in ['A', 'C', 'E']:
        ws[letter + '1'] = system_names[counter]
        ws[letter + '1'].alignment = Alignment(horizontal='center', vertical='center')
        counter += 1

    counter = 0
    for cell in cells:
        if counter % 2 == 0:
            ws[cell + str(2)] = 'X'
            ws[cell + str(2)].alignment = Alignment(horizontal='center', vertical='center')

        else:
            ws[cell + str(2)] = 'Y'
            ws[cell + str(2)].alignment = Alignment(horizontal='center', vertical='center')
        counter += 1

    for i in range(5):
        ws['A' + str(i + 3)] = (linear[i])[0]
        ws['B' + str(i + 3)] = (linear[i])[1]

    for i in range(5):
        ws['C' + str(i + 3)] = (dynamic[i])[0]
        ws['D' + str(i + 3)] = (dynamic[i])[1]

    for i in range(5):
        ws['E' + str(i + 3)] = (anything[i])[0]
        ws['F' + str(i + 3)] = (anything[i])[1]

    plt.subplot(1, 3, 1)
    x = [l[0] for l in linear]
    y = [l[1] for l in linear]
    plt.title('Linear')
    plt.plot(x, y)
    plt.subplot(1, 3, 2)
    x = [l[0] for l in dynamic]
    y = [l[1] for l in dynamic]
    plt.plot(x, y)
    plt.title('Dynamic')
    plt.subplot(1, 3, 3)
    x = [l[0] for l in anything]
    y = [l[1] for l in anything]
    plt.plot(x, y)
    plt.title('Anything')
    plt.savefig("/Users/AlexTheLion/Desktop/PythonCourse_SystemProgramming/Task_5/systems/systems.png", dpi=150)

    wb.save(table_file_path)


make_table()
