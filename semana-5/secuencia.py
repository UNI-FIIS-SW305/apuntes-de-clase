from listas_enlazadas import NodoSimple


class SecuenciaListasEnlazadas:

    def __init__(self) -> None:
        self.cabeza_lista = None
        self.final_lista = None
        self.numero_elementos = 0

    def esta_vacia(self):
        return self.numero_elementos == 0

    def insertar_frente(self, elemento):
        """
        Similar a apilar()
        """
        nuevo_nodo = NodoSimple(elemento=elemento, siguiente=self.cabeza_lista)

        if self.esta_vacia():
            self.final_lista = nuevo_nodo

        self.cabeza_lista = nuevo_nodo
        self.numero_elementos = self.numero_elementos + 1

    def insertar_final(self, elemento):
        nuevo_nodo = NodoSimple(elemento=elemento, siguiente=None)

        if self.esta_vacia():
            self.final_lista = nuevo_nodo
            self.cabeza_lista = nuevo_nodo
        else:
            self.final_lista.siguiente = nuevo_nodo
            self.final_lista = self.final_lista.siguiente

        self.numero_elementos = self.numero_elementos + 1

    def remover_frente(self):

        if self.esta_vacia():
            return None

        resultado = self.cabeza_lista.elemento
        self.cabeza_lista = self.cabeza_lista.siguiente

        if self.cabeza_lista is None:
            self.final_lista = None

        self.numero_elementos = self.numero_elementos - 1
        return resultado

    def remover_final(self):
        if self.esta_vacia():
            return None
        elif self.numero_elementos == 1:
            return self.remover_frente()
        else:
            resultado = self.final_lista.elemento
            penultimo_nodo = self.cabeza_lista

            while penultimo_nodo.siguiente != self.final_lista:
                penultimo_nodo = penultimo_nodo.siguiente

            penultimo_nodo.siguiente = None
            self.final_lista = penultimo_nodo
            self.numero_elementos = self.numero_elementos - 1

            return resultado

    def representar(self):
        elementos = []

        puntero_actual = self.cabeza_lista
        while puntero_actual is not None:
            elementos.append(str(puntero_actual.elemento))
            puntero_actual = puntero_actual.siguiente

        return f"({','.join(elementos)})"

    def obtener_elemento(self, posicion):
        if posicion > self.numero_elementos - 1 or posicion < 0:
            return None

        nodo_objetivo = self.cabeza_lista
        for _ in range(posicion):
            nodo_objetivo = nodo_objetivo.siguiente

        return nodo_objetivo.elemento

    def obtener_posicion(self, elemento):

        nodo_objetivo = self.cabeza_lista

        for posicion_candidata in range(self.numero_elementos - 1):
            if nodo_objetivo.elemento == elemento:
                return posicion_candidata
            nodo_objetivo = nodo_objetivo.siguiente

        return -1

    def insertar(self, posicion, elemento):
        if posicion > self.numero_elementos - 1 or posicion < 0:
            return None
        elif posicion == 0:
            self.insertar_frente(elemento)
        elif posicion == self.numero_elementos:
            self.insertar_final(elemento)
        else:
            nodo_predecesor = self.cabeza_lista
            for _ in range(posicion - 1):
                nodo_predecesor = nodo_predecesor.siguiente

            nuevo_nodo = NodoSimple(
                elemento=elemento, siguiente=nodo_predecesor.siguiente
            )
            nodo_predecesor.siguiente = nuevo_nodo

            self.numero_elementos = self.numero_elementos + 1

    def remover(self, posicion):
        return


if __name__ == "__main__":

    mi_secuencia = SecuenciaListasEnlazadas()
    print(f"{mi_secuencia.numero_elementos=}")  # Deberia ser 0
    print(f"{mi_secuencia.esta_vacia()=}")  # Deberia ser True

    mi_secuencia.insertar_final(0)
    mi_secuencia.insertar_final(1)
    mi_secuencia.insertar_final(2)
    mi_secuencia.insertar_final(3)

    print(f"{mi_secuencia.obtener_elemento(posicion=-1)=}")  # Deberia ver: None
    print(f"{mi_secuencia.obtener_elemento(posicion=4)=}")  # Deberia ver: None
    print(f"{mi_secuencia.obtener_elemento(posicion=2)=}")  # Deberia ver: 2
    print(f"{mi_secuencia.obtener_elemento(posicion=0)=}")  # Deberia ver: 0

    # print(f"{mi_secuencia.representar()=}")  # Deberia ver: 0, 1, 2, 3
    mi_secuencia.insertar_final(2)
    print(f"{mi_secuencia.representar()=}")  # Deberia ver: 0, 1, 2, 3, 2
    print(f"{mi_secuencia.obtener_posicion(3)=}")  # Deberia ver: 3
    print(f"{mi_secuencia.obtener_posicion(2)=}")  # Deberia ver: 2
    print(f"{mi_secuencia.obtener_posicion(4)=}")  # Deberia ver: -1

    print(f"{mi_secuencia.representar()=}")
    mi_secuencia.insertar(posicion=2, elemento=20)
    print(f"{mi_secuencia.representar()=}")  # Deberia ver: 0, 1, 20, 2, 3, 2

    mi_secuencia.insertar(posicion=4, elemento=40)
    print(f"{mi_secuencia.representar()=}")  # Deberia ver: 0, 1, 20, 2, 40, 3, 2

    print(
        f"{mi_secuencia.remover(posicion=2)=}"
    )  # Deberia retornar 20. La lista queda: 0, 1, 2, 40, 3, 2
    print(
        f"{mi_secuencia.remover(posicion=3)=}"
    )  # Deberia retornar 40. La lista queda: 0, 1, 2, 3, 2
    print(f"{mi_secuencia.representar()=}")  # Deberia ver: 0, 1, 2, 3, 2

    print("F I N")
