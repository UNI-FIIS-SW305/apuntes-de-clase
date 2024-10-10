from laboratorio import (
    NotacionPolacaInversa,
    ErrorNotacionPolaca,
    PilaCapacidadFija,
    ErrorEnPila,
    CalculadoraGanancias,
    ErrorTransaccion,
)

import pytest


def test_p1_sumar_dos_numeros():
    notacion_polaca = NotacionPolacaInversa(expresion="3 4 +")

    assert notacion_polaca.evaluar() == 7


def test_p1_sumar_y_restar():
    notacion_polaca = NotacionPolacaInversa(expresion=" 3 4 - 5 +")
    assert notacion_polaca.evaluar() == 4.0


def test_p1_expresion_con_multiplicacion():
    notacion_polaca = NotacionPolacaInversa(expresion=" 3 4 + 5 6 + x ")
    assert notacion_polaca.evaluar() == 77


def test_p1_cuatro_operaciones():
    notacion_polaca = NotacionPolacaInversa(expresion=" 5 2 + 8 3 - x 4 / ")
    assert notacion_polaca.evaluar() == 8.75


def test_p1_argumentos_insuficientes():
    with pytest.raises(ErrorNotacionPolaca):
        notacion_polaca = NotacionPolacaInversa(expresion=" 4 + 5 6 + x ")
        notacion_polaca.evaluar()


def test_p1_exceso_de_argumentos():
    with pytest.raises(ErrorNotacionPolaca):
        notacion_polaca = NotacionPolacaInversa(expresion="  2 3 4 + 5 6 + x ")
        notacion_polaca.evaluar()


def test_p1_argumentos_invalidos():
    with pytest.raises(ErrorNotacionPolaca):
        notacion_polaca = NotacionPolacaInversa(expresion="  3 4 + 5 6 a x ")
        notacion_polaca.evaluar()


def test_p2_tamanio_pila():
    pila = PilaCapacidadFija(capacidad=3, sobrescribir=False)
    assert pila.tamanio() == 0

    pila.apilar(1)
    pila.apilar(2)
    assert len(pila.elementos) == 3
    assert len([elemento for elemento in pila.elementos if elemento is not None]) == 2

    assert pila.tamanio() == 2


def test_p2_esta_vacia():
    pila = PilaCapacidadFija(capacidad=3, sobrescribir=False)
    assert pila.esta_vacia()

    pila.apilar(1)

    assert not pila.esta_vacia()


def test_p2_apilar_en_exceso_sin_sobrescribir():
    pila = PilaCapacidadFija(capacidad=3, sobrescribir=False)

    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)

    with pytest.raises(ErrorEnPila):
        pila.apilar(4)


def test_p2_cima():
    pila = PilaCapacidadFija(capacidad=3, sobrescribir=False)
    with pytest.raises(ErrorEnPila):
        pila.cima()

    pila.apilar(1)
    assert pila.cima() == 1
    assert pila.tamanio() == 1

    pila.apilar(2)
    assert pila.cima() == 2
    assert pila.tamanio() == 2


def test_p2_desapilar():
    pila = PilaCapacidadFija(capacidad=3, sobrescribir=False)
    assert len(pila.elementos) == 3

    with pytest.raises(ErrorEnPila):
        pila.desapilar()

    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)
    assert len(pila.elementos) == 3

    assert pila.desapilar() == 3
    assert pila.tamanio() == 2
    assert pila.cima() == 2

    assert pila.desapilar() == 2
    assert pila.tamanio() == 1
    assert pila.cima() == 1

    assert pila.desapilar() == 1
    assert pila.esta_vacia()

    assert len(pila.elementos) == 3


def test_p2_apilar_en_exceso_con_sobrescribir():
    pila = PilaCapacidadFija(capacidad=3, sobrescribir=True)

    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)

    pila.apilar(4)

    assert pila.cima() == 4
    assert pila.tamanio() == 3

    pila.apilar(5)
    assert pila.cima() == 5
    assert pila.tamanio() == 3

    assert pila.desapilar() == 5
    assert pila.desapilar() == 4
    assert pila.desapilar() == 3

    assert len(pila.elementos) == 3

    assert pila.esta_vacia()


def test_p3_comprar_una_accion():

    calculadora_ganancias = CalculadoraGanancias()

    calculadora_ganancias.registrar_compra(
        "100 accion(es) al precio de 20 PEN cada una."
    )

    assert len(calculadora_ganancias.catalogo_acciones()) == 1
    assert calculadora_ganancias.catalogo_acciones()[0] == {
        "unidades": 100,
        "precio": 20,
    }


def test_p3_comprar_varias_acciones():

    calculadora_ganancias = CalculadoraGanancias()

    calculadora_ganancias.registrar_compra(
        "100 accion(es) al precio de 20 PEN cada una."
    )
    calculadora_ganancias.registrar_compra(
        "20 accion(es) al precio de 24 PEN cada una."
    )

    calculadora_ganancias.registrar_compra(
        "200 accion(es) al precio de 36 PEN cada una."
    )

    assert len(calculadora_ganancias.catalogo_acciones()) == 3
    assert calculadora_ganancias.catalogo_acciones()[0] == {
        "unidades": 100,
        "precio": 20,
    }
    assert calculadora_ganancias.catalogo_acciones()[1] == {
        "unidades": 20,
        "precio": 24,
    }

    assert calculadora_ganancias.catalogo_acciones()[2] == {
        "unidades": 200,
        "precio": 36,
    }


def test_p3_registrar_venta():
    calculadora_ganancias = CalculadoraGanancias()

    calculadora_ganancias.registrar_compra(
        "100 accion(es) al precio de 20 PEN cada una."
    )
    calculadora_ganancias.registrar_compra(
        "20 accion(es) al precio de 24 PEN cada una."
    )

    calculadora_ganancias.registrar_compra(
        "200 accion(es) al precio de 36 PEN cada una."
    )

    assert 940 == calculadora_ganancias.registrar_venta(
        "150 accion(es) al precio de 30 PEN cada una."
    )

    assert len(calculadora_ganancias.catalogo_acciones()) == 1
    assert calculadora_ganancias.catalogo_acciones()[0] == {
        "unidades": 170,
        "precio": 36,
    }


def test_p3_numero_acciones():
    calculadora_ganancias = CalculadoraGanancias()

    calculadora_ganancias.registrar_compra(
        "100 accion(es) al precio de 20 PEN cada una."
    )
    assert calculadora_ganancias.acciones_disponibles() == 100

    calculadora_ganancias.registrar_compra(
        "20 accion(es) al precio de 24 PEN cada una."
    )
    assert calculadora_ganancias.acciones_disponibles() == 120

    calculadora_ganancias.registrar_compra(
        "200 accion(es) al precio de 36 PEN cada una."
    )
    assert calculadora_ganancias.acciones_disponibles() == 320

    calculadora_ganancias.registrar_venta(
        "150 accion(es) al precio de 30 PEN cada una."
    )
    assert calculadora_ganancias.acciones_disponibles() == 170


def test_p3_error_en_unidades():
    calculadora_ganancias = CalculadoraGanancias()

    with pytest.raises(ErrorTransaccion):
        calculadora_ganancias.registrar_compra(
            "100a accion(es) al precio de 20 PEN cada una."
        )
    with pytest.raises(ErrorTransaccion):
        calculadora_ganancias.registrar_venta(
            "150a accion(es) al precio de 30 PEN cada una."
        )


def test_p3_error_en_precio():
    calculadora_ganancias = CalculadoraGanancias()

    with pytest.raises(ErrorTransaccion):
        calculadora_ganancias.registrar_compra(
            "100 accion(es) al precio de x20 PEN cada una."
        )
    with pytest.raises(ErrorTransaccion):
        calculadora_ganancias.registrar_venta(
            "150 accion(es) al precio de x30 PEN cada una."
        )


def test_p3_acciones_insuficientes():
    calculadora_ganancias = CalculadoraGanancias()

    calculadora_ganancias.registrar_compra(
        "100 accion(es) al precio de 20 PEN cada una."
    )
    assert calculadora_ganancias.acciones_disponibles() == 100

    calculadora_ganancias.registrar_compra(
        "20 accion(es) al precio de 24 PEN cada una."
    )
    assert calculadora_ganancias.acciones_disponibles() == 120

    calculadora_ganancias.registrar_compra(
        "200 accion(es) al precio de 36 PEN cada una."
    )
    assert calculadora_ganancias.acciones_disponibles() == 320

    with pytest.raises(ErrorTransaccion):
        calculadora_ganancias.registrar_venta(
            "321 accion(es) al precio de 30 PEN cada una."
        )

    assert len(calculadora_ganancias.catalogo_acciones()) == 3
    assert calculadora_ganancias.acciones_disponibles() == 320
