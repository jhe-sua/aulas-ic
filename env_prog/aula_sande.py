alunos = ["Joao", "Arthur", "Luis"]
notas = [10, 8.5, 5.4]
materias = ["calulo", "GA", "IC"]
for dados in zip(alunos, notas, materias):
    modo_1 = "O aluno {} tirou {} em {}".format(dados[0], dados[1], dados[2])
    modo_2 = f"O aluno {dados[0]} tirou {dados[1]} em {dados[2]}"
    print(modo_1)
    print(modo_2)


