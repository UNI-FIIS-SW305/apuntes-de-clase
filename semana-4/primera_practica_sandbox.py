if __name__ == "__main__":
    catalogo_libros = [
        {"codigo": 1, "titulo": "La vuelta al mundo en 80 dias"},
        {"codigo": 2, "titulo": "After"},
        {"codigo": 3, "titulo": "La guerra del fin del mundo"},
    ]

    usuarios_y_sus_libros = {}
    usuarios_y_sus_libros["carlos"] = [3]
    usuarios_y_sus_libros["luis"] = [1]

    print(f"{usuarios_y_sus_libros["luis"]=}")

    libros_disponibles = [] # Lista con los libros no-comprados.
    libros_comprados = []
    for libros_de_usuario in usuarios_y_sus_libros.values():
        libros_comprados = libros_comprados + libros_de_usuario

    print(f"{usuarios_y_sus_libros.values()=}")
    print(f"{libros_comprados=}")

    for libro in catalogo_libros:
        if libro["codigo"] not in libros_comprados:
            libros_disponibles.append(libro)

    print(f"{libros_disponibles=}")

