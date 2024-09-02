class OperacionesAritmeticas:
    def ingresoNumeros(self):
        numeroUno = float(input("Ingresa un numero: "))
        numeroDos = float(input("Ingresa un numero: "))
        return numeroUno, numeroDos

    def suma(self, numeroUno, numeroDos):
        return numeroUno + numeroDos


if __name__ == '__main__':
    operacion = OperacionesAritmeticas()
    num1, num2 = operacion.ingresoNumeros()
    print(f"{num1} + {num2} = {operacion.suma(num1, num2)}")