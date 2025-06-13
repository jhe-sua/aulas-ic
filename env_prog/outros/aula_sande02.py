alunos = ["pepe", "joao","pedro","miguel","joao","joao","joao",("pepe", "joao","pedro","miguel","joao","joao","joao")]
set_alunos = set(alunos)
print(len(set_alunos))
set_alunos.add("meninino")
print(set_alunos)
set_alunos.add("meninino")
print(set_alunos)

print("meninino" in set_alunos)