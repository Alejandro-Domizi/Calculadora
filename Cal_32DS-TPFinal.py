from tkinter import *
import tkinter as tk
from math import *
from tkinter import EXCEPTION, font
from tkinter import ttk
from tkinter.constants import ANCHOR, DISABLED
from tkinter import messagebox


#defino una funcion limpieza para borrar el contenido del calculo de la tabla 1 y 2
def limpiezatab1():
    global operaciontab1
    calculotab1.set('0') #pone un cero en la pantalla
    operaciontab1 = ''   #borra la cuenta de la consola

def limpiezatab2():
    global operaciontab2
    calculotab2.set('0') #pone un cero en la pantalla
    operaciontab2 = ''   #borra la cuenta de la consola

#defino la funcion que almacena las pulsaciones de las teclas
def pulsartab1(tecla):
    global operaciontab1
    operaciontab1 = operaciontab1 + tecla
    calculotab1.set(operaciontab1)
    

def pulsartab2(tecla):
    global operaciontab2
    operaciontab2 = operaciontab2 + tecla
    calculotab2.set(operaciontab2)

#Defino la funcion que actua al tocar el =

def hacer_cuentatab1():
    global operaciontab1
    try:
        total = str(eval(operaciontab1))
    except Exception:
        limpiezatab1()
        total = 'ERROR' 
    calculotab1.set(total)
    operaciontab1 = total

def hacer_cuentatab2():
    global operaciontab2
    try:
        total = str(eval(operaciontab2))
    except Exception:
        limpiezatab2()
        total = 'ERROR' 
    calculotab2.set(total)
    operaciontab2 = total
    


def borrartab1():
    global operaciontab1
    lista = []
    #creo una lista con los valores de operacion
    for i in range(len(operaciontab1)):
        lista.append(operaciontab1[i])
    #borro el ultimo caracter
    lista =  lista [:-1]
    operaciontab1 =  ''.join(lista)
    #muestro la cadena en la pantalla
    calculotab1.set(operaciontab1)


def borrartab2():
    global operaciontab2
    lista = []
    #creo una lista con los valores de operacion
    for i in range(len(operaciontab2)):
        lista.append(operaciontab2[i])
    #borro el ultimo caracter
    lista =  lista [:-1]
    operaciontab2 =  ''.join(lista)
    #muestro la cadena en la pantalla
    calculotab2.set(operaciontab2)



#ventana para contener la calculadora

root = Tk()
root.iconbitmap('1234.ico')
root.title('CalDomSco')
root.geometry('590x775')
root.resizable(0,0)

#Creacion de solapas
tabcontrol = ttk.Notebook(root)
tabcontrol.pack(fill='both', expand='yes')
tabcontrol.config(width = 590, height = 775)
tab1 = tk.Frame(tabcontrol)
tab2 = tk.Frame(tabcontrol)
tab3 = tk.Frame(tabcontrol)
tabcontrol.add(tab1, text='Calculadora')
tabcontrol.add(tab2, text='Calculadora Cientifica')
tabcontrol.add(tab3, text='Calculadora IMC')
tab1.config (bg = '#778899')
tab2.config (bg = '#0085A5')
tab3.config (bg = '#751371')


#Funcion de about_us

def about_us():
    messagebox.showinfo('Calculadora', 'Este proyecto se realiza para Programacion II 32DS con Python-Tkinter')

#creamos la barra de menu y submenu

menubar = Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)

#creamos las variables para mostrar el calculo en la pantalla

calculotab1 = tk.StringVar()
calculotab2 = tk.StringVar()
calculoPesotab3 = tk.StringVar()
calculoAlturatab3 = tk.StringVar()

#llamo a la funcion limpieza para inicializar la calculadora
limpiezatab1()
limpiezatab2()



#creamos la pantalla tab1

pantalla = Entry(tab1, font = ('arial',17,'bold'), 
                    width= 37,
                    bd= 15, 
                    justify = 'right', 
                    state = tk.DISABLED,
                    textvariable= calculotab1
                )

pantalla.place(x = 35, y= 40)

#creamos la pantalla tab2

pantalla2 = Entry(tab2, font = ('arial',17,'bold'), 
                    width= 37,
                    bd= 15, 
                    justify = 'right', 
                    state = tk.DISABLED,
                    textvariable= calculotab2
                )

pantalla2.place(x = 35, y= 20)

#creamos la pantalla tab3

pantalla3 = Entry(tab3, font = ('arial',17,'bold'), 
                    width= 37,
                    bd= 15, 
                    justify = 'right', 
                    state = tk.DISABLED,
                    
                )

pantalla3.place(x = 30, y= 40)


#pantalla3 = tk.Frame(tabcontrol)
imagetab3=PhotoImage(file="IMC.png")
pantalla3image=Label(tab3, image=imagetab3)
pantalla3image.place(x=0 , y=405)

#defino las dimensiones de las teclas
ancho = 9
alto = 2
ancho1 = 9
alto1 = 1
alto2 = 3
ancho2 = 45
alto3 = 3
ancho3 = 58

#creo una variable para almacenar el calculo del lado de consola
operaciontab1 = ''
operaciontab2 = ''



#BOTONES tab1 calculadora normal

#Primera fila: 1 2 3 +
buttonFont = font.Font( size=11, weight='bold')
boton1 = Button(tab1, text='1', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab1('1')).place(x=70, y=220)

boton2 = Button(tab1,text='2', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab1('2')).place(x=180, y=220)

boton3 = Button(tab1,text='3', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab1('3')).place(x=290, y=220)

boton_suma = Button(tab1,text='+', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab1('+')).place(x=400, y=220)

#Segunda fila: 4 5 6 -

boton4 = Button(tab1,text='4', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab1('4')).place(x=70, y=295)

boton5 = Button(tab1,text='5', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab1('5')).place(x=180, y=295)

boton6 = Button(tab1,text='6', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab1('6')).place(x=290, y=295)

boton_resta = Button(tab1,text='-', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab1('-')).place(x=400, y=295)

#tercera fila: 7 8 9 x

boton7 = Button(tab1,text='7', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab1('7')).place(x=70, y=370)

boton8 = Button(tab1,text='8', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab1('8')).place(x=180, y=370)

boton9 = Button(tab1,text='9', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab1('9')).place(x=290, y=370)

boton_por = Button(tab1,text='x', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab1('*')).place(x=400, y=370)

#Cuarta fila: ( 0 ) /

boton_par_izq = Button(tab1,text='(', width=ancho, height=alto, bg='gray36', border="8", font=buttonFont, command=lambda:pulsartab1('(')).place(x=70, y=445)

boton0 = Button(tab1,text='0', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab1('0')).place(x=180, y=445)

boton_par_der = Button(tab1,text=')', width=ancho, height=alto, bg='gray36', border="8", font=buttonFont, command=lambda:pulsartab1(')')).place(x=290, y=445)

boton_division = Button(tab1,text='/', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab1('/')).place(x=400, y=445)

#Quinta fila: Raiz, coma decimal, potencia, resto

boton_raiz = Button(tab1,text='√', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab1('sqrt(')).place(x=70, y=520)

boton_coma = Button(tab1,text='.', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab1('.')).place(x=180, y=520)

boton_potencia = Button(tab1,text='EXP', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab1('**')).place(x=290, y=520)

boton_resto = tk.Button(tab1,text='%', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab1('%')).place(x=400, y=520)


#Sexta Fila: Clear, Factorial, Pi, =, Del

boton_clear = Button(tab1,text='C', width=ancho, height=alto, bg='red3', border="8", fg='white', font=buttonFont, command=limpiezatab1).place(x=70, y=595)

boton_factorial = Button(tab1,text='!', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab1('factorial(')).place(x=180, y=595)

boton_pi = Button(tab1,text='π', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab1(str(pi))).place(x=290, y=595)

boton_igual = Button(tab1,text='=', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=hacer_cuentatab1).place(x=400, y=595)

boton_borrar = Button(tab1,text='DEL', width=ancho2, height=alto, bg='green4', border="10", font=buttonFont, command=borrartab1).place(x=70, y=670)



#BOTONES tab2 Calculadora cientifica

#Primera fila: 1 2 3 +
buttonFont = font.Font( size=11, weight='bold')
boton1 = Button(tab2, text='1', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab2('1')).place(x=70, y=220)

boton2 = Button(tab2,text='2', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab2('2')).place(x=180, y=220)

boton3 = Button(tab2,text='3', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab2('3')).place(x=290, y=220)

boton_suma = Button(tab2,text='+', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab2('+')).place(x=400, y=220)

#Segunda fila: 4 5 6 -

boton4 = Button(tab2,text='4', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab2('4')).place(x=70, y=295)

boton5 = Button(tab2,text='5', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab2('5')).place(x=180, y=295)

boton6 = Button(tab2,text='6', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab2('6')).place(x=290, y=295)

boton_resta = Button(tab2,text='-', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab2('-')).place(x=400, y=295)

#tercera fila: 7 8 9 x

boton7 = Button(tab2,text='7', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab2('7')).place(x=70, y=370)

boton8 = Button(tab2,text='8', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab2('8')).place(x=180, y=370)

boton9 = Button(tab2,text='9', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab2('9')).place(x=290, y=370)

boton_por = Button(tab2,text='x', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab2('*')).place(x=400, y=370)

#Cuarta fila: ( 0 ) /

boton_par_izq = Button(tab2,text='(', width=ancho, height=alto, bg='gray36', border="8", font=buttonFont, command=lambda:pulsartab2('(')).place(x=70, y=445)

boton0 = Button(tab2,text='0', width=ancho, height=alto, bg='ghost white', border="8", font=buttonFont, command=lambda:pulsartab2('0')).place(x=180, y=445)

boton_par_der = Button(tab2,text=')', width=ancho, height=alto, bg='gray36', border="8", font=buttonFont, command=lambda:pulsartab2(')')).place(x=290, y=445)

boton_division = Button(tab2,text='/', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab2('/')).place(x=400, y=445)

#Quinta fila: Raiz, coma decimal, potencia, resto

boton_raiz = Button(tab2,text='√', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab2('sqrt(')).place(x=70, y=520)

boton_coma = Button(tab2,text='.', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab2('.')).place(x=180, y=520)

boton_potencia = Button(tab2,text='EXP', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab2('**')).place(x=290, y=520)

boton_resto = tk.Button(tab2,text='%', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab2('%')).place(x=400, y=520)


#Sexta Fila: Clear, Factorial, Pi, =, Del

boton_clear = Button(tab2,text='C', width=ancho, height=alto, bg='red3', border="8", fg='white', font=buttonFont, command=limpiezatab2).place(x=70, y=595)

boton_factorial = Button(tab2,text='!', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab2('factorial(')).place(x=180, y=595)

boton_pi = Button(tab2,text='π', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=lambda:pulsartab2(str(pi))).place(x=290, y=595)

boton_igual = Button(tab2,text='=', width=ancho, height=alto, bg='gray64', border="8", font=buttonFont, command=hacer_cuentatab2).place(x=400, y=595)

boton_borrar = Button(tab2,text='DEL', width=ancho2, height=alto, bg='green4', border="10", font=buttonFont, command=borrartab2).place(x=70, y=670)

# tan, ln, sin, cos

botontan = Button(tab2, text='tan', width=ancho1, height=alto1,bg='dark orange', border="8", font=buttonFont, command=lambda:pulsartab2('tan(')).place(x=70,y=100)

botonln = Button(tab2, text='ln', width=ancho1, height=alto1,bg='dark orange', border="8", font=buttonFont, command=lambda:pulsartab2('log(')).place(x=180,y=100)

botonsin = Button(tab2, text='sin', width=ancho1, height=alto1,bg='dark orange', border="8", font=buttonFont, command=lambda:pulsartab2('sin(')).place(x=290,y=100)

botoncos =Button(tab2, text='cos', width=ancho1, height=alto1,bg='dark orange', border="8", font=buttonFont, command=lambda:pulsartab2('cos(')).place(x=400,y=100)

#arctan, log, arsin, arccos

botonarctan = Button(tab2, text='arctan', width=ancho1, height=alto1,bg='dark orange', border="8", font=buttonFont, command=lambda:pulsartab2('atan(')).place(x=70, y=155)

botonlog = Button(tab2, text='log', width=ancho1, height=alto1,bg='dark orange', border="8", font=buttonFont, command=lambda:pulsartab2('log10(')).place(x=180,y=155)

botonarcsin = Button(tab2, text='arcsin', width=ancho1, height=alto1, bg='dark orange', border="8", font=buttonFont, command=lambda:pulsartab2('asin(')).place(x=290,y=155)

botonarccos = Button(tab2, text='arccos', width=ancho1, height=alto1,bg='dark orange', border="8", font=buttonFont, command=lambda:pulsartab2('acos(')).place(x=400,y=155)


#tab3 Calculadora IMC

# ------- Funciones --------


def calculotab3():
    try:
        calculoPesotab3 = float(pantallaPeso.get())  # * entry.get recibe la información, la procesa y la envía a una etiqueta vacía['text'] que es donde aparecerá el resultado de la cuenta
        calculoAlturatab3 = float(pantallaAltura.get().replace(',', '.'))  # * recibe los valores en una entrada y envía el resultado en una etiqueta 

        imc = calculoPesotab3 / (calculoAlturatab3 ** 2)

        resultado = imc
    
        if resultado <= 18.5:
            label_imc_texto['text'] = 'Su IMC es:  Bajo de peso'
        elif 18.5 <= resultado <= 24.99:
            label_imc_texto['text'] = 'Su IMC es:  Normal'
        elif 25 <= resultado <= 29.99:
            label_imc_texto['text'] = 'Su IMC es:  Sobrepeso'
        elif 30 <= resultado <= 34.99:
            label_imc_texto['text'] = 'Su IMC es:  Obesidad Grado 1'
        elif 35 <= resultado <= 39.99:
            label_imc_texto['text'] = 'Su IMC es:  Obesidad grado 2'
        elif resultado >= 40:
            label_imc_texto['text'] = 'Su IMC es:  Obesidad morbida'

        pantallaPeso.delete(0, "end")
        pantallaAltura.delete(0, "end")
        
    except:
        messagebox.showinfo(
            '¡Atención!', 'Rellena todos los campos con sus respectivos atributos.\n')
        pantallaPeso.delete(0, "end")
        pantallaAltura.delete(0, "end")
        return

    resultadoStr = str(resultado)
    label_imc_resultado['text'] = resultadoStr[:5]
    label_imc_texto['text'] = '{:.{}f}'.format(resultado).replace(',', '.')  # cuenta: el IMC va en el cuadrado azul, de acuerdo con los números enviados en las entradas de altura y peso

# ------- Etiqueta Superior "Resultado."  --------

label_imc_resultado = Label(tab3, text='', width=ancho3, height=alto3, bg = 'Gray', font='Ivy 11 bold', anchor='center', borderwidth=4, relief="sunken")
label_imc_resultado.place(x=30, y=35) 

    
# ------- Etiqueta "Su IMC es: "  --------

label_imc_texto = Label(tab3, text='', width=ancho2, height=alto2, bg = 'Gray', font='Ivy 11 bold', anchor='center', borderwidth=4, relief="sunken")
label_imc_texto.place(x=90, y=520)   

# Obtener y almacenar datos 


# Titulo

Label (tab3, text = "Calcule su indice de masa corporal", font = "Georgia 20", fg = "white", bg = '#751371').place (x = 70, y = 125)


#texto de peso

peso_label = Label(tab3, text = 'Ingrese su peso:', fg = 'white', font = 'arial 17', bg='#751371')
peso_label.place( x = 50, y = 200 )
kg_label = Label(tab3, text = 'Kg', fg = 'white', font = 'arial 17', bg='#751371')
kg_label.place( x = 480, y = 200 )

#Cuadro de peso

pantallaPeso = Entry(tab3, font = ('arial',17,'bold'), 
                    width= 12,
                    bd= 10, 
                    justify = 'right', 
                )
pantallaPeso.place(x = 270, y= 190)

# Texto de altura

altura_label = Label(tab3, text = 'Ingrese su altura:', fg = 'white', font = 'arial 17', bg='#751371')
altura_label.place( x = 50, y = 260 )

cm_label = Label(tab3, text = 'Cm', fg = 'white', font = 'arial 17', bg='#751371')
cm_label.place( x = 480, y = 260 )

#Cuadro de altura

pantallaAltura = Entry(tab3, font = ('arial',17,'bold'), 
                    width= 12,
                    bd= 10, 
                    justify = 'right', 
                )
pantallaAltura.place(x = 270, y= 250)





# boton calcular IMC

label_confirmar = Button(tab3, command=calculotab3, text = 'Calcular IMC', relief=RAISED, font = 'arial 12 bold', fg = 'black', width=ancho2, overrelief=RIDGE, height=alto1, bg='#B0B724', border="8").place(x=70, y=330)


root.mainloop()