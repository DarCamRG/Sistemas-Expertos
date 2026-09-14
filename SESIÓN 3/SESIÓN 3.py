#SESIÓN 3 - INCERTIDUMBRE Y LÓGICA DIFUSA 
#Taller 3 Logica Difusa Comerical

#Taller Laboratorio Logica Difusa Comerical
#Experiencia de Conductores

def membresia_triangular (x, a, b, c):

    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b -a)
    elif b < x < c:
        return (c - x) / (c - b)

#Def. 3 Conjuntos difusos

conjuntos = {
    "Novato":       (0, 0, 5),
    "Intermedio":   (2, 5, 8),
    "Experto":      (5, 10, 20)
}

conductores = [3, 6, 12]

for anios in conductores:
    print ("Conductor con {anios} años de experiencia:")
    grados = {}
    for categoria, (a, b, c) in conjuntos.items():
        grado = membresia_triangular(anios, a, b, c)
        grados[categoria] = grado
        print ("- {categoria}: {grado:.3f}")

#Determinacion algoritmica de mayor grado

categoria_ganadora = max(grados, key=grados.get)
print("Categoria Dominante: {categoria_ganadora} (grado {grados[categoria_ganadora]})")