import tkinter as tk
from tkinter import Tk, ttk  # Importar ttk para Treeview
from controllers.controllerInicio import Controlador  # Asegurarse de que el controlador esté en su lugar

class Interfaz:

    expresion_regular = ""
    lista_cadenas = list()

    def __init__(self):
        root = Tk()
        self.root = root
        self.root.title("Inicio")

        # Primera parte
        
        #Primer punto: Entrada de Expresión Regular
        self.expresion_regular_label = tk.Label(self.root, text="Introduce la expresion regular:")
        self.expresion_regular_label.pack()

        self.expresion_regular_tf = tk.Entry(self.root)
        self.expresion_regular_tf.pack()

        self.guardar_expresion_regular = tk.Button(self.root, text="Guardar expresion regular", command=self.evento_guardar_expresion_regular)
        self.guardar_expresion_regular.pack()

        self.expresion_regular_label = tk.Label(self.root, text="")
        self.expresion_regular_label.pack()



        #Segunda punto: Entrada de Cadenas

        # Crear el Treeview (usamos ttk.Treeview)
        self.tree = ttk.Treeview(self.root, columns=("Cadena"), show="headings")
        self.tree.heading("Cadena", text="Cadena")
        self.tree.pack(pady=10)

        # Botón para agregar un nuevo nombre
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


        #Tercer punto: Botón de Validación
        self.validar_cadena_bt = tk.Button(self.root, text="Validar cadenas",command=self.evento_validar)
        self.add_button.pack(pady=5)

        #Cuarto punto:
        self.resultado_label = tk.Label(self.root, text="")
        self.resultado_label.pack()

        # Controlador
        self.controlador = Controlador(self)


    #Boton para guardar la expresion regular
    def evento_guardar_expresion_regular(self):
        self.expresion_regular = self.expresion_regular_tf.get()
        self.expresion_regular_label.config(text=self.expresion_regular)
        

    def evento_validar():
        print("evalua")        
    
    
    def actualizar_resultado(self, texto):
        self.resultado_label.config(text=texto)






    '''
        Tabla
    '''
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
        # Obtener el elemento seleccionado
        seleccionado = self.tree.selection()
        if seleccionado:
            # Obtener el valor de la columna seleccionada
            cadena = self.tree.item(seleccionado[0], 'values')[0]
            self.lista_cadenas.remove(cadena)  # Eliminar de la lista
            self.actualizar_tabla()  # Actualizar la tabla


    #Metodo para mostrar 
    def mostrar(self):
        self.root.mainloop()