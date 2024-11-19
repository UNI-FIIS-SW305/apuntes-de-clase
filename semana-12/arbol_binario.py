from secuencia import SecuenciaListasEnlazadas


class NodoBinario:
    def __init__(self, elemento, nodo_izquierdo, nodo_derecho):
        self.elemento = elemento
        self.nodo_izquierdo = nodo_izquierdo
        self.nodo_derecho = nodo_derecho


class ArbolBinario:
    def __init__(self) -> None:
        self.raiz = None

    def representar(self):
        # Va a ser recursivo
        if self.raiz is not None:
            self.representar_nodo(prefijo="", nodo=self.raiz)
        else:
            print("El arbol esta vacio")
        print()

    def representar_nodo(self, prefijo, nodo):
        if nodo is not None:
            indentado = "    "
            # TODO 1
            self.representar_nodo(prefijo=prefijo + indentado, nodo=nodo.nodo_derecho)
            print(prefijo + "|-- " + str(nodo.elemento))
            # TODO 2
            self.representar_nodo(prefijo=prefijo + indentado, nodo=nodo.nodo_izquierdo)

    def comparar(self, otro_arbol):
        return comparar_nodos(self.raiz, otro_arbol.raiz)

    def obtener_tamanio(self):
        return obtener_tamanio_nodo(self.raiz)

    def obtener_altura(self):
        return obtener_altura_nodo(self.raiz)

    def recorrer_en_preorden(self):
        print("Recorrido en preorden: ", end=" ")
        recorrer_nodo_en_preorden(self.raiz)
        print()

    def recorrer_en_postorden(self):
        print("Recorrido en postorden: ", end=" ")
        recorrer_nodo_en_postorden(self.raiz)
        print()

    def recorrer_en_inorden(self):
        print("Recorrido en inorden: ", end=" ")
        recorrer_nodo_en_inorden(self.raiz)
        print()

    def recorrer_por_profundidad(self):  # O(n**2)
        if self.raiz is None:  # O(1)
            print("El arbol estas vacio")  # O(1)
        else:
            print("Recorrido por profundidad: ", end=" ")  # O(1)
            lista_de_nodos = [self.raiz]  # O(1)

            while len(lista_de_nodos) > 0:  # O(n)
                nodo_actual = lista_de_nodos.pop(0)  # Orden superior? O(n)
                print(nodo_actual.elemento, end=" ")

                if nodo_actual.nodo_izquierdo is not None:
                    lista_de_nodos.append(nodo_actual.nodo_izquierdo)  # O(1)
                if nodo_actual.nodo_derecho is not None:
                    lista_de_nodos.append(nodo_actual.nodo_derecho)

            print()

    def recorrer_por_profundidad_eficiente(self):  # O(n)
        if self.raiz is None:  # O(1)
            print("El arbol estas vacio")  # O(1)
        else:
            print("Recorrido por profundidad: ", end=" ")  # O(1)
            secuencia_lista_enlazada = SecuenciaListasEnlazadas()
            secuencia_lista_enlazada.insertar_final(self.raiz)

            while not secuencia_lista_enlazada.esta_vacia():  # O(n)
                nodo_actual = (
                    secuencia_lista_enlazada.remover_frente()
                )  # Orden superior? O(1)
                print(nodo_actual.elemento, end=" ")

                if nodo_actual.nodo_izquierdo is not None:
                    secuencia_lista_enlazada.insertar_final(
                        nodo_actual.nodo_izquierdo
                    )  # O(1)
                if nodo_actual.nodo_derecho is not None:
                    secuencia_lista_enlazada.insertar_final(nodo_actual.nodo_derecho)

            print()

    def retornar_en_preorden(self):
        lista_de_elementos = []
        retornar_en_preorden_recursiva(self.raiz, lista_de_elementos)
        return lista_de_elementos

    def retornar_en_postorden(self):
        lista_de_elementos = []
        retornar_en_postorden_auxiliar(self.raiz, lista_de_elementos)
        return lista_de_elementos

    def retornar_en_inorden(self):
        lista_de_elementos = []
        retornar_en_inorden_auxiliar(self.raiz, lista_de_elementos)
        return lista_de_elementos


def retornar_en_inorden_auxiliar(un_nodo, lista_de_elementos):
    if un_nodo is not None:
        retornar_en_inorden_auxiliar(un_nodo.nodo_izquierdo, lista_de_elementos)
        lista_de_elementos.append(un_nodo.elemento)
        retornar_en_inorden_auxiliar(un_nodo.nodo_derecho, lista_de_elementos)


def retornar_en_postorden_auxiliar(un_nodo, lista_de_elementos):
    if un_nodo is not None:
        retornar_en_postorden_auxiliar(un_nodo.nodo_izquierdo, lista_de_elementos)
        retornar_en_postorden_auxiliar(un_nodo.nodo_derecho, lista_de_elementos)
        lista_de_elementos.append(un_nodo.elemento)


def retornar_en_preorden_recursiva(raiz_de_subarbol, lista_de_elementos):
    if raiz_de_subarbol is not None:
        lista_de_elementos.append(raiz_de_subarbol.elemento)
        retornar_en_preorden_recursiva(
            raiz_de_subarbol.nodo_izquierdo, lista_de_elementos
        )
        retornar_en_preorden_recursiva(
            raiz_de_subarbol.nodo_derecho, lista_de_elementos
        )


def recorrer_nodo_en_inorden(nodo):
    if nodo is not None:
        recorrer_nodo_en_inorden(nodo.nodo_izquierdo)
        print(nodo.elemento, end=" ")
        recorrer_nodo_en_inorden(nodo.nodo_derecho)


def recorrer_nodo_en_postorden(nodo):
    if nodo is not None:
        recorrer_nodo_en_postorden(nodo.nodo_izquierdo)
        recorrer_nodo_en_postorden(nodo.nodo_derecho)
        print(nodo.elemento, end=" ")


def recorrer_nodo_en_preorden(nodo):
    # Inspeccionaba el nodo -> Inspeccionaba el subarbol izquierdo -> Inspeccionaba el subarbol derecho.
    if nodo is not None:
        print(nodo.elemento, end=" ")
        recorrer_nodo_en_preorden(nodo.nodo_izquierdo)
        recorrer_nodo_en_preorden(nodo.nodo_derecho)


def obtener_altura_nodo(nodo):
    if nodo is None:
        return -1
    else:
        altura_subarbol_derecho = obtener_altura_nodo(nodo.nodo_derecho)
        altura_subarbol_izquierdo = obtener_altura_nodo(nodo.nodo_izquierdo)

        return 1 + max(altura_subarbol_derecho, altura_subarbol_izquierdo)
        # return max(altura_subarbol_derecho, altura_subarbol_izquierdo)


def obtener_tamanio_nodo(nodo):
    if nodo is None:
        return 0
    else:
        return (
            1
            + obtener_tamanio_nodo(nodo.nodo_izquierdo)
            + obtener_tamanio_nodo(nodo.nodo_derecho)
        )


def comparar_nodos(un_nodo, otro_nodo):
    if un_nodo is None and otro_nodo is None:
        return True

    if un_nodo is None or otro_nodo is None:
        return False

    return (
        un_nodo.elemento == otro_nodo.elemento
        and comparar_nodos(un_nodo.nodo_izquierdo, otro_nodo.nodo_izquierdo)
        and comparar_nodos(un_nodo.nodo_derecho, otro_nodo.nodo_derecho)
    )


def crear_arbol_de_prueba():
    nodo_dos = NodoBinario(elemento=2, nodo_izquierdo=None, nodo_derecho=None)

    subarbol_izquierdo = NodoBinario(
        elemento=3, nodo_izquierdo=nodo_dos, nodo_derecho=None
    )

    subarbol_derecho = NodoBinario(elemento=9, nodo_izquierdo=None, nodo_derecho=None)
    subarbol_derecho.nodo_izquierdo = NodoBinario(
        elemento=8, nodo_izquierdo=None, nodo_derecho=None
    )

    nodo_veinte = NodoBinario(elemento=20, nodo_izquierdo=None, nodo_derecho=None)
    nodo_veinte.nodo_derecho = NodoBinario(
        elemento=30, nodo_izquierdo=None, nodo_derecho=None
    )

    subarbol_derecho.nodo_derecho = nodo_veinte

    nodo_raiz = NodoBinario(
        elemento=5, nodo_izquierdo=subarbol_izquierdo, nodo_derecho=subarbol_derecho
    )

    arbol = ArbolBinario()
    arbol.raiz = nodo_raiz

    return arbol


if __name__ == "__main__":
    arbol = crear_arbol_de_prueba()
    otro_arbol = crear_arbol_de_prueba()
    arbol.representar()

    print(f"{arbol.comparar(otro_arbol)=}")  # Deberia ser True
    print(f"{arbol.obtener_tamanio()=}")  # Deberia 7
    print(f"{arbol.obtener_altura()=}")  # Deberia 3
    retorno = arbol.recorrer_en_preorden()
    print(f"{retorno=}")

    elementos_en_preorden = arbol.retornar_en_preorden()
    print(f"{elementos_en_preorden=}")  # Deberia ser [5 3 2 9 8 20 30 ]

    elementos_en_postorden = arbol.retornar_en_postorden()
    print(f"{elementos_en_postorden=}")  # Deberia ser [5 3 2 9 8 20 30 ]

    arbol.recorrer_en_postorden()
    arbol.recorrer_en_inorden()

    elementos_en_inorden = arbol.retornar_en_inorden()
    print(f"{elementos_en_inorden=}")

    # arbol_distinto = crear_arbol_de_prueba()
    # arbol_distinto.raiz.nodo_izquierdo.nodo_izquierdo.elemento = 1
    # arbol_distinto.representar()

    # print(f"{arbol.comparar(arbol_distinto)=}")  # Deberia ser False

    arbol.recorrer_por_profundidad()  # Deberia ser: 5, 3, 9, 2, 8, 20, 30.
    arbol.recorrer_por_profundidad_eficiente()  # Deberia ser: 5, 3, 9, 2, 8, 20, 30.
