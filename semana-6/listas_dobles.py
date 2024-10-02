class NodoDoble:

    def __init__(self, elemento, siguiente, anterior) -> None:
        self.elemento = elemento
        self.siguiente = siguiente
        self.anterior = anterior


class SecuenciaListaDoble:

    def __init__(self) -> None:
        self.cabeza_lista = None
        self.final_lista = None
        self.numero_elementos = 0

    def esta_vacia(self):
        return self.numero_elementos == 0

    def insertar_frente(self, elemento):
        nuevo_nodo = NodoDoble(
            elemento=elemento, anterior=None, siguiente=self.cabeza_lista
        )

        if self.esta_vacia():
            self.final_lista = nuevo_nodo

        self.cabeza_lista = nuevo_nodo
        self.numero_elementos = self.numero_elementos + 1

    def representar(self):
        if self.esta_vacia():
            return "()"

        elementos = []
        nodo_actual = self.cabeza_lista
        while nodo_actual is not None:
            elementos.append(nodo_actual.elemento)
            nodo_actual = nodo_actual.siguiente

        return f"({','.join([str(elemento) for elemento in elementos])})"

    def insertar_final(self, elemento):
        nuevo_nodo = NodoDoble(
            elemento=elemento, anterior=self.final_lista, siguiente=None
        )

        if self.esta_vacia():
            self.cabeza_lista = nuevo_nodo
        else:
            self.final_lista.siguiente = nuevo_nodo

        self.final_lista = nuevo_nodo
        self.numero_elementos = self.numero_elementos + 1


if __name__ == "__main__":

    secuencia = SecuenciaListaDoble()

    # secuencia.insertar_frente(0)
    # secuencia.insertar_frente(1)
    # secuencia.insertar_frente(2)
    # secuencia.insertar_frente(3)

    # print(f"{secuencia.cabeza_lista.elemento=}")  # Deberia ser: 3
    # print(f"{secuencia.final_lista.elemento=}")  # Deberia ser: 0

    print(f"{secuencia.representar()=}")  # Salida: (3,2,1,0)
    secuencia.insertar_final(10)
    secuencia.insertar_final(20)
    print(f"{secuencia.representar()=}")  # Salida: (3,2,1,0, 10, 20)
