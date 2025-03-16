# Juego basico de "QUIEN QUIERE SER MILLONARIO"
# Fecha: 07/03/2024                      
# Programador: Nelson Velez, Nicolaz Blanco, Abraham Paredes              
# ID: 30114798                       
# Version: 0.16.4                           
# Actualizacion: 17/06/2024
import tkinter as tk
from tkinter import Scrollbar, Text, messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
from basededatos import BaseDeDatosJugadores
import banco  # Importa las preguntas y respuestas
import funciones  # Importa las funciones para los comodines

class MillonarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("¿Quién quiere ser millonario?")
        self.root.configure(bg='#E0FFFF')  # Color de fondo aquamarina

        # Tamaño inicial de la ventana principal
        self.root.geometry("700x350")  # Ancho x Alto
        
        # Inicializar la base de datos de jugadores
        self.base_de_datos = BaseDeDatosJugadores('datos_jugadores.db')


        # Frame para el contenido principal
        self.frame_principal = tk.Frame(self.root, bg='#E0FFFF')  # Color de fondo aquamarina
        self.frame_principal.pack(expand=True, fill=tk.BOTH)  # Expandir y llenar la ventana

        self.nombre_jugador = tk.StringVar()
        self.dinero = 0
        self.dificultad = tk.StringVar(value="facil")

        self.comodin_50_usado = False
        self.comodin_respuesta_usado = False

        # Cargar y redimensionar las imágenes
        self.cargar_imagenes()

        self.setup_widgets()

    def cargar_imagenes(self):
        # Carga la imagen para el botón "Iniciar Juego"
        self.imagen_inicio = Image.open("web-button.png").resize((150, 50), Image.Resampling.LANCZOS)
        self.imagen_inicio = ImageTk.PhotoImage(self.imagen_inicio)

        # Carga la imagen para el botón "Puntaje"
        self.imagen_puntaje = Image.open("DB-button.png").resize((150, 50), Image.Resampling.LANCZOS)
        self.imagen_puntaje = ImageTk.PhotoImage(self.imagen_puntaje)
        
    def setup_widgets(self):
        # Frame para el formulario de nombre
        frame_nombre = tk.Frame(self.frame_principal, bg='#E0FFFF')  # Color de fondo aquamarina
        frame_nombre.pack(pady=50, padx=10)

        tk.Label(frame_nombre, text="¡Bienvenido a ¿Quién quiere ser millonario?!", font=("Comic Sans MS", 24), bg='#E0FFFF').pack(pady=10)
        tk.Label(frame_nombre, text="Por favor, ingresa tu nombre:", font=("Roboto", 16), bg='#E0FFFF').pack()

        # Campo de entrada para el nombre del jugador
        entry_nombre = tk.Entry(frame_nombre, textvariable=self.nombre_jugador, font=("Roboto", 14), width=30)
        entry_nombre.pack(pady=20)

        # Botón de Iniciar Juego con imagen ovalada
        btn_iniciar = tk.Button(frame_nombre, image=self.imagen_inicio, borderwidth=0, command=self.iniciar_juego)
        btn_iniciar.config(width=150, height=50)
        btn_iniciar.pack(padx=70,pady=10, side=tk.LEFT)
        
        # Botón para imprimir la base de datos
        btn_imprimir_bd = tk.Button(frame_nombre,image=self.imagen_puntaje,borderwidth=0, command=self.imprimir_base_de_datos)
        btn_imprimir_bd.pack(padx=70,pady=10,side=tk.RIGHT)

    def iniciar_juego(self):
        self.nombre = self.nombre_jugador.get()
        if not self.nombre:
            messagebox.showwarning("Advertencia", "Por favor ingresa tu nombre.")
            return

        self.root.withdraw()  # Oculta la ventana principal

        self.juego_ventana = tk.Toplevel()
        self.juego_ventana.title(f"Bienvenido {self.nombre}")
        self.juego_ventana.configure(bg='#E0FFFF')  # Color de fondo aquamarina

        # Permitir que la ventana se expanda y se adapte
        self.juego_ventana.pack_propagate(False)  # Evita que el frame se ajuste al contenido automáticamente
        self.juego_ventana.geometry("800x600")  # Tamaño inicial del juego

        tk.Label(self.juego_ventana, text=f"Hola {self.nombre}, elige la dificultad:", font=("Roboto", 18), bg='#E0FFFF').pack(pady=20)

        # Botones para seleccionar la dificultad
        btn_facil = tk.Button(self.juego_ventana, text="Fácil", font=("Roboto", 16), bg='#87CEEB', command=lambda: self.comenzar_juego("facil"))
        btn_facil.config(width=15)
        btn_facil.pack(pady=10)

        btn_medio = tk.Button(self.juego_ventana, text="Medio", font=("Roboto", 16), bg='#87CEEB', command=lambda: self.comenzar_juego("medio"))
        btn_medio.config(width=15)
        btn_medio.pack(pady=10)

        btn_dificil = tk.Button(self.juego_ventana, text="Difícil", font=("Roboto", 16), bg='#87CEEB', command=lambda: self.comenzar_juego("dificil"))
        btn_dificil.config(width=15)
        btn_dificil.pack(pady=10)

    def comenzar_juego(self, dificultad):
        self.dificultad.set(dificultad)  # Actualiza la variable de control de la dificultad
        if dificultad == "facil":
            self.juego = banco.pregunta_facil.copy()
        elif dificultad == "medio":
            self.juego = banco.pregunta_medio.copy()
        elif dificultad == "dificil":
            self.juego = banco.pregunta_dificil.copy()
        else:
            messagebox.showerror("Error", "Dificultad no válida.")
            return

        self.jugar_ronda()

    def jugar_ronda(self):
        if not self.juego:
            self.mostrar_resultados()
            return

        self.pregunta_actual = self.juego.pop(0)
        self.mostrar_pregunta(self.pregunta_actual)

    def mostrar_pregunta(self, pregunta):
        if hasattr(self, 'pregunta_ventana'):
            self.pregunta_ventana.destroy()

        self.pregunta_ventana = tk.Toplevel(self.juego_ventana)
        self.pregunta_ventana.title("Pregunta")
        self.pregunta_ventana.configure(bg='#E0FFFF')  # Color de fondo aquamarina

        tk.Label(self.pregunta_ventana, text=pregunta.pregunta, font=("Roboto", 18), bg='#E0FFFF').pack(pady=20)

        for opcion in pregunta.opciones:
            tk.Button(self.pregunta_ventana, text=opcion, font=("Roboto", 14), bg='#87CEEB', width=30, command=lambda o=opcion: self.verificar_respuesta(o)).pack(pady=10)

        tk.Button(self.pregunta_ventana, text="50/50", font=("Roboto", 16), bg='#FFA500', command=self.usar_comodin_50).pack(pady=10)
        tk.Button(self.pregunta_ventana, text="Respuesta", font=("Roboto", 16), bg='#FFA500', command=self.usar_comodin_respuesta).pack(pady=10)

    def verificar_respuesta(self, respuesta):
        if respuesta.startswith(self.pregunta_actual.respuesta_correcta):
            self.dinero += 500
            messagebox.showinfo("Correcto", f"¡Respuesta correcta! Tienes {self.dinero}$.")
        else:
            messagebox.showinfo("Incorrecto", "Respuesta incorrecta. Fin del juego.")
            self.mostrar_resultados()
            return

        self.pregunta_ventana.destroy()
        self.jugar_ronda()

    def usar_comodin_50(self):
        if not self.comodin_50_usado:
            funciones.usar_comodin_50(self.pregunta_actual)
            self.comodin_50_usado = True
            self.mostrar_pregunta(self.pregunta_actual)
        else:
            messagebox.showwarning("Advertencia", "Ya has usado el comodín 50/50.")

    def usar_comodin_respuesta(self):
        if not self.comodin_respuesta_usado:
            self.respuesta_correcta = funciones.usar_comodin_respuesta(self.pregunta_actual)
            self.comodin_respuesta_usado = True
            messagebox.showinfo("Respuesta del Comodín", f"La respuesta correcta es: {self.respuesta_correcta}")
        else:
            messagebox.showwarning("Advertencia", "Ya has usado el comodín de respuesta.")

    def mostrar_resultados(self):
        messagebox.showinfo("Fin del juego", f"Has terminado el juego con {self.dinero}$. ¿Deseas volver a jugar?")
        
        # Reabrir la conexión antes de agregar el jugador
        self.base_de_datos = BaseDeDatosJugadores('datos_jugadores.db') 
        self.base_de_datos.cursor = self.base_de_datos.conexion.cursor()

        # Registrar jugador en la base de datos
        self.base_de_datos.agregar_jugador(self.nombre, self.dinero, self.dificultad.get())

        # Cerrar conexión después de agregar el jugador
        self.base_de_datos.cerrar_conexion()    # Registrar jugador en la base de datos

        # Crear un botón para volver a jugar
        btn_volver_a_jugar = tk.Button(self.juego_ventana, text="Volver a Jugar", font=("Roboto", 16), bg='#FFA500', command=self.reiniciar_juego)
        btn_volver_a_jugar.pack(pady=20)

    def reiniciar_juego(self):
        self.dinero = 0
        self.comodin_50_usado = False
        self.comodin_respuesta_usado = False

        self.juego_ventana.destroy()
        self.root.deiconify()  # Muestra la ventana principal nuevamente
        self.setup_widgets()  # Vuelve a configurar los widgets para comenzar un nuevo juego

    def imprimir_base_de_datos(self):
        # Crear una nueva ventana para mostrar la base de datos
        ventana_bd = tk.Toplevel(self.root)
        ventana_bd.title("Base de Datos - Jugadores")
        ventana_bd.configure(bg='#E0FFFF')  # Color de fondo aquamarina

        try:
            # Obtener jugadores ordenados por dinero ganado (de mayor a menor)
            jugadores = self.base_de_datos.obtener_jugadores_ordenados()

            # Crear un Text widget para mostrar los datos
            txt_jugadores = tk.Text(ventana_bd, font=("Roboto", 12), wrap=tk.WORD, height=20, width=80, bg='#FFFFFF')
            txt_jugadores.pack(padx=20, pady=20)

            # Agregar un scrollbar
            scrollbar = tk.Scrollbar(ventana_bd, command=txt_jugadores.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            txt_jugadores.config(yscrollcommand=scrollbar.set)

            # Mostrar los datos de los jugadores en el Text widget
            txt_jugadores.insert(tk.END, "----- Jugadores en la base de datos -----\n")
            for jugador in jugadores:
                txt_jugadores.insert(tk.END, f"ID: {jugador[0]}, Nombre: {jugador[1]}, Dinero Ganado: {jugador[2]}, Dificultad: {jugador[3]}\n")
            txt_jugadores.insert(tk.END, "-----------------------------------------\n")

        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener datos de la base de datos: {e}")

        finally:
            # Cerrar la conexión con la base de datos al cerrar la ventana
            ventana_bd.protocol("WM_DELETE_WINDOW", self.cerrar_conexion_bd)
            ventana_bd.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MillonarioApp(root)
    root.mainloop()
