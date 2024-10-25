class Controlador:


    def __init__(self, vista):
        self.vista = vista
        self.a ="" 

    def actualizar_label(self, texto):
        a = texto
        var = self
        # Puedes agregar lógica adicional aquí si lo necesitas.
        self.vista.actualizar_resultado(texto)

    def mostrar_texto(self,texto):
        self.vista.agregar_resultado(texto+": hola")