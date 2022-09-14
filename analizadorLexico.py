from tokens import Token
from errores import Error
import re
# Variables de clases
token = Token ()
error = Error ()

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
                        elif buffer == 'Texto':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 3
                        elif buffer == 'Estilo':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 5
                        else:
                            error.nuevoError (buffer, 'Error Lexico', (columna - 1), fila)
                        token.nuevoToken (caracter, 'Cierre', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == '=':
                        if buffer == 'Funcion':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 4
                            columna += 1
                        else:
                            error.nuevoError (buffer, 'Error lexico', (columna - 1), fila)
                            buffer = ''
                        token.nuevoToken (caracter, 'Asignación', columna, fila)
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

            #! Pendientes determinar los demás estados
            # Estado para cuando entra en "Tipo"
            #? --------------  Estado 2 --------------------- 
            elif estado == 2:
                if re.search('[A-Za-z]', caracter):
                    buffer += caracter
                    columna += 1
                elif caracter == centinela:
                    print ('Cadena analizada')










            # Estado para cuando entra en "Texto"
            #? --------------  Estado 3 --------------------- 
            elif estado == 3:
                if bandera == False:
                    if caracter == '<':
                        #print (texto)
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
                        #! Colocar aqui por si se necesita validar lo que esta dentro del texto
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
                        columna += 1
                        if buffer == '</':
                            estado = 10
                            buffer = ''
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
                    #! Colocar aqui por si se necesita validar lo que esta dentro del texto
                    else:
                        buffer += caracter
                        columna += 1



            # Estado para cuando entra en "Funcion"
            #? --------------  Estado 4 --------------------- 
            elif estado == 4:
                pass

            # Estado para cuando entra en "Estilo"
            #? --------------  Estado 5 --------------------- 
            elif estado == 5:
                pass

            # #? --------------  Estado 6 --------------------- 
            # elif estado == 6:
            #     pass

            # #? --------------  Estado 7 --------------------- 
            # elif estado == 7:
            #     pass

            # #? --------------  Estado 8 --------------------- 
            # elif estado == 8:
            #     pass
            
            # Estado para cuando existe cierre de tag principal
            #? --------------  Estado 10 --------------------- 
            elif estado == 10:
                if re.search('[A-Za-z]', caracter):
                    buffer += caracter
                    columna += 1
                elif caracter == centinela:
                    print ('Cadena analizada')
                else:
                    if caracter == '>':
                        # Ingresa a la opcion de tipo
                        if buffer == 'Tipo' or buffer == 'Texto' or buffer == 'Funcion' or buffer == 'Estilo':
                            token.nuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 0
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
        print ('Prueba')
        print (texto)


    
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
        