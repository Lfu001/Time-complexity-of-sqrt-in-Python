from math import sqrt
from time import time

import matplotlib.pyplot as plt
import numpy as np


def measure_time_math_sqrt(n: int):
    t = time()
    for _ in range(100000):
        sqrt(n)
    return time() - t


def measure_time_np_sqrt(n: int):
    t = time()
    for _ in range(100000):
        np.sqrt(n)
    return time() - t


def measure_time_py_operator(n: int):
    t = time()
    for _ in range(100000):
        n**0.5
    return time() - t


if __name__ == "__main__":
    x = np.array(range(1000))
    v_measure_time_math_sqrt = np.vectorize(measure_time_math_sqrt)
    v_measure_time_np_sqrt = np.vectorize(measure_time_np_sqrt)
    v_measure_time_py_operator = np.vectorize(measure_time_py_operator)
    y_math = v_measure_time_math_sqrt(x) * 1000
    y_np = v_measure_time_np_sqrt(x) * 1000
    y_py = v_measure_time_py_operator(x) * 1000

    fig = plt.figure()
    plt.plot(x, y_math, label="math.sqrt", color="C0")
    plt.plot(x, y_np, label="numpy.sqrt", color="C1")
    plt.plot(x, y_py, label="** 0.5", color="C2")
    plt.title("Comparison of time to compute sqrt")
    plt.xlabel("input size: n")
    plt.ylabel("Computing time [ms]")
    plt.legend()
    plt.grid()
    fig.savefig("comparison_of_time_to_compute_sqrt.png")
