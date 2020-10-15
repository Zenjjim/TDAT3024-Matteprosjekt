import numpy as np
import scipy
from oppgave_1 import exp

# Har:
# Dreiemoment L
# Treghetsmoment I (matrise)
# W_i
# Har exp() fra oppgave 1a)

# Trenger:
# Σ_i

def litenSigmaTilStor(liten):
    return np.array([[0, -liten[2], liten[1]], [liten[2], 0, -liten[0]], [-liten[1], liten[0], 0]])


def rungeKutta(x0, W0, x, h):
    # Count number of iterations using step size or
    # step height h
    n = (int)((x - x0)/h)
    # Iterate for number of iterations
    W = W0

    I = np.array([[1,0,0],[0,1,0],[0,0,1]]) # need proper data
    L = np.dot(I, [1,1,1]) # Need proper data
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = np.linalg.inv(I)*W.transpose()*L
        k2 = np.linalg.inv(I)*exp(litenSigmaTilStor(k1),-h/2)*W.transpose()*L
        k3 = np.linalg.inv(I)*exp(litenSigmaTilStor(k2), -h/2)*W.transpose()*L
        k4 = np.linalg.inv(I)*exp(litenSigmaTilStor(k3), -h)*W.transpose()*L

        # Update next value of y
        W = W*exp(litenSigmaTilStor(k1) + 2*litenSigmaTilStor(k2) + 2*litenSigmaTilStor(k3) + litenSigmaTilStor(k4), h/6)

        # Update next value of x
        x0 = x0 + h
    return W

if __name__ == "__main__":
  testLiten = np.array([2, 3, 4])
  print(litenSigmaTilStor(testLiten))
