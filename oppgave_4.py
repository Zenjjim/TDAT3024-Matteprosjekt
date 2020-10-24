import numpy as np
from oppgave_1 import exp

def liten_sigma_til_stor(liten):
    return np.array([[0, -liten[2], liten[1]],
                     [liten[2], 0, -liten[0]],
                     [-liten[1], liten[0], 0]
                    ])


def rungeKutta(x0, treghetsmoment, dreiemoment, h):
    # Iterate for number of iterations
    W = x0

    treg_inv = np.linalg.inv(treghetsmoment)
    W_trans = W.transpose()

    "Apply Runge Kutta Formulas to find next value of W"
    k1 = np.matmul(np.matmul(treg_inv, W_trans), dreiemoment)
    k2 = np.matmul(np.matmul(np.matmul(treg_inv, exp(liten_sigma_til_stor(k1),-h/2)),W_trans),
                   dreiemoment)
    k3 = np.matmul(np.matmul(np.matmul(treg_inv, exp(liten_sigma_til_stor(k2), -h / 2)), W_trans),
                   dreiemoment)
    k4 = np.matmul(np.matmul(np.matmul(treg_inv, exp(liten_sigma_til_stor(k3), -h)), W_trans),
                   dreiemoment)

    # Update next value of W
    W = np.matmul(W, exp(liten_sigma_til_stor(k1) + 2*liten_sigma_til_stor(k2) +
            2*liten_sigma_til_stor(k3) + liten_sigma_til_stor(k4),h/6))

    return W
