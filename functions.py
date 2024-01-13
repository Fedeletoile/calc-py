from tkinter import *
from tkinter import ttk

ventana = Tk()

ventana.title("Calculadora")

i = 0

e_texto = Entry(ventana, font= ("calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

btn1 = Button(ventana, text = "1", width = 8, height = 2, bg= 'lightblue', command = lambda: click_button(1))
btn2 = Button(ventana, text = "2", width = 8, height = 2, command = lambda: click_button(2))
btn3 = Button(ventana, text = "3", width = 8, height = 2, bg= 'lightblue', command = lambda: click_button(3))
btn4 = Button(ventana, text = "4", width = 8, height = 2, command = lambda: click_button(4))
btn5 = Button(ventana, text = "5", width = 8, height = 2, bg= 'lightblue', command = lambda: click_button(5))
btn6 = Button(ventana, text = "6", width = 8, height = 2, command = lambda: click_button(6))
btn7 = Button(ventana, text = "7", width = 8, height = 2, bg= 'lightblue', command = lambda: click_button(7))
btn8 = Button(ventana, text = "8", width = 8, height = 2, command = lambda: click_button(8))
btn9 = Button(ventana, text = "9", width = 8, height = 2, bg= 'lightblue', command = lambda: click_button(9))
btn0 = Button(ventana, text = "0", width = 8, height = 2, bg= 'lightblue', command = lambda: click_button(0))

btn_dele = Button(ventana, text = "AC", width = 8, height = 2, command = lambda: dele())
btn_par1 = Button(ventana, text = "(", width = 8, height = 2, bg= 'lightgrey', command = lambda: click_button("("))
btn_par2 = Button(ventana, text = ")", width = 8, height = 2, command = lambda: click_button(")"))
btn_dot = Button(ventana, text = ".", width =  8, height = 2, command = lambda: click_button("."))
btn_comma = Button(ventana, text = ",", width =  8, height = 2, command = lambda: click_button(","))

btn_sum = Button(ventana, text = "+", width = 8, height = 2, command = lambda: click_button("+"))
btn_rest = Button(ventana, text = "-", width = 8, height = 2, bg= 'lightgrey', command = lambda: click_button("-"))
btn_div = Button(ventana, text = "/", width = 8, height = 2, bg= 'lightgrey', command = lambda: click_button("/"))
btn_mult = Button(ventana, text = "x", width = 8, height = 2, command = lambda: click_button("*"))
btn_equal = Button(ventana, text = "=", width = 8, height = 2, bg= 'lightgrey', command = lambda: realizar_op())


btn_dele.grid(row = 1, column = 0, padx = 3, pady = 3,)
btn_par1.grid(row = 1, column = 1, padx = 3, pady = 3,)
btn_par2.grid(row = 1, column = 2, padx = 3, pady = 3,)
btn_div.grid(row = 1, column = 3, padx = 3, pady = 3,)
btn_mult.grid(row = 2, column = 3, padx = 3, pady = 3,)
btn_rest.grid(row = 3, column = 3, padx = 3, pady = 3,)
btn_sum.grid(row = 4, column = 3, padx = 3, pady = 3, )
btn1.grid(row = 4, column = 0, padx = 3, pady = 3,)
btn2.grid(row = 4, column = 1, padx = 3, pady = 3,)
btn3.grid(row = 4, column = 2, padx = 3, pady = 3,)
btn4.grid(row = 3, column = 0, padx = 3, pady = 3,)
btn5.grid(row = 3, column = 1, padx = 3, pady = 3,)
btn6.grid(row = 3, column = 2, padx = 3, pady = 3,)
btn7.grid(row = 2, column = 0, padx = 3, pady = 3,)
btn8.grid(row = 2, column = 1, padx = 3, pady = 3,)
btn9.grid(row = 2, column = 2, padx = 3, pady = 3,)
btn0.grid(row = 5, column = 1, padx = 3, pady = 3,)
btn_equal.grid(row = 5, column = 3, padx = 3, pady = 3,)
btn_dot.grid(row = 5, column = 0, padx = 3, pady = 3,)
btn_comma.grid(row = 5, column = 2, padx = 3, pady = 3,)


# if __name__ == '__main__':
#     print("ok")

def click_button(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def dele():
    e_texto.delete(0, END)
    i = 0

def realizar_op():
    ec = e_texto.get()
    result = eval(ec)
    e_texto.delete(0, END)
    e_texto.insert(0, result)
    i = 0


ventana.mainloop()




# def suma(a, b):
#     return a + b
# def resta(a, b):
#     return a - b
# def multip(a, b):
#     return a * b
# def division(a, b):
#     return a / b
# def potencia(a, b):
#     return a ** b 

# num1 = float(input("Ingrese un numero: "))
# num2 = float(input("Ingrese otro numero: "))

# op = 0

# while op != 6:
#     print("""
#     Operacion a realizar:
#     1- Suma
#     2- Resta
#     3- Multiplicacion
#     4- Division
#     5- Potencia
#     6- Salir
#     """)

#     op = int(input())

#     if op == 1:
#         print(suma(num1, num2))
#     if op == 2:
#         print(resta(num1,num2))
#     if op == 3:
#         print(multip(num1, num2))
#     if op == 4:
#         print(division(num1, num2))
#     if op == 5:
#         print(potencia(num1, num2))
#     if op == 6:
#         print("Hasta luego y muchas gracias")
#     else:
#         print("Ingrese un numero valido por favor")



