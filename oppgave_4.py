import numpy as np
import scipy


I = np.array([[1,0,0],[0,1,0],[0,0,1]])
L = np.array([[]])
rotasjonsVektorw = np.array([1,1,1])
treghetsmomentI = 3
dreiemomentL = np.dot(treghetsmomentI, rotasjonsVektorw)

def getSigma(sigmaVector):
    pass

def RK4_iteration(W):
    sigma1 = np.linalg.inv(I)*W.transpose()*dreiemomentL


print(I.transpose())

# GEEKS FOR GEEKS
# Finds value of y for a given x using step size h
# and initial value y0 at x0.


def rungeKutta(x0, y0, x, h):
    # Count number of iterations using step size or
    # step height h
    n = (int)((x - x0)/h)
    # Iterate for number of iterations
    y = y0
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * dydx(x0 + h, y + k3)

        # Update next value of y
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)

        # Update next value of x
        x0 = x0 + h
    return y
