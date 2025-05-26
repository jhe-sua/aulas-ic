#compresion de diccionario
numero_cuadrado = {x: x**2 for x in range(10)}
print(numero_cuadrado)

#sin compresion
numero_cuadrado2 = {}

for x in range(10):
    numero_cuadrado2[x] = x**2

print(numero_cuadrado2)

vazio = {}
chaves_numeros = iter(numero_cuadrado2)
teste = vazio.fromkeys(chaves_numeros, "pepe")

print(vazio)
print(teste)
