class Dijkstra:
    def __init__(self):
        self.matrizAristas = []
        self.origen = ''
        self.origenRuta = ''
        self.destino = ''
        self.peso = 0
        self.visitados = []

    def setMatrizOrigenDestino(self, matrizAristas, origen, destino):
        self.matrizAristas = matrizAristas
        self.origen = origen
        self.origenRuta = origen
        self.destino = destino

    def getVisitados(self):
        mensaje = self.origenRuta + "->"
        peso = 0
        if type(self.visitados) != str:
            for fila in self.visitados:
                if self.visitados.index(fila) != len(self.visitados) - 1:
                    mensaje = mensaje + f"{fila[0]}->"
                else:
                    mensaje = mensaje + f"{fila[0]}"
                peso += fila[1]
            mensaje = f"Ruta:[{mensaje}] Costo Total: {peso}"
            self.origenRuta = ''
            self.visitados = []
            return mensaje
        else:
            mensaje = self.visitados
            self.origenRuta = ''
            self.visitados = []
            return mensaje

    def getMatrizAristas(self):
        return self.matrizAristas

    def dijkstra(self):

        verticeOrigenExiste = False
        verticeDestinoExiste = False

        # Recorremos para saber si existen los dos
        for fila in range(len(self.matrizAristas)):
            if self.matrizAristas[fila][0] == self.origen:
                verticeOrigenExiste = True
            if self.matrizAristas[fila][1] == self.destino:
                verticeDestinoExiste = True

        # Si existen entonces
        if verticeOrigenExiste and verticeDestinoExiste:
            visitadoAux = []  # para ir guardando los visitados
            llegoDestino = False
            mismoRecorrido = 0
            while not llegoDestino:
                if self.origen != self.destino:  # si el origen es diferente del destino
                    for fila in range(len(self.matrizAristas)):
                        if self.matrizAristas[fila][0] == self.origen:  # Si encuentra al origen

                            if self.matrizAristas[fila][1] == self.destino:  # Pregunta que si en la misma tupla esta el destino
                                self.peso = [self.matrizAristas[fila][1], self.matrizAristas[fila][2]]
                                visitadoAux.append(self.matrizAristas[fila][1])
                                llegoDestino = True
                                break


                            if self.peso == 0: # Pregunta si el peso es cero
                                self.peso = [self.matrizAristas[fila][1],self.matrizAristas[fila][2]]  # guarda [el vecino del origen, peso]
                                visitadoAux.append(self.matrizAristas[fila][1])  # [guarda el vecino]
                                continue

                            if self.matrizAristas[fila][2] <= self.peso[1] and self.matrizAristas[fila][1] != self.destino:  # Pregunta si encontro un peso menor
                                if self.matrizAristas[fila][1] not in visitadoAux:  # Pregunta si no estan en los visitados y si no es el destino
                                    self.peso = [self.matrizAristas[fila][1], self.matrizAristas[fila][2]]
                                    visitadoAux.append(self.matrizAristas[fila][1])

                                else:
                                    mismoRecorrido += 1
                                    if mismoRecorrido > 2:
                                        self.peso = 0
                                        break

                    self.visitados.append(self.peso)
                    if type(self.peso) == int and self.peso == 0:  # Dado que atras se guarda como un vector el peso
                        # Si todavia es un int entonces no encontro conexiones
                        self.visitados = f"No hay conexion entre los nodos"
                        break;
                    self.origen = self.peso[0]  # Cambiamos el nodo origen, ahora es el vecino del origen con peso menor
                    self.peso = 0
                else:  # Por si el nodo origen es el mismo destino
                    for fila in self.matrizAristas:
                        if fila[0] == self.origen and fila[1] == self.origen:
                            self.visitados = f"Nodo se apunta asi mismo con peso {fila[2]}"
                            break;
                    break

        else:  # si no los nodos ingresados no existen
            if not verticeOrigenExiste and not verticeDestinoExiste:
                self.visitados = "Vertice origen y vertice destino inexistente\n" \
                                 "o no existe camino entre ellos"
            elif not verticeOrigenExiste and verticeDestinoExiste:
                self.visitados = "Vertice origen inexistente"
            else:
                self.visitados = "Vertice Destino inexistente"


dikstras = Dijkstra()
dikstras.setMatrizOrigenDestino(
    [['a', 'a', 1], ['a', 'b', 1], ['a', 'c', 3], ['a', 'd', 4], ['b', 'a', 2], ['b', 'b', 3], ['b', 'd', 9],
     ['c', 'a', 1], ['c', 'c', 20], ['d', 'a', 5], ['d', 'b', 3], ['d', 'd', 8]], 'b', 'b')
print(dikstras.getMatrizAristas())
dikstras.dijkstra()
print(dikstras.getVisitados())
