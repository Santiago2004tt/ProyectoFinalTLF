import tkinter as tk
from controllers.controllerInicio import Controlador

class Interfaz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ventana de Validación")

        # Crear widgets
        self.texto_label = tk.Label(self.root, text="Introduce el texto:")
        self.texto_label.pack()

        self.textfield = tk.Entry(self.root)
        self.textfield.pack()

        self.boton = tk.Button(self.root, text="Mostrar en Label", command=self.manejar_evento_boton)
        self.boton.pack()

        self.resultado_label = tk.Label(self.root, text="")
        self.resultado_label.pack()

        self.nuevo_label = tk.Label(self.root, text="")
        self.nuevo_label.pack()

        # Controlador
        self.controlador = Controlador(self)

    def manejar_evento_boton(self):
        texto = self.textfield.get()
        self.controlador.actualizar_label(texto)
        self.controlador.mostrar_texto()

    def mostrar(self):
        self.root.mainloop()
    
    def actualizar_resultado(self, texto):
        self.resultado_label.config(text=texto)

    def agregar_resultado(self, texto):
        self.nuevo_label.config(text=texto)
