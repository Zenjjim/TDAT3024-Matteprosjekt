from oppgave_4 import rungeKutta
import numpy as np
from oppgave_1 import treghetsmoment

if __name__ == "__main__":
    x0 = np.identity(3)
    """Oppgave 5a"""
    rotasjonshastighet = np.array([1, 0.05, 0])
    #dreiemoment = np.matmul(np.matmul(x0,treghetsmoment()), rotasjonshastighet)
    dreiemoment = np.matmul(treghetsmoment(), rotasjonshastighet)
    #print(dreiemoment)


    svar = rungeKutta(x0, treghetsmoment(),dreiemoment, 0.1)
    print(svar)