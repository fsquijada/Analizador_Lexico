import math
import re
# Constructor de las operaciones que se realizan
class ConstructorOperaciones:
    def __init__ (self, operacion, resultado):
        self.operacion = operacion
        self.resultado = resultado
# Métodos de todas las operaciones
class OperacionesAritmeticas:
    def __init__ (self):
        self.pilaOperaciones = []
        self.resultados = []
        self.contador = 0
        self.texto = ''
        self.error = False

    # Método para operar los números y operaciones que fueron ingresados a la pila
    def ReporteOperaciones (self, titulo, texto, arreglo):
        self.texto = ''
        self.contador = 0
        while self.contador < (len (self.pilaOperaciones)-1):
            dato = self.pilaOperaciones [self.contador]
            if dato == 'SUMA' or dato == 'RESTA' or dato == 'MULTIPLICACION' or dato == 'DIVISION' or dato == 'POTENCIA' or dato == 'RAIZ' or dato == 'INVERSA' or dato == 'SENO' or dato == 'COSENO' or dato == 'TANGENTE' or dato == 'MOD':
                self.texto += '('
                resultado = self.Lados (dato)
            if self.error == False:
                nuevo = ConstructorOperaciones (self.texto, resultado)
            else:
                nuevo = ConstructorOperaciones (self.texto, 'Error')
            self.resultados.append (nuevo)
            self.texto = ''
            self.contador += 1
            self.error = False
        self.pilaOperaciones = []
        self.GenerarResultados (titulo, texto, arreglo)

    # Opera ambos lados de las ecuaciones
    def Lados (self, dato):
        self.contador += 1
        ladoIzquierdo = self.pilaOperaciones[self.contador]
        auxiliar = ladoIzquierdo
        # Valida si el dato es un número o una operación
        if ladoIzquierdo == 'SUMA' or ladoIzquierdo == 'RESTA' or ladoIzquierdo == 'MULTIPLICACION' or ladoIzquierdo == 'DIVISION' or ladoIzquierdo == 'POTENCIA' or ladoIzquierdo == 'RAIZ' or ladoIzquierdo == 'INVERSA' or ladoIzquierdo == 'SENO' or ladoIzquierdo == 'COSENO' or ladoIzquierdo == 'TANGENTE' or ladoIzquierdo == 'MOD':
            self.texto += '('
            ladoIzquierdo = self.Lados (ladoIzquierdo)
        else:
            # Verifica que sea una operación que necesite solo un número
            if dato == 'INVERSA':
                self.texto += f'Inv({ladoIzquierdo}))'
                if ladoIzquierdo != 0:
                    operacion = 1/ladoIzquierdo
                else:
                    operacion = 0
                    self.error = True
                return operacion
            elif dato == 'SENO':
                self.texto += f'sen({ladoIzquierdo}))'
                operacion = math.sin(ladoIzquierdo)
                return operacion
            elif dato == 'COSENO':
                self.texto += f'cos({ladoIzquierdo}))'
                operacion = math.cos(ladoIzquierdo)
                return operacion
            elif dato == 'TANGENTE':
                self.texto += f'tan({ladoIzquierdo}))'
                auxiliar = str(ladoIzquierdo)
                if re.search('[\.][0-9]*[1-9]+[0-9]*', auxiliar) or ladoIzquierdo < 0:
                    operacion = math.tan(ladoIzquierdo)
                else:
                    operacion = 0
                    self.error = True
                return operacion
            # Revisa que sea el dato no operado para agregarlo al texto
            if auxiliar == ladoIzquierdo:
                self.texto += f'{ladoIzquierdo}'
        self.contador += 1
        ladoDerecho = self.pilaOperaciones[self.contador]
        auxiliar = ladoDerecho
        # Esta sección es únicamente para colocar el signo al texto de la operación
        if dato == 'INVERSA':
            self.texto += ' inv '
        elif dato == 'SENO':
            self.texto += ' sen '
        elif dato == 'COSENO':
            self.texto += ' cos '
        elif dato == 'TANGENTE':
            self.texto += ' tan '
        elif dato == 'SUMA':
            self.texto += ' + '
        elif dato == 'RESTA':
            self.texto += ' - '
        elif dato == 'MULTIPLICACION':
            self.texto += ' * '
        elif dato == 'DIVISION':
            self.texto += ' / '
        elif dato == 'POTENCIA':
            self.texto += ' ^ '
        elif dato == 'RAIZ':
            self.texto += ' raiz '
        elif dato == 'MOD':
            self.texto += ' % '
        # A partir de esta sección comienza el lado derecho de la operación
        if ladoDerecho == 'SUMA' or ladoDerecho == 'RESTA' or ladoDerecho == 'MULTIPLICACION' or ladoDerecho == 'DIVISION' or ladoDerecho == 'POTENCIA' or ladoDerecho == 'RAIZ' or ladoDerecho == 'INVERSA' or ladoDerecho == 'SENO' or ladoDerecho == 'COSENO' or ladoDerecho == 'TANGENTE' or ladoDerecho == 'MOD':
            self.texto += '('
            ladoDerecho = self.Lados (ladoDerecho)
        # Revisa que sea el dato no operado para agregarlo al texto
        if auxiliar == ladoDerecho:
            self.texto += f'{ladoDerecho}'
        # if dato == 'INVERSA':
        #     operacion = 1/ladoDerecho
        #     return operacion
        # elif dato == 'SENO':
        #     operacion = sin(ladoDerecho)
        #     return operacion
        # elif dato == 'COSENO':
        #     operacion = cos(ladoDerecho)
        #     return operacion
        # elif dato == 'TANGENTE':
        #     operacion = tan(ladoDerecho)
        #     return operacion
        self.texto += ')'
        # Operaciones entre el lado izquierdo y el lado derecho
        if dato == 'SUMA':
            operacion = ladoIzquierdo + ladoDerecho
            return operacion
        elif dato == 'RESTA':
            operacion = ladoIzquierdo - ladoDerecho
            return operacion
        elif dato == 'MULTIPLICACION':
            operacion = ladoIzquierdo * ladoDerecho
            return operacion
        elif dato == 'DIVISION':
            if ladoDerecho != 0:
                operacion = ladoIzquierdo / ladoDerecho
            else:
                operacion = 0
                self.error = True
            return operacion
        elif dato == 'POTENCIA':
            operacion = ladoIzquierdo ** ladoDerecho
            return operacion
        elif dato == 'RAIZ':
            if ladoDerecho != 0:
                operacion = ladoIzquierdo ** (1/ladoDerecho)
            else:
                operacion = 0
                self.error = True
            return operacion
        elif dato == 'MOD':
            if ladoDerecho != 0:
                operacion = ladoIzquierdo % ladoDerecho
            else:
                operacion = 0
                self.error = True 
            return operacion

    # Método para generar resultados
    def GenerarResultados (self, titulo, texto, arreglo):
        # Primero cambia los valores de los colores
        contador = 0
        while contador < len(arreglo):
            if arreglo[contador] == 'ROJO':
                arreglo[contador] = '#FF0000'
            elif arreglo[contador] == 'AMARILLO':
                arreglo[contador] = '#FFFF00'
            elif arreglo[contador] == 'AZUL':
                arreglo[contador] = '#0000FF'
            elif arreglo[contador] == 'VERDE':
                arreglo[contador] = '#008000'
            elif arreglo[contador] == 'NARANJA' or arreglo[contador] == 'ANARANJADO':
                arreglo[contador] = '#FFA500'
            elif arreglo[contador] == 'BLANCO':
                arreglo[contador] = '#000000'
            elif arreglo[contador] == 'FUSIA':
                arreglo[contador] = '#FF00FF'
            elif arreglo[contador] == 'AQUA':
                arreglo[contador] = '#00FFFF'
            elif arreglo[contador] == 'CAFE':
                arreglo[contador] = '#A52A2A'
            elif arreglo[contador] == 'MORADO':
                arreglo[contador] = '#800080'
            elif arreglo[contador] == 'GRIS':
                arreglo[contador] = '#808080'
            elif arreglo[contador] == 'CYAN':
                arreglo[contador] = '#00FFFF'
            elif arreglo[contador] == 'ROSADO':
                arreglo[contador] = '#FFC0CB'
            else: # Si no es ninguna de las anteriores que coloque negro
                arreglo[contador] = '#FFFFFF'
            contador = contador + 2            
        file = open ('Reportes\RESULTADOS_202004812.html', 'w', encoding='utf-8')
        file.write('<!DOCTYPE html>\n')
        file.write('<html lang=\"en\">\n')
        file.write('<head>\n')
        file.write('\t<meta charset="UTF-8">\n')
        file.write('\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
        file.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        file.write(f'\t<title>Archivo de salida</title>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('\t<div align="center">\n')
        file.write(f'\t\t<font size={arreglo[1]}, color="{arreglo[0]}">{titulo}</font>\n')
        file.write('\t</div>\n')
        file.write('\t<div align="center">\n')
        file.write(f'\t\t<font size={arreglo[3]}, color="{arreglo[2]}">{texto}</font>\n')
        file.write('\t</div>\n')
        file.write('\t<h1></h1>\n')
        file.write('\t<div align="center">\n')
        # Parte iterativa por cada operación realizada
        for resultado in self.resultados:
            file.write(f'\t<font size={arreglo[5]}, color="{arreglo[4]}">Operacion: {resultado.operacion}</font>\n')
            file.write('\t<h1></h1>\n')
            file.write(f'\t<font size={arreglo[5]}, color="{arreglo[4]}">Resultado: {resultado.resultado}</font>\n')
            file.write(f'\t<h3> -------------------------------------------- </h3>\n')
        file.write('\t</div>\n')
        file.write('</body>\n')
        file.write('</html>\n')
        file.close()