# Juego basico de "QUIEN QUIERE SER MILLONARIO" modulo con funcionamiento de comodines 
# Fecha: 15/03/2024                      
# Programador: Nicolaz Blanco, Nelson Velez            
# ID: 30114798                       
# Version: 0.3.5                         
# Actualizacion: 04/04/2024
import random
comodin_50_usado = 0
def usar_comodin_50(pregunta): 
    global comodin_50_usado
    if comodin_50_usado < 1:
        incorrectas = [opcion for opcion in pregunta.opciones if opcion[0] != pregunta.respuesta_correcta]
        eliminar = random.sample(incorrectas, 2)
        pregunta.opciones = [opcion for opcion in pregunta.opciones if opcion not in eliminar]
        comodin_50_usado += 1
    else:
        print("El comodín 50/50 ya ha sido usado.")

comodin_respuesta_usado = 0
def usar_comodin_respuesta(pregunta):
    global comodin_respuesta_usado
    if comodin_respuesta_usado < 1:
        print(f"La respuesta correcta es: {pregunta.respuesta_correcta}")
        comodin_respuesta_usado += 1
    else:
        print("El comodín de respuesta ya ha sido usado.")

def resetear_comodines():
    global comodin_50_usado, comodin_respuesta_usado
    comodin_50_usado = 0
    comodin_respuesta_usado = 0