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


if __name__ == "__main__":

    mi_secuencia = SecuenciaListasEnlazadas()
    print(f"{mi_secuencia.numero_elementos=}")  # Deberia ser 0
    print(f"{mi_secuencia.esta_vacia()=}")  # Deberia ser True

    mi_secuencia.insertar_frente(2)  # Secuencia deberia ser: 2 ->
    mi_secuencia.insertar_frente(1)  # Secuencia deberia ser: 1-> 2
    mi_secuencia.insertar_frente(0)  # Secuencia deberia ser: 0 -> 1-> 2

    print(f"{mi_secuencia.representar()=}")
    print(f"{mi_secuencia.remover_final()=}")  # Deberia ver: 2
    print(f"{mi_secuencia.remover_final()=}")  # Deberia ver: 1
    print(f"{mi_secuencia.remover_final()=}")  # Deberia ver: 0
    print(f"{mi_secuencia.remover_final()=}")  # Deberia ver: None
    print(f"{mi_secuencia.representar()=}")  # Deberia ver: ()

    # print(f"{mi_secuencia.eliminar_frente()=}")  # Deberia ver: None
    # mi_secuencia.insertar_final(0)
    # print(f"{mi_secuencia.eliminar_frente()=}")  # Deberia ver: 0
    # print(f"{mi_secuencia.representar()=}")
    # print(f"{mi_secuencia.cabeza_lista=}")  # Deberia ver: None
    # print(f"{mi_secuencia.final_lista=}")  # Deberia ver: None

    # mi_secuencia.insertar_final(1)
    # mi_secuencia.insertar_final(2)

    # print(f"{mi_secuencia.representar()=}")  # Deberia ver: (0, 1, 2)
    # print(f"{mi_secuencia.eliminar_frente()=}")  # Deberia ver: 0
    # print(f"{mi_secuencia.representar()=}")  # Deberia ver: ( 1, 2)

    print("F I N")
