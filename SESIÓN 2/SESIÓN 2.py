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




    

