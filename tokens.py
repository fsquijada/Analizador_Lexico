class ConstructorToken:
    def __init__ (self, lexema, tipo, columna, fila):
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna 
        self.fila = fila

class Token:
    def __init__ (self):
        self.listaTokens = []
    
    # Agrega un nuevo Token al listado
    def NuevoToken (self, lexema, tipo, columna, fila):
        nuevo = ConstructorToken (lexema, tipo, columna, fila)
        self.listaTokens.append (nuevo)

    # Genera un reporte en formato HTML de los tokens encontrados
    def GenerarHtmlTokens (self):
        file = open ('Reportes\TOKENS_202004812.html', 'w', encoding='utf-8')
        file.write('<!DOCTYPE html>\n')
        file.write('<html lang=\"en\">\n')
        file.write('<head>\n')
        file.write('\t<meta charset="UTF-8">\n')
        file.write('\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
        file.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        file.write('\t<title>Tokens</title>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('\t<div align="center">\n')
        file.write('\t\t<h1>Tabla de Tokens</h1>\n')
        file.write('\t</div>')
        file.write('\t<table class="colapsado" border="1" align="center">\n')
        file.write('\t\t<tr>\n')
        file.write('<td align="center">Numero</td>\n')
        file.write('<td align="center">Lexema</td>\n')
        file.write('<td align="center">Tipo</td>\n')
        file.write('<td align="center">Columna</td>\n')
        file.write('<td align="center">Fila</td>\n')
        file.write('\t\t</tr>\n')
        contador = 1
        for token in self.listaTokens:
            file.write('\t\t<tr>\n')
            file.write(f'\t\t<td align="center">{contador}</td>\n')
            file.write(f'\t\t<td align="center">{token.lexema}</td>\n')
            file.write(f'\t\t<td align="center">{token.tipo}</td>\n')
            file.write(f'\t\t<td align="center">{token.columna}</td>\n')
            file.write(f'\t\t<td align="center">{token.fila}</td>\n')
            file.write('\t\t</tr>\n')
            contador += 1
        file.write('\t\t</table>\n')
        file.write('</body>\n')
        file.write('</html>\n')
        file.close()
    