from math import sqrt

print("Aula 02", end="\n\n")

#Atribuição condicional (se ternario):
x = -1
y = sqrt(x) if x > 0 else "numero complexo" if x == 2 else "el pepe"
print(y)

#Tipo None, é o valor predefinido 
def fuction():
    pass

# operadores in e is
# is é utilizada para saber se dois ponteiros apontam ao mesmo objeto
# por isso é diferente de == que apenas compara valores
# se tivermos x e y, e y is x retornar true, se atribuirmos algo ao "x" o "y" tambem muda.
x = [4,6]
y = [4,6]

print(x == y)
print(x is y)

#atribuindo mais de um ponteiro
x = y = (1,2,3)

print(x == y)
print(x is y)

#in, é p equivalente ao ∈ da matrmatica

l = [1,2,3]
k = [[1,2,3],4,5]

print(l in k)

