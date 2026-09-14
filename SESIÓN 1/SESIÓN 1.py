#SESIÓN 1 — INTRODUCCIÓN A SISTEMAS EXPERTOS Y REPASO PYTHON 
#Taller 1 Logica Proposicional

#Taller Laboratorio - Sistemas de Diagnostico IT
#Help Desk?
#Diccionario

servidor_estado = {
"cpu_uso": 92, #%
"memoria_libre": 15, #%
"ping_respuesta": 320, #ms
"temperatura": 85, #C°
"ventilador_apagado": False,
"ventilador_encendido": True
}   

#Supuesto Motor de Inferencia

#Caso Temperatura Alta
#temperatura

def diagnosticar_servidor(Funcionamiento):
    if Funcionamiento ["temperatura"] > 80 and Funcionamiento ["ventilador_apagado "] == False:
        return "El servidor está en riesgo de sobrecalentamiento. Activar ventilador."


    # Caso Ping Alto Problemas de Red
    # ping_respuesta
    elif Funcionamiento["ping_respuesta"] > 1000:
        return "El servidor está experimentando problemas de red. Verificar la conexión."


    #Caso CPU Alto
    # cpu_uso
    elif Funcionamiento["cpu_uso"] > 90 and Funcionamiento["memoria_libre"] < 10:
        return "El servidor está experimentando alta carga de CPU y poca memoria libre. Considerar optimizar procesos."


    #Caso Memoria Baja 
    #memoria_libre
    elif Funcionamiento["memoria_libre"] < 10:
        return "El servidor tiene poca memoria libre. Considerar liberar espacio."

    #Caso Ventilador Apagado
    #ventilador_apagado
    elif Funcionamiento["ventilador_apagado"] == True:
        return "El ventilador del servidor está apagado. Activar ventilador para evitar sobrecalentamiento."    

    #Caso Ventilador Encendido
    #ventilador_encendido
    elif Funcionamiento["ventilador_encendido"] == True:    
        return "El ventilador del servidor está encendido y funcionando correctamente."

    

    #Caso Normal
    else:
        return "El servidor está funcionando dentro de los parámetros normales."    
 





