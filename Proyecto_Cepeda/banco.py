# banco.py
# Juego basico de "QUIEN QUIERE SER MILLONARIO" modulo con repertorio de preguntas
# Fecha: 15/03/2024                      
# Programador: Nicolaz Blanco             
# ID: 30114798                       
# Version: 0.2.1                          
# Actualizacion: 04/04/2024
class Preguntas:
    def __init__(self, pregunta, opciones, respuesta_correcta):
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
        self.opciones_originales = opciones.copy()

    def resetear_opciones(self):
        self.opciones = self.opciones_originales.copy()

pregunta_facil = [
    Preguntas(
        "¿Cuál es la capital de Francia?\n",
        ["a) Madrid", "b) París", "c) Roma", "d) Londres"],
        "b"
    ),
    Preguntas(
        "¿Cuál es la capital de España?\n",
        ["a) Madrid", "b) París", "c) Roma", "d) Londres"],
        "a"
    ),
    Preguntas(
        "¿Cuál es la capital de Italia?\n",
        ["a) Madrid", "b) París", "c) Roma", "d) Londres"],
        "c"
    ),
    Preguntas(
        "¿Cuál es la capital de Inglaterra?\n",
        ["a) Madrid", "b) París", "c) Roma", "d) Londres"],
        "d"
    ),
]

pregunta_medio = [
    Preguntas(
        "¿Qué tipo de enlace se forma entre el sodio y el cloro?\n",
        ["a) Enlace covalente", "b) Enlace iónico", "c) Enlace metálico", "d) Enlace de hidrógeno"],
        "b"
    ),
    Preguntas(
        "¿Cuál es la fórmula química del agua?\n",
        ["a) CO2", "b) NaCl", "c) H2O", "d) CH4"],
        "c"
    ),
    Preguntas(
        "Una bombilla de 60 W se deja encendida durante 1 hora. ¿Cuánta energía eléctrica consume?\n",
        ["a) 360 Wh", "b) 720 Wh", "c) 1080 Wh", "d) 1440 Wh"],
        "a"
    ),
    Preguntas(
        "Si tengo 12 manzanas y las reparto en partes iguales entre 4 personas, ¿cuántas manzanas recibe cada persona?\n",
        ["a) 2 manzanas", "b) 3 manzanas", "c) 4 manzanas", "d) 5 manzanas"],
        "c"
    ),
]

pregunta_dificil = [
    Preguntas(
        "Un resorte se comprime 10 cm. ¿Qué energía potencial elástica se almacena?\n",
        ["a) 5 J", "b) 10 J", "c) 15 J", "d) 20 J"],
        "c"
    ),
    Preguntas(
        "Si un cuerpo se mueve con una velocidad de 10 m/s y una masa de 5 kg, ¿cuál es su energía cinética?\n",
        ["a) 25 J", "b) 50 J", "c) 75 J", "d) 100 J"],
        "b"
    ),
    Preguntas(
        "¿Cuál es la fórmula para calcular el trabajo realizado por una fuerza constante?\n",
        ["a) W = F * d * cos(θ)", "b) W = F * d * sin(θ)", "c) W = F * d", "d) W = F / d"],
        "a"
    ),
    Preguntas(
        "¿Cuál es la fórmula para calcular la potencia?\n",
        ["a) P = W / t", "b) P = W * t", "c) P = W + t", "d) P = W - t"],
        "a"
    ),
]
