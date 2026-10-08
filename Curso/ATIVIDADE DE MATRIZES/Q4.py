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