def somar(a, b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

def potencia(a,b):
    return a ** b


def exibir_resultado(a, b, funcao):
    print(f"Voce chamou a funcao  {funcao}")
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 1, somar)  # O resultado da operação 10 + 1 = 11
exibir_resultado(10, 2, subtrair)  # O resultado da operação 10 - 2 = 8
exibir_resultado(10, 3, multiplicar)  # O resultado da operação 10 * 3 = 30
exibir_resultado(10, 4, dividir)  # O resultado da operação 10 / 4 = 2.5

op = potencia

exibir_resultado(10, 4, potencia) # O resultado da operação 10 + 4 = 10000

print(op(23,23))
