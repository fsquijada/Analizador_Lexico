from cmath import cos, sin, tan
import math

class ConstructorOperaciones:
    def __init__ (self, operacion, resultado):
        self.operacion = operacion
        self.resultado = resultado

class OperacionesAritmeticas:
    def __init__ (self):
        self.pilaOperaciones = []
        self.resultados = []
        self.contador = 0
        self.texto = ''

    def operacionesIngresadas (self):
        for operacion in self.pilaOperaciones:
            print (operacion)

    def operarPila (self):
        self.texto = ''
        self.contador = 0
        while self.contador < (len (self.pilaOperaciones)-1):
            dato = self.pilaOperaciones [self.contador]
            if dato == 'SUMA' or dato == 'RESTA' or dato == 'MULTIPLICACION' or dato == 'DIVISION' or dato == 'POTENCIA' or dato == 'RAIZ' or dato == 'INVERSA' or dato == 'SENO' or dato == 'COSENO' or dato == 'TANGENTE' or dato == 'MOD':
                self.texto += '('
                resultado = self.lados (dato)
            print (self.texto)
            print (resultado)
            nuevo = ConstructorOperaciones (self.texto, resultado)
            self.resultados.append (nuevo)
            self.texto = ''
            self.contador += 1
        self.pilaOperaciones = []

    def lados (self, dato):
        self.contador += 1
        ladoIzquierdo = self.pilaOperaciones[self.contador]
        auxiliar = ladoIzquierdo
        if ladoIzquierdo == 'SUMA' or ladoIzquierdo == 'RESTA' or ladoIzquierdo == 'MULTIPLICACION' or ladoIzquierdo == 'DIVISION' or ladoIzquierdo == 'POTENCIA' or ladoIzquierdo == 'RAIZ' or ladoIzquierdo == 'INVERSA' or ladoIzquierdo == 'SENO' or ladoIzquierdo == 'COSENO' or ladoIzquierdo == 'TANGENTE' or ladoIzquierdo == 'MOD':
            self.texto += '('
            ladoIzquierdo = self.lados (ladoIzquierdo)
        else:
            if dato == 'INVERSA':
                self.texto += f'Inv({ladoIzquierdo}))'
                operacion = 1/ladoIzquierdo
                return operacion
            elif dato == 'SENO':
                operacion = sin(ladoIzquierdo)
                return operacion
            elif dato == 'COSENO':
                operacion = cos(ladoIzquierdo)
                return operacion
            elif dato == 'TANGENTE':
                operacion = tan(ladoIzquierdo)
                return operacion
            if auxiliar == ladoIzquierdo:
                self.texto += f'{ladoIzquierdo}'
        self.contador += 1
        ladoDerecho = self.pilaOperaciones[self.contador]
        auxiliar = ladoDerecho
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
            self.texto += ' mod '
        if ladoDerecho == 'SUMA' or ladoDerecho == 'RESTA' or ladoDerecho == 'MULTIPLICACION' or ladoDerecho == 'DIVISION' or ladoDerecho == 'POTENCIA' or ladoDerecho == 'RAIZ' or ladoDerecho == 'INVERSA' or ladoDerecho == 'SENO' or ladoDerecho == 'COSENO' or ladoDerecho == 'TANGENTE' or ladoDerecho == 'MOD':
            self.texto += '('
            ladoDerecho = self.lados (ladoDerecho)
        if auxiliar == ladoDerecho:
            self.texto += f'{ladoDerecho}'
        if dato == 'INVERSA':
            operacion = 1/ladoDerecho
            return operacion
        elif dato == 'SENO':
            operacion = sin(ladoDerecho)
            return operacion
        elif dato == 'COSENO':
            operacion = cos(ladoDerecho)
            return operacion
        elif dato == 'TANGENTE':
            operacion = tan(ladoDerecho)
            return operacion
        elif dato == 'SUMA':
            self.texto += ')'
            operacion = ladoIzquierdo + ladoDerecho
            return operacion
        elif dato == 'RESTA':
            operacion = ladoIzquierdo - ladoDerecho
            return operacion
        elif dato == 'MULTIPLICACION':
            operacion = ladoIzquierdo * ladoDerecho
            return operacion
        elif dato == 'DIVISION':
            operacion = ladoIzquierdo / ladoDerecho
            return operacion
        elif dato == 'POTENCIA':
            operacion = ladoIzquierdo ** ladoDerecho
            return operacion
        elif dato == 'RAIZ':
            operacion = ladoIzquierdo ** (1/ladoDerecho)
            return operacion
        elif dato == 'MOD':
            operacion = ladoIzquierdo % ladoDerecho
            return operacion
