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
    
#Caso Ping Alto Problemas de Red
#ping_respuesta


