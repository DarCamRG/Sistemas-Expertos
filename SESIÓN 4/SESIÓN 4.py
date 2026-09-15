#SESIÓN 4 INFERENCIA DIFUSA (MODELO MANDANI)
#Taller 4 Inferencia Difusa

#Taller laboratorio MotorLogicoRRHH
#Variables

desempeño_pobre = 0.1
desempeño_promedio = 0.5
desempeño_excelente = 0.85

antiguedad_corta = 0.2
antiguedad_larga = 0.6

#Motor 3 regla logica de MAX y MIN
def evaluar_reglas_bono():

    #R1 SI el desempeño es pobre o Antiguedad es Corta = Bono Bajo
    activacion_bono_bajo = max (desempeño_pobre, antiguedad_corta)

    #R2 SI el desempeño es Promedio = Bono Medio
    activacion_bono_medio = desempeño_promedio

    #R3 SI Desempeño es Excelente y Antiguedad es Larga = Bono Alto
    activacion_bono_alto = min(desempeño_excelente, antiguedad_larga)

    return{
        "BAJO": activacion_bono_bajo,
        "MEDIO": activacion_bono_medio,
        "ALTO": activacion_bono_alto
    }

#EJECUCION
resultado = evaluar_reglas_bono()
print ("Niveles de activacion para el bono", resultado)

#Agrecacion OR MAX
#Reglas distintas concluyen "Bono Alto" 0.4 0.7
#Agregacion de Mundano (Mamdani) tiene que si o si usar el maximo OR:

fuerza_r_a = 0.4
fuerza_r_b = 0.7
fuerza_final_bono_alto = max(fuerza_r_a, fuerza_r_b)
print("Fuerza Final Agregada Bono Alto: {fuerza_final_bono_alto}")

