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

    def operarPila (self):
        while self.contador < (len (self.pilaOperaciones)-1):
            dato = self.pilaOperaciones [self.contador]
            if dato == 'SUMA' or dato == 'RESTA' or dato == 'MULTIPLICACION' or dato == 'DIVISION' or dato == 'POTENCIA' or dato == 'RAIZ' or dato == 'INVERSO' or dato == 'SENO' or dato == 'COSENO' or dato == 'TANGENTE' or dato == 'MOD':
                resultado = self.lados (dato)
            print (self.texto)
            print (resultado)
            self.texto = ''
            self.contador += 1
        self.contador = 0

    def lados (self, dato):
        self.contador += 1
        ladoIzquierdo = self.pilaOperaciones[self.contador]
        if ladoIzquierdo == 'SUMA' or ladoIzquierdo == 'RESTA' or ladoIzquierdo == 'MULTIPLICACION' or ladoIzquierdo == 'DIVISION' or ladoIzquierdo == 'POTENCIA' or ladoIzquierdo == 'RAIZ' or ladoIzquierdo == 'INVERSO' or ladoIzquierdo == 'SENO' or ladoIzquierdo == 'COSENO' or ladoIzquierdo == 'TANGENTE' or ladoIzquierdo == 'MOD':
            ladoIzquierdo = self.lados (ladoIzquierdo)
        self.contador += 1
        ladoDerecho = self.pilaOperaciones[self.contador]
        if ladoDerecho == 'SUMA' or ladoDerecho == 'RESTA' or ladoDerecho == 'MULTIPLICACION' or ladoDerecho == 'DIVISION' or ladoDerecho == 'POTENCIA' or ladoDerecho == 'RAIZ' or ladoDerecho == 'INVERSO' or ladoDerecho == 'SENO' or ladoDerecho == 'COSENO' or ladoDerecho == 'TANGENTE' or ladoDerecho == 'MOD':
            ladoDerecho = self.lados (ladoDerecho)
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
            operacion = ladoIzquierdo / ladoDerecho
            return operacion
    

    def suma (self, izquierdo, derecho):
        return int(izquierdo + derecho)

    def resta (self, izquierdo, derecho):
        return (izquierdo - derecho)
    
    def multiplicacion (self, izquierdo, derecho):
        return (izquierdo * derecho)
    
    def division (self, izquierdo, derecho):
        if derecho == 0:
            return 'Error'
        return (izquierdo / derecho)

    def potencia (self, izquierdo, derecho):
        return izquierdo ** derecho

    def raiz (self, izquierdo, derecho):
        if derecho == 0:
            return 'Error'
        return izquierdo ** (1/derecho)

    def inverso (self, izquierdo):
        if izquierdo == 0:
            return 'Error'
        return 1 / izquierdo

    def seno (self, izquierdo):
        return sin(izquierdo)

    def coseno (self, izquierdo):
        return cos(izquierdo)

    def tangente (self, izquierdo):
        return tan(izquierdo)

    def mod (self, izquierdo, derecho):
        return izquierdo % derecho
