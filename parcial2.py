#importaremos las librerias que utilizaremos 
from tkinter import *
from tkinter import messagebox as mbx
import json 

#defino el nombre del archivo donde se guardaran los libros 
archivo= "libreria.json"

#abrimos una ventana en la cual pondremos los botones, entradas y etiquetas que usaremo y la nombrare biblioteca unal
ventana= Tk()
ventana.title("biblioteca unal")

#crearemos una funcion para guardar libros en un archivo json
def guardar_libros(lista):
    with open(archivo,"w") as f:
        json.dump(lista, f)

#crearemos una funcion para cargar los libros guardado y en tal casos no hallan libros guardados mostrara una pantalla de error
def cargar_libros():
    try:
        with open(archivo, "r") as f:
            return json.load(f)
    except:  
        return []

#crearemos una funcion para agregar los libros que escribamos en la interfaz grafica
def agregar():
    titulo= Entry_titulo.get()
    autor= entry_autor.get()
    categoria= categoria_var.get()
    #esta linea confirma si hemos llenado las casillas de titulo y autor en la interfaz
    if titulo and autor:
        #esta linea de codigo crea diccionarios con los datos y los añade a la lista de libros
        libros.append({"titulo":titulo, "autor":autor, "categoria":categoria, "disponible": True})
        guardar_libros(libros)
        mostrar(libros)

#crearemos una funcion para buscar los libros por el 
def buscar():
    #pasa a minusculas lo que se escribio en el campo de busqueda 
    clave= entry_buscar.get().lower()
    #se filtra la lista de libros donde solo queden los titulos buscados 
    resultados = [l for l in libros if clave in l["titulo"].lower()]
    mostrar(resultados)

def marcar():
    seleccion= lista.curselection()
    if seleccion:
        texto= lista.get(seleccion[0])
        titulo= texto.split(" - ")[0]
        for l in libros:
            if l["titulo"] == titulo:
                l["disponible"]= not l["disponible"]
        guardar_libros(libros)
        mostrar(libros)

def mostrar(lista_libros):
    lista.delete(0,END)
    for l in lista_libros:
        estado= "disponible" if l["disponible"] else "prestado"
        lista.insert(END, f"{l['titulo']} - {l['autor']} ({l['categoria']}) [{estado}]")


libros= cargar_libros()

#aqui empezaremos a crear la interfaz grafica  
Label(ventana, text= "titulo:",).pack()
Entry_titulo= Entry(ventana)
Entry_titulo.pack()

Label(ventana, text= "autor:").pack()
entry_autor= Entry(ventana)
entry_autor.pack()

#esta funcion es un menu desplegable para seleccionar diferentes opciones
#las cuales seran las categorias a las cuales pertenecen los libros
categoria_var= StringVar()
categoria_var.set("ciencia")
Label(ventana, text= "categorias").pack()
OptionMenu(ventana, categoria_var, "ciencia","literatura","ingenieria").pack()

#crearemos un boton con la funcion de agregar libros 
Button(ventana, text= "agregar libro", command= agregar).pack()

Label(ventana, text= "buscar").pack()
entry_buscar= Entry(ventana)
entry_buscar.pack()
#crearemos un boton que tendra la funcion de buscar libros por titulos 
Button(ventana, text= "buscar libro", command= buscar).pack()

#crearemos un boton para marcar si el libro ha sido prestado o devuelto
Button(ventana, text= "marca prestado o devuelto", command= marcar).pack()

#crearemos una lista la cual mostrara los libros
lista= Listbox(ventana, width=50)
lista.pack()
mostrar(libros)

#usaremos esta funcion para mantener la b¿ventana abierta
ventana.mainloop()