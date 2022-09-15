from tokens import Token
from errores import Error
from operaciones import OperacionesAritmeticas
import re
# Variables de clases
token = Token ()
error = Error ()
operaciones = OperacionesAritmeticas ()

class Analizador:
    def __init__(self):
        pass

    def analizar (self, cadena):
        # Inicializando los atributos
        columna = 1
        fila = 1
        buffer = ''
        centinela = '#'
        cadena += centinela
        estado = 0
        texto = ''
        bandera = False
        titulo = False
        descripcion = False
        contenido = False
        estilos = ['Negro', 10, 'Negro', 10, 'Negro', 10]

        # Analizando el texto plano
        #i = 0
        #while i < len(texto):
        for caracter in cadena:
            #caracter = texto[i]
            # Iniciando a estudiar los estados
            #? --------------  Estado 0 --------------------- 
            if estado == 0:
                # Verificamos que empiece con un signo menor que
                if caracter == '<':
                    token.nuevoToken (caracter, 'Apertura', columna, fila)
                    columna += 1
                    estado = 1
                elif caracter == centinela:
                    print ('Cadena analizada')
                else:
                    if caracter == '\n':
                        columna = 1
                        fila = fila + 1
                    elif caracter == '\t':
                        columna += 4
                    elif caracter == ' ':
                        columna += 1
                    elif caracter == '\r':
                        pass
                    else:
                        error.nuevoError (caracter, 'Error léxico', columna, fila)
                        columna += 1
                    buffer = ''

            # Estado para reconocer el texto que está dentro de los tag superiores
            #? --------------  Estado 1 --------------------- 
            elif estado == 1:
                if re.search('[A-Za-z]', caracter):
                    buffer += caracter
                    columna += 1
                elif caracter == centinela:
                    print ('Cadena analizada')
                else:
                    if caracter == '>':
                        # Ingresa a la opcion de tipo
                        if buffer == 'Tipo':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 2
                        elif buffer == 'Texto' or buffer == 'Titulo':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 3
                        elif buffer == 'Estilo':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 5
                        elif buffer == 'ESCRIBIR':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 0
                        elif buffer == 'Descripcion' or buffer == 'Contenido':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 4
                        else:
                            error.nuevoError (buffer, 'Error Lexico', (columna - 1), fila)
                        token.nuevoToken (caracter, 'Cierre', columna, fila)
                        columna += 1
                        buffer = ''
                        texto = ''
                    elif caracter == '=':
                        if buffer == 'Funcion':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            columna += 1
                        else:
                            error.nuevoError (buffer, 'Error lexico', (columna - 1), fila)
                            buffer = ''
                        token.nuevoToken (caracter, 'Asignación', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == '/':
                        token.nuevoToken (caracter, 'Cierre Tag', (columna - 1), fila)
                        columna += 1
                        estado = 100
                    else:
                        if caracter == '\n':
                            columna = 1
                            fila = fila + 1
                        elif caracter == '\t':
                            columna += 4
                        elif caracter == ' ':
                            columna += 1
                        elif caracter == '\r':
                            pass
                        else:
                            error.nuevoError (caracter, 'Error léxico', columna, fila)
                            columna += 1

            # Estado para cuando entra en "Tipo" para buscar "<" de las operaciones aritmeticas
            #? --------------  Estado 2 --------------------- 
            elif estado == 2:
                # Verificamos que empiece con un signo menor que
                if caracter == '<':
                    token.nuevoToken (caracter, 'Apertura', columna, fila)
                    columna += 1
                    estado = 6
                elif caracter == centinela:
                    print ('Cadena analizada')
                else:
                    if caracter == '\n':
                        columna = 1
                        fila = fila + 1
                    elif caracter == '\t':
                        columna += 4
                    elif caracter == ' ':
                        columna += 1
                    elif caracter == '\r':
                        pass
                    else:
                        error.nuevoError (caracter, 'Error léxico', columna, fila)
                        columna += 1
                    buffer = ''
                  
            # Estado para cuando entra en "Texto"
            #? --------------  Estado 3 --------------------- 
            elif estado == 3:
                if bandera == False:
                    if caracter == '<':
                        buffer += caracter
                        columna += 1
                        bandera = True
                    elif caracter == centinela:
                        print ('Cadena analizada')
                    else:
                        texto += caracter
                        if caracter == '\n':
                            columna = 1
                            fila += 1
                        elif caracter == '\t':
                            columna += 4
                        elif caracter == ' ':
                            columna += 1
                        elif caracter == '\r':
                            pass
                        else:
                            columna += 1
                else:
                    if caracter == '<':
                        texto += buffer
                        buffer = caracter
                        columna += 1
                    elif caracter == centinela:
                        print ('Cadena analizada')
                    elif caracter == '/':
                        buffer += caracter
                        if buffer == '</':
                            token.nuevoToken (texto, 'Cadena de texto', (columna - 2), fila)
                            token.nuevoToken ('<', 'Apertura', (columna - 1), fila)
                            token.nuevoToken (caracter, 'Cierre Tag', columna, fila)
                            estado = 100
                            bandera = False
                            buffer = ''
                        columna += 1
                    elif caracter == '\n':
                        columna = 1
                        fila += 1
                    elif caracter == '\t':
                        columna += 4
                    elif caracter == ' ':
                        buffer += caracter
                        columna += 1
                    elif caracter == '\r':
                        pass
                    else:
                        buffer += caracter
                        columna += 1

            # Estado para cuando entra en "Funcion"
            #? --------------  Estado 4 --------------------- 
            elif estado == 4:
                if re.search('[A-Za-z]', caracter):
                    buffer += caracter
                    columna += 1
                elif caracter == centinela:
                    print ('Cadena analizada')
                else:
                    if caracter == '<':
                        # Ingresa a la opcion de cierre de numero
                        token.nuevoToken (caracter, 'Cierre', columna, fila)
                        columna += 1
                        if buffer != '':
                            error.nuevoError (buffer, 'Error Lexico', (columna - 1), fila)
                        buffer = caracter
                    elif caracter == '[':
                        token.nuevoToken (caracter, 'Apertura Texto', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == ']':
                        if buffer == 'TEXTO' or buffer == 'TIPO':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                        else:
                            error.nuevoError (buffer, 'Error Lexico', (columna - 1), fila)
                        token.nuevoToken (caracter, 'Cierre Texto', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == '/':
                        buffer += caracter
                        if buffer == '</':
                            token.nuevoToken (caracter, 'Cierre Tag', columna, fila)
                            estado = 100
                            bandera = False
                            buffer = ''
                        columna += 1
                    else:
                        if caracter == '\n':
                            columna = 1
                            fila = fila + 1
                        elif caracter == '\t':
                            columna += 4
                        elif caracter == ' ':
                            columna += 1
                        elif caracter == '\r':
                            pass
                        else:
                            error.nuevoError (caracter, 'Error léxico', columna, fila)
                            columna += 1

            # Estado para cuando entra en "Estilo"
            #? --------------  Estado 5 --------------------- 
            elif estado == 5:
                # Verificamos que empiece con un signo menor que
                if caracter == '<':
                    token.nuevoToken (caracter, 'Apertura', columna, fila)
                    columna += 1
                    estado = 9
                elif caracter == centinela:
                    print ('Cadena analizada')
                else:
                    if caracter == '\n':
                        columna = 1
                        fila = fila + 1
                    elif caracter == '\t':
                        columna += 4
                    elif caracter == ' ':
                        columna += 1
                    elif caracter == '\r':
                        pass
                    else:
                        error.nuevoError (caracter, 'Error léxico', columna, fila)
                        columna += 1
                    buffer = '' 

            # Estado dentro del tag de la operacion aritmetica
            # #? --------------  Estado 6 --------------------- 
            elif estado == 6:
                if re.search('[A-Za-z]', caracter):
                    buffer += caracter
                    columna += 1
                elif caracter == centinela:
                    print ('Cadena analizada')
                else:
                    if caracter == '>':
                        # Ingresa a la opcion de tipo
                        if buffer == 'SUMA' or buffer == 'RESTA' or buffer == 'MULTIPLICACION' or buffer == 'DIVISION' or buffer == 'POTENCIA' or buffer == 'RAIZ' or buffer == 'INVERSO' or buffer == 'SENO' or buffer == 'COSENO' or buffer == 'TANGENTE' or buffer == 'MOD':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            operaciones.pilaOperaciones.append (buffer)
                            estado = 2
                        elif buffer == 'Numero':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 7
                        elif buffer == 'Tipo':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 0
                        elif buffer == 'Operacion':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 2
                        else:
                            error.nuevoError (buffer, 'Error Lexico', (columna - 1), fila)
                        token.nuevoToken (caracter, 'Cierre', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == '=':
                        if buffer == 'Operacion':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            columna += 1
                        else:
                            error.nuevoError (buffer, 'Error lexico', (columna - 1), fila)
                        token.nuevoToken (caracter, 'Asignación', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == '/':
                        token.nuevoToken (caracter, 'Cierre Tag', columna, fila)
                        columna += 1
                        buffer = ''
                    else:
                        if caracter == '\n':
                            columna = 1
                            fila = fila + 1
                        elif caracter == '\t':
                            columna += 4
                        elif caracter == ' ':
                            columna += 1
                        elif caracter == '\r':
                            pass
                        else:
                            error.nuevoError (caracter, 'Error léxico', columna, fila)
                            columna += 1

            # Estado en el que entra con el tag "Numero"
            # #? --------------  Estado 7 --------------------- 
            elif estado == 7:
                if re.search('[0-9]', caracter) or re.search('[\.]', caracter):
                    buffer += caracter
                    columna += 1
                elif caracter == centinela:
                    print ('Cadena analizada')
                else:
                    if caracter == '<':
                        if re.search ('[\.]', buffer):
                            operaciones.pilaOperaciones.append (float(buffer))
                            token.nuevoToken (buffer, 'Decimal', (columna - 1), fila)
                        else:
                            operaciones.pilaOperaciones.append (int(buffer))
                            token.nuevoToken (buffer, 'Entero', (columna - 1), fila)
                        token.nuevoToken (caracter, 'Apertura', columna, fila)
                        columna += 1
                        estado = 8
                        buffer = ''
                    elif caracter == centinela:
                        print ('Cadena analizada')
                    else:
                        if caracter == '\n':
                            columna = 1
                            fila = fila + 1
                        elif caracter == '\t':
                            columna += 4
                        elif caracter == ' ':
                            columna += 1
                        elif caracter == '\r':
                            pass
                        else:
                            error.nuevoError (caracter, 'Error léxico', columna, fila)
                            columna += 1

            # Estado de cierre de tag "Numero"
            # #? --------------  Estado 8 --------------------- 
            elif estado == 8:
                if re.search('[A-Za-z]', caracter):
                    buffer += caracter
                    columna += 1
                elif caracter == centinela:
                    print ('Cadena analizada')
                else:
                    if caracter == '>':
                        # Ingresa a la opcion de cierre de numero
                        if buffer == 'Numero':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 2
                        else:
                            error.nuevoError (buffer, 'Error Lexico', (columna - 1), fila)
                        token.nuevoToken (caracter, 'Cierre', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == '/':
                        token.nuevoToken (caracter, 'Cierre Tag', columna, fila)
                        columna += 1
                        buffer = ''
                    else:
                        if caracter == '\n':
                            columna = 1
                            fila = fila + 1
                        elif caracter == '\t':
                            columna += 4
                        elif caracter == ' ':
                            columna += 1
                        elif caracter == '\r':
                            pass
                        else:
                            error.nuevoError (caracter, 'Error léxico', columna, fila)
                            columna += 1

            # Estado para cuando entre en cada Tag de 'Estilo'
            # #? --------------  Estado 9 --------------------- 
            elif estado == 9:
                if re.search('[A-Za-z]', caracter):
                    buffer += caracter
                    if buffer == 'Titulo':
                        token.nuevoToken (buffer, 'Palabra reservada', columna, fila)
                        titulo = True
                        buffer = ''
                    elif buffer == 'Descripcion':
                        token.nuevoToken (buffer, 'Palabra reservada', columna, fila)
                        descripcion = True
                        buffer = ''
                    elif buffer == 'Contenido':
                        token.nuevoToken (buffer, 'Palabra reservada', columna, fila)
                        contenido = True
                        buffer = ''
                    columna += 1
                elif caracter == centinela:
                    print ('Cadena analizada')
                else:
                    if caracter == ' ':
                        columna += 1
                        buffer = ''
                    elif caracter == '=':
                        if buffer == 'Color':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 10
                        elif buffer == 'Tamanio':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 11
                        token.nuevoToken (caracter, 'Asignación', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == '/':
                        token.nuevoToken (caracter, 'Cierre Tag', columna, fila)
                        columna += 1
                        estado = 100
                    elif caracter == '\n':
                        columna = 1
                        fila = fila + 1
                    elif caracter == '\t':
                        columna += 4
                    elif caracter == '\r':
                        pass
                    else:
                        error.nuevoError (caracter, 'Error léxico', columna, fila)
                        columna += 1

            # Estado para definiar color y tamaño del html
            # #? --------------  Estado 10 --------------------- 
            elif estado == 10:
                if re.search('[A-Za-z]', caracter):
                    if caracter == 'T':
                        if buffer != '':
                            if titulo == True:
                                estilos[0] = buffer
                            elif descripcion == True:
                                estilos[2] = buffer
                            elif contenido == True:
                                estilos[4] = buffer
                            token.nuevoToken (buffer, 'Color', (columna-2), fila)
                            buffer = ''
                            estado = 9
                    buffer += caracter
                    columna += 1
                elif caracter == centinela:
                    print ('Cadena analizada')
                else:
                    if caracter == '\n':
                        columna = 1
                        fila = fila + 1
                    elif caracter == ' ':
                        columna += 1
                    elif caracter == '\t':
                        columna += 4
                    elif caracter == '\r':
                        pass
                    else:
                        error.nuevoError (caracter, 'Error léxico', columna, fila)
                        columna += 1




            # 
            # #? --------------  Estado 11 --------------------- 
            elif estado == 11:
                if re.search('[0-9]', caracter):
                    buffer += caracter
                    columna += 1
                elif caracter == centinela:
                    print ('Cadena analizada')
                else:
                    if caracter == '/':
                        if buffer != '':
                            if titulo == True:
                                estilos[1] = buffer
                            elif descripcion == True:
                                estilos[3] = buffer
                            elif contenido == True:
                                estilos[5] = buffer
                            token.nuevoToken (buffer, 'Tamaño', (columna-1), fila)
                        token.nuevoToken (caracter, 'Cierre Tag', columna, fila)
                        columna += 1
                        buffer = caracter
                    elif caracter == '>':
                        token.nuevoToken (caracter, 'Cierre', columna, fila)
                        titulo = False
                        descripcion = False
                        contenido = False
                        estado = 5
                        buffer = ''
                    elif caracter == ' ':
                        columna += 1
                    elif caracter == '\n':
                        columna = 1
                        fila = fila + 1
                    elif caracter == '\t':
                        columna += 4
                    elif caracter == '\r':
                        pass
                    else:
                        error.nuevoError (caracter, 'Error léxico', columna, fila)
                        columna += 1




            # Estado para cuando existe cierre de tag principal
            #? --------------  Estado 100 --------------------- 
            elif estado == 100:
                if re.search('[A-Za-z]', caracter):
                    buffer += caracter
                    columna += 1
                elif caracter == centinela:
                    print ('Cadena analizada')
                else:
                    if caracter == '>':
                        # Ingresa a la opcion de tipo
                        if buffer == 'Tipo' or buffer == 'Texto' or buffer == 'Funcion' or buffer == 'Estilo' or buffer == 'Titulo' or buffer == 'Descripcion' or buffer == 'Contenido':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 0
                        # elif buffer == 'Titulo':
                        #     token.nuevoToken (buffer, 'Cadena de texto', (columna - 1), fila)
                        #     estado = 0
                        else:
                            error.nuevoError (buffer, 'Error Lexico', (columna - 1), fila)
                        token.nuevoToken (caracter, 'Cierre', columna, fila)
                        columna += 1
                        buffer = ''
                    else:
                        if caracter == '\n':
                            columna = 1
                            fila = fila + 1
                        elif caracter == '\t':
                            columna += 4
                        elif caracter == ' ':
                            columna += 1
                        elif caracter == '\r':
                            pass
                        else:
                            error.nuevoError (caracter, 'Error léxico', columna, fila)
                            columna += 1

            # Aumentando i por cada letra
            # i += 1
        print ('\n\n************************')
        print ('Lista de tokens')
        token.tokensIngresados ()
        print ('\n\n************************')
        print ('Lista errores')
        error.erroresIngresados ()
        print ('\n\n************************')
        print ('Lista operaciones')
        operaciones.operacionesIngresadas ()
        print ('Prueba')
        print (texto)
        print ('\n\n************************')
        print (f'Titulo: {estilos[0]}, {estilos[1]}')
        print (f'Descripcion: {estilos[2]}, {estilos[3]}')
        print (f'Contenido: {estilos[4]}, {estilos[5]}')


    
    # def caracteresEspeciales (self, caracter, columna, fila):
    #     if caracter == '\n':
    #         columna = 1
    #         fila = fila + 1
    #     elif caracter == '\t':
    #         columna += 4
    #     elif caracter == ' ':
    #         columna += 1
    #     elif caracter == '\r':
    #         pass
    #     else:
    #         error.nuevoError (caracter, 'Error léxico', columna, fila)
    #         columna += 1
        