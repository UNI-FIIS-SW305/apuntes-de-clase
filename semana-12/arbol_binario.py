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

    # arbol_distinto = crear_arbol_de_prueba()
    # arbol_distinto.raiz.nodo_izquierdo.nodo_izquierdo.elemento = 1
    # arbol_distinto.representar()

    # print(f"{arbol.comparar(arbol_distinto)=}")  # Deberia ser False
