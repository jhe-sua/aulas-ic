"""Calculadora Simples"""
import os
import sys

def limpa_tela():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def calculadora():
    """
    retorna o valor de uma conta
    :param:
        conta: expressão aritmetica
    """
    conta = input("Escreva uma conta aritmetica simples: ")
    print(eval(conta))

def calc2(operandos, operador):
    conta = f'{operandos[0]}'
    for o in operandos[1:]:
        conta += operador + str(o)
    return eval(conta)

def calc3():
    conta = ""
    while True:
        o = input("Numero: ")
        op = input("digite operador: ")
        p = input("Numero: ")

        fim = input("para sair aperte enter")
        if fim == "":
            print(eval (f"{o}{op}{p}"))
            return

def calc4():
    """
    calculadora interativa
    """
    resultado = ""
    
    while True:
        conta = input(f"escreva uma conta simples \n\n {resultado} ")
        resultado = eval(str(resultado) + conta)
        limpa_tela()

# o * significa que passara um ou mais argumentos, isso define a variavel como uma tupla
def calc5(*ops):
    """
    soma numero arbitrario de argumentos
    """
    return sum(ops)


    

        