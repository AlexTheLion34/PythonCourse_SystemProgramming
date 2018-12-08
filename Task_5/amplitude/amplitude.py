import math


def calc_amplitude():
    a = int(input("Enter coefficient a = "))
    b = int(input("Enter coefficient b = "))
    a_temp = 2 * a * b / (a ** 2 + 121)
    b_temp = 22 * b / (a ** 2 + 121)
    print("Output amplitude: Am = " + str(math.sqrt(a_temp ** 2 + b_temp ** 2)))


calc_amplitude()
