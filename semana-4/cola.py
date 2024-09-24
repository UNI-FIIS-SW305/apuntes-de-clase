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


def prueba_josefo():
    sobreviviente = obtener_sobreviviente(numero_soldados=41, contador=3)
    print(f"{sobreviviente=}")  # Deberia ser 31


if __name__ == "__main__":
    # un_trabajo_impresion = Trabajo(nombre_documento="susti.pdf", usuario="cgavidia")
    # cola_de_impresion = ColaDeImpresion()
    # cola_de_impresion.agregar_trabajo(un_trabajo_impresion)

    # print(f"{cola_de_impresion.cola.elementos=}")

    # print(f"{cola_de_impresion.cola.representar()=}")
    # print("F I N")

    prueba_josefo()
