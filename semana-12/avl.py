from abb import ArbolBinarioBusqueda
from arbol_binario import NodoBinario


class ArbolAvl(ArbolBinarioBusqueda):

    def insertar(self, elemento):
        print(f"AVL: Insertar {elemento}")

        self.raiz = insertar_avl(nodo=self.raiz, elemento=elemento)


def insertar_avl(nodo, elemento):
    if nodo is None:
        nodo = NodoBinario(elemento=elemento, nodo_izquierdo=None, nodo_derecho=None)
    elif nodo.elemento == elemento:
        raise ValueError("No esta permitido elementos duplicados")
    elif elemento < nodo.elemento:
        nodo.nodo_izquierdo = insertar_avl(nodo.nodo_izquierdo, elemento)
    else:
        nodo.nodo_derecho = insertar_avl(nodo.nodo_derecho, elemento)

    nodo = balancear_nodo(nodo)
    return nodo


def balancear_nodo(nodo):
    pass


if __name__ == "__main__":
    arbol_avl = ArbolAvl()
    arbol_avl.insertar(30)

    arbol_avl.representar()
