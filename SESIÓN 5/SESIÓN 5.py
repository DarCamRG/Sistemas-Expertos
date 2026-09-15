#SESIÓN 5 DEFUZZIFICACIÓN 
#Taller 5 defuzzificacion
#Centro de Gravedad

#Funcion COG implementacion Centroide
def centro_de_gravedad (x, curva):
    x = np.array(x, dtype=float)
    curva = np.array(curva, dtype=float)
    return np.sum(x * curva) / np.sum(curva)

