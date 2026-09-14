#SESIÓN 2 — MOTOR DE INFERENCIA Y MODUS PONENS
#Taller 2 Traza de Inferencia

#Taller Laboratorio - Motor de Fraude Bancario
#Sistema de Detección de Fraude
#Base Inicial de Hechos

Hechos = {
    "monto": 7500,
    "pais extranjero": True,
    "compra_nocturna": True,
    "multiples_intentos": False
}

#Base de Reglas
reglas = [
    {"id": "R1", "condiciones": {"monto_alto": True}, "conclusion": {"transaccion_inusual": True}},
    {"id": "R2", "condiciones": {"transaccion_inusual": True, "pais extranjero": True}, "conclusion": {"bloquear_tarjeta": True}},
    {"id": "R3", "condiciones": {"compra_nocturna": True, "monto_alto": True}, "conclusion": {"alerta_seguridad": True}},
    {"id": "R4", "condiciones": {"bloquear_tarjeta": True, "alerta_seguridad": True}, "conclusion": {"notificar_cliente": True}},
]

#Regla del Monto Basicamente Si el Monto es Mayor a 5000 entonces es un Monto Alto
if Hechos["monto"] > 5000:
    Hechos["monto_alto"] = True
else:
    Hechos["monto_alto"] = False

#Motor de Inferencia
nuevos_hechos = True
while nuevos_hechos:
    nuevos_hechos = False
    for regla in reglas:
        #El operador all() es el que toma la el papel de Puerta Logica AND
        #Todas las Normas (Norman Onsborn) tengo sueño deben cumplirse simultaneamente
        condiciones_cumplidas = all(Hechos.get(condicion, False) == valor for condicion, valor in regla["condiciones"].items())

        if condiciones_cumplidas:
            for clave, valor in regla["conclusion"].items():
                if clave not in Hechos:
                    Hechos[clave] = valor
                    nuevos_hechos = True
                    print(f"Disparando {regla['id']} -> Nuevo hecho: {clave}={valor}")

print("\nHechos final:", Hechos)







    

