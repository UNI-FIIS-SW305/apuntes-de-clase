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


def prueba_pilas():
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


class ColaBasadaEnListaEnlazadas:

    def __init__(self) -> None:
        self.cabeza_lista = None
        self.numero_elementos = 0

    def encolar(self, elemento):
        nuevo_nodo = NodoSimple(elemento=elemento, siguiente=None)

        if self.cabeza_lista is None:
            self.cabeza_lista = nuevo_nodo
        else:
            ultimo_nodo = self.cabeza_lista
            # Algo pasa
            while ultimo_nodo.siguiente is not None:
                ultimo_nodo = ultimo_nodo.siguiente

            ultimo_nodo.siguiente = nuevo_nodo

        self.numero_elementos = self.numero_elementos + 1

    def esta_vacia(self):
        return self.numero_elementos == 0

    def desencolar(self):
        if self.esta_vacia():
            return None

        resultado = self.cabeza_lista.elemento
        self.cabeza_lista = self.cabeza_lista.siguiente
        self.numero_elementos = self.numero_elementos - 1

        return resultado

    def representar(self):
        elementos = []
        nodo_actual = self.cabeza_lista
        while nodo_actual is not None:
            elementos.append(str(nodo_actual.elemento))
            nodo_actual = nodo_actual.siguiente

        return f'({",".join(elementos)})'

    def primero(self):
        if self.numero_elementos == 0:
            return None
        return self.cabeza_lista.elemento


class ColaBasadaEnListasEnlazadas2:

    def __init__(self) -> None:
        self.cabeza_lista = None
        self.final_lista = None
        self.numero_elementos = 0

    def representar(self):
        elementos = []
        nodo_actual = self.cabeza_lista
        while nodo_actual is not None:
            elementos.append(str(nodo_actual.elemento))
            nodo_actual = nodo_actual.siguiente

        return f'({",".join(elementos)})'

    def esta_vacia(self):
        return self.numero_elementos == 0

    def encolar(self, elemento):
        nuevo_nodo = NodoSimple(elemento=elemento, siguiente=None)

        if self.esta_vacia():
            self.cabeza_lista = nuevo_nodo
        else:
            self.final_lista.siguiente = nuevo_nodo

        self.final_lista = nuevo_nodo
        self.numero_elementos = self.numero_elementos + 1

    def desencolar(self):
        if self.esta_vacia():
            return None

        resultado = self.cabeza_lista.elemento
        self.cabeza_lista = self.cabeza_lista.siguiente

        if self.esta_vacia():
            self.final_lista = None

        self.numero_elementos = self.numero_elementos - 1
        return resultado

    def primero(self):
        if self.esta_vacia():
            return None
        return self.cabeza_lista.elemento


if __name__ == "__main__":
    # una_cola = ColaBasadaEnListaEnlazadas()
    una_cola = ColaBasadaEnListasEnlazadas2()

    una_cola.encolar(1)
    una_cola.encolar(2)
    una_cola.encolar(3)

    resultado = una_cola.desencolar()
    print(f" Desencolar ->{resultado=}")  # Deberia ser: 1
    print(f"{una_cola.numero_elementos=}")  # Deberia ser: 2
    print(f"{una_cola.representar()=}")  # Deberia ser: (2,3)

    print(f"{una_cola.primero()=}")  # Deberia ser: 2

    # Primera cola: 1000 elementos
    # Segunda cola: 2 millones elementos
