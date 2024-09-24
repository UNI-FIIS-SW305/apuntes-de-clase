class ColaBasadaEnListas:

    def __init__(self):
        self.elementos = []

    def representar(self):
        # print(f"{self.elementos=}")
        primer_elemento = self.elementos[0]
        if hasattr(primer_elemento, "representar"):
            return str([elemento.representar() for elemento in self.elementos])
        else:
            return str([elemento for elemento in self.elementos])

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if self.tamanio() == 0:
            return None
        return self.elementos.pop(0)

    def primero(self):
        if self.tamanio() == 0:
            return None
        return self.elementos[0]

    def tamanio(self):
        return len(self.elementos)

    def esta_vacia(self):
        return self.tamanio() == 0


def pruebas_colas():
    una_cola = ColaBasadaEnListas()
    print(f"{una_cola.representar()=}")  # Deberia: []

    una_cola.encolar(1)
    una_cola.encolar(2)
    una_cola.encolar(3)

    print(f"{una_cola.representar()=}")  # Deberia: [1, 2, 3]

    resultado = una_cola.desencolar()
    print(f"{resultado=}")
    print(f"{una_cola.representar()=}")  # Deberia: [2, 3]
    resultado = una_cola.primero()
    print(f"{resultado=}")  # Deberia ser 2
    print(f"{una_cola.representar()=}")  # Deberia: [2, 3]
    print(f"{una_cola.tamanio()=}")  # Deberia: 2
    print(f"{una_cola.esta_vacia()=}")  # Deberia ser: False

    cola_vacia = ColaBasadaEnListas()
    resultado = cola_vacia.desencolar()
    print(f"{resultado=}")  # Deberia ser: None
    print(f"{cola_vacia.esta_vacia()=}")  # Deberia ser: True


def obtener_sobreviviente(numero_soldados, contador):
    cola_soldados = ColaBasadaEnListas()
    for soldado in range(1, numero_soldados + 1):
        # print(f"{soldado=}")
        cola_soldados.encolar(soldado)

    print(f"{cola_soldados.representar()=}")

    while cola_soldados.tamanio() > 1:
        contador_actual = 1
        while contador_actual < contador:
            soldado_sobreviviente = cola_soldados.desencolar()
            cola_soldados.encolar(soldado_sobreviviente)
            contador_actual = contador_actual + 1

        soldado_muerto = cola_soldados.desencolar()
        print(f"QEPD={soldado_muerto}")

    return cola_soldados.primero()


class Trabajo:

    def __init__(self, nombre_documento, usuario) -> None:
        self.nombre_documento = nombre_documento
        self.usuario = usuario

    def __repr__(self) -> str:
        return self.representar()

    def __str__(self):
        return self.representar()

    def representar(self):
        return f"Documento {self.nombre_documento} enviado por {self.usuario}"


class ColaDeImpresion:

    def __init__(self) -> None:
        self.cola = ColaBasadaEnListas()

    def agregar_trabajo(self, trabajo: Trabajo):
        self.cola.encolar(trabajo)

    def numero_pendientes(self):
        return self.cola.tamanio()

    def mostrar_pendientes(self):
        if self.cola.esta_vacia():
            print("Nada que imprimir")
            return

        for orden in range(len(self.cola.elementos)):
            trabajo = self.cola.elementos[orden]
            print(
                f"{orden + 1}: Archivo: {trabajo.nombre_documento} Autor: {trabajo.usuario}"
            )

    def imprimir(self):
        archivo_a_imprimir = self.cola.desencolar().nombre_documento
        print(f"Imprimiendo: {archivo_a_imprimir} ...")

    def imprimir_todos(self):
        # numero_elementos = self.cola.tamanio()

        # for _ in range(numero_elementos):
        #     archivo_a_imprimir = self.cola.desencolar().nombre_documento
        #     print(f"Imprimiendo: {archivo_a_imprimir} ...")

        while self.cola.tamanio() > 0:
            self.imprimir()


def prueba_josefo():
    sobreviviente = obtener_sobreviviente(numero_soldados=41, contador=3)
    print(f"{sobreviviente=}")  # Deberia ser 31


def prueba_cola():
    un_trabajo_impresion = Trabajo(nombre_documento="susti.pdf", usuario="cgavidia")
    cola_de_impresion = ColaDeImpresion()
    cola_de_impresion.agregar_trabajo(un_trabajo_impresion)
    cola_de_impresion.agregar_trabajo(
        Trabajo(nombre_documento="reclamo.doc", usuario="luisangel")
    )

    print(f"{cola_de_impresion.numero_pendientes()=}")
    cola_de_impresion.mostrar_pendientes()

    cola_de_impresion.imprimir_todos()

    # cola_de_impresion.imprimir()  # Deberia ser susti
    # cola_de_impresion.imprimir()  # Deberia ser reclamo

    cola_de_impresion.mostrar_pendientes()  # Deberia mostrar nada

    # print(f"{cola_de_impresion.cola.representar()=}")
    print("F I N")


class ColaDoblementeTerminada:

    def __init__(self) -> None:
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def insertar_al_frente(self, elemento):
        self.elementos.insert(0, elemento)

    def insertar_al_final(self, elemento):
        self.elementos.append(elemento)

    def tamanio(self):
        return len(self.elementos)

    def remover_del_frente(self):
        if self.tamanio() == 0:
            return None
        return self.elementos.pop(0)

    def remover_del_final(self):
        if self.tamanio() == 0:
            return None
        return self.elementos.pop(-1)

    def primero(self):
        if self.tamanio() == 0:
            return None
        return self.elementos[0]

    def ultimo(self):
        if self.tamanio() == 0:
            return None
        return self.elementos[-1]


if __name__ == "__main__":
    cola_doble = ColaDoblementeTerminada()
    print(f"{cola_doble.esta_vacia()=}")  # Deberia ser True

    cola_doble.insertar_al_frente(2)
    cola_doble.insertar_al_frente(1)

    cola_doble.insertar_al_final(3)
    cola_doble.insertar_al_final(4)

    print(f"{cola_doble.elementos=}")  # Deberia ser [1, 2, 3, 4]
    print(f"{cola_doble.primero()=}")  # Deberia ser 1
    print(f"{cola_doble.ultimo()=}")  # Deberia ser 4
    print(f"{cola_doble.elementos=}")  # Deberia ser [1, 2, 3, 4]

    # print(f"{cola_doble.remover_del_frente()=}")  # Deberia ser 1
    # print(f"{cola_doble.remover_del_frente()=}")  # Deberia ser 2

    # print(f"{cola_doble.elementos=}")  # Deberia ser [ 3, 4]

    # print(f"{cola_doble.remover_del_final()=}")  # Deberia ser 4
    # print(f"{cola_doble.elementos=}")  # Deberia ser [ 3 ]
