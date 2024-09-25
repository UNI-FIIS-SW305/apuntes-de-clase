from typing import Any


class NodoSimple:

    def __init__(self, elemento, siguiente) -> None:
        self.elemento = elemento
        self.siguiente = siguiente


def pruebas_lista_enlazada():
    cabeza_lista = NodoSimple(elemento="Maria", siguiente=None)
    nodo_juan = NodoSimple(elemento="Juan", siguiente=None)

    cabeza_lista.siguiente = nodo_juan
    nodo_juan.siguiente = NodoSimple(elemento="Pepa", siguiente=None)

    nodo_actual = cabeza_lista
    while nodo_actual is not None:
        print(f"{nodo_actual.elemento=}")
        nodo_actual = nodo_actual.siguiente


class PilaBasadaEnListasEnlazadas:

    def __init__(self) -> None:
        self.cabeza_lista = None  # Este campo apunta hacia una instancia de NodeSimple.
        self.numero_elementos = 0

    def apilar(self, elemento):
        nuevo_nodo = NodoSimple(elemento=elemento, siguiente=self.cabeza_lista)
        self.cabeza_lista = nuevo_nodo
        self.numero_elementos = self.numero_elementos + 1

    def tamanio(self):
        return self.numero_elementos

    def esta_vacia(self):
        # return self.numero_elementos == 0
        return self.cabeza_lista is None

    def cima(self):
        if self.esta_vacia():
            return None

        return self.cabeza_lista.elemento

    def desapilar(self):
        if self.esta_vacia():
            return None

        resultado = self.cabeza_lista.elemento
        self.cabeza_lista = self.cabeza_lista.siguiente

        self.numero_elementos = self.numero_elementos - 1
        return resultado


if __name__ == "__main__":
    pila = PilaBasadaEnListasEnlazadas()

    pila.apilar("w")
    pila.apilar("o")
    pila.apilar("r")

    valor = pila.desapilar()  # Deberia tener: r
    print(f"{valor=}")

    valor = pila.desapilar()  # Deberia tener: o
    print(f"{valor=}")
    print(f"{pila.tamanio()=}")  # Deberia ser: 1

    print(f"{pila.cima()=}")  # Deberia ser: w
