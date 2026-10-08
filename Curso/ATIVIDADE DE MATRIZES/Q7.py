############# Exercicio 7 #############

notas = []
aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(5):
    aluno = []
    print("Aluno", i + 1)

for j in range(3):
    nota = float(input("Digite a nota: "))
    aluno.append(nota)

notas.append(aluno)

print("===== RELATORIO =====")

for i in range(5):
    media = sum(notas[i]) / 3

if media > 7:
    situacao = "Aprovado"
    aprovados += 1
elif media >= 5:
    situacao = "Recuperacao"
    recuperacao += 1
else:
    situacao = "Reprovado"
    reprovados += 1

print("Aluno", i + 1, "- Media:",
round(media, 2), "-", situacao)

print()
print("Aprovados:", aprovados)
print("Recuperacao:", recuperacao)
print("Reprovados:", reprovados)

maior = max(max(linha) for linha in notas)
menor = min(min(linha) for linha in notas)

soma = 0
for linha in notas:
    soma += sum(linha)

media_geral = soma / 15

print("Maior nota da turma:", maior)
print("Menor nota da turma:", menor)
print("Media geral:", round(media_geral, 2))