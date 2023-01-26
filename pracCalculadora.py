from tkinter import *

Root= Tk()

Root.title("Calculadora V2") 

miFrame=Frame(Root)
miFrame.pack()

operacion=""

i=0
#-------------------------------Pantalla------------------------------------


Pantalla= Entry(miFrame)
Pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
Pantalla.config(background="black", fg="blue", justify="right")

#-------------------------------Botones-------------------------------------

#-------------------------------Pulsaciones del teclado---------------------

def NumeroPulsado(valor):
	global i
	Pantalla.insert(i, valor)
	i += 1



def borrar():
	Pantalla.delete(0, END)
	i=0





def Realizar_operacion():
	operacion= Pantalla.get()
	respuesta= eval(operacion)
	Pantalla.delete(0, END)
	Pantalla.insert(0, respuesta)
	i=0





#-------------------------------Fila2---------------------------------------

BotonParentIz= Button(miFrame)
BotonParentIz.grid(row=2, column=2, padx=10, pady=10)
BotonParentIz.config(text="(", width=3, command =lambda:NumeroPulsado("("))

BotonParentDe= Button(miFrame)
BotonParentDe.grid(row=2, column=3, padx=10, pady=10)
BotonParentDe.config(text=")", width=3, command =lambda:NumeroPulsado(")"))

BotonLimpiar= Button(miFrame)
BotonLimpiar.grid(row=2, column=1, padx=10, pady=10)
BotonLimpiar.config(text= "c", command=lambda:borrar(), width=3)



BotonDividir= Button(miFrame)
BotonDividir.grid(row=2, column=4, padx=10, pady=10)
BotonDividir.config(text="÷", command =lambda:NumeroPulsado("/"), width=3)

#-----------------------------Fila3----------------------------------------

Boton7= Button(miFrame)
Boton7.grid(row=3, column=1, padx=10, pady=10)
Boton7.config(text="7", width=3, command=lambda:NumeroPulsado(7))

Boton8= Button(miFrame)
Boton8.grid(row=3, column=2, padx=10, pady=10)
Boton8.config(text="8", width=3, command=lambda:NumeroPulsado(8))

Boton9= Button(miFrame)
Boton9.grid(row=3, column=3, padx=10, pady=10)
Boton9.config(text="9", width=3, command=lambda:NumeroPulsado(9))

Botonmult= Button(miFrame)
Botonmult.grid(row=3, column=4, padx=10, pady=10)
Botonmult.config(text="x", width=3,command =lambda:NumeroPulsado("*"))

#-----------------------------Fila4----------------------------------------

Boton4= Button(miFrame)
Boton4.grid(row=4, column=1, padx=10, pady=10)
Boton4.config(text="4", width=3, command=lambda:NumeroPulsado(4))

Boton5= Button(miFrame)
Boton5.grid(row=4, column=2, padx=10, pady=10)
Boton5.config(text="5", width=3, command=lambda:NumeroPulsado(5))

Boton6= Button(miFrame)
Boton6.grid(row=4, column=3, padx=10, pady=10)
Boton6.config(text="6", width=3, command=lambda:NumeroPulsado(6))

Botonrest= Button(miFrame)
Botonrest.grid(row=4, column=4, padx=10, pady=10)
Botonrest.config(text="-", width=3, command =lambda:NumeroPulsado("-"), justify="right")

#-----------------------------Fila5----------------------------------------

Boton1= Button(miFrame)
Boton1.grid(row=5, column=1, padx=10, pady=10)
Boton1.config(text="1", width=3, command=lambda:NumeroPulsado(1))

Boton2= Button(miFrame)
Boton2.grid(row=5, column=2, padx=10, pady=10)
Boton2.config(text="2", width=3, command=lambda:NumeroPulsado(2))

Boton3= Button(miFrame)
Boton3.grid(row=5, column=3, padx=10, pady=10)
Boton3.config(text="3", width=3, command=lambda:NumeroPulsado(3))

Botonsum= Button(miFrame)
Botonsum.grid(row=5, column=4, padx=10, pady=10)
Botonsum.config(text="+", width=3,command =lambda:NumeroPulsado("+"))

#-----------------------------Fila6----------------------------------------

Boton0= Button(miFrame)
Boton0.grid(row=6, column=1, padx=10, pady=10)
Boton0.config(text="0", width=3, command=lambda:NumeroPulsado(0))

BotonComa= Button(miFrame)
BotonComa.grid(row=6, column=2, padx=10, pady=10)
BotonComa.config(text=",", width=3, command =lambda:NumeroPulsado(","))

BotonPunto= Button(miFrame)
BotonPunto.grid(row=6, column=3, padx=10, pady=10)
BotonPunto.config(text=".", width=3, command =lambda:NumeroPulsado("."))

BotonIgual= Button(miFrame)
BotonIgual.grid(row=6, column=4, padx=10, pady=10)
BotonIgual.config(text="=", width=3, command =lambda:Realizar_operacion())











Root.mainloop()



#teorias


#----------------------------------Suma-------------------------------------
#def suma(num):
	#global operacion
	#global resultado
	#resultado+=int(num)
	#operacion="suma"

	#NumeroPantalla.set(resultado)
#
#-----------------------------------Resta----------------------------------------

#def resta(num):
	#global operacion
	#global resultado

	#resultado-=int(num)
	#operacion="Resta"

	#NumeroPantalla.set(resultado)


#------------------------------------Multiplicación---------------------------------

#def multiplicacion(num1, num2):
	#global operacion
	#global resultado

	#resultado=int(num1 * num2)
	#operacion="Multiplicacion"

	#NumeroPantalla.set(resultado)


#------------------------------------Division-----------------------------------

#def division(num):
	#global operacion
	#global resultado

	#resultado= NumeroPantalla.get/num
	#operacion= division

	#NumeroPantalla.set(resultado)

#--------------------------------------Borrador------------------------------------

#def borrar():
	#Pantalla.delete(0, END)
	#resultado=0



#----------------------------------El resultado-------------------------------------
#def El_Resultado():
	#global resultado
	#NumeroPantalla.set(resultado + int(NumeroPantalla.get()))
	#resultado=0
