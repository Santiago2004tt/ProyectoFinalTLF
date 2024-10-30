from models.punto1 import model_punto_1 as p1

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

    def verificar_expresion_regular(exp_regular: str):
        return p1.es_regex_valida(exp_regular)
    
    def validar_cadena(cadena: str, exp_regular: str):
        return p1.validar_expresion(cadena, exp_regular)
