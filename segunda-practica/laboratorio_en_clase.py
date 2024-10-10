class ErrorNotacionPolaca(Exception):
    pass


class ErrorEnPila(Exception):
    pass


class ErrorTransaccion(Exception):
    pass


class NotacionPolacaInversa:
    def __init__(self, expresion):
        # [INICIO]: Implemente el constructor entre [INICIO] y [FIN].
        # No edite antes de esta línea.

        self.expresion = expresion
        self.pila = []

        # [FIN]

    def evaluar(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.

        diccionario_operadores = {
            "+": operacion_sumar,
            "-": lambda operando_1, operando_2: operando_1 - operando_2,
            "x": lambda operando_1, operando_2: operando_1 * operando_2,
            "/": lambda operando_1, operando_2: operando_1 / operando_2,
        }

        tokens = self.expresion.split()

        for token in tokens:
            if token.isdigit():
                self.pila.append(float(token))
            elif token in diccionario_operadores.keys():
                funcion = diccionario_operadores[token]

                if len(self.pila) < 2:
                    raise ErrorNotacionPolaca()

                operando_derecho = self.pila.pop()
                operando_izquierdo = self.pila.pop()

                resultado = funcion(operando_izquierdo, operando_derecho)
                self.pila.append(resultado)
            else:
                raise ErrorNotacionPolaca("Token invalidad")

        if len(self.pila) > 1:
            raise ErrorNotacionPolaca("Operandos en exceso.")

        return self.pila.pop()

        # [FIN]


def operacion_sumar(operando_1, operando_2):
    return operando_1 + operando_2


class PilaCapacidadFija:
    def __init__(self, capacidad, sobrescribir):
        self.elementos = [None for _ in range(capacidad)]
        self.sobrescribir = sobrescribir
        self.capacidad = capacidad
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        self.numero_elementos = 0
        self.indice_cima = None

        # [FIN]

    def tamanio(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.

        numero_elementos = 0
        for elemento in self.elementos:
            if elemento is not None:
                numero_elementos = numero_elementos + 1

        return numero_elementos
        # [FIN]

    def apilar(self, elemento):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        if not self.sobrescribir:
            if self.tamanio() + 1 > self.capacidad:
                raise ErrorEnPila()

            self.indice_cima = self.tamanio()
            self.elementos[self.indice_cima] = elemento
            # TODO: Revisar el enfoque del señor Fernandez.
        else:
            if self.indice_cima is None:
                indice_apilar = 0
            else:
                indice_apilar = self.indice_cima + 1  # TBD

            # [ None, None, None]
            # [ 1, None, None]
            # [ 1, 2, None]
            # [ 1, 2, 3] --> Apilar 4 (indice 3)
            # [ 4, 2, 3] # indice_cima 0

            if self.tamanio() < self.capacidad:
                pass
            elif self.tamanio() == self.capacidad:
                if not (indice_apilar < self.capacidad):
                    indice_apilar = indice_apilar - self.capacidad

            self.elementos[indice_apilar] = elemento
            self.indice_cima = indice_apilar
        # [FIN]

    def esta_vacia(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        return self.tamanio() == 0
        # [FIN]

    def cima(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.

        if self.esta_vacia():
            raise ErrorEnPila()

        return self.elementos[self.tamanio() - 1]
        # [FIN]

    def desapilar(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        if self.esta_vacia():
            raise ErrorEnPila()

        # if self.tamanio() == self.capacidad:
        #     resultado = self.elementos[]
        # [FIN]


class CalculadoraGanancias:
    def __init__(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]

    def registrar_compra(self, descripcion_transaccion):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]

    def registrar_venta(self, descripcion_transaccion):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.

        pass
        # [FIN]

    def catalogo_acciones(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]

    def acciones_disponibles(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]


if __name__ == "__main__":
    # [INICIO]: Pruebe sus soluciones entre [INICIO] y [FIN].
    # No edite antes de esta línea.
    notacion_polaca = NotacionPolacaInversa(expresion=" 5 2 + 8 3 - x 4 / ")
    notacion_polaca.evaluar()
    # [FIN]
