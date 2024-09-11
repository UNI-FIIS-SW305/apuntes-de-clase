import math


class NumeroComplejo:

    def __init__(self, parte_real, parte_imaginaria):
        self.parte_real = parte_real
        self.parte_imaginaria = parte_imaginaria

    def negar(self):
        return NumeroComplejo(
            parte_real=-self.parte_real, parte_imaginaria=-self.parte_imaginaria
        )

    def sumar(self, sumando):
        return NumeroComplejo(
            parte_real=self.parte_real + sumando.parte_real,
            parte_imaginaria=self.parte_imaginaria + sumando.parte_imaginaria,
        )

    def restar(self, operando):
        return NumeroComplejo(
            parte_real=self.parte_real - operando.parte_real,
            parte_imaginaria=self.parte_imaginaria - operando.parte_imaginaria,
        )

    def multiplicar(self, multiplicando):
        parte_real = (
            self.parte_real * multiplicando.parte_real
            - self.parte_imaginaria * multiplicando.parte_imaginaria
        )

        parte_imaginaria = (
            self.parte_real * multiplicando.parte_imaginaria
            + multiplicando.parte_real * self.parte_imaginaria
        )

        return NumeroComplejo(
            parte_real=parte_real,
            parte_imaginaria=parte_imaginaria
        )

    def modulo(self):
        return math.sqrt(self.parte_real**2 + self.parte_imaginaria**2)


if __name__ == "__main__":
    print("Hola!")

    # parte_real = 1
    # parte_imaginario = 2
    # numero_complejo = NumeroComplejo(parte_real, parte_imaginario)

    # print(numero_complejo.parte_real)
    # print(numero_complejo.parte_imaginaria)

    # numero_complejo_2 = numero_complejo.negar()
    # print(numero_complejo_2.parte_real)
    # print(numero_complejo_2.parte_imaginaria)

    # numero_complejo_3 = numero_complejo.sumar(numero_complejo_2)
    # print(numero_complejo_3.parte_real)
    # print(numero_complejo_3.parte_imaginaria)

    # numero_complejo_4 = numero_complejo.restar(numero_complejo_2)
    # print(numero_complejo_4.parte_real)
    # print(numero_complejo_4.parte_imaginaria)

    # numero_complejo_5 = numero_complejo.multiplicar(numero_complejo_2)
    # print(numero_complejo_5.parte_real)  # 3
    # print(numero_complejo_5.parte_imaginaria)  # - 4

    mi_complejo = NumeroComplejo(parte_real=3, parte_imaginaria=4)
    modulo = mi_complejo.modulo()
    print(modulo)  # 5
