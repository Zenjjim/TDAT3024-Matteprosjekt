# Implementer varianten av Eulers metode gitt i likning (6) i avnsitt 4.1.
import numpy as np
from oppgave_1 import exp
from oppgave_2 import X_t
import matplotlib.pyplot as plt
# I er treghetsmoment, W_i resultatene og L er dreiemomentet

plots = [[[] for x in range(3)] for y in range(3)]


def calculate_omega_i(I, W_i, L):
    I_inv = np.linalg.inv(I)
    W_t = np.transpose(W_i)
    return np.matmul(np.matmul(I_inv, W_t), L)


def Euler(h, X_0, I, L):
    W_i = X_0
    x_t = X_t(0)
    find_diff(0, x_t, W_i)
    for i in range(1, int(1/h)+1):
        # For all W-values after w0
        omega_i = calculate_omega_i(I, W_i, L)
        # Find Omega formel 18
        Omega = np.array([[0, -omega_i[2], omega_i[1]],
                          [omega_i[2], 0, -omega_i[0]],
                          [-omega_i[1], omega_i[0], 0]])
        # Calculate W_i+1
        W_i = np.matmul(W_i, exp(Omega, h))
        x_t = X_t(h*i)
        find_diff(i, x_t, W_i)
    return W_i


def test():
    L = np.array([1, 0, 0])
    indentity = np.identity(3)
    X_0 = indentity
    I = indentity
    W = Euler(0.25, X_0, I, L)
    fig, axs = plt.subplots(3, 3)

    axis = ['x', 'y', 'z']
    for i in range(3):
        for j in range(3):
            axs[i, j].plot(plots[i][j])
            axs[i, j].set_title(f'Axis [{axis[i]},{axis[j]}]')

    plt.show()


def find_diff(i, x_t, W_i):
    diff = np.abs(W_i - x_t)
    for i in range(3):
        for j in range(3):
            plots[i][j].append(diff[i][j])


test()
