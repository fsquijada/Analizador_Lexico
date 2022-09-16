from cmath import cos, sin, tan
import math

class ConstructorOperaciones:
    def __init__ (self, numeroOperacion, operacion, resultado):
        self.numeroOperacion = numeroOperacion
        self.operacion = operacion
        self.resultado = resultado

class OperacionesAritmeticas:
    def __init__ (self):
        self.pilaOperaciones = []
        self.resultados = []
        self.contador = 0
        self.numeroOperacion = 0
        self.texto = ''

    def operacionesIngresadas (self):
        for operacion in self.pilaOperaciones:
            print (operacion)

    def operarPila (self):
        while self.contador < (len (self.pilaOperaciones)-1):
            dato = self.pilaOperaciones [self.contador]
            if dato == 'SUMA' or dato == 'RESTA' or dato == 'MULTIPLICACION' or dato == 'DIVISION' or dato == 'POTENCIA' or dato == 'RAIZ' or dato == 'INVERSA' or dato == 'SENO' or dato == 'COSENO' or dato == 'TANGENTE' or dato == 'MOD':
                resultado = self.lados (dato)
            print (self.texto)
            print (resultado)
            self.texto = ''
            self.contador += 1
        self.contador = 0

    def lados (self, dato):
        self.contador += 1
        ladoIzquierdo = self.pilaOperaciones[self.contador]
        if ladoIzquierdo == 'SUMA' or ladoIzquierdo == 'RESTA' or ladoIzquierdo == 'MULTIPLICACION' or ladoIzquierdo == 'DIVISION' or ladoIzquierdo == 'POTENCIA' or ladoIzquierdo == 'RAIZ' or ladoIzquierdo == 'INVERSA' or ladoIzquierdo == 'SENO' or ladoIzquierdo == 'COSENO' or ladoIzquierdo == 'TANGENTE' or ladoIzquierdo == 'MOD':
            ladoIzquierdo = self.lados (ladoIzquierdo)
        else:
            if dato == 'INVERSA':
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
        self.contador += 1
        ladoDerecho = self.pilaOperaciones[self.contador]
        if ladoDerecho == 'SUMA' or ladoDerecho == 'RESTA' or ladoDerecho == 'MULTIPLICACION' or ladoDerecho == 'DIVISION' or ladoDerecho == 'POTENCIA' or ladoDerecho == 'RAIZ' or ladoDerecho == 'INVERSA' or ladoDerecho == 'SENO' or ladoDerecho == 'COSENO' or ladoDerecho == 'TANGENTE' or ladoDerecho == 'MOD':
            ladoDerecho = self.lados (ladoDerecho)
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
    