from abb import ArbolBinarioBusqueda
from arbol_binario import NodoBinario, obtener_altura_nodo


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


def obtener_factor_equilibrio(nodo):
    if nodo is None:
        return 0
    else:
        return obtener_altura_nodo(nodo.nodo_izquierdo) - obtener_altura_nodo(
            nodo.nodo_derecho
        )


def rotar_a_la_derecha(nodo):
    nueva_raiz = nodo.nodo_izquierdo
    subarbol_a_mover = nueva_raiz.nodo_derecho

    nueva_raiz.nodo_derecho = nodo
    nodo.nodo_izquierdo = subarbol_a_mover

    return nueva_raiz


def rotar_a_la_izquierda(nodo):
    nueva_raiz = nodo.nodo_derecho
    subarbol_a_mover = nueva_raiz.nodo_izquierdo

    nueva_raiz.nodo_izquierdo = nodo
    nodo.nodo_derecho = subarbol_a_mover

    return nueva_raiz


def balancear_nodo(nodo):
    if abs(obtener_factor_equilibrio(nodo)) <= 1:
        print(f"El nodo {nodo.elemento} se encuentra balanceado")
        return nodo
    else:
        print(f"El nodo {nodo.elemento} NO se encuentra balanceado")

        altura_izquierda = obtener_altura_nodo(nodo.nodo_izquierdo)
        altura_derecha = obtener_altura_nodo(nodo.nodo_derecho)

        if altura_izquierda > altura_derecha:
            nodo_a_balancear = nodo.nodo_izquierdo

            altura_izquierda = obtener_altura_nodo(nodo_a_balancear.nodo_izquierdo)
            altura_derecha = obtener_altura_nodo(nodo_a_balancear.nodo_derecho)

            if altura_derecha > altura_izquierda:
                # Rotacion Doble. Primero rotacion izquierda.
                print(f"Rotacion Doble {nodo.elemento=}-> Rotacion izquierda")
                nodo.nodo_izquierdo = rotar_a_la_izquierda(nodo_a_balancear)

            # Rotacion Simple Derecha
            print(f"Rotacion derecha {nodo.elemento=}")
            nodo = rotar_a_la_derecha(nodo)
        else:
            nodo_a_balancear = nodo.nodo_derecho

            altura_izquierda = obtener_altura_nodo(nodo_a_balancear.nodo_izquierdo)
            altura_derecha = obtener_altura_nodo(nodo_a_balancear.nodo_derecho)

            if altura_izquierda > altura_derecha:
                print(f"Rotacion Doble {nodo.elemento=}-> Rotacion derecha")
                nodo.nodo_derecho = rotar_a_la_derecha(nodo_a_balancear)

            print(f"Rotacion izquierda {nodo.elemento=}")
            nodo = rotar_a_la_izquierda(nodo)

    return nodo


if __name__ == "__main__":
    arbol_avl = ArbolAvl()
    arbol_avl.insertar(30)
    arbol_avl.insertar(50)

    arbol_avl.insertar(60)
    arbol_avl.insertar(25)

    arbol_avl.insertar(15)

    print("Antes de rotar")
    arbol_avl.representar()
    arbol_avl.insertar(35)

    print("Despues de rotar")
    arbol_avl.representar()
