from random import choices, randint, sample

def fitness(genoma):
    longitud = len(genoma)
    maxfitness = longitud*(longitud-1)/2
    diagMenor, diagMayor = 0, 0
    for i in range(longitud-1):
        for j in range(i+1,longitud):
            if genoma[j] == (genoma[i]-(j-i)):
                diagMenor += 1
            elif genoma[j] == (genoma[i]+(j-i)):
                diagMayor += 1
    maxfitness -= (diagMenor + diagMayor)
    return maxfitness

def crearGenotipo( longitud = 8 ):
    tipogen = []
    for i in range(longitud):
        tipogen.append(i+1)
    return sample(tipogen, longitud)

def crearPoblacion( tamano = 4 , long = 8):
    return [crearGenotipo(long) for _ in range(tamano)]

def reproduccion(poblacion):
    ruleta = [fitness(genoma) for genoma in poblacion]
    nuevapoblacion = []
    for _ in range(int(len(poblacion)/2)):
        genoma1, genoma2 = choices(poblacion, weights = ruleta, k=2)
        nuevapoblacion += cruza(genoma1, genoma2)
    return nuevapoblacion

def seleccion(poblacionvieja, poblacionnueva):
    poblaciontotal = poblacionnueva + poblacionvieja
    fenotipoPob = [(fitness(x), x) for x in poblaciontotal]
    fenotipoPob.sort()
    fenotipoPob.reverse()
    mejorpoblacion = [fenotipoPob[x][1] for x in range(len(fenotipoPob)) if x<4]
    return mejorpoblacion

def cruza(genoma1, genoma2):
    if len(genoma1) != len(genoma2):
        print("ERROR: Genomas de diferente longitud")
        return
    longitud = len(genoma1)
    corte1 = randint(0,longitud)
    corte2 = randint(0,longitud)
    if corte2 < corte1:
        corte1, corte2 = corte2, corte1
    ngenoma1 = [0 for _ in range(longitud)]
    ngenoma2 = [0 for _ in range(longitud)]

    ngenoma1[corte1:corte2] = genoma1[corte1:corte2]
    for i in genoma2:
        if i not in ngenoma1:
            ngenoma1[ngenoma1.index(0)] = i

    ngenoma2[corte1:corte2] = genoma2[corte1:corte2]
    for i in genoma1:
        if i not in ngenoma2:
            ngenoma2[ngenoma2.index(0)] = i

    return mutacion(ngenoma1), mutacion(ngenoma2)

def mutacion( genoma ):
    longitud = len(genoma)
    if choices([0,1], weights = [1,9])[0] == 1:
        mutacion1 = randint(0,longitud-1)
        mutacion2 = randint(0,longitud-1)
        genoma[mutacion1], genoma[mutacion2] = genoma[mutacion2], genoma[mutacion1]
    return genoma

def obtenerFenotipo( genoma ):
    fenotipo = 0
    longitud = len(genoma) - 1
    for i in range(len(genoma)):
        fenotipo += genoma[i]*2**(longitud-i)
    return fenotipo

def evolucion(generaciones = 50, tampob = 4, longitud = 8):
    poblacion = crearPoblacion(tampob, longitud)
    for _ in range(generaciones):
        nuevapoblacion = seleccion(poblacion, reproduccion(poblacion))
        poblacion = nuevapoblacion
    fenotipoPob = [(fitness(x), x) for x in nuevapoblacion]
    #print(fenotipoPob)
    elmejor = max(fenotipoPob)
    return elmejor

# Main Function
if __name__ == '__main__':
    bestgenoma = evolucion(500,4,20)
    print(bestgenoma)
    cadena = bestgenoma[1]
    table= []
    longitud = len(cadena)
    for x in range(longitud):
        table.append(["."]*longitud)

    for i in range(longitud):
        table[longitud-cadena[i]][i]="Q"

    for row in table:
            print(" ".join(row))
    # genoma = [1,2,3,4,5,6,7,8]
    # print(fitness(genoma))
    # genoma = [8,7,6,5,4,3,2,1]
    # print(fitness(genoma))
