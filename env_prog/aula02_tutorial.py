from math import sqrt as sq
import math
import sys

#pip8 contem as convenções de estilo

def minha_funcao():
    a = float(sys.argv[1])
    b = float(sys.argv[2])

    print(a+b)

if __name__ == "__main__":
    minha_funcao()
    print(locals() == globals())