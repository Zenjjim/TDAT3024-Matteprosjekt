import matplotlib.pyplot as plt
from oppgave_1 import treghetsmoment
import numpy as np
from oppgave_4 import rungeKutta


x0 = np.identity(3)
treghetsmoment = treghetsmoment()

rotasjonsvektor_a = np.array([1, 0.05, 0])
dreiemoment_a = np.matmul(treghetsmoment, rotasjonsvektor_a)

plots = [[[] for x in range(3)] for y in range(3)]

# Interval [0‚1] with step size 0.01
for k in range(100):
    x_i = rungeKutta(x0, treghetsmoment, dreiemoment_a, 0.01)
    for i in range(3):
        for j in range(3):
            plots[i][j].append(x_i[i][j])

    x0 = x_i

print(x0)

for i in range(3):
    for j in range(3):
        plt.plot(plots[i][j])

plt.ylabel('some numbers')
plt.show()