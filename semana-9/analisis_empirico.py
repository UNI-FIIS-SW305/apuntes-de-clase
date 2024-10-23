import time
import pandas as pd


def sumar_n_primeros_enteros(n):
    resultado = 0
    for numero in range(1, n + 1):
        resultado = resultado + numero

    return resultado


if __name__ == "__main__":
    valores_de_n = [10**exponente for exponente in range(1, 9)]
    tiempos_de_ejecucion = []

    for valor_n in valores_de_n:
        inicio_ejecucion = time.time()  # 01- 01 - 1970
        sumar_n_primeros_enteros(valor_n)
        tiempo_ejecucion = time.time() - inicio_ejecucion
        tiempos_de_ejecucion.append(tiempo_ejecucion)

    print(f"{valores_de_n=}")
    print(f"{tiempos_de_ejecucion=}")

    datos_analisis = pd.DataFrame(
        {"valores_de_n": valores_de_n, "tiempos_de_ejecucion": tiempos_de_ejecucion}
    )

    print(datos_analisis.head())
