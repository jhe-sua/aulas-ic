l = []

#estrutura basica do "for"
for i in range(1000):
    if i % 100 == 0:
        l.append(i)

print(l)

#e possivel somar listas
print(l+l)

#tipo boolean
Verdadeiro = True
Falso = False

#estrutura basica do match

x = "1"
match x:
    case "1":
        print("El pepe")
    case _:
        print

#containers termos as sequencias e as no sequencias
#   sequencias: tuple, list, string
#   no sequencia: dict, set

s = {3, "a", "d"}
print(type(s))

# função construtora de um set
t = set("abacaxi")
print(t)

print(s.union(t))
print(s.intersection(t))
print(s-t)

#dict = coleccion
d = {"adlid": 13, "alejandro": 13, "angel": 18, "miguel": 21, "david": 23, "ada": 25}
print(d.keys())
print(d.values())

#definiendo funções
def fib(n):
    """Secuencia de fibonaci com n elemntos"""
    a, b = 0, 1
    
    for i in range(n):
        print(a, end=" ")
        a, b = b, b+a
    else:
        print()

fib(10)

#trabalhando com tuplas

for n, i in d.items():
    print(f"nome: {n}\nidade: {i}\n---")

for i in d.items():
    print(f"nome e idade: {i[0]}, {i[1]}")