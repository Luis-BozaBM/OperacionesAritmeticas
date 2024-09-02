import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacion = operacion_var.get()

        if operacion == "Suma":
            resultado = num1 + num2
        elif operacion == "Resta":
            resultado = num1 - num2
        elif operacion == "Multiplicación":
            resultado = num1 * num2
        elif operacion == "División":
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir entre cero.")
                return
            resultado = num1 / num2
        else:
            messagebox.showerror("Error", "Operación no válida.")
            return

        label_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")


ventana = tk.Tk()
ventana.title("Calculadora")

tk.Label(ventana, text="Número 1:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(ventana, text="Número 2:").grid(row=1, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

operacion_var = tk.StringVar(value="Suma")
tk.Radiobutton(ventana, text="Suma", variable=operacion_var, value="Suma").grid(row=2, column=0, padx=10, pady=10)
tk.Radiobutton(ventana, text="Resta", variable=operacion_var, value="Resta").grid(row=2, column=1, padx=10, pady=10)
tk.Radiobutton(ventana, text="Multiplicación", variable=operacion_var, value="Multiplicación").grid(row=3, column=0,
                                                                                                    padx=10, pady=10)
tk.Radiobutton(ventana, text="División", variable=operacion_var, value="División").grid(row=3, column=1, padx=10,
                                                                                        pady=10)

tk.Button(ventana, text="Calcular", command=calcular).grid(row=4, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.grid(row=5, column=0, columnspan=2, pady=10)

ventana.mainloop()


def suma(a, b):
    numeroOne = float(input("Ingresa un numero: "))
    numeroDos = float(input("Ingresa un numero"))
    resultado = numeroOne * numeroDos
    print(f"El resultado es : {resultado}")

suma(6, 8)
