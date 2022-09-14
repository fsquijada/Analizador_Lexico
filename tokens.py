class ConstructorToken:
    def __init__ (self, lexema, tipo, columna, fila):
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna 
        self.fila = fila

class Token:
    def __init__ (self):
        self.listaTokens = []
        
    def nuevoToken (self, lexema, tipo, columna, fila):
        nuevo = ConstructorToken (lexema, tipo, columna, fila)
        self.listaTokens.append (nuevo)
        return True

    def tokensIngresados (self):
        for token in self.listaTokens:
            print (f'Lexema: {token.lexema}, Tipo: {token.tipo}, Columna: {token.columna}, Fila: {token.fila}')
        return True
    