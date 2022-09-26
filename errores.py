class ConstructorError:
    def __init__ (self, lexema, tipo, columna, fila):
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna 
        self.fila = fila

class Error:
    def __init__ (self):
        self.listaErrores = []
    
    # Agrega un nuevo error a la lista de errores
    def NuevoError (self, lexema, tipo, columna, fila):
        nuevo = ConstructorError (lexema, tipo, columna, fila)
        self.listaErrores.append (nuevo)

    # Genera un reporte en formato HTML de los errores encontrados    
    def GenerarHtmlErrores (self):
        file = open ('C:\\Users\\fredy\\OneDrive\\Escritorio\\P1_202004812\\Reportes\\ERRORES_202004812.html', 'w', encoding='utf-8')
        file.write('<!DOCTYPE html>\n')
        file.write('<html lang=\"en\">\n')
        file.write('<head>\n')
        file.write('\t<meta charset="UTF-8">\n')
        file.write('\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
        file.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        file.write('\t<title>Errores</title>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('\t<div align="center">\n')
        file.write('\t\t<h1>Tabla de Errores</h1>\n')
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
        for error in self.listaErrores:
            file.write('\t\t<tr>\n')
            file.write(f'\t\t<td align="center">{contador}</td>\n')
            file.write(f'\t\t<td align="center">{error.lexema}</td>\n')
            file.write(f'\t\t<td align="center">{error.tipo}</td>\n')
            file.write(f'\t\t<td align="center">{error.columna}</td>\n')
            file.write(f'\t\t<td align="center">{error.fila}</td>\n')
            file.write('\t\t</tr>\n')
            contador += 1
        file.write('\t\t</table>\n')
        file.write('</body>\n')
        file.write('</html>\n')
        file.close()
    