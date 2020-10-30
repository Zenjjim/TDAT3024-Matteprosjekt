import matplotlib.pyplot as plt
from oppgave_1 import treghetsmoment
import numpy as np
from oppgave_4 import rungeKutta

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

x0 = np.identity(3)
treghetsmoment = treghetsmoment()

rotasjonsvektor_a = np.array([0.05, 0 , 1])
dreiemoment_a = np.matmul(treghetsmoment, rotasjonsvektor_a)

plots = []

# Interval [0‚1] with step size 0.01
for k in range(30000):
    x_i = rungeKutta(x0, treghetsmoment, dreiemoment_a, 0.01)
    plots.append(x_i)
    x0 = x_i

p0 = [0.799319, -3.477045e-01, 0.490093]
p1 = [0.852512, 9.113778e-16, -0.522708]
p2 = [0.296422, 9.376042e-01, 0.181748]


fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))


def get_arrow(i):
    origin = [0, 0, 0]
    plot = plots[int(i)]
    X, Y, Z = zip(origin, origin, origin)
    U, V, W = zip(plot[0], plot[1], plot[2])
    return X, Y, Z, U, V, W


quiver = ax.quiver(*get_arrow(0))

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)


def update(i):
    global quiver
    quiver.remove()
    print(i)
    quiver = ax.quiver(*get_arrow(i), arrow_length_ratio=0.01)


ani = FuncAnimation(fig, update, frames=np.linspace(
    0, len(plots)-1, int((len(plots)-1)/60)), interval=50)
plt.show()