matriz = [
    [10, 20, 30],
    [40, 50, 60]
]

# O i e a linha
# O j e a coluna
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print("Linha:", i)
        print("Coluna:", j)
        print("Valor:", matriz[i][j])


matriz = []

for i in range(3):
    linha = []

    for j in range(3):
        numero = int(input("Digite um número: "))
        linha.append(numero)

    matriz.append(linha)


    print(matriz)

    
    for linha in matriz:
        print(linha)

        