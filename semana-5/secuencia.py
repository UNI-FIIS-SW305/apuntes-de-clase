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
        self.cabeza_lista = nuevo_nodo
        self.numero_elementos = self.numero_elementos + 1


if __name__ == "__main__":

    mi_secuencia = SecuenciaListasEnlazadas()
    print(f"{mi_secuencia.numero_elementos=}")  # Deberia ser 0
    print(f"{mi_secuencia.esta_vacia()=}")  # Deberia ser True

    mi_secuencia.insertar_frente(2)  # Secuencia deberia ser: 2 ->
    mi_secuencia.insertar_frente(1)  # Secuencia deberia ser: 1-> 2
    mi_secuencia.insertar_frente(0)  # Secuencia deberia ser: 0 -> 1-> 2

    print("F I N")
