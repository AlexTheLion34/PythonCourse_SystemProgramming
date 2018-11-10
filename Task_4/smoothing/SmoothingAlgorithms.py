import matplotlib.pyplot as plt
import numpy as np
import random

main_list = [int(random.random() * 40) for _ in range(50)]


def tomorrow_like_yesterday():
    copy_main_list = main_list
    new_array = [0 for _ in range(len(copy_main_list))]
    new_array[0] = copy_main_list[0]
    for i in range(len(new_array)):
        if i != 0:
            new_array[i] = copy_main_list[i - 1]
    return new_array


def simple_moving_average():
    new_array = main_list.copy()
    window_size = 5
    start_index = 0
    for i in range(len(new_array)):
        sum = 0
        if i >= window_size - 1:
            counter = start_index
            while counter <= i:
                sum += new_array[counter]
                counter += 1
            new_array[i] = sum // window_size
            start_index += 1
    return new_array


def simple_moving_average_weight():
    new_array = main_list.copy()
    window_size = 5
    array_of_weights = [0.88, 0.90, 0.92, 0.93, 0.98]
    start_index = 0
    for i in range(len(new_array)):
        sum = 0
        if i >= window_size - 1:
            counter = start_index
            weight_index = 0
            while counter <= i:
                sum += int(new_array[counter] * array_of_weights[weight_index])
                counter += 1
                weight_index += 1
            new_array[i] = sum // window_size
            start_index += 1
    return new_array


def exponential():
    copy_main_list = main_list
    new_array = [0 for _ in range(len(copy_main_list))]
    alpha = 0.8
    for i in range(len(copy_main_list)):
        if i == 0:
            new_array.append(copy_main_list[i])
        else:
            new_array[i] = int(new_array[i - 1] + alpha * (copy_main_list[i] - new_array[i - 1]))
    new_array = new_array[:-1]
    return new_array


def test():
    x = np.arange(0, 50, 1)
    first = tomorrow_like_yesterday()
    second = simple_moving_average()
    third = simple_moving_average_weight()
    fourth = exponential()
    plt.plot(x, main_list)
    plt.plot(x, first, 'g')
    plt.plot(x, second, 'r')
    plt.plot(x, third, 'm')
    plt.plot(x, fourth, 'k')
    plt.savefig("/Users/AlexTheLion/Desktop/PythonCourse_SystemProgramming/Task_4/smoothing/graphs/graph.png", dpi=150)


test()
