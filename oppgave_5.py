from oppgave_4 import rungeKutta
import numpy as np
from oppgave_1 import treghetsmoment

if __name__ == "__main__":
    x0 = np.identity(3)
    treghetsmoment = treghetsmoment()

    """Oppgave 5a"""
    rotasjonsvektor_a = np.array([1, 0.05, 0])

    """
    dreiemoment_x = treghetsmoment[0][0]*rotasjonsvektor[0]
    dreiemoment_y = treghetsmoment[1][1]*rotasjonsvektor[1]
    dreiemoment_z = treghetsmoment[2][2]*rotasjonsvektor[2]

    dreiemoment = np.array([dreiemoment_x, dreiemoment_y, dreiemoment_z])
    """
    dreiemoment_a = np.matmul(treghetsmoment, rotasjonsvektor_a)

    print("Oppgave 5a:")
    print(rungeKutta(x0, treghetsmoment,dreiemoment_a, 0.1))

    """Oppgave 5b"""
    rotasjonsvektor_b = np.array([0, 1, 0.05])

    dreiemoment_b = np.matmul(treghetsmoment, rotasjonsvektor_b)

    print("Oppgave 5b:")
    print(rungeKutta(x0, treghetsmoment, dreiemoment_b, 0.1))

    """Oppgave 5c"""
    rotasjonsvektor_c = np.array([0.05, 0, 1])

    dreiemoment_c = np.matmul(treghetsmoment, rotasjonsvektor_c)

    print("Oppgave 5c:")
    print(rungeKutta(x0, treghetsmoment, dreiemoment_c, 0.1))