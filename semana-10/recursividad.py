def calcular_factorial(numero):
    if isinstance(numero, int):
        if numero < 0:
            return None
        elif numero == 1 or numero == 0:
            return 1
        else:
            return numero * calcular_factorial(numero - 1)

    return None


def multiplicar(numero_menor, numero_mayor):
    if numero_menor == 0:
        return 0
    elif numero_menor == 1:
        return numero_mayor
    else:
        return numero_mayor + multiplicar(numero_menor - 1, numero_mayor)


def calcular_potencia(base, exponente):
    if isinstance(base, int) and isinstance(exponente, int):
        if exponente < 0:
            return None
        elif exponente == 0:
            return 1
        elif exponente == 1:
            return base

        return base * calcular_potencia(base, exponente - 1)


def sumar_lista_yazid(elementos):
    if elementos is None:
        return None

    if isinstance(elementos, list):
        if len(elementos) == 0:
            return 0
        elif len(elementos) == 1:
            return elementos[0]
        else:
            primer_elemento = elementos.pop(0)
            return primer_elemento + sumar_lista_yazid(elementos=elementos)

    return None


def sumar_lista_chavez(elementos):
    if elementos is None:
        return None

    if len(elementos) == 0:
        return 0
    elif len(elementos) == 1:
        return elementos[0]
    else:
        nueva_lista = elementos[1:]
        return elementos[0] + sumar_lista_chavez(elementos=nueva_lista)


def sumar_lista(elementos):
    return sumar_lista_farid(elementos=elementos, posicion=0)


def sumar_lista_auxiliar(elementos, posicion_inicio_lista):
    posicion_fin_lista = len(elementos) - 1
    if posicion_inicio_lista == posicion_fin_lista:
        return elementos[posicion_inicio_lista]
    else:
        nuevo_inicio_lista = posicion_inicio_lista + 1
        return elementos[posicion_inicio_lista] + sumar_lista_auxiliar(
            elementos, posicion_inicio_lista=nuevo_inicio_lista
        )


def sumar_lista_farid(elementos, posicion=0):
    if not isinstance(elementos, list):
        return None
    if posicion == len(elementos):
        return 0
    return elementos[posicion] + sumar_lista_farid(elementos, posicion + 1)


def invertir_lista(elementos):
    if not isinstance(elementos, list):
        return None

    if len(elementos) >= 1:
        inicio_lista = elementos.pop(0)
        invertir_lista(elementos=elementos)
        elementos.append(inicio_lista)

    return None


def invertir_lista_yazid(elementos):
    lista_invertida = []
    invertir_lista_auxiliar(elementos=elementos, lista_invertida=lista_invertida)

    return lista_invertida


def invertir_lista_auxiliar(elementos, lista_invertida):
    if len(elementos) != len(lista_invertida):
        posicion = len(lista_invertida)
        valor_elemento = elementos[posicion]

        lista_invertida.insert(0, valor_elemento)
        invertir_lista_auxiliar(elementos, lista_invertida)


def invertir_lista_in_place(elementos):
    if not isinstance(elementos, list):
        return None

    invertir_lista_in_place_auxiliar(elementos, posicion=0)


def invertir_lista_in_place_auxiliar(elementos, posicion):
    # [1, 2, 3, 4] -> posicion = 0 ---> [4, 2, 3, 1]
    # [1, 2, 3, 4] -> posicion = 1 ---> [4, 3, 2, 1]

    # resultado = []
    if posicion < len(elementos) // 2:
        posicion_de_intercambio = len(elementos) - 1 - posicion

        elementos[posicion], elementos[posicion_de_intercambio] = (
            elementos[posicion_de_intercambio],
            elementos[posicion],
        )

        invertir_lista_in_place_auxiliar(elementos=elementos, posicion=posicion + 1)


def algoritmo_de_euclides(un_numero, otro_numero):
    numero_menor = un_numero
    numero_mayor = otro_numero

    if numero_menor > numero_mayor:
        numero_mayor, numero_menor = numero_menor, numero_mayor

    return algoritmo_de_euclides_auxiliar(
        numero_menor=numero_menor, numero_mayor=numero_mayor
    )


def algoritmo_de_euclides_auxiliar(numero_mayor, numero_menor):
    if numero_menor == 0:
        return numero_mayor
    else:
        return algoritmo_de_euclides_auxiliar(
            numero_mayor=numero_menor, numero_menor=numero_mayor % numero_menor
        )


def algoritmo_euclides_jhostin(un_numero, otro_numero):
    if otro_numero == 0:
        return un_numero

    return algoritmo_euclides_jhostin(otro_numero, un_numero % otro_numero)


def esta_ordenada(elementos):
    if len(elementos) <= 1:
        return True
    else:
        return elementos[0] <= elementos[1] and esta_ordenada(elementos=elementos[1:])


def busqueda_binaria(elementos, objetivo):
    if (
        not isinstance(elementos, list)
        or not isinstance(objetivo, int)
        or elementos is None
    ):
        return None

    if not esta_ordenada(elementos):
        return None

    posicion_inicio = 0
    posicion_fin = len(elementos) - 1
    posicion_medio = (posicion_inicio + posicion_fin) // 2
    elemento_del_medio = elementos[posicion_medio]

    if elemento_del_medio == objetivo:
        pass
    elif objetivo < elemento_del_medio:
        pass
    else:
        pass


if __name__ == "__main__":
    # print(f"{calcular_factorial(-1)=}")  # None
    # print(f"{calcular_factorial('4')=}")  # None
    # print(f"{calcular_factorial(4)=}")  # 24

    # print(f"{multiplicar(6, 4)=}")  # 24
    # print(f"{multiplicar(6, 0)=}")  # 0

    # print(f"{calcular_potencia('2', '5')=}")  # None
    # print(f"{calcular_potencia(2,5)=}")  # 32
    # print(f"{calcular_potencia(2,exponente=-1)=}")  # None

    # print(f"{sumar_lista_chavez(elementos=None)}")  # None
    # print(f"{sumar_lista_chavez(elementos='[1, 2, 3, 4, 5]')}")  # None
    # print(f"{sumar_lista_chavez(elementos=[1 , 3 , 5, 7, 9])=}")  # 25

    # elementos = [1, 3, 5, 7, 9]

    # print(f"{elementos=}")
    # print(f"{sumar_lista(elementos=elementos)=}")  # 25
    # # print(f"{sumar_lista(elementos=elementos)=}")  # 25
    # print(f"{elementos=}")  #  [1, 3, 5, 7, 9]

    # print(f"{invertir_lista(None)=}")  # Retorne None
    # print(f"{invertir_lista(123)}")  # Retorne None

    # elementos = [8, 5, 3, 4, 1]
    # # invertir_lista(elementos=elementos)  # Deberia retornar [1, 4, 3, 5, 8]
    # invertir_lista_in_place(elementos=elementos)
    # print(f"{elementos=}")

    # print(f"{algoritmo_de_euclides(un_numero= 1272, otro_numero=4032)=}")
    # print(f"{algoritmo_de_euclides(un_numero= 4032, otro_numero=1272)=}")

    # print(f"{algoritmo_euclides_jhostin(un_numero= 1272, otro_numero=4032)=}")
    # print(f"{algoritmo_euclides_jhostin(un_numero= 4032, otro_numero=1272)=}")

    print(f"{busqueda_binaria(elementos=None, objetivo=23)=}")  # Deberia retornar None
    print(
        f"{busqueda_binaria(elementos='[1, 2, 3]', objetivo=23)=}"
    )  # Deberia retornar None
    print(
        f"{busqueda_binaria(elementos=[1, 2, 3], objetivo='23')=}"
    )  # Deberia retornar None

    elementos_ordenado = [2, 5, 8, 10, 13, 20, 23, 50, 90]
    elementos_desordenado = [2, 5, 8, 13, 10, 20, 23, 50, 90]

    print(f"{esta_ordenada(elementos_ordenado)=}")  # Deberia ser True
    print(f"{esta_ordenada(elementos_desordenado)=}")  # Deberia ser True

    print(
        f"{busqueda_binaria(elementos=elementos_desordenado, objetivo=23)=}"
    )  # Deberia retornar None

    print(
        f"{busqueda_binaria(elementos=elementos_ordenado, objetivo=23)=}"
    )  # Deberia retornar True

    print(
        f"{busqueda_binaria(elementos=elementos_ordenado, objetivo=7)=}"
    )  # Deberia retornar False
