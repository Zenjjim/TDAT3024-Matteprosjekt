import numpy as np
import math

def exp(omega_matrise, h):
    i = np.identity(omega_matrise.shape[0])
    omega = np.sqrt(omega_matrise[0][1] ** 2 + omega_matrise[0][2] ** 2 + omega_matrise[1][2] ** 2)
    return i + (1 - np.cos(omega * h)) * (np.matmul(omega_matrise, omega_matrise) / (omega * omega)) + np.sin(
        omega * h) * (omega_matrise / omega)


def energi_rot(treghetsmoment, rotasjons_vektor):
    dreiemoment = np.dot(treghetsmoment, rotasjons_vektor)
    return (1 / 2) * np.matmul(dreiemoment, rotasjons_vektor)


# Nøkkelens treghetsmoment I
def treghetsmoment():
    L_1 = 0.08  # Lengden av håndtaket
    R_1 = 0.01  # Radius til håndtaket

    L_2 = 0.04  # Lengden til sylinderen festet til håndtaket
    R_2 = 0.01  # Radius til sylinderen

    p = 6.7  # Massetettheten til håndtak og sylinder per cm3
    x1 = -1.0  # Massesenteret til håndtaket
    x2 = 2.0  # Massesenteret til sylinderen

    M_1 = math.pi * R_1 ** 2 * L_1 * 1000000 * p  # Håndtakets masse
    M_2 = math.pi * R_2 ** 2 * L_2 * 1000000 * p  # Sylinderens masse

    Ixx = (M_1 * (R_1 ** 2) / 4) + (M_1 * (L_1 ** 2) / 12) + (M_2 * (R_2 ** 2) / 2)

    Iyy = (M_1 * (R_1 ** 2)) + (M_2 * L_2**2 / 4) + (M_1 * (R_1 ** 2) / \
          2) + (M_2 * (R_2 ** 2) / 4) + (M_2 * (L_2 ** 2) / 12)

    Izz = (M_1 * (R_1 ** 2)) + (M_2 * L_2**2 / 4) + (M_1 * (R_1 ** 2) / 4) + (M_1 * \
          (L_1 ** 2) / 12) + (M_2 * (R_2 ** 2) / 4) + (M_2 * (L_2 ** 2) / 12)

    return np.array([[Ixx, 0, 0],
                     [0, Iyy, 0],
                     [0, 0, Izz]
                     ])


if __name__ == "__main__":
    w = [1, 2, 3]  # Rotasjonsvektor


    """Oppgave 1a"""
    print("Oppgave 1a:")
    h = 4  # Steglengde

    # Omega matrisen
    omega = np.array([
        [0, -w[2], w[1]],
        [w[2], 0, -w[0]],
        [-w[1], w[0], 0]
    ])
    print(np.matmul(exp(omega, h).transpose(), exp(omega, h)))

    """Oppgave 1b"""
    print("Oppgave 1b:")
    rot_vek = np.array(w)
    treg_mom = 3 # Skal dette bare være tall?
    print(energi_rot(treg_mom, rot_vek), "J")

    """Oppgave 1c"""
    print("Oppgave 1c:")

    treghet = treghetsmoment()
    print("Treghetsmoment om x-akse:",treghet[0][0])
    print("Treghetsmoment om y-akse:",treghet[1][1])
    print("Treghetsmoment om z-akse:",treghet[2][2])
