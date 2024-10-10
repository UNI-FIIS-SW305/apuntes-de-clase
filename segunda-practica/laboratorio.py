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

        self.pila = []
        self.expresion = expresion

        # [FIN]

    def evaluar(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.

        caracter_a_funcion = {
            "+": lambda operando, otro_operando: operando + otro_operando,
            "-": lambda operando, otro_operando: operando - otro_operando,
            "x": lambda operando, otro_operando: operando * otro_operando,
            "/": lambda operando, otro_operando: operando / otro_operando,
        }

        for caracter in self.expresion.split():
            if caracter.isdigit():
                self.pila.append(float(caracter))
            elif caracter in caracter_a_funcion.keys():
                operacion = caracter_a_funcion[caracter]

                if len(self.pila) < 2:
                    raise ErrorNotacionPolaca("No hay suficientes argumentos.")
                segundo_operando = self.pila.pop()
                primer_operando = self.pila.pop()

                self.pila.append(operacion(primer_operando, segundo_operando))

        if len(self.pila) > 1:
            raise ErrorNotacionPolaca("Demasiados argumentos")

        return self.pila.pop()

        # [FIN]


if __name__ == "__main__":
    # [INICIO]: Pruebe sus soluciones entre [INICIO] y [FIN].
    # No edite antes de esta línea.
    pass
    # [FIN]


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
        return self.numero_elementos
        # [FIN]

    def apilar(self, elemento):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        if not self.sobrescribir:
            if self.tamanio() + 1 > self.capacidad:
                raise ErrorEnPila("Capacidad excedida")

            if self.indice_cima is None:
                nuevo_indice = 0
            else:
                nuevo_indice = self.indice_cima + 1
            self.numero_elementos = self.numero_elementos + 1
            self.elementos[nuevo_indice] = elemento
            self.indice_cima = nuevo_indice
        else:
            if self.indice_cima is None:
                nuevo_indice = 0
                self.numero_elementos = self.numero_elementos + 1
            else:
                nuevo_indice = self.indice_cima + 1

                if self.tamanio() < self.capacidad:
                    self.numero_elementos = self.numero_elementos + 1
                elif self.tamanio() == self.capacidad:
                    if not (self.indice_cima + 1 < self.capacidad):
                        nuevo_indice = nuevo_indice - self.capacidad

            self.elementos[nuevo_indice] = elemento
            self.indice_cima = nuevo_indice

        # [FIN]

    def esta_vacia(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        return self.numero_elementos == 0
        # [FIN]

    def cima(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        if self.esta_vacia():
            raise ErrorEnPila()
        return self.elementos[self.indice_cima]
        # [FIN]

    def desapilar(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        if self.esta_vacia():
            raise ErrorEnPila()
        resultado = self.cima()

        self.numero_elementos = self.numero_elementos - 1
        self.indice_cima = self.indice_cima - 1
        return resultado
        # [FIN]


class CalculadoraGanancias:
    def __init__(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        self.cola_acciones = []
        self.numero_acciones = 0
        # [FIN]

    def registrar_compra(self, descripcion_transaccion):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.

        palabras = descripcion_transaccion.split()
        try:
            unidades_compradas = int(palabras[0])
            precio_compra = int(palabras[5])
        except ValueError as error:
            raise ErrorTransaccion(error)

        operacion = {
            "unidades": unidades_compradas,
            "precio": precio_compra,
        }
        self.cola_acciones.append(operacion)

        self.numero_acciones = self.numero_acciones + unidades_compradas
        # [FIN]

    def registrar_venta(self, descripcion_transaccion):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.

        palabras = descripcion_transaccion.split()
        try:
            unidades_vendidas = int(palabras[0])
            precio_venta = int(palabras[5])
        except ValueError as error:
            raise ErrorTransaccion(error)

        if unidades_vendidas > self.acciones_disponibles():
            raise ErrorTransaccion()

        ganancias = precio_venta * unidades_vendidas
        pendientes_venta = unidades_vendidas

        while pendientes_venta > 0:
            informacion_compra = self.cola_acciones.pop(0)
            acciones_compradas = informacion_compra["unidades"]
            precio_compra = informacion_compra["precio"]

            if acciones_compradas <= pendientes_venta:
                ganancias = ganancias - acciones_compradas * precio_compra
                pendientes_venta = pendientes_venta - acciones_compradas
            else:
                acciones_no_vendidas = acciones_compradas - pendientes_venta
                self.cola_acciones.insert(
                    0, {"unidades": acciones_no_vendidas, "precio": precio_compra}
                )

                ganancias = ganancias - pendientes_venta * precio_compra
                pendientes_venta = 0

        self.numero_acciones = self.numero_acciones - unidades_vendidas
        return ganancias
        # [FIN]

    def catalogo_acciones(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        return self.cola_acciones
        # [FIN]

    def acciones_disponibles(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        return self.numero_acciones
        # [FIN]
