import tkinter as tk
from tkinter import Tk, ttk
from controllers.controllerInicio import Controlador

class Interfaz:

    expresion_regular = ""
    is_exp_regular = False
    lista_cadenas = list()

    def __init__(self):
        root = Tk()
        self.root = root
        self.root.title("Inicio")

        # Primera parte: Entrada de Expresión Regular
        self.expresion_regular_label = tk.Label(self.root, text="Introduce la expresión regular:")
        self.expresion_regular_label.pack()

        self.expresion_regular_tf = tk.Entry(self.root)
        self.expresion_regular_tf.pack()

        self.guardar_expresion_regular = tk.Button(self.root, text="Guardar expresión regular", command=self.evento_guardar_expresion_regular)
        self.guardar_expresion_regular.pack()

        self.expresion_regular_label = tk.Label(self.root, text="")
        self.expresion_regular_label.pack()

        # Segunda parte: Entrada de Cadenas
        self.tree = ttk.Treeview(self.root, columns=("Cadena"), show="headings")
        self.tree.heading("Cadena", text="Cadena")
        self.tree.pack(pady=10)

        # Botón para agregar una nueva cadena
        self.add_entry_label = tk.Label(self.root, text="Nueva cadena:")
        self.add_entry_label.pack(pady=5)
        
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Agregar", command=self.agregar_cadena)
        self.add_button.pack(pady=5)

        # Botón para eliminar
        self.delete_button = tk.Button(self.root, text="Eliminar seleccionado", command=self.eliminar_seleccionado)
        self.delete_button.pack(pady=10)

        # Llenar la tabla con los datos de la lista
        self.actualizar_tabla()

        # Botón de Validación
        self.validar_cadena_bt = tk.Button(self.root, text="Validar cadenas", command=self.evento_validar)
        self.validar_cadena_bt.pack(pady=5)

        # Evento de selección en el Treeview
        self.tree.bind('<<TreeviewSelect>>', self.validar_seleccion)

        # Resultado
        self.resultado_label = tk.Label(self.root, text="")
        self.resultado_label.pack()

        # Controlador
        self.controlador = Controlador(self)

    # Botón para guardar la expresión regular
    def evento_guardar_expresion_regular(self):
        self.expresion_regular = self.expresion_regular_tf.get()
        if Controlador.verificar_expresion_regular(self.expresion_regular):
            self.is_exp_regular = True
            self.expresion_regular_label.config(text=self.expresion_regular)
        else:
            self.is_exp_regular = False
            self.expresion_regular_label.config(text="Expresión no válida")

    def evento_validar(self):
        if self.is_exp_regular:
            for item in self.tree.get_children():
                cadena = self.tree.item(item, 'values')[0]
                es_valida = Controlador.validar_cadena(cadena, self.expresion_regular)
                
                # Cambiar color de fondo según si la cadena es válida o no
                if es_valida:
                    self.tree.item(item, tags=('valido',))
                else:
                    self.tree.item(item, tags=('invalido',))

            # Aplicar estilos para colores de fondo
            self.tree.tag_configure('valido', background='lightgreen')
            self.tree.tag_configure('invalido', background='lightcoral')

    def validar_seleccion(self, event):
        if self.is_exp_regular:
            seleccionado = self.tree.selection()
            if seleccionado:
                cadena = self.tree.item(seleccionado[0], 'values')[0]
                if Controlador.validar_cadena(cadena, self.expresion_regular):
                    self.resultado_label.config(text=f"{cadena} es válido", fg="green")
                else:
                    self.resultado_label.config(text=f"{cadena} no es válido", fg="red")

    def actualizar_tabla(self):
        # Limpiar la tabla antes de insertar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)
        # Insertar los elementos de la lista en el Treeview
        for nombre in self.lista_cadenas:
            self.tree.insert("", tk.END, values=(nombre,))

    def agregar_cadena(self):
        nueva_cadena = self.entry.get()
        if nueva_cadena:
            self.lista_cadenas.append(nueva_cadena)
            self.entry.delete(0, tk.END)  # Limpiar el campo de entrada
            self.actualizar_tabla()  # Actualizar la tabla

    def eliminar_seleccionado(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            cadena = self.tree.item(seleccionado[0], 'values')[0]
            self.lista_cadenas.remove(cadena)  # Eliminar de la lista
            self.actualizar_tabla()  # Actualizar la tabla

    def mostrar(self):
        self.root.mainloop()
