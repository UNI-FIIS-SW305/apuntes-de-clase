class GrafoDirigidoMatrizAdyacencia:

    def __init__(self, lista_vertices):
        self.lista_vertices = lista_vertices

        numero_de_vertices = len(lista_vertices)
        self.matriz_de_adyacencia = []

        for _ in range(numero_de_vertices):
            self.matriz_de_adyacencia.append([0 for _ in range(numero_de_vertices)])

        # print(f"{self.matriz_de_adyacencia=}")

    def obtener_indice(self, vertice):

        if vertice not in self.lista_vertices:
            return -1

        return self.lista_vertices.index(vertice)

    def agregar_arista(self, vertice_inicio, vertice_fin):
        indice_inicio, indice_fin = self.obtener_indice(
            vertice_inicio
        ), self.obtener_indice(vertice_fin)

        if indice_inicio == -1 or indice_fin == -1:
            return

        file_vertice_inicio = self.matriz_de_adyacencia[
            indice_inicio
        ]  # Tipo de dato: Lista de Python
        file_vertice_inicio[indice_fin] = 1

    def contiene_arista(self, vertice_inicio, vertice_fin):
        indice_inicio, indice_fin = self.obtener_indice(
            vertice_inicio
        ), self.obtener_indice(vertice_fin)

        if indice_inicio == -1 or indice_fin == -1:
            return None

        return self.matriz_de_adyacencia[indice_inicio][indice_fin]

    def remover_arista(self, vertice_inicio, vertice_fin):
        indice_inicio, indice_fin = self.obtener_indice(
            vertice_inicio
        ), self.obtener_indice(vertice_fin)

        if indice_inicio == -1 or indice_fin == -1:
            return None

        self.matriz_de_adyacencia[indice_inicio][indice_fin] = 0

    def representar(self):
        resultado = " "
        for vertice in self.lista_vertices:
            resultado += " " + vertice

        resultado += "\n"

        for indice, fila in enumerate(self.matriz_de_adyacencia):
            resultado += self.lista_vertices[indice] + " " + str(fila) + "\n"

        return resultado


class GrafoMatrizAdyacencia:

    def __init__(self, lista_vertices, es_dirigido) -> None:
        self.es_dirigido = es_dirigido

        self.lista_vertices = lista_vertices
        numero_de_vertices = len(lista_vertices)
        self.matriz_de_adyacencia = []

        for _ in range(numero_de_vertices):
            self.matriz_de_adyacencia.append([0 for _ in range(numero_de_vertices)])

    def obtener_indice(self, vertice):

        if vertice not in self.lista_vertices:
            return -1

        return self.lista_vertices.index(vertice)

    def agregar_arista(self, vertice_inicio, vertice_fin, peso):
        indice_inicio, indice_fin = self.obtener_indice(
            vertice_inicio
        ), self.obtener_indice(vertice_fin)

        if indice_inicio == -1 or indice_fin == -1:
            return

        self.matriz_de_adyacencia[indice_inicio][indice_fin] = peso
        if not self.es_dirigido:
            self.matriz_de_adyacencia[indice_fin][indice_inicio] = peso

    def representar(self):
        resultado = " "
        for vertice in self.lista_vertices:
            resultado += " " + vertice

        resultado += "\n"

        for indice, fila in enumerate(self.matriz_de_adyacencia):
            resultado += self.lista_vertices[indice] + " " + str(fila) + "\n"

        return resultado


if __name__ == "__main__":
    lista_vertices = ["A", "B", "C", "D", "E", "F"]
    # grafo = GrafoDirigidoMatrizAdyacencia(lista_vertices=lista_vertices)

    # print(f"{grafo.obtener_indice("B")=}")  # Deberia ver 1
    # print(f"{grafo.obtener_indice("C")=}")  # Deberia ver 2
    # print(f"{grafo.obtener_indice("Z")=}")  # Deberia ver -1

    # grafo.agregar_arista("A", "B")
    # grafo.agregar_arista("C", "A")
    # grafo.agregar_arista("B", "E")
    # grafo.agregar_arista("B", "D")
    # grafo.agregar_arista("D", "E")
    # grafo.agregar_arista("C", "F")

    # grafo.agregar_arista("Z", "W")

    # print(grafo.representar())

    # print(f"{grafo.contiene_arista('A', 'B')=}")  # Deberia retornar: 1
    # print(f"{grafo.contiene_arista('B', 'A')=}")  # Deberia retornar: 0
    # print(f"{grafo.contiene_arista('Z', 'W')=}")  # Deberia retornar: None

    # grafo.remover_arista("A", "B")
    # print(grafo.representar())
    # print(f"{grafo.contiene_arista('A', 'B')=}")  # Deberia retornar: 0

    grafo = GrafoMatrizAdyacencia(lista_vertices=lista_vertices, es_dirigido=False)
    grafo.agregar_arista("A", "B", 5)
    grafo.agregar_arista("B", "E", 9)
    grafo.agregar_arista("B", "D", 6)

    grafo.agregar_arista("D", "E", 8)

    grafo.agregar_arista("C", "F", 11)
    grafo.agregar_arista("C", "A", 1)

    print(grafo.representar())
