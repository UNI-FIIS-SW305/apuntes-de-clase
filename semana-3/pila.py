class PilaBasadaEnListasPrime:

    def __init__(self) -> None:
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.insert(0, elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None

        return self.elementos.pop(0)

    def esta_vacia(self):
        return self.tamanio() == 0

    def tamanio(self):
        return len(self.elementos)

    def cima(self):
        if self.esta_vacia():
            return None

        return self.elementos[0]


class PilaBasadaEnListas:

    def __init__(self) -> None:
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def tamanio(self):
        return len(self.elementos)

    def desapilar(self):
        if self.esta_vacia():
            return None

        return self.elementos.pop()

    def cima(self):
        if self.esta_vacia():
            return None

        return self.elementos[-1]

    def esta_vacia(self):
        return self.tamanio() == 0


def probar_pilas():
    # pila = PilaBasadaEnListas()
    pila = PilaBasadaEnListasPrime()
    print(f"{pila.elementos=}")

    pila.apilar("w")
    pila.apilar("o")
    pila.apilar("r")
    print(f"{pila.elementos=}")

    valor = pila.desapilar()  # Deberia tener: r
    print(f"{valor=}")
    print(f"{pila.elementos=}")  # Deberia ser: [w, o]
    valor = pila.cima()
    print(f"{valor=}")  # Deberia ser O
    print(f"{pila.elementos=}")  # Deberia ser: [w, o]

    print(f"{pila.tamanio()=}")  # Deberia ser 2

    print(f"{pila.esta_vacia()=}")  # Deberia ser False

    # otra_pila = PilaBasadaEnListas()
    # valor = otra_pila.desapilar()  # Deberia tener: None
    # print(f"{valor=}")

    otra_pila = PilaBasadaEnListas()
    valor = otra_pila.cima()  # Deberia tener: None
    print(f"{valor=}")

    print(f"{otra_pila.esta_vacia()=}")  # Deberia ser True


def invertir_texto(texto):
    resultado = ""

    pila = PilaBasadaEnListas()

    for letra in texto:
        pila.apilar(letra)

    print(f"{pila.elementos=}")

    # for _ in range(pila.tamanio()):
    #     resultado = resultado + pila.desapilar()

    while not pila.esta_vacia():
        resultado = resultado + pila.desapilar()

    return resultado


def probar_invertir():
    resultado = invertir_texto("AMOR")
    print(f"{resultado=}")  # Deberia ser ROMA


def validar_parentesis(expresion):
    pila = PilaBasadaEnListas()

    for parentesis in expresion:
        if parentesis == "(":
            pila.apilar(parentesis)
        elif parentesis == ")":
            if not pila.esta_vacia():
                pila.desapilar()
            else:
                return False

    print(f"{pila.elementos}")

    return pila.esta_vacia()


def probar_parentesis(self):
    resultado = validar_parentesis("(()())")  # Deberia ser True
    print(f"{resultado=}")

    resultado = validar_parentesis("(()()))")  # Deberia ser False
    print(f"{resultado=}")

    resultado = validar_parentesis("())(")  # Deberia ser False
    print(f"{resultado=}")


def validar_parentesis_prime(expresion):
    pila = PilaBasadaEnListas()

    simbolos_de_entrada = ["(", "{", "["]
    simbolos_de_cierre = [")", "}", "]"]

    for simbolo_actual in expresion:
        if simbolo_actual in simbolos_de_entrada:
            # Para simbolos de apertura.
            pila.apilar(simbolo_actual)
        elif simbolo_actual in simbolos_de_cierre:
            if not pila.esta_vacia():
                simbolo_en_pila = pila.desapilar()

                if simbolos_de_entrada.index(
                    simbolo_en_pila
                ) != simbolos_de_cierre.index(simbolo_actual):
                    return False

            else:
                return False

    print(f"{pila.elementos}")

    return pila.esta_vacia()


if __name__ == "__main__":
    resultado = validar_parentesis_prime("[(){{}}()]")
    print(f"{resultado=}")  # Deberia ser True

    resultado = validar_parentesis_prime("[(])")
    print(f"{resultado=}")  # Deberia ser False
