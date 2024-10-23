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

    def remover_frente(self):
        if self.esta_vacia():
            return None

        resultado = self.cabeza_lista.elemento

        self.cabeza_lista = self.cabeza_lista.siguiente
        if self.cabeza_lista is None:
            self.final_lista = None
        else:
            self.cabeza_lista.anterior = None

        self.numero_elementos = self.numero_elementos - 1

        return resultado

    def remover_ultimo(self):
        if self.esta_vacia():
            return None

        resultado = self.final_lista.elemento
        self.final_lista = self.final_lista.anterior

        if self.final_lista is None:
            self.cabeza_lista = None
        else:
            self.final_lista.siguiente = None

        self.numero_elementos = self.numero_elementos - 1

        return resultado

    def obtener_elemento(self, posicion):
        if posicion < 0 or posicion >= self.numero_elementos:
            return None

        nodo_en_posicion = self.cabeza_lista
        indice = 0

        while indice < posicion:
            nodo_en_posicion = nodo_en_posicion.siguiente
            indice = indice + 1

        return nodo_en_posicion.elemento

    def obtener_posicion(self, elemento):
        nodo_en_posicion = self.cabeza_lista
        posicion_actual = 0

        # Bucle
        while nodo_en_posicion is not None:
            if nodo_en_posicion.elemento == elemento:
                return posicion_actual

            nodo_en_posicion = nodo_en_posicion.siguiente
            posicion_actual = posicion_actual + 1

        return -1

    def insertar(self, posicion, elemento):
        if posicion > self.numero_elementos or posicion < 0:
            return None
        elif posicion == 0:
            self.insertar_frente(elemento)
        elif posicion == self.numero_elementos:
            self.insertar_final(elemento)
        else:
            nodo_en_posicion = self.cabeza_lista

            for _ in range(posicion):
                nodo_en_posicion = nodo_en_posicion.siguiente

            nodo_predecesor = nodo_en_posicion.anterior
            nuevo_nodo = NodoDoble(
                elemento=elemento, anterior=nodo_predecesor, siguiente=nodo_en_posicion
            )

            nodo_en_posicion.anterior = nuevo_nodo
            nodo_predecesor.siguiente = nuevo_nodo

            self.numero_elementos = self.numero_elementos + 1

    def remover(self, posicion):
        if posicion < 0 or posicion >= self.numero_elementos:
            return None
        elif posicion == 0:
            return self.remover_frente()
        elif posicion == self.numero_elementos - 1:
            return self.remover_ultimo()
        else:
            nodo_actual = self.cabeza_lista

            posicion_actual = 0

            while nodo_actual is not None:
                if posicion_actual == posicion:
                    break

                nodo_actual = nodo_actual.siguiente
                posicion_actual = posicion_actual + 1

            nodo_en_posicion = nodo_actual
            nodo_anterior = nodo_en_posicion.anterior
            nodo_siguiente = nodo_en_posicion.siguiente

            nodo_anterior.siguiente = nodo_siguiente
            nodo_siguiente.anterior = nodo_anterior

            self.numero_elementos = self.numero_elementos - 1
            return nodo_en_posicion.elemento


def prueba_secuencia_doble():
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
    secuencia.insertar_final(30)
    print(f"{secuencia.representar()=}")  # Salida: (10, 20, 30)

    # print(f"1 {secuencia.remover_frente()=}")  # Salida: 10
    # print(f"2 {secuencia.remover_frente()=}")  # Salida: 20
    # print(f"3 {secuencia.remover_frente()=}")  # Salida: 30

    print(f"1 {secuencia.remover_ultimo()=}")  # Salida: 30
    print(f"2 {secuencia.remover_ultimo()=}")  # Salida: 20
    print(f"3 {secuencia.remover_ultimo()=}")  # Salida: 10

    print(f" {secuencia.esta_vacia()=}")  # Deberia ser True
    print(f" {secuencia.cabeza_lista=}")  # Deberia ser None
    print(f" {secuencia.final_lista=}")  # Deberia ser None


def prueba_lista_doble():
    secuencia = SecuenciaListaDoble()

    secuencia.insertar_final(0)
    secuencia.insertar_final(1)
    secuencia.insertar_final(2)
    secuencia.insertar_final(3)
    secuencia.insertar_final(4)

    print(f"{secuencia.representar()=}")

    resultado = secuencia.remover(posicion=4)
    print(f"{resultado=}")
    print(f"{secuencia.representar()=}")

    # secuencia.insertar_final(4)

    # print(f"{secuencia.obtener_elemento(posicion=2)=}")  # Deberia ser 2
    # print(f"{secuencia.obtener_elemento(posicion=5)=}")  # Deberia ser None

    # print(f"{secuencia.obtener_posicion(4)=}")  # Deberia ser 4
    # print(f"{secuencia.obtener_posicion(6)=}")  # Deberia ser -1

    # # print(f"{secuencia.representar()=}")

    # secuencia.insertar(posicion=5, elemento=5)
    # print(f"{secuencia.representar()=}")  # Deberia ser (0,1,2,3,4,5,4)

    # print(f"{secuencia.insertar(posicion=10, elemento=10)=}")
    # print(f"{secuencia.representar()=}")  # Deberia ser (0,1,2,3,4,5,4)


def es_palindromo(palabra):
    if palabra is None:
        return False

    if len(palabra) == 0:
        return True

    lista_doble = SecuenciaListaDoble()

    # TODO: Revisar el metodo insertar
    for caracter in palabra:
        lista_doble.insertar_final(caracter)

    nodo_izquierda = lista_doble.cabeza_lista
    nodo_derecha = lista_doble.final_lista

    indice = 0

    while indice <= len(palabra) / 2:
        if nodo_izquierda.elemento != nodo_derecha.elemento:
            return False

        nodo_izquierda = nodo_izquierda.siguiente
        nodo_derecha = nodo_derecha.anterior

        indice = indice + 1

    return True


if __name__ == "__main__":
    # print(f"{es_palindromo('rodar')=}")  # False
    # print(f"{es_palindromo('radar')=}")  # True
    # print(f"{es_palindromo('anna')=}")  # True
    # print(f"{es_palindromo(None)=}")  # False
    # print(f"{es_palindromo('')=}")  # True

    secuencia = SecuenciaListaDoble()
    secuencia.insertar(0, 0)
    secuencia.insertar(1, 1)

    print(f"{secuencia.representar()=}")
