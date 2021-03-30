# coding=utf-8
import random
from math import factorial
from random import seed
random.seed()

def combinaciones(m, n):
    return factorial(m) // (factorial(n) * factorial(m - n))
class Punto():
    def __init__(self, x, y):
        self.x, self.y = x, y

#use id(x) if objects have the same name
class Rect():
    def __init__(self, name, h, w):
        self.name = name
        self.width  = w
        self.height = h
        self.rotation = False
    
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y;
    
    def rotar(self):
        self.width, self.height = self.height, self.width
        self.rotation = not self.rotation

    def getPosicionX(self):
        return self.x + self.width

    def getPosicionY(self):
        return self.y + self.height
    
    def imprimir(self, pos=False):
        if (pos):
            self (self.name, self.x, self.y)
        else:
            print(self.name, self.width, self.height, self.rotation)
def getData(filename, d,c):
    #get data from the file 
    lines = [line.rstrip('\n') for line in open(filename, "r") ]

    #get dimensiones
    d.append(int(lines[0].split(" ")[0]))
    d.append(int(lines[0].split(" ")[1]))
    
    #save the cortes dimensions and clean the data for empty spaces
    for i in range(2, len(lines)):
        c.append(lines[i].split(" "))
        #c[i-2].pop() if (i != len(lines)-1) else -1      
    #print (d, c)
    #returns number of plachas cause numbers are hard to deal with as refernces
    return int(lines[1])

def salida():
    return 0

#Iniciation 
class Individuo:
    # 
    def __init__(self, g):
        self.genes = []
        n = random.randint(0, len(g))
        for i in range(0, n):
            x = random.randint(0, len(g)-1)
            if not (g[x] in self.genes):
                self.genes.append(g[x])
                if (random.randint(0,100)%5):
                    (self.genes[-1]).rotar()
        self.fitness = 0
    
    def getGene(self, i):
        return self.genes[i]
    
    def setGene(self, i, value):
        self.genes[i] = value
        self.fitness = 0
    
    def getFitness(self):
        if (self.fitness):
            self.fitness = 1
        return self.fitness
    
    def imprimir(self):
        for g in self.genes:
            g.imprimir()
        
class Poblacion:
    def __init__(self, size, ini, genes):
        self.individuos = []
        if (ini):
            for i in range(0, size):
                self.individuos.append(Individuo(genes))

    def getFittest(self):
        fittest = self.individuos[0]
        for i in range(0, size()):
            if (fittest.getFitness() <= self.individuos[i].getFitness()):
                fittest = self.individuos[i]
    
    def size(self):
        return (len(self.individuos))

    def setIndividuo(self, i, indiv):
        self.individuo[i] = indiv

#Evaluation - shove it all in the board
#n^2
class Fitness():
    def __init__(self, x):
        self.solucion = x

    def calculateFitness(self, indiv, p, area, n):
        fitness = area
        if not indiv.genes:
            return 0
        indiv.genes[0].setX(0)
        indiv.genes[0].setY(0)
        nxt, y, x = 1, 0, 0
        #ancho
        for i in range(nxt, len(indiv.genes)):
            crr = indiv.genes[i-1].getX() + indiv.genes[i-1].width
            if (crr < p[0]):
                indiv.genes[i].setX(crr)
                indiv.genes[i].setY(y)
            else:
                x = crr
                nxt = i
                break

        #cambia el alto
        for i in range(nxt, len(indiv.genes)):
            crr = indiv.genes[i-1].getY() + indiv.genes[i-1].height
            if (crr < p[1]):
                indiv.genes[i].setX(x)
                indiv.genes[i].setY(crr)
            else:
                nxt = i
                break 
        for i in range(0, nxt-1):
            indiv.genes[i].imprimir()
            print(indiv.genes[i].x, indiv.genes[i].y, )
        return 1

#Selection

#Crossover

#Mutation

#Termination

#Fit wherever it fits 
def randomize(n, d, c):
    print (n)

#Genes - 3n
def crearGenes(cortes):
    g = []
    for c in cortes:
        for i in range (0, int(c[3])): 
            g.append(Rect(c[0], int(c[1]), int(c[2])))

    return g

#INTENTO#1---NO FAILURE
#INTENTO#2---Intentar buscar que piezas tienen mismos anchos
#Intento 3 ---- Genetic Algorithm ? 
def main():
    import timeit
    start = timeit.default_timer()

    dim, cortes = [], []
    num = getData("test", dim, cortes)
    genes = crearGenes(cortes)
    x = combinaciones(len(cortes), len(cortes)/2) if combinaciones(len(cortes), len(cortes)/2) <100 else 100
    poblacion = Poblacion(x, True, genes)
    plancha = Rect('plancha', int(dim[0]), int(dim[1]))
    fit = Fitness(2)
    fit.calculateFitness(poblacion.individuos[0], 
        [int(dim[0]), int(dim[1])], plancha.width*plancha.height,
        num)
    #for i in range(0, poblacion.size()):
        #print (i)
        #poblacion.individuos[i].imprimir();
        #i.imprimir()
    stop = timeit.default_timer()
    print('Time: ', stop - start)  

if __name__ == "__main__":
    main()
