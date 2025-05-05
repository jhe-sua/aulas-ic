
#Função vazia sem erros pelo interpretador
#def myfuction(A):
#    pass

c = 5

def mynum(b):
    match b:
        case 1:
            return "Numero 1"
        case 2:
            return "Numero 2"
        case 3:
            return "Numero 3"
        case 5 | 6 | 7:
            return "bad numero"
        case _:
            return "Outro numero que não é 1, 2 ou 3"
        
print(mynum(c))
