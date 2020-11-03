import tkinter

window = tkinter.Tk()
window.geometry("800x500")
'''
etiqueta = tkinter.Label(window, text="hola mundo", bg="blue")

etiqueta.pack(side=tkinter.BOTTOM)  # posicionar
etiqueta.pack(fill=tkinter.X)  # llenar
etiqueta.pack(fill=tkinter.Y, expand=1)
etiqueta.pack(fill=tkinter.BOTH, expand=1)
'''


def saludo(nombre):
    print("hola" + nombre)


'''
boton1 = tkinter.Button(window, text="Presionar", padx=50, pady=100,
                        command=saludo)  # funcion sin (), si lo pongo con parentesis se ejecuta la funcion
'''
'''
boton1 = tkinter.Button(
    window, text="Presionar",
    padx=50, pady=100,command=lambda: saludo(
        'ivancheu'))  # si quiero pasar params, pongo --> lambda: fun()  // ahora si se agrega parenteisis y dentro el parametro
boton1.pack()
'''

# caja de texto que toma un valor con un boton
cajaTexto = tkinter.Entry(window, font="Helvetica 24")
cajaTexto.pack()

def getText():
    codigo = cajaTexto.get()
    print(codigo)

boton1 = tkinter.Button(window, text='tomar', command = getText)
boton1.pack()



window.mainloop()
