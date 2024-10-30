import re

class model_punto_1:
    def validar_expresion(cadena, expresion_regular):
    # Compilar la expresión regular para mejorar el rendimiento en validaciones múltiples
        patron = re.compile(expresion_regular)
    # Buscar coincidencia en toda la cadena
        return bool(patron.fullmatch(cadena))

    def es_regex_valida(expresion):
        try:
            re.compile(expresion)  # Intenta compilar la expresión
            return True
        except re.error:
            return False


