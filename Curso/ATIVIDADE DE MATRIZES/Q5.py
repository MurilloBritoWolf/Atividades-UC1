############# Exercicio 5 #############
notas = []

for i in range(3):
    aluno = []

print("Aluno", i + 1)

for j in range(3):
    nota = float(input("Digite a nota: "))
aluno.append(nota)

notas.append(aluno)

for i in range(3):
    media = sum(notas[i]) / 3
    print("Aluno", i + 1, "- Media:", round(media, 2))
