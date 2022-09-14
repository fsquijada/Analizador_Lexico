class ConstructorError:
    def __init__ (self, lexema, tipo, columna, fila):
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna 
        self.fila = fila

class Error:
    def __init__ (self):
        self.listaErrores = []
        
    def nuevoError (self, lexema, tipo, columna, fila):
        nuevo = ConstructorError (lexema, tipo, columna, fila)
        self.listaErrores.append (nuevo)

    def erroresIngresados (self):
        for error in self.listaErrores:
            print (f'{error.lexema}, {error.tipo}, {error.columna}, {error.fila}')
    