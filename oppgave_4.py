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


def liten_sigma_til_stor(liten):
  return np.array([[0, -liten[2], liten[1]],
                   [liten[2], 0, -liten[0]],
                   [-liten[1], liten[0], 0]
                   ])


def rungeKutta(x0, W0, x, h):
  # Count number of iterations using step size or
  # step height h
  n = (int)((x - x0)/h)
  # Iterate for number of iterations
  W = W0

  treghetsmoment = np.array([[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1]
                            ]) # Need proper data

  dreiemoment = np.array([1, 0, 0])  # Need proper data

  treg_inv = np.linalg.inv(treghetsmoment)
  W_trans = W.transpose()
  for i in range(1, n + 1):
      "Apply Runge Kutta Formulas to find next value of y"

      k1 = np.matmul(np.matmul(treg_inv, W_trans), dreiemoment)
      k2 = np.matmul(np.matmul(np.matmul(treg_inv, exp(liten_sigma_til_stor(k1),-h/2)),W_trans),dreiemoment)
      k3 = np.matmul(np.matmul(np.matmul(treg_inv, exp(liten_sigma_til_stor(k2), -h / 2)), W_trans), dreiemoment)
      k4 = np.matmul(np.matmul(np.matmul(treg_inv, exp(liten_sigma_til_stor(k3), -h)), W_trans), dreiemoment)

      # Update next value of W
      W = np.matmul(W, exp(liten_sigma_til_stor(k1) + 2*liten_sigma_til_stor(k2) +
                2*liten_sigma_til_stor(k3) + liten_sigma_til_stor(k4),h/6))

  return W


if __name__ == "__main__":
    testLiten = np.array([2, 3, 4])
    print(liten_sigma_til_stor(testLiten))
