from arbol_binario import ArbolBinario, NodoBinario


class ArbolBinarioBusqueda(ArbolBinario):
    def buscar(self, objetivo):
        return buscar_en_nodo(self.raiz, objetivo)

    def buscar_iterativo(self, objetivo):
        nodo_actual = self.raiz

        while nodo_actual is not None:
            if nodo_actual.elemento == objetivo:
                return nodo_actual
            elif objetivo < nodo_actual.elemento:
                nodo_actual = nodo_actual.nodo_izquierdo
            elif objetivo > nodo_actual.elemento:
                nodo_actual = nodo_actual.nodo_derecho

        return None

    def insertar(self, elemento):
        self.raiz = insertar_en_nodo(self.raiz, elemento)

    def eliminar(self, elemento_a_eliminar):
        self.raiz = eliminar_nodo(self.raiz, elemento_a_eliminar)


def obtener_nodo_sucesor(nodo):
    nodo_minimo = nodo
    while nodo_minimo.nodo_izquierdo is not None:
        nodo_minimo = nodo_minimo.nodo_izquierdo

    return nodo_minimo


def eliminar_nodo(nodo, elemento_a_eliminar):
    if nodo is None:
        return None  # TODO: Revisar luego

    if nodo.elemento == elemento_a_eliminar:
        if nodo.nodo_izquierdo is None and nodo.nodo_derecho is None:
            # Es una hoja!
            nodo = None
        elif nodo.nodo_izquierdo is None:
            nodo = nodo.nodo_derecho
        elif nodo.nodo_derecho is None:
            nodo = nodo.nodo_izquierdo
        else:
            nodo_sucesor = obtener_nodo_sucesor(nodo.nodo_derecho)

    elif elemento_a_eliminar < nodo.elemento:
        return eliminar_nodo(
            nodo.nodo_izquierdo, elemento_a_eliminar
        )  # TODO: Revisar luego
    elif elemento_a_eliminar > nodo.elemento:
        return eliminar_nodo(
            nodo.nodo_derecho, elemento_a_eliminar
        )  # TODO: Revisar luego

    return nodo


def insertar_en_nodo(nodo, elemento_a_insertar):
    # Retorna un nodo.

    if nodo is None:
        return NodoBinario(
            elemento=elemento_a_insertar, nodo_derecho=None, nodo_izquierdo=None
        )

    if nodo.elemento == elemento_a_insertar:
        print(f"El elemento {elemento_a_insertar} ya existe")
        return nodo

    if elemento_a_insertar < nodo.elemento:
        nodo.nodo_izquierdo = insertar_en_nodo(nodo.nodo_izquierdo, elemento_a_insertar)
    elif elemento_a_insertar > nodo.elemento:
        nodo.nodo_derecho = insertar_en_nodo(nodo.nodo_derecho, elemento_a_insertar)

    return nodo


def buscar_en_nodo(nodo, objetivo):
    if nodo is None:
        return None

    if nodo.elemento == objetivo:
        return nodo
    elif objetivo < nodo.elemento:
        return buscar_en_nodo(nodo.nodo_izquierdo, objetivo)
    elif objetivo > nodo.elemento:
        return buscar_en_nodo(nodo.nodo_derecho, objetivo)


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
    print(f"{arbol_busqueda.buscar(21)=}")  # Deberia ser: None

    print(
        f"{arbol_busqueda.buscar_iterativo(20).elemento=}"
    )  # Deberia ser: NodoBinario(elemento=20)
    print(f"{arbol_busqueda.buscar_iterativo(21)=}")  # Deberia ser: None

    # nuevo_arbol = ArbolBinarioBusqueda()
    # nuevo_arbol.insertar(5)
    # nuevo_arbol.insertar(3)
    # nuevo_arbol.insertar(9)

    # nuevo_arbol.insertar(30)

    # # nuevo_arbol.insertar(20)
    # # nuevo_arbol.insertar(8)
    # # nuevo_arbol.insertar(2)

    # nuevo_arbol.representar()  # Deberia ver un ABB 5, 3, 9

    arbol_busqueda.eliminar(2)
    print("Dos ha sido eliminado")
    arbol_busqueda.representar()

    arbol_busqueda.eliminar(20)
    print("20 ha sido eliminado")
    arbol_busqueda.representar()

    arbol_busqueda.eliminar(5)
    print("5 ha sido eliminado")
    arbol_busqueda.representar()
