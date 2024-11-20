from arbol_binario import ArbolBinario, NodoBinario


class ArbolBinarioBusqueda(ArbolBinario):
    def buscar(self, objetivo):
        return NodoBinario(elemento=None, nodo_derecho=None, nodo_izquierdo=None)


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

    arbol = ArbolBinarioBusqueda()
    arbol.raiz = nodo_raiz

    return arbol


if __name__ == "__main__":
    arbol_busqueda = crear_arbol_de_prueba()
    print(f"{type(arbol_busqueda)=}")
    arbol_busqueda.representar()

    print(
        f"{arbol_busqueda.buscar(20).elemento=}"
    )  # Deberia ser: NodoBinario(elemento=20)
    print(f"{arbol_busqueda.buscar(21).elemento=}")  # Deberia ser: None
