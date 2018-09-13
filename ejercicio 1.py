from tkinter import*

def calcular():
    ubica=enEUbicacion.get()
    tipo=enETipoVenta.get()
    cantidad=int(enECantidad.get())
    

    if(ubica=="Palco" and tipo=="Pre-venta"):
        ValorVenta = 22000*cantidad
        aporte=ValorVenta*0.15
                     
    enEValorVenta.insert(ValorVenta)
    enEAporte.insert(aporte)


teatro = Tk()
teatro.title("UV-Teatro")
teatro.geometry("200x160")
                

ventanaEntradas = Frame(teatro,pady = 10)
etEUbicacion = Label(ventanaEntradas, text="Ubicación")
etEUbicacion.grid(row=0, column=0)
enEUbicacion = Entry(ventanaEntradas, width = 10)
enEUbicacion.grid(row=0,column=1)
etETipoVenta = Label(ventanaEntradas, text="Tipo")
etETipoVenta.grid(row=1, column=0)
enETipoVenta = Entry(ventanaEntradas, width = 10)
enETipoVenta.grid(row=1,column=1)
etECantidad = Label(ventanaEntradas, text="Cantidad")
etECantidad.grid(row=2, column=0)
enECantidad = Entry(ventanaEntradas, width = 10)
enECantidad.grid(row=2,column=1)
etCalcular = Button(ventanaEntradas, text="Calcular Valores", command=calcular)
etCalcular.grid(row=3,columnspan=2)
etEValorVenta = Label(ventanaEntradas, text="Valor venta")
etEValorVenta.grid(row=4, column=0)
enEValorVenta = Entry(ventanaEntradas, width = 10)
enEValorVenta.grid(row=4,column=1)
etEAporte = Label(ventanaEntradas, text="Valor aporte")
etEAporte.grid(row=5, column=0)
enEAporte = Entry(ventanaEntradas, width = 10)
enEAporte.grid(row=5,column=1)


ventanaEntradas.pack()


teatro.mainloop()
