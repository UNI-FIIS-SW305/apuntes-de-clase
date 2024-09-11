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


if __name__ == "__main__":
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
