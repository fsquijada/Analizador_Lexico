class ConstructorOperaciones:
    def __init__ (self, lexema, tipo, columna, fila):
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna 
        self.fila = fila

class OperacionesAritmeticas:
    def __init__ (self):
        self.pilaOperaciones = []

    def operacionesIngresadas (self):
        for operacion in self.pilaOperaciones:
            print (operacion)