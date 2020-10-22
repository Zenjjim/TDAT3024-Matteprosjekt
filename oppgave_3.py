# Implementer varianten av Eulers metode gitt i likning (6) i avnsitt 4.1. Og test metoden p ̊a systemet som best ̊ar av likningene (3) og (4)._
import numpy as np
from oppgave_1 import exp
# I er treghetsmoment, W_i resultatene og L er dreiemomentet


def calculate_omega_i(I, W_i, L):
    I_inv = np.linalg.inv(I)
    W_t = np.transpose(W_i)
    return I_inv @ W_t @ L


def Euler(h, X_0, I, L):
    W_i = [X_0]
    for i in range(1, h):
        # For all W-values after w0
        omega_i = calculate_omega_i(I, W_i[-1], L)
        # Find Omega formel 18
        Omega = np.array([[0, -omega_i[2], omega_i[1]],
                          [omega_i[2], 0, -omega_i[0]],
                          [-omega_i[1], omega_i[0], 0]])
        # Calculate W_i+1
        W_i.append(np.matmul(W_i[-1], exp(Omega, 1/h)))
    return W_i


def test():
    L = np.array([1, 0, 0])
    indentity = np.identity(3)
    X_0 = indentity
    I = indentity
    W = Euler(4, X_0, I, L)
    for array in W:
        print(array)

test()
