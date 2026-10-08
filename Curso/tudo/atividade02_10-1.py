# EXERCÍCIO 1 
linguagens = ["Python", "JavaScript", "Java", "C++", "lua"]

print("Primeira linguagem:", linguagens[0])

print("Terceira linguagem:", linguagens[2])

print("Última linguagem:", linguagens[-1])#O -1 ele retorna o valor da última posição do vetor

print("Quantidade de linguagens digitadas é:", len(linguagens))

#EXERCÍCIO 2
lista_compras = []

for i in range(5):
    produto = input(f"Digite o produto {i + 1}: ")
    lista_compras.append(produto)

print("========== lista de compras ==========")

for produto in lista_compras:
    print(produto)

# EXERCÍCIO 3

numeros = []

for i in range(8):
    num = int(input(f"Digite o {i + 1}° número: "))
    numeros.append(num)

print("Os números pares encontrados são:")

for num in numeros:
    if num % 2 == 0:
        print(num)

# EXERCÍCIO 4

notas = []

for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

print("Todas as notas:", notas)

media = sum(notas) / len(notas)
print("Média das notas:", media)

print("Maior nota:", max(notas))

print("Menor nota:", min(notas))

# EXERCÍCIO 5 
produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Headset"]

busca = input("Digite o produto que deseja procurar: ")

if busca in produtos:
    print("Produto encontrado!")
else:
    print("Produto não encontrado!")

# EXERCÍCIO 6
valores = [12, 45, 7, 89, 23, 56, 3, 78]

maior = valores[0]

for num in valores:

    if num > maior:
   
        maior = num

print("O maior número da lista é:", maior)
