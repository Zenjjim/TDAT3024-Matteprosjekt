import numpy as np

def exp(omega_matrise, h):
    i = np.identity(omega_matrise.shape[0])
    omega = np.sqrt(omega_matrise[0][1] ** 2 + omega_matrise[0][2] ** 2 + omega_matrise[1][2] ** 2)
    return i + (1 - np.cos(omega * h)) * (np.matmul(omega_matrise, omega_matrise) / (omega * omega)) + np.sin(
        omega * h) * (omega_matrise / omega)


def energi_rot(I, rotVek):
    L = np.dot(I, rotVek)
    return (1 / 2) * np.dot(L, rotVek)


if __name__ == "__main__":
    """Oppgave 1a"""
    print("Oppgave 1a:")
    h = 4  # Steglengde
    w = {"x": 1, "y": 2, "z": 3}  # Rotasjonsvektor

    # Omega matrisen
    omega = np.array([
        [0, -w["z"], w["y"]],
        [w["z"], 0, -w["x"]],
        [-w["y"], w["x"], 0]
    ])
    print(np.matmul(exp(omega, h).transpose(), exp(omega, h)))

    """Oppgave 1b"""
    print("Oppgave 1b:")
    rotVek = np.array([1, 1, 1])
    I = 3
    print(energi_rot(I, rotVek))

    """Oppgave 1c"""
    print("Oppgave 1c:")
    L_1 = 0.08  # Lengden av håndtaket
    R_1 = 0.01  # Radius til håndtaket

    L_2 = 0.04  # Lengden til sylinderen festet til håndtaket
    R_2 = 0.01  # Radius til sylinderen

    p = 6.7  # Massetettheten til håndtak og sylinder
    x1 = -1.0  # Massesenteret til håndtaket
    x2 = 2.0  # Massesenteret til sylinderen

    M_1 = 253.0 / 2  # Håndtakets masse
    M_2 = 253.0 / 2  # Sylinderens masse

    # Nøkkelens treghetsmoment I
    Ixx = M_1 * (R_1 ** 2) / 4 + M_1 * (L_1 ** 2) / 12 + M_2 * (R_2 ** 2) / 2

    Iyy = M_1 * (R_1 ** 2) + M_2 * L_2 / 4 + M_1 * (R_1 ** 2) / \
          2 + M_2 * (R_2 ** 2) / 4 + M_2 * (L_2 ** 2) / 12

    Izz = M_1 * (R_1 ** 2) + M_2 * L_2 / 4 + M_1 * (R_1 ** 2) / 4 + M_1 * \
          (L_1 ** 2) / 12 + M_2 * (R_2 ** 2) / 4 + M_2 * (L_2 ** 2) / 12

    print(Ixx)
    print(Iyy)
    print(Izz)
