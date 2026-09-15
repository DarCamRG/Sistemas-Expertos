#SESIÓN 5 DEFUZZIFICACIÓN 
#Taller 5 defuzzificacion
#Centro de Gravedad

import numpy as np

#Funcion COG implementacion Centroide
def centro_de_gravedad (x, curva):
    x = np.array(x, dtype=float)
    curva = np.array(curva, dtype=float)
    return np.sum(x * curva) / np.sum(curva)

x_validacion = [10, 20, 30, 40]
mu_validacion = [0.2, 0.8, 0.8, 0.0]
resultado_validacion = centro_de_gravedad(x_validacion, mu_validacion)
print(f"Validacion debe ser igual al {resultado_validacion:.2f}")

#Escenario Sistemas de Frenado
#Eje X: fuerza de frenado (0 a 100 Newtons), 100 elementos

x_freando = np.linspace(0, 100, 100)

#Curva de Gas (gauss) 

sigma = 10
centro = 70
curva_frenado = np.exp(-((x_freando - centro) ** 2) / (2 * sigma ** 2 ))

#Aplicacion de la defuzzificacion mostrar la fuerza de frenado
fuerza_frenado = centro_de_gravedad(x_freando, curva_frenado)
print(f"Fuerza de frenado exacta calculada(crisp): {fuerza_frenado:.2f} Newtons")
