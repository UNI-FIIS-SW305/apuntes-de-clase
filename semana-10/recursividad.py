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
        return elementos[0] + sumar_lista(elementos=elementos[1:])


if __name__ == "__main__":
    # print(f"{calcular_factorial(-1)=}")  # None
    # print(f"{calcular_factorial('4')=}")  # None
    # print(f"{calcular_factorial(4)=}")  # 24

    # print(f"{multiplicar(6, 4)=}")  # 24
    # print(f"{multiplicar(6, 0)=}")  # 0

    # print(f"{calcular_potencia('2', '5')=}")  # None
    # print(f"{calcular_potencia(2,5)=}")  # 32
    # print(f"{calcular_potencia(2,exponente=-1)=}")  # None

    # print(f"{sumar_lista_yazid(elementos=None)}")  # None
    # print(f"{sumar_lista_yazid(elementos='[1, 2, 3, 4, 5]')}")  # None
    print(f"{sumar_lista_yazid(elementos=[1 , 3 , 5, 7, 9])=}")  # 25
