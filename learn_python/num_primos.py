numerosP = []

for n in range(2, 1000):
    for x in range(2, n):
        if n % x == 0:
#            print(n, 'é igual a', x, '*', n//x)
            break
    else:
        #ao final do loop isto se executa se o loop não for finalizado pelo break
        numerosP.append(n)

print(numerosP, "a quantidade de numeros primos é" ,len(numerosP))

#Numeros primos palindromos 
numerosPl = []

for num in numerosP:
    #iinvertendo numero
    q = int(str(num)[::-1])
    if q in numerosP:
        numerosPl.append(num)

print(numerosPl, "a quantidade de numeros primos palindromos é", len(numerosPl))

    
