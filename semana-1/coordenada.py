import math

# import typing


class Coordenada:

    def __init__(self, valor_x, valor_y):
        self.x = valor_x
        self.y = valor_y

    def calcular_distancia(self, otra_coordenada: "Coordenada"):

        diferencia_x = self.x - otra_coordenada.x
        diferencia_y = self.y - otra_coordenada.y

        return math.sqrt(diferencia_x**2 + diferencia_y**2)

    def __str__(self):
        return f"x={self.x} y={self.y}"

    def __repr__(self) -> str:
        return str(self)


if __name__ == "__main__":
    mi_coordenada = Coordenada(0, 0)
    print(f"{mi_coordenada.x=}")  # f-string
    print(f"{mi_coordenada.y=}")

    otra_coordenada = Coordenada(1, 1)
    print(f"{otra_coordenada.x=}")
    print(f"{otra_coordenada.y=}")

    print(f"{mi_coordenada.calcular_distancia(otra_coordenada)=}")

    # print(f"{str(otra_coordenada)=}")
    print(f"{otra_coordenada}")

    mi_objeto = 1
    mi_objeto = otra_coordenada
    print(type(mi_objeto))

    print(isinstance(mi_objeto, Coordenada))
