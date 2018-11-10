# Ввод матриц
def enter_matrix():
    a = []
    print("Enter matrix А 3x3: ")
    for i in range(3):
        a.append([int(j) for j in input().split()])
    b = []
    print("Enter matrix B 3x1: ")
    for i in range(3):
        b.append([int(j) for j in input().split()])
    print("Enter matrix C 1x3: ")
    c = [int(s) for s in input().split()]
    return a, b, c


# Вычисление передаточной функции
def calc_transmission():
    matrix_tuple = enter_matrix()
    
    a = matrix_tuple[0]
    b = matrix_tuple[1]
    c = matrix_tuple[2]

    alpha_n = b[0][0] * c[0] + b[1][0] * c[1] + b[2][0] * c[2]

    betta_n = ((-1 * b[0][0] * c[0] * a[2][2]) - (b[0][0] * c[0] * a[1][1]) + (b[0][0] * c[1] * a[1][0]) +
                    (b[0][0] * c[2] * a[2][0]) + (b[1][0] * c[0] * a[0][1]) - (b[1][0] * c[1] * a[2][2]) -
                    (b[1][0] * c[1] * a[2][0]) + (b[1][0] * c[2] * a[2][1]) + (b[2][0] * c[0] * a[0][2]) +
                    (b[2][0] * c[1] * a[1][2]) - (b[2][0] * c[2] * a[1][1]) - (b[2][0] * c[2] * a[0][0]))

    gamma_n = (b[0][0] * c[0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) + b[0][0] * c[1] * (a[2][0] * a[1][2] - a[2][2] * a[1][0]) +
               b[0][0] * c[2] * (a[1][0] * a[2][1] - a[2][0] * a[1][1]) - b[1][0] * c[0] * (a[0][1] * a[2][2] + a[2][1] * a[0][2]) +
               b[1][0] * c[1] * (a[0][0] * a[2][2] - a[2][0] * a[2][2]) + b[1][0] * c[2] * (a[2][1] * a[0][0] + a[2][0] * a[0][1]) +
               b[2][0] * c[0] * (a[0][1] * a[1][2] - a[0][2] * a[1][1]) + b[2][0] * c[1] * (a[1][0] * a[0][2] - a[1][2] * a[0][0]) +
               b[2][0] * c[2] * (a[0][0] * a[1][1] - a[1][0] * a[0][1]))

    alpha_d = -1 * (a[2][2] + a[1][1] + a[0][0])

    betta_d = (a[1][1] * a[2][2] + a[0][0] * a[2][2])

    gamma_d = -1 * (a[0][0] * a[2][2] * a[1][1] - a[0][2] * a[1][0] * a[2][1] - a[0][1] * a[1][2] * a[2][0])

    if alpha_n >= 0:
        alpha_n = '+' + str(alpha_n)
    if betta_n >= 0:
        betta_n = '+' + str(betta_n)
    if gamma_n >= 0:
        gamma_n = '+' + str(gamma_n)
    if alpha_d >= 0:
        alpha_d = '+' + str(alpha_d)
    if betta_d >= 0:
        betta_d = '+' + str(betta_d)
    if gamma_d >= 0:
        gamma_d = '+' + str(gamma_d)

    numerator = str(alpha_n) + "s^2" + str(betta_n) + "s" + str(gamma_n)
    numerator = numerator.replace('+', '')
    denominator = "s^3" + str(alpha_d) + "s^2" + str(betta_d) + "s" + str(gamma_d)

    separator = ""
    if len(denominator) > len(numerator):
        delta = (len(denominator) - len(numerator)) // 2
        numerator = (" " * delta) + numerator
        for i in range(len(denominator)):
            separator = '-' + separator
    else:
        delta = (len(numerator) - len(denominator)) // 2
        denominator = (" " * delta) + denominator
        for i in range(len(numerator)):
            separator = '-' + separator

    print("\n" + "Transmission function: " + "\n")
    print(numerator)
    print(separator)
    print(denominator)


calc_transmission()
