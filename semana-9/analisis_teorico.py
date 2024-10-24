import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def funcion_temporal_iteracion(n):
    return 1 + n * 2 + 1


def funcion_temporal_gauss(n):
    return 1 + 1 + 1 + 1


def analisis_suma_enteros(n):
    valores_n = np.linspace(0, 20, 21)

    # Algoritmo iterativo
    operaciones_iteracion = []
    operaciones_gauss = []

    for n in valores_n:
        operaciones_iteracion.append(int(funcion_temporal_iteracion(n)))
        operaciones_gauss.append(int(funcion_temporal_gauss(n)))

    print(f"{valores_n=}")
    print(f"{operaciones_iteracion=}")
    print(f"{operaciones_gauss=}")

    plt.plot(valores_n, operaciones_iteracion, label="Algoritmo Iterativo")
    plt.plot(valores_n, operaciones_gauss, label="Formula de Gauss")
    plt.xlabel("Valor de n")
    plt.ylabel("Numero de operacion (Valor de la funcion temporal)")
    plt.legend(loc="upper left")


def funcion_temporal_A(n):
    return 3 * n**3


def funcion_temporal_B(n):
    return 3 * n**3 + 2 * n**2 + 3 * n + 5


def equivalentes_asintoticos():
    valores_n = [10**exponente for exponente in range(1, 9)]

    operaciones_funcion_A = []
    operaciones_funcion_B = []

    for n in valores_n:
        operaciones_funcion_A.append(int(funcion_temporal_A(n)))
        operaciones_funcion_B.append(int(funcion_temporal_B(n)))

    plt.plot(
        valores_n, operaciones_funcion_A, label="3 * n**3", linestyle="--", marker="o"
    )
    plt.plot(
        valores_n,
        operaciones_funcion_B,
        label="3 * n**3 + 2 * n**2 + 3 * n + 5",
        linestyle="--",
        marker="o",
        alpha=0.7,
    )
    plt.xlabel("Valor de n")
    plt.ylabel("Numero de operacion (Valor de la funcion temporal)")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend(loc="upper left")

    datos = pd.DataFrame(
        {
            "valores_n": valores_n,
            "operaciones_funcion_A": operaciones_funcion_A,
            "operaciones_funcion_B": operaciones_funcion_B,
        }
    )


def orden(n):
    return n**3


if __name__ == "__main__":
    valores_n = [valor_n for valor_n in range(0, 121, 5)]
    print(f"{valores_n=}")

    # operaciones_funcion_A = []
    operaciones_funcion_B = []

    for n in valores_n:
        # operaciones_funcion_A.append(int(funcion_temporal_A(n)))
        operaciones_funcion_B.append(int(funcion_temporal_B(n)))

    plt.plot(
        valores_n,
        operaciones_funcion_B,
        label="3 * n**3 + 2 * n**2 + 3 * n + 5",
        linestyle="--",
        marker="o",
    )

    cota_superior_candidata = []
    valor_c = 4
    for n in valores_n:
        cota_superior_candidata.append(valor_c * orden(n))

    plt.plot(
        valores_n,
        cota_superior_candidata,
        label=f"{valor_c} * n**3",
        linestyle="--",
        marker="o",
    )

    plt.xlabel("Valor de n")
    plt.ylabel("Numero de operacion (Valor de la funcion temporal)")
    # plt.xscale("log")
    # plt.yscale("log")
    plt.legend(loc="upper left")
