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

def diagnosticar_servidor(Funcionamiento):
    #Caso Temperatura Alta
    if Funcionamiento ["temperatura"] > 80 and Funcionamiento.get("ventilador_apagado", False) == True:
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


#-----------------------------------------------------------------------------------------------------

       

    print("Caso Normal")
    print("Diagnostico: El servidor está funcionando dentro de los parámetros normales. No se requiere acción adicional.")
    print(diagnosticar_servidor(servidor_estado))


    #Caso ping_respuesta
    print("Caso Problemas de Red")
    caso1 = {temperatura: 40, ventilador_apagado: False, ping_respuesta: 1500}
    print(diagnosticar_servidor(caso1))  

             
    #Caso cpu_uso y memoria_libre
    print("Caso CPU y Memoria")
    caso2 = {"temperatura": 40, "ventilador_apagado": False, "ping_respuesta": 50, "cpu_uso": 95, "memoria_libre": 5}
    print(diagnosticar_servidor(caso2)) 

    #Caso memoria_libre
    print("Caso Memoria Baja")
    caso3 = {"temperatura": 40, "ventilador_apagado": False, "ping_respuesta": 50, "cpu_uso": 50, "memoria_libre": 8}
    print(diagnosticar_servidor(caso3)) 

    #Caso ventilador_apagado
    print("Caso Ventilador Apagado")
    caso4 = {"temperatura": 90, "ventilador_apagado": True, "ping_respuesta": 50, "cpu_uso": 50, "memoria_libre": 15}
    print(diagnosticar_servidor(caso4)) 

    #Caso ventilador_encendido
    print("Caso Ventilador Encendido")
    caso5 = {"temperatura": 40, "ventilador_apagado": False, "ping_respuesta": 50, "cpu_uso": 50, "memoria_libre": 15, "ventilador_encendido": True}
    print(diagnosticar_servidor(caso5))

    #Caso Sobrecarga
    print("Caso Sobrecarga")
    Caso6 = {"temperatura": 90, "ventilador_apagado": True, "ping_respuesta": 1500, "cpu_uso": 95, "memoria_libre": 5}
    print(diagnosticar_servidor(Caso6))





