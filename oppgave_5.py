from oppgave_4 import rungeKutta
import numpy as np
from oppgave_1 import treghetsmoment

if __name__ == "__main__":
    x0 = np.identity(3)

    """Oppgave 5a"""
    svar = rungeKutta(x0, np.array([1, 0.05, 0]),treghetsmoment(),0.1)
    print(svar)
