import random
import sys
from collections import Counter as ct
from collections import defaultdict as df

#exercicio 1
lista = [random.randint(0, 15000) for i in range(500)]
lista_ct = ct(lista)
#print(lista_ct)

#exercicio 2
valor_default = df(lambda:0)
for i in lista:
    valor_default[i] += 1
#print(valor_default)

#exercicio 3
def somar_dois():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print(a + b)

