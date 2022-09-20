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
        self.listadoTokens = []
        self.listadoDeErrores = []

    def Analizar (self, cadena):
        # Inicializando los atributos
        columna = 1
        fila = 1
        buffer = ''
        centinela = '#'
        cadena += centinela
        estado = 0
        texto = ''
        textoTitulo = ''
        bandera = False
        titulo = False
        descripcion = False
        contenido = False
        estilos = ['Negro', 10, 'Negro', 10, 'Negro', 10]
        # Reiniciando los datos
        self.listadoTokens = []
        self.listadoDeErrores = []
        token.listaTokens = []
        error.listaErrores = []

        # Analizando el texto plano
        for caracter in cadena:
            # Iniciando a estudiar los estados a la espera de un signo '<'
            #? --------------  Estado 0 --------------------- 
            if estado == 0:
                # Verificamos que empiece con un signo menor que
                if caracter == '<':
                    token.NuevoToken (caracter, 'Apertura', columna, fila)
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
                        error.NuevoError (caracter, 'Error léxico', columna, fila)
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
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 2
                        elif buffer == 'Texto' or buffer == 'Titulo':
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            if buffer == 'Texto':
                                estado = 3
                            else:
                                estado = 12
                        elif buffer == 'Estilo':
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 5
                        elif buffer == 'ESCRIBIR':
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 0
                        elif buffer == 'Descripcion' or buffer == 'Contenido':
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 4
                        else:
                            error.NuevoError (buffer, 'Error Lexico', (columna - 1), fila)
                        token.NuevoToken (caracter, 'Cierre', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == '=':
                        if buffer == 'Funcion':
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            columna += 1
                        else:
                            error.NuevoError (buffer, 'Error lexico', (columna - 1), fila)
                            buffer = ''
                        token.NuevoToken (caracter, 'Asignación', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == '/':
                        token.NuevoToken (caracter, 'Cierre Tag', (columna - 1), fila)
                        columna += 1
                        estado = 13
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
                            error.NuevoError (caracter, 'Error léxico', columna, fila)
                            columna += 1

            # Estado para cuando entra en "Tipo" para buscar "<" de las operaciones aritmeticas
            #? --------------  Estado 2 --------------------- 
            elif estado == 2:
                # Verificamos que empiece con un signo menor que
                if caracter == '<':
                    token.NuevoToken (caracter, 'Apertura', columna, fila)
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
                        error.NuevoError (caracter, 'Error léxico', columna, fila)
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
                            texto += '<br>'
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
                            token.NuevoToken (texto, 'Cadena de texto', (columna - 2), fila)
                            token.NuevoToken ('<', 'Apertura', (columna - 1), fila)
                            token.NuevoToken (caracter, 'Cierre Tag', columna, fila)
                            estado = 13
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

            # Estado para cuando entra en "Descripción" y "Contenido"
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
                        token.NuevoToken (caracter, 'Cierre', columna, fila)
                        columna += 1
                        if buffer != '':
                            error.NuevoError (buffer, 'Error Lexico', (columna - 1), fila)
                        buffer = caracter
                    elif caracter == '[':
                        token.NuevoToken (caracter, 'Apertura Texto', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == ']':
                        if buffer == 'TEXTO' or buffer == 'TIPO':
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                        else:
                            error.NuevoError (buffer, 'Error Lexico', (columna - 1), fila)
                        token.NuevoToken (caracter, 'Cierre Texto', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == '/':
                        buffer += caracter
                        if buffer == '</':
                            token.NuevoToken (caracter, 'Cierre Tag', columna, fila)
                            estado = 13
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
                            error.NuevoError (caracter, 'Error léxico', columna, fila)
                            columna += 1

            # Estado para cuando entra en "Estilo"
            #? --------------  Estado 5 --------------------- 
            elif estado == 5:
                # Verificamos que empiece con un signo menor que
                if caracter == '<':
                    token.NuevoToken (caracter, 'Apertura', columna, fila)
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
                        error.NuevoError (caracter, 'Error léxico', columna, fila)
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
                        if buffer == 'Operacion' or buffer == 'SUMA' or buffer == 'RESTA' or buffer == 'MULTIPLICACION' or buffer == 'DIVISION' or buffer == 'POTENCIA' or buffer == 'RAIZ' or buffer == 'INVERSO' or buffer == 'SENO' or buffer == 'COSENO' or buffer == 'TANGENTE' or buffer == 'MOD':
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            if buffer != 'Operacion':
                                operaciones.pilaOperaciones.append (buffer)
                            estado = 2
                        elif buffer == 'Numero':
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 7
                        elif buffer == 'Tipo':
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 0
                        # elif buffer == 'Operacion':
                        #     token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                        #     estado = 2
                        else:
                            error.NuevoError (buffer, 'Error Lexico', (columna - 1), fila)
                        token.NuevoToken (caracter, 'Cierre', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == '=':
                        if buffer == 'Operacion':
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            columna += 1
                        else:
                            error.NuevoError (buffer, 'Error lexico', (columna - 1), fila)
                        token.NuevoToken (caracter, 'Asignación', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == '/':
                        token.NuevoToken (caracter, 'Cierre Tag', columna, fila)
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
                            error.NuevoError (caracter, 'Error léxico', columna, fila)
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
                            token.NuevoToken (buffer, 'Decimal', (columna - 1), fila)
                        else:
                            operaciones.pilaOperaciones.append (int(buffer))
                            token.NuevoToken (buffer, 'Entero', (columna - 1), fila)
                        token.NuevoToken (caracter, 'Apertura', columna, fila)
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
                            error.NuevoError (caracter, 'Error léxico', columna, fila)
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
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 2
                        else:
                            error.NuevoError (buffer, 'Error Lexico', (columna - 1), fila)
                        token.NuevoToken (caracter, 'Cierre', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == '/':
                        token.NuevoToken (caracter, 'Cierre Tag', columna, fila)
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
                            error.NuevoError (caracter, 'Error léxico', columna, fila)
                            columna += 1

            # Estado para cuando entre en cada Tag de 'Estilo'
            # #? --------------  Estado 9 --------------------- 
            elif estado == 9:
                if re.search('[A-Za-z]', caracter):
                    buffer += caracter
                    if buffer == 'Titulo':
                        token.NuevoToken (buffer, 'Palabra reservada', columna, fila)
                        titulo = True
                        buffer = ''
                    elif buffer == 'Descripcion':
                        token.NuevoToken (buffer, 'Palabra reservada', columna, fila)
                        descripcion = True
                        buffer = ''
                    elif buffer == 'Contenido':
                        token.NuevoToken (buffer, 'Palabra reservada', columna, fila)
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
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 10
                        elif buffer == 'Tamanio':
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 11
                        token.NuevoToken (caracter, 'Asignación', columna, fila)
                        columna += 1
                        buffer = ''
                    elif caracter == '/':
                        token.NuevoToken (caracter, 'Cierre Tag', columna, fila)
                        columna += 1
                        estado = 13
                    elif caracter == '\n':
                        columna = 1
                        fila = fila + 1
                    elif caracter == '\t':
                        columna += 4
                    elif caracter == '\r':
                        pass
                    else:
                        error.NuevoError (caracter, 'Error léxico', columna, fila)
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
                            if buffer == 'ROJO' or buffer == 'AMARILLO' or buffer == 'AZUL' or buffer == 'VERDE' or buffer == 'NARANJA' or buffer == 'ANARANJADO' or buffer == 'BLANCO' or buffer == 'FUSIA' or buffer == 'AQUA' or buffer == 'CAFE' or buffer == 'MORADO' or buffer == 'GRIS' or buffer == 'CYAN' or buffer == 'ROSADO' or buffer == 'NEGRO':
                                token.NuevoToken (buffer, 'Palabra reservada', (columna-1), fila)
                            else:
                                error.NuevoError (buffer, 'Error léxico', (columna - 1), fila)
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
                        error.NuevoError (caracter, 'Error léxico', columna, fila)
                        columna += 1

            # Estado para colocar el tamaño del texto que tendrá el HTML
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
                            token.NuevoToken (buffer, 'Entero', (columna-1), fila)
                        token.NuevoToken (caracter, 'Cierre Tag', columna, fila)
                        columna += 1
                        buffer = caracter
                    elif caracter == '>':
                        token.NuevoToken (caracter, 'Cierre', columna, fila)
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
                        error.NuevoError (caracter, 'Error léxico', columna, fila)
                        columna += 1

            # Estado para cuando entra en "Titulo"
            #? --------------  Estado 12 --------------------- 
            elif estado == 12:
                if bandera == False:
                    if caracter == '<':
                        buffer += caracter
                        columna += 1
                        bandera = True
                    elif caracter == centinela:
                        print ('Cadena analizada')
                    else:
                        textoTitulo += caracter
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
                        textoTitulo += buffer
                        buffer = caracter
                        columna += 1
                    elif caracter == centinela:
                        print ('Cadena analizada')
                    elif caracter == '/':
                        buffer += caracter
                        if buffer == '</':
                            token.NuevoToken (textoTitulo, 'Cadena de texto', (columna - 2), fila)
                            token.NuevoToken ('<', 'Apertura', (columna - 1), fila)
                            token.NuevoToken (caracter, 'Cierre Tag', columna, fila)
                            estado = 13
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

            # Estado para cuando existe cierre de tag principal
            #? --------------  Estado 13 --------------------- 
            elif estado == 13:
                if re.search('[A-Za-z]', caracter):
                    buffer += caracter
                    columna += 1
                elif caracter == centinela:
                    print ('Cadena analizada')
                else:
                    if caracter == '>':
                        # Ingresa a la opcion de tipo
                        if buffer == 'Tipo' or buffer == 'Texto' or buffer == 'Funcion' or buffer == 'Estilo' or buffer == 'Titulo' or buffer == 'Descripcion' or buffer == 'Contenido':
                            token.NuevoToken (buffer, 'Palabra reservada', (columna - 1), fila)
                            estado = 0
                        else:
                            error.NuevoError (buffer, 'Error Lexico', (columna - 1), fila)
                        token.NuevoToken (caracter, 'Cierre', columna, fila)
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
                            error.NuevoError (caracter, 'Error léxico', columna, fila)
                            columna += 1
        # Para generar los reportes en HTML
        self.listadoTokens = token.listaTokens
        self.listadoDeErrores = error.listaErrores
        operaciones.ReporteOperaciones (textoTitulo, texto, estilos)
        error.GenerarHtmlErrores()
        token.GenerarHtmlTokens()

