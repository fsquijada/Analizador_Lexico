from lib2to3.pgen2 import token
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import *
import re
# Importacion de clases
from analizadorLexico import Analizador
from errores import Error
from tokens import Token
# Importación para abrir pdf
import subprocess
# Variables
root = Tk()
analizador =  Analizador()
error = Error()
token = Token()

class Menus:
    #!::::::::::::::::::::::::::::::::VENTANAS::::::::::::::::::::::::::::::::::::::::::::::
    def __init__(self):
        self.ruta = ''
        # MENÚ PRINCIPAL
        root.geometry(self.EditorVentana(root, 800, 500))
        root.title('INGENIERIA USAC - Proyecto 1')
        root.iconbitmap('Archivos/books.ico')
        root.config(background='lightblue')
        root.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
        # Frames
        frameTitulo = Frame (root)
        frameTitulo.config(width='800', height='70', bg='lightblue')
        frameTitulo.pack()
        frame = Frame (root)
        frame.config(width='800', height='350', bg='lightblue')
        frame.pack()
        frame2 = Frame (root)
        frame2.config(width='600', height='250', bg='lightblue')
        frame2.pack()
        # Barra de herramientas
        menu = Menu (root)#, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
        root.config (menu=menu)
        # Sección de archivo en barra de herramientas
        barraArchivo = Menu(menu, tearoff=0)#, tearoff=1, background='#ffcc99', foreground='black') 
        menu.add_cascade(label='Archivo', menu=barraArchivo)
        barraArchivo.add_command(label='Abrir', command=lambda: self.AbrirArchivo(cuadroTexto, botonGuardar))
        barraArchivo.add_command(label='Guardar como', command=lambda: self.GuardarComo(cuadroTexto, botonGuardar))
        barraArchivo.add_separator()
        barraArchivo.add_command(label='Salir', command=lambda: self.EliminarVentana(root))
        # Sección de ayuda en barra de herramientas
        barraAyuda = Menu(menu, tearoff=0)
        menu.add_cascade(label='Ayuda', menu=barraAyuda)
        barraAyuda.add_command(label='Manual de usuario', command=lambda: self.AbrirManual('Manuales\Manual de Usuario.pdf'))
        barraAyuda.add_command(label='Manual Técnico', command=lambda: self.AbrirManual('Manuales\Manual Técnico.pdf'))
        barraAyuda.add_command(label='Temas de ayuda', command=lambda: self.Informacion())
        # Label de información
        tituloSuperior = Label (frameTitulo, text='ANALIZADOR LÉXICO')
        tituloSuperior.config(background='lightblue', font=('Arial', 16, 'bold'), justify='center')
        tituloSuperior.grid(column=0, row=0, padx=0, pady=10, columnspan=1)
        tituloSuperior.place()
        # Cuadro de texto
        cuadroTexto = Text (frame, width='70', height='10')
        cuadroTexto.grid(column=0, row=1, ipadx=10, ipady=45, padx=10, pady=20)
        # Botones
        botonGuardar = ttk.Button (frame2, text='Guardar', command=lambda: self.Guardar(cuadroTexto))
        botonGuardar.grid(column=1, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonGuardar['state'] = 'disabled'
        botonGuardarComo = ttk.Button (frame2, text='Guardar Como', command=lambda: self.GuardarComo(cuadroTexto, botonGuardar))
        botonGuardarComo.grid(column=2, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonAnalizar = ttk.Button (frame2, text='Analizar texto', command=lambda: self.AnalizarTexto(cuadroTexto, botonTokens, botonErrores))
        botonAnalizar.grid(column=3, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonTokens = ttk.Button (frame2, text='Listado Tokens', command=lambda: self.VentanaTokens())
        botonTokens.grid(column=1, row=2, ipadx=50, ipady=5, padx=10, pady=10)
        botonTokens['state'] = 'disabled'
        botonErrores = ttk.Button (frame2, text='Listado Errores', command=lambda: self.VentanaErrores())
        botonErrores.grid(column=2, row=2, ipadx=60, ipady=5, padx=10, pady=10)
        botonErrores['state'] = 'disabled'
        botonSalir = ttk.Button (frame2, text='Salir', command=lambda: self.EliminarVentana(root))
        botonSalir.grid(column=3, row=2, ipadx=60, ipady=5, padx=10, pady=10)
        # Para que la ventana principal se inicie automáticamente
        root.mainloop()

    # Crear Ventana para la lista de cursos
    def VentanaErrores (self):
        # Ocultar ventana principal
        self.OcultarVentana(root)
        # Ventana de Selección de archivo
        ventanaErrores = Toplevel ()
        ventanaErrores.geometry(self.EditorVentana(root, 800, 500))
        ventanaErrores.title('INGENIERIA USAC - Tabla de errores')
        ventanaErrores.iconbitmap('archivos/books.ico')
        ventanaErrores.config(background='lightblue')
        ventanaErrores.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
        ventanaErrores.protocol('WM_DELETE_WINDOW', root.quit)
        # Frame
        frameTitulo = Frame (ventanaErrores)
        frameTitulo.config(width='800', height='70', bg='lightblue')
        frameTitulo.pack()
        frame = Frame (ventanaErrores)
        frame.config(width='600', height='200', bg='lightblue')
        frame.pack()
        frame2 = Frame (ventanaErrores)
        frame2.config(width='600', height='250', bg='lightblue')
        frame2.pack()
        # Label de información
        tituloSuperior = Label (frameTitulo, text=' TABLA DE ERRORES')
        tituloSuperior.config(background='lightblue', font=('Arial', 16, 'bold'), justify='center')
        tituloSuperior.grid(column=0, row=0, padx=0, pady=10, columnspan=1)
        tituloSuperior.place()
        # Tabla
        tabla = ttk.Treeview(frame, columns=('#1', '#2', '#3', '#4'), height='8')
        #tabla.bind('<Button-1>', Click)
        tabla.grid(row='10', column='0', columnspan='2', pady=100)
        tabla.column('#0', width=50)
        tabla.column('#1', width=240, anchor=CENTER)
        tabla.column('#2', width=105, anchor=CENTER)
        tabla.column('#3', width=80, anchor=CENTER)
        tabla.column('#4', width=70, anchor=CENTER)
        # Títulos de la tabla
        tabla.heading('#0', text='NO.', anchor=CENTER)
        tabla.heading('#1', text='LEXEMA', anchor=CENTER)
        tabla.heading('#2', text='TIPO', anchor=CENTER)
        tabla.heading('#3', text='COLUMNA', anchor=CENTER)
        tabla.heading('#4', text='FILA', anchor=CENTER)
        # Carga de datos para la tabla
        self.InsertarErrores(tabla)
        # Botones
        botonRegresar = ttk.Button (frame2, text='Regresar', command=lambda: self.MostrarEliminarVentana(root, ventanaErrores))
        botonRegresar.grid(column=3, row=2, ipadx=60, ipady=5, padx=10, pady=10)

    # Crear Ventana para la lista de cursos
    def VentanaTokens (self):
        # Ocultar ventana principal
        self.OcultarVentana(root)
        # Ventana de Selección de archivo
        ventanaTokens = Toplevel ()
        ventanaTokens.geometry(self.EditorVentana(root, 800, 500))
        ventanaTokens.title('INGENIERIA USAC - Tabla de tokens')
        ventanaTokens.iconbitmap('archivos/books.ico')
        ventanaTokens.config(background='lightblue')
        ventanaTokens.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
        ventanaTokens.protocol('WM_DELETE_WINDOW', root.quit)
        # Frame
        frameTitulo = Frame (ventanaTokens)
        frameTitulo.config(width='800', height='70', bg='lightblue')
        frameTitulo.pack()
        frame = Frame (ventanaTokens)
        frame.config(width='600', height='200', bg='lightblue')
        frame.pack()
        frame2 = Frame (ventanaTokens)
        frame2.config(width='600', height='250', bg='lightblue')
        frame2.pack()
        # Label de información
        tituloSuperior = Label (frameTitulo, text=' TABLA DE TOKENS')
        tituloSuperior.config(background='lightblue', font=('Arial', 16, 'bold'), justify='center')
        tituloSuperior.grid(column=0, row=0, padx=0, pady=10, columnspan=1)
        tituloSuperior.place()
        # Tabla
        tabla = ttk.Treeview(frame, columns=('#1', '#2', '#3', '#4'), height='8')
        #tabla.bind('<Button-1>', Click)
        tabla.grid(row='10', column='0', columnspan='2', pady=100)
        tabla.column('#0', width=50)
        tabla.column('#1', width=240, anchor=CENTER)
        tabla.column('#2', width=105, anchor=CENTER)
        tabla.column('#3', width=80, anchor=CENTER)
        tabla.column('#4', width=70, anchor=CENTER)
        # Títulos de la tabla
        tabla.heading('#0', text='NO.', anchor=CENTER)
        tabla.heading('#1', text='LEXEMA', anchor=CENTER)
        tabla.heading('#2', text='TIPO', anchor=CENTER)
        tabla.heading('#3', text='COLUMNA', anchor=CENTER)
        tabla.heading('#4', text='FILA', anchor=CENTER)
        # Carga de datos para la tabla
        self.InsertarTokens(tabla)
        # Botones
        botonRegresar = ttk.Button (frame2, text='Regresar', command=lambda: self.MostrarEliminarVentana(root, ventanaTokens))
        botonRegresar.grid(column=3, row=2, ipadx=60, ipady=5, padx=10, pady=10)

    #!:::::::::::::::::::::::::::MÉTODOS DE VENTANAS::::::::::::::::::::::::::::::::::::::::
    # Función para definir el tamaño de la ventana y centrarlo en la pantalla
    def EditorVentana (self, ventana, ancho, alto):
        x = ventana.winfo_screenwidth() // 2 - ancho // 2
        y = ventana.winfo_screenheight() // 2 - alto // 2
        posicion = f'{str(ancho)}x{str(alto)}+{str(x)}+{str(y)}'
        return posicion

    # Método para eliminar la pantalla actual y mostrar en pantalla la ventana oculta
    def MostrarEliminarVentana (self, ventanaMostrar, ventanaEliminar):
        ventanaEliminar.destroy()
        ventanaMostrar.deiconify()

    # Método para ocultar la ventana actual
    def OcultarVentana (self, ventana):
        ventana.withdraw()

    # Método para eliminar la ventana actual
    def EliminarVentana (self, ventana):
        ventana.destroy()

    #!::::::::::::::::::::::::::::MÉTODOS GENERALES:::::::::::::::::::::::::::::::::::::::::
    # Método para abrir y cargar archivos
    def AbrirArchivo (self, cuadroTexto, boton):
        if self.ruta != '':
            respuesta = askyesno('Abrir archivo', '¿Deseas guardar el texto actual antes de abrir otro archivo?')
            if respuesta == True:
                self.Guardar(cuadroTexto)
        ruta = filedialog.askopenfilename(title='Abrir', filetypes=(('Archivos LFP (*.lfp)','*.lfp'),))
        if (ruta != ''):
            archivo = open (ruta, 'r', 1, 'utf-8')
            textoPlano = archivo.read ()
            archivo.close ()
            cuadroTexto.delete(1.0, 'end-1c')
            cuadroTexto.insert(1.0, textoPlano)
            boton['state'] = 'normal'
            self.ruta = ruta
            showinfo('Carga de cursos', 'Los datos se han cargado correctamente')
    
    # Abre un manual en formato pdf
    def AbrirManual (self, ruta):
        rutaAbierta = ruta
        subprocess.Popen([rutaAbierta], shell=True)

    # Abre un manual en formato pdf
    def AnalizarTexto (self, texto, botonToken, botonError):
        documento = texto.get(1.0, 'end-1c')
        analizador.analizar(documento)
        botonToken['state'] = 'normal'
        botonError['state'] = 'normal'
        showinfo('Analizador', 'El texto se ha analizado correctamente')

    # Guarda el texto que se encuentra en el cuadro de texto
    def Guardar (self, texto):
        cuadroTexto = texto.get(1.0, 'end-1c')
        if cuadroTexto != '':
            documento = open (self.ruta, 'w', encoding='utf-8')
            documento.write(cuadroTexto)
            documento.close()
            showinfo('Guardar', 'El texto se ha guardado correctamente')
        else:
            showerror('Guardar', 'No existe nada en el cuadro de texto para guardar')

    # Guarda con un nuevo nombre el texto que se encuentra en el cuadro de texto
    def GuardarComo (self, texto, boton):
        cuadroTexto = texto.get(1.0, 'end-1c')
        if cuadroTexto != '':
            nombreArchivo = filedialog.asksaveasfilename(title='Guardar como..', filetypes= (('lfp files', '*.lfp'),))#('Todos los archivos','*.*')))
            if nombreArchivo != '':
                busqueda = re.findall('\.lfp', nombreArchivo)
                if busqueda != []:
                    documento = open (nombreArchivo, 'w', encoding='utf-8')
                    self.ruta = nombreArchivo
                else:
                    documento = open (f'{nombreArchivo}.lfp', 'w', encoding='utf-8')
                    self.ruta = f'{nombreArchivo}.lfp'
                documento.write(cuadroTexto)
                documento.close()
                boton['state'] = 'normal'
                showinfo('Guardar como', 'El texto se ha guardado correctamente')
        else:
            showerror('Guardar como', 'No existe nada en el cuadro de texto para guardar')

    # Método para agregar datos de error en la tabla
    def InsertarErrores (self, tabla):
        contador = 1
        for dato in analizador.listadoDeErrores:
            tabla.insert('', END, text=contador, values=(dato.lexema, dato.tipo, dato.columna, dato.fila))
            contador += 1
    
    # Método para agregar datos de tokens en la tabla
    def InsertarTokens (self, tabla):
        contador = 1
        for dato in analizador.listadoTokens:
            tabla.insert('', END, text=contador, values=(dato.lexema, dato.tipo, dato.columna, dato.fila))
            contador += 1
    
    # Muestra la información del estudiante que realizó el proyecto.
    def Informacion (self):
        showinfo ('Estudiante', 'Fredy Samuel Quijada Ceballos\nCarne: 202004812')