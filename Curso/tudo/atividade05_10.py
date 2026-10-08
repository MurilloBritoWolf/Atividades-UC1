
############# Exercicio 1 #############
matriz = [
[10, 20, 30],
[40, 50, 60],
[70, 80, 90]
]

print("Linha 0, coluna 1:", matriz[0][1])
print("Linha 1, coluna 2:", matriz[1][2])
print("Linha 2, coluna 0:", matriz[2][0])




############# Exercicio 2 #############


matriz = [
[5, 8, 3],
[2, 7, 9],
[4, 6, 1]
]

print("Todos os elementos:")
for linha in matriz:
    for numero in linha:
        print(numero)

print("Numeros pares:")
for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            print(numero)

print("Numeros maiores que 5:")
for linha in matriz:
    for numero in linha:
        if numero > 5:
            print(numero)

############# Exercicio 3 #############

matriz = [
[7, 8, 9],
[5, 6, 7],
[8, 9, 10]
]

soma = 0
maior = matriz[0][0]
menor = matriz[0][0]

for linha in matriz:
    for numero in linha:
        soma += numero

if numero > maior:
    maior = numero

if numero < menor:
    menor = numero

media = soma / 9

print("Soma:", soma)
print("Media:", media)
print("Maior:", maior)
print("Menor:", menor)

############# Exercicio 4 #############
matriz = []

for i in range(2):
    linha = []

for j in range(3):
    numero = int(input(f"Digite o valor [{i}][{j}]: "))
linha.append(numero)

matriz.append(linha)

print("Matriz:")
for linha in matriz:
    print(linha)

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

############# Exercicio 6 A -#############
assentos = [
[0, 1, 0, 0],
[1, 1, 0, 0],
[0, 0, 0, 1]
]

livres = 0
ocupados = 0

for linha in assentos:
    for assento in linha:
        if assento == 0:
            livres += 1
else:
    ocupados += 1

print("Assentos disponiveis:", livres)
print("Assentos ocupados:", ocupados)
############# Exercicio 6 B -#############
assentos = [
[0, 1, 0, 0],
[1, 1, 0, 0],
[0, 0, 0, 1]
]

linha = int(input("Digite a linha (0 a 2): "))
coluna = int(input("Digite a coluna (0 a 3): "))

if 0 <= linha < 3 and 0 <= coluna < 4:
    if assentos[linha][coluna] == 0:
        print("Assento esta disponivel!")
    else:
        print("Assento esta ocupado!")
else:
    print("Assento invalido!")
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
