from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import *
import subprocess

# Variables
root = Tk()

class Menus:
    #!::::::::::::::::::::::::::::::::VENTANAS::::::::::::::::::::::::::::::::::::::::::::::
    def __init__(self):
        # MENÚ PRINCIPAL
        root.geometry(self.EditorVentana(root, 800, 500))
        root.title('INGENIERIA USAC - Proyecto 1')
        root.iconbitmap('Archivos/books.ico')
        root.config(background='lightblue')
        root.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
        # Frames
        frame = Frame (root)
        frame.config(width='600', height='250', bg='lightblue')
        frame.pack()
        frame2 = Frame (root)
        frame2.config(width='600', height='250', bg='lightblue')
        frame2.pack()
        # Botones
        botonAgregar = ttk.Button (frame2, text='Agregar Curso')#, command=lambda: self.VentanaAgregar(ventanaGestionarCursos))
        botonAgregar.grid(column=1, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonEditar = ttk.Button (frame2, text='Editar Curso')#, command=lambda: self.VentanaEditar(ventanaGestionarCursos, tabla))
        botonEditar.grid(column=2, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonEditar['state'] = 'disabled'
        botonEliminar = ttk.Button (frame2, text='Eliminar Curso')#, command=lambda: self.EliminarCurso(ventanaGestionarCursos, tabla.item(tabla.selection())['text'], tabla.item(tabla.selection())['values'][0]))
        botonEliminar.grid(column=3, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonEliminar['state'] = 'disabled'
        botonBuscar = ttk.Button (frame2, text='Buscar Curso')#, command=lambda: self.VentanaCodigo(ventanaGestionarCursos))
        botonBuscar.grid(column=2, row=2, ipadx=55, ipady=5, padx=10, pady=10)
        botonRegresar = ttk.Button (frame2, text='Regresar')#, command=lambda: self.MostrarEliminarVentana(root, ventanaGestionarCursos))
        botonRegresar.grid(column=3, row=2, ipadx=60, ipady=5, padx=10, pady=10)
        # Para que la ventana principal se inicie automáticamente
        root.mainloop()


    #!:::::::::::::::::::::::::::MÉTODOS DE VENTANAS::::::::::::::::::::::::::::::::::::::::
    # Función para definir el tamaño de la ventana y centrarlo en la pantalla
    def EditorVentana (self, ventana, ancho, alto):
        x = ventana.winfo_screenwidth() // 2 - ancho // 2
        y = ventana.winfo_screenheight() // 2 - alto // 2
        posicion = f'{str(ancho)}x{str(alto)}+{str(x)}+{str(y)}'
        return posicion

    def AbrirManual (self, ruta):
        #path = 'Manuales/Manual de Usuario.pdf'
        path = ruta
        subprocess.Popen([path], shell=True)