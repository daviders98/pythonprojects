class Dijkstra:
    # Inicializador de variables en instancia de clase
    def __init__(self, etapas):
        self.etapas = etapas
        self.caminosOptimos = []
        self.condicion = True
        self.nodosInicio = []
        self.costoAcumulado = []
        self.nodosFinal = []
        self.nodosUnicosInicio = []
        self.nodosUnicosFinal = []
        self.matrix = []
        self.solucionGlobal = []
        self.costoOptimo = 0
        self.caminosPosibles = 0

    # Función recursiva
    def calcular(self, etapaActual):
        self.etapaActual = etapaActual
        self.contador = 1

        # primera iteración se piden los datos y se calculan los caminos optimos por renglón.
        if self.etapas == self.etapaActual:
            while self.condicion:
                self.nodosInicio.append(input(
                    "Coloca el nodo de inicio número " + str(self.contador) + " de la etapa " + str(
                        self.etapaActual) + ":\n"))
                self.nodosFinal.append(input(
                    "Coloca el nodo de final número " + str(self.contador) + " de la etapa " + str(
                        self.etapaActual) + ":\n"))
                self.costoAcumulado.append(input("Coloca el costo de ir del nodo " + str(
                    self.nodosInicio[len(self.nodosInicio) - 1]) + " al nodo " + str(
                    self.nodosFinal[len(self.nodosFinal) - 1]) + ":\n"))
                continuar = input(
                    "Hay más nodos de la etapa " + str(self.etapaActual) + "? Sí es así, coloca un 1, si no, un 0\n")
                if continuar == "1":
                    self.contador += 1
                else:
                    self.toMatrix()
                    self.solve()
                    break;
        else:
            self.nodosInicio = []
            self.nodosFinal = []
            # Para las demás iteraciones se usan los nodos de inicio como nodos finales de la iteracion siguiente.
            self.nodosUnicosFinal = []
            self.costoAcumulado = []
            x = 0
            for t in range(len(self.caminosOptimos)):
                self.nodosUnicosFinal.append(self.caminosOptimos[t][2])
            while self.condicion:
                self.nodosInicio.append(
                    input("Coloca el nodo de inicio número " + str(self.contador) + " para el nodo final "
                          + self.nodosUnicosInicio[x] + " de la etapa " + str(self.etapaActual) + ":\n"))
                self.nodosFinal.append(self.nodosUnicosInicio[x])
                costoPuntual = int(input("Coloca el costo de ir del nodo " + str(
                    self.nodosInicio[len(self.nodosInicio) - 1]) + " al nodo " + str(
                    self.nodosUnicosInicio[x]) + " de la etapa " + str(self.etapaActual) + ":\n"))
                costoPuntual += int(self.caminosOptimos[x][1])
                self.costoAcumulado.append(costoPuntual)
                continuar = input("Hay más nodos iniciales para el nodo final " + str(
                    self.nodosUnicosInicio[x]) + " de la etapa " + str(
                    self.etapaActual) + "? Sí es así, coloca un 1, si no, un 0\n")
                if continuar == "1":
                    self.contador += 1
                else:
                    x += 1
                    self.contador = 1
                if x == len(self.nodosUnicosInicio):
                    break;
            self.toMatrix()
            self.solve()
        if self.etapaActual > 1:
            self.etapaActual -= 1
            self.calcular(self.etapaActual)
        self.imprimirSolucion()

    # Reformateo de datos en una matriz de forma que se une en una lista de listas [[nodoinicio,costo,nodofinal],[...],...]
    def toMatrix(self):
        # PONER EN FUNCIÓN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.nodosUnicosInicio = []
        for l in self.nodosInicio:
            if l not in self.nodosUnicosInicio:
                self.nodosUnicosInicio.append(l)
        self.nodosUnicosFinal = []
        for m in self.nodosFinal:
            if m not in self.nodosUnicosFinal:
                self.nodosUnicosFinal.append(m)
        tempArray = []
        for i in range(len(self.nodosInicio)):
            for j in range(len(self.nodosUnicosInicio)):
                if (self.nodosInicio[i] == self.nodosUnicosInicio[j]):
                    tempArray.append([self.nodosInicio[i], int(self.costoAcumulado[i]), self.nodosFinal[i]])
        self.matrix = tempArray
        self.caminosPosibles += len(self.nodosUnicosInicio) * len(self.nodosUnicosFinal)

    # Saca el/los camino(s) óptimo(s) y lo(s) guarda en la propiedad caminosOptimos, que es un arreglo.
    def solve(self):
        costos = []
        minimos = []
        finalesOptimos = []
        for i in range(len(self.nodosUnicosInicio)):
            costos.append([])
            for j in range(len(self.matrix)):
                if self.nodosUnicosInicio[i] == self.matrix[j][0]:
                    costos[i].append(int(self.matrix[j][1]))
        for i in range(len(self.nodosUnicosInicio)):
            minimos.append(min(costos[i]))
        # Checa a qué nodo de final pertenece el minimo de cada nodo de inicio (renglón) y lo agrega como camino optimo
        temporal = []
        for i in range(len(self.nodosUnicosInicio)):
            for h in range(len(minimos)):
                for j in range(len(self.matrix)):
                    if self.matrix[j][0] == self.nodosUnicosInicio[i] and int(self.matrix[j][1]) == minimos[h]:
                        temporal.append(self.matrix[j])
        # Quita elementos repetidos si hay 2 con el mismo costo de diferentes nodos de inicio/final.
        new_k = []
        for elem in temporal:
            if elem not in new_k:
                new_k.append(elem)
        self.caminosOptimos = new_k
        self.solucionGlobal += self.caminosOptimos
        print(self.solucionGlobal)

    def imprimirSolucion(self):
        camino = []
        for e in range(self.caminosPosibles):
            if e > 0 and len(self.solucionGlobal) > 0:
                self.solucionGlobal.pop()
            camino.append([])
            rango = len(self.solucionGlobal) - 1
            for f in range(rango, -1, -1):
                if e == 0:
                    if f == rango:
                        optimo = self.solucionGlobal[f][1]
                        elemento = self.solucionGlobal[f][2]
                        camino[e].append(self.solucionGlobal[f][0])
                        camino[e].append(self.solucionGlobal[f][2])
                    else:
                        if elemento == self.solucionGlobal[f][0]:
                            elemento = self.solucionGlobal[f][2]
                            camino[e].append(self.solucionGlobal[f][2])
                else:
                    if self.solucionGlobal[f][1] == optimo:
                        elemento = self.solucionGlobal[f][2]
                        camino[e].append(self.solucionGlobal[f][0])
                        camino[e].append(self.solucionGlobal[f][2])
                    else:
                        if elemento == self.solucionGlobal[f][0]:
                            elemento = self.solucionGlobal[f][2]
                            camino[e].append(self.solucionGlobal[f][2])

        for way in camino:
            if way != "" and len(way)>0:
                print(way)

# Código principal :D

etapas = input("Cuantas etapas son?")
algoritmo = Dijkstra(int(etapas))
algoritmo.calcular(algoritmo.etapas)
