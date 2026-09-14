#SESIÓN 3 - INCERTIDUMBRE Y LÓGICA DIFUSA 
#Taller 3 Logica Difusa Comerical

#Taller Laboratorio Logica Difusa Comerical
#Experiencia de Conductores

def membresia_triangular (x, a, b, c):
    if x <= a or x >= C:
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
    print