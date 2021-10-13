from random import choices, randrange, choice

def fitness(fenotipo):
    x = fenotipo
    f = -x**4 + 3*x**3 + 8*x + 2
    return f

def crearGenotipo( longitud = 5 ):
    return choices([0,1], k=longitud)

def crearPoblacion( tamano = 4 ):
    return [crearGenotipo() for _ in range(tamano)]

def reproduccion(poblacion):
    ruleta = [fitness(obtenerFenotipo(genoma)) for genoma in poblacion]
    nuevapoblacion = []
    for _ in range(int(len(poblacion)/2)):
        genoma1, genoma2 = choices(poblacion, weights = ruleta, k=2)
        nuevapoblacion += cruza(genoma1, genoma2)
    return nuevapoblacion

def seleccion(poblacionvieja, poblacionnueva):
    poblaciontotal = poblacionnueva + poblacionvieja
    fenotipoPob = [(fitness(obtenerFenotipo(x)), x) for x in poblaciontotal]
    fenotipoPob.sort()
    fenotipoPob.reverse()
    mejorpoblacion = [fenotipoPob[x][1] for x in range(len(fenotipoPob)) if x<4]
    return mejorpoblacion

def cruza(genoma1, genoma2):
    if len(genoma1) != len(genoma2):
        print("ERROR: Genomas de diferente longitud")
        return
    longitud = len(genoma1)
    indiceCruza = randrange(1,longitud,1)
    ngenoma1 = genoma1[0:indiceCruza] + genoma2[indiceCruza:longitud]
    ngenoma2 = genoma2[0:indiceCruza] + genoma1[indiceCruza:longitud]
    return mutacion(ngenoma1), mutacion(ngenoma2)

def mutacion( genoma ):
    longitud = len(genoma)
    if choices([0,1], weights = [1,9])[0] == 1:
        mutacion = randrange(0,longitud,1)
        genoma[mutacion] = abs(genoma[mutacion]-1)
    return genoma

def obtenerFenotipo( genoma ):
    fenotipo = 0
    longitud = len(genoma) - 1
    for i in range(len(genoma)):
        fenotipo += genoma[i]*2**(longitud-i)
    return fenotipo

def evolucion(generaciones = 20):
    poblacion = crearPoblacion()
    for _ in range(generaciones):
        nuevapoblacion = seleccion(poblacion, reproduccion(poblacion))
        poblacion = nuevapoblacion
    fenotipoPob = [(fitness(obtenerFenotipo(x)), x) for x in nuevapoblacion]
    elmejor = max(fenotipoPob)
    return elmejor

# Main Function
if __name__ == '__main__':
    print(evolucion())
