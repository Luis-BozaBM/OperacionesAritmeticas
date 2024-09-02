

def ingresoNumeros():
    numeroUno = float(input("Ingresa un numero: "))
    numeroDos = float(input("Ingresa un numero"))
    return numeroUno, numeroDos
def suma(numeroUno, numeroDos):
    return numeroUno + numeroDos


if __name__ == '__main__':
    num1, num2 = ingresoNumeros()
    print(f"{num1} + {num2} = {suma(num1 + num2)}")



