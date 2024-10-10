# SW 305: Segunda Práctica Calificada

## Instrucciones

- **Tienen que hacer uso del repositorio de GitHub Classroom para el envío del examen, en el tiempo establecido.** No se aceptarán envíos en otros medios (repositorios privados, correo electrónico, etc) o fuera de tiempo.
- Para evitar inconvenientes, se requiere que envíen sus soluciones parciales a la nube (haciendo _Commit_ y _Push_) por lo menos cada media hora.
- Está permitido consultar el material de clase (diapositivas, libros, código fuente, y apuntes personales). **Consultar recursos como Google, ChatGPT, u otros compañeros está estrictamente prohibido, y se aplicará el reglamento de ser detectado.**
- Utilice la notación y el estilo de programación desarrollado en clase. Se disminuirá puntaje en caso contrario.
- Sólamente ingrese código en las secciones marcadas como `[INICIO]` y `[FIN]`. No edite otras partes de `laboratorio.py`, u otros archivos.
- La instrucción `pass` es un texto temporal. Puede eliminarlo para implementar su solución.
- El uso de `import` está prohibido. No está permitido importar o instalar librerías externas.
- Utilice la sección final de `laboratorio.py` para probar sus soluciones. Todas sus soluciones deben contener pruebas, que demuestren su funcionamiento.

## Primer Problema (7 puntos)

La [notación polaca inversa (NPI)](https://omegaup.com/arena/problem/Notacion-Polaca-Inversa/#problems) es una manera no-ambigua de definir operaciones aritméticas sin necesidad de usar paréntesis.
Por ejemplo, si tenemos la expresión aritmética `(<EXPRESION-1>) <OPERADOR> (<EXPRESION-2>)`, su equivalente en notación polaca sería `<EXPRESION-NPI-1> <EXPRESION-NPI-2> <OPERADOR>`, donde `<EXPRESION-NPI-1>` es `<EXPRESION-1>` en notación polaca inversa, y `<EXPRESION-NPI-2>` es la `<EXPRESION-2>` expresada en notación polaca inversa.
La notación polaca inversa de un número es simplemente el mismo número.
Por ejemplo, la expresión aritmética `((5 + 2) x (8 − 3))/4` es equivalente a `5 2 + 8 3 - x 4 /` en notación polaca inversa.

En el archivo `laboratorio.py` complete la implementación de la clase `NotacionPolacaInversa`. Considere lo siguiente:

- En constructor contiene un sólo parámetro: una cadena de caracteres con la expresión en notación polaca inversa a evaluar.
- La clase tiene un sólo método `evaluar()`, que retorna el valor numérico de una expresión en NPI. Por ejemplo:
  ```python
  notacion_polaca = NotacionPolacaInversa(expresion=" 5 2 + 8 3 - x 4 / ")
  notacion_polaca.evaluar() # Debe retornar: 8.75
  ```
  Para obtener `8.75`, considerar lo siguiente: 1) `5 2 +` es equivalente a `5 + 2 = 7`, 2) `8 3 -` es equivalente a `8 - 3 = 5`, 3) El operando `x` multiplica los números `7` (paso 1) y `5` (paso 2), por lo que produce `7 * 5 = 35`. 4) El operando `/` divide los números `35` (paso 3) y `4` (a la izquierda de `\`), por el que el resultado de la expresión es `35 / 4 = 8.75`. Nótese que es equivalente a evaluar `((5 + 2) x (8 − 3))/4 = 8.75`.
- Las expresiones NPI consisten en cadenas de caracteres donde los operandos (valores numéricos) y operadores (`+` para sumar, `-` para restar, `x` para multiplicar y `/` para dividir) están separados por espacios en blanco. En caso la expresión contenga un caracter inválido, lanzar una excepción `ErrorNotacionPolaca` (ya definida en `laboratorio.py`). Por ejemplo:

  ```python
  notacion_polaca = NotacionPolacaInversa(expresion=" 3 4 + 5 6 a x ")
  notacion_polaca.evaluar() # Debe lanzar ErrorNotacionPolaca
  ```

- Todas las operaciones soportadas por `NotacionPolacaInversa` tienen dos operandos. En caso se provean más o menos operandos en una expresión NPI, lanzar una excepción `ErrorNotacionPolaca`. Por ejemplo:

  ```python
  notacion_polaca = NotacionPolacaInversa(expresion=" 4 + 5 6 + x ")
  notacion_polaca.evaluar() # Debe lanzar ErrorNotacionPolaca
  ```

  Nótese que para el primer operador `+`, sólo se tiene un solo operando (`4`), en lugar de dos.

## Segundo Problema (7 puntos)

Implemente el TAD Pila usando vectores (en Python, tipo `list`), de modo que el vector tenga una longitud fija, que determina la capacidad máxima de la pila.

En el archivo `laboratorio.py` complete la implementación de la clase `PilaCapacidadFija`. Considere lo siguiente:

- El constructor recibe dos parámetros: `capacidad`, un entero que determina el tamaño del vector que almacenará los elementos, y `sobrescribir`, un booleano que determina si al exceder la capacidad se debe sobrescribir elementos antiguos. Tanto `elementos`, `capacidad`, y `sobrescribir` ya están definidos como campos en la clase, pero puede definir campos adicionales de ser necesario.

- El método `tamanio` retorna el número de elementos en la lista. Por ejemplo:

  ```python
      pila = PilaCapacidadFija(capacidad=3, sobrescribir=False)
      pila.tamanio() == 0 #  Debe retornar 0
  ```

- El método `apilar` agregar elementos a la pila, **sin modificar el tamaño del vector `elementos`**. En caso el campo `sobrescribir` tenga el valor de `False`, al sobrepasar la `capacidad` de la pila se debe lanzar una excepción `ErrorEnPila` (ya definida en `laboratorio.py`). Por ejemplo:

  ```python
  pila = PilaCapacidadFija(capacidad=3, sobrescribir=False) # El vector pila.elementos contiene: [None, None, None]

  pila.apilar(1) # El vector pila.elementos contiene: [1, None, None]
  pila.apilar(2) # El vector pila.elementos contiene: [1, 2, None]
  pila.apilar(3) # El vector pila.elementos contiene: [1, 2, 3]

  pila.apilar(4) # Debe lanzar la excepción ErrorEnPila
  ```

- Cuando el campo `sobrescribir` tenga el valor de `True`, al sobrepasar la `capacidad` de la pila se debe reemplazar el elemento más antiguo con el nuevo valor a apilar. Por ejemplo:

  ```python
  pila = PilaCapacidadFija(capacidad=3, sobrescribir=True) # El vector pila.elementos contiene: [None, None, None]

  pila.apilar(1) # El vector pila.elementos contiene: [1, None, None]
  pila.apilar(2) # El vector pila.elementos contiene: [1, 2, None]
  pila.apilar(3) # El vector pila.elementos contiene: [1, 2, 3]

  pila.apilar(4) # El vector pila.elementos contiene: [4, 2, 3]
  ```

- El método `esta_vacia` retorna `True` si la pila está vacía, y `False` en caso contrario. Por ejemplo:

  ```python
  pila = PilaCapacidadFija(capacidad=3, sobrescribir=False)
  pila.esta_vacia() # Debe retornar True

  pila.apilar(1)

  pila.esta_vacia() # Debe retornar False
  ```

- El método `cima` retorna el valor en la cima de la pila, sin modificar el contenido de la pila. En caso la pila esté vacía, se debe lanzar la excepción `ErrorEnPila`. Por ejemplo:

  ```python
  pila = PilaCapacidadFija(capacidad=3, sobrescribir=False)
  pila.cima() # Debe lanzar ErrorEnPila

  pila.apilar(1)
  pila.cima() # Debe retornar 1
  pila.tamanio() # Debe retornar 1
  ```

- El método `desapilar` retorna el elemento en la cima y lo remueve de la pila. En caso la pila esté vacía, se debe lanzar la excepción `ErrorEnPila`. Por ejemplo:

  ```python
    pila = PilaCapacidadFija(capacidad=3, sobrescribir=False)

    pila.desapilar() # Debe lanzar ErrorEnPila

    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)

    pila.desapilar() # Debe retornar 3
    pila.tamanio() # Debe retornar 2
  ```

## Tercer Problema (6 puntos)

En el archivo `laboratorio.py`, complete la implementación de la clase `CalculadoraGanancias`, utilizada para calcular las ganancias de capital para un inversionista en la bolsa de valores.
Considere lo siguiente:

- El método `registrar_compra` recibe como parámetro una descripción textual del número de acciones a comprar a un precio determinado, en el formato `"<NUMERO-ACCIONES> accion(es) al precio de <PRECIO-ACCIONES> PEN cada una."`. Por ejemplo:

  ```python
    calculadora_ganancias = CalculadoraGanancias()

    calculadora_ganancias.registrar_compra(
        "100 accion(es) al precio de 20 PEN cada una."
    )
  ```

  Nótese que estamos indicando que compramos 100 acciones al precio de 20 nuevos soles. En caso `<NUMERO-ACCIONES>` o `<PRECIO-ACCIONES>` no sean números enteros válidos, lanzar una excepción `ErrorTransaccion` (ya definida en `laboratorio.py`). Por ejemplo:

  ```python
    calculadora_ganancias = CalculadoraGanancias()

    calculadora_ganancias.registrar_compra(
        "100 accion(es) al precio de x20 PEN cada una."
    ) # Debe lanzar ErrorTransaccion
  ```

- El método `registrar_venta` recibe como parámetro una descripción textual del número de acciones a vender a un precio determinado, en el formato `"<NUMERO-ACCIONES> accion(es) al precio de <PRECIO-ACCIONES> PEN cada una."`. Este método debe retornar las ganancias de capital de la operación, considerando que las acciones se deben **vender en orden de antiguedad**. Por ejemplo:

  ```python
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
    calculadora_ganancias.registrar_venta(
        "150 accion(es) al precio de 30 PEN cada una."
    ) # Debe retornar 940

  ```

  Nótese que de las 150 acciones vendidas: 1) Se venden primero las 100 acciones compradas a 20 nuevos soles, con una ganancia de `100 * (30 - 20) = 1000`, 2) Luego, vendemos las 20 acciones compradas a 24 soles, con una ganancia de `20 * (30 - 24) = 120`, 3) Finalmente, para completar 150, vendemos 30 acciones compradas a 36 soles, con una pérdida de `30 * (30 - 36) = -180`. Entonces, las ganancias de capital son: `1000 + 120 - 180 = 940`.

  De manera similar a `registrar_compra`, los valores de `<NUMERO-ACCIONES>` y `<PRECIO-ACCIONES>` deben ser números enteros válidos, caso contrario se genera un error `ErrorTransaccion`. Por ejemplo:

  ```python
    calculadora_ganancias = CalculadoraGanancias()

    calculadora_ganancias.registrar_venta(
        "150 accion(es) al precio de x30 PEN cada una."
    ) # Debe lanzar un error ErrorTransaccion

  ```

  Además, en caso se intente vender más acciones de las que se han comprado se debe lanzar un error `ErrorTransaccion`. Por ejemplo:

  ```python
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
    calculadora_ganancias.registrar_venta(
        "321 accion(es) al precio de 30 PEN cada una."
    ) # Debe lanzar un error ErrorTransaccion
  ```

  Nótese que se han comprado solamente `100 + 20 + 200 = 320` acciones, por lo que no es posible vender `321`.

- El método `catalogo_acciones()` retorna una lista de diccionarios (con llaves `unidades` y `precio`, y valores enteros), indicando el número de acciones que tengo en mi portafolio junto a su precio. Por ejemplo:

  ```python
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
    calculadora_ganancias.registrar_venta(
        "150 accion(es) al precio de 30 PEN cada una."
    )

    calculadora_ganancias.catalogo_acciones()  # Debe retornar: [{ "unidades": 170, "precio": 36}]
    # Revise la explicación de la registrar_venta() para más detalle.
  ```

- El método `acciones_disponibles()` retorna el número de acciones que tengo en mi portafolio. Por ejemplo:

  ```python
    calculadora_ganancias = CalculadoraGanancias()

    calculadora_ganancias.registrar_compra(
        "100 accion(es) al precio de 20 PEN cada una."
    )
    calculadora_ganancias.acciones_disponibles() # Debe retornar: 100

    calculadora_ganancias.registrar_compra(
        "20 accion(es) al precio de 24 PEN cada una."
    )
    calculadora_ganancias.acciones_disponibles() # Debe retornar: 120
  ```
