import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


def calc_characteristics():

    a = np.array([[0, 1], [-4, -5]])

    b = np.array([[0], [1]])

    c = np.array([[5, 6]])

    d = np.array([[0]])

    system = signal.StateSpace(a, b, c, d)
    w, mag, phase = signal.bode(system)

    plt.subplot(1, 2, 1)
    plt.title("Frequency characteristic")
    plt.semilogx(w, mag)
    plt.subplot(1, 2, 2)
    plt.title("Phase characteristic")
    plt.semilogx(w, phase)

    plt.savefig("/Users/AlexTheLion/Desktop/PythonCourse_SystemProgramming/Task_5/characteristics/characteristics.png")


calc_characteristics()
