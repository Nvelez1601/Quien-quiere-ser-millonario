# Juego basico de "QUIEN QUIERE SER MILLONARIO" modulo de base de datos
# Fecha: 10/06/2024                      
# Programador: Nelson Velez              
# ID: 30114798                       
# Version: 0.3.4                          
# Actualizacion: 17/06/2024

import sqlite3

class BaseDeDatosJugadores:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.conexion = sqlite3.connect(nombre_archivo)
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS jugadores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                dinero_ganado INTEGER,
                dificultad TEXT
            )
        ''')
        self.conexion.commit()

    def agregar_jugador(self, nombre, dinero_ganado, dificultad):
        self.cursor.execute("INSERT INTO jugadores (nombre, dinero_ganado, dificultad) VALUES (?, ?, ?)",
                            (nombre, dinero_ganado, dificultad))
        self.conexion.commit()  # Realizar commit para guardar los cambios

    def obtener_jugadores_ordenados(self):
        self.cursor.execute("SELECT * FROM jugadores ORDER BY dinero_ganado DESC")
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.conexion.close()
