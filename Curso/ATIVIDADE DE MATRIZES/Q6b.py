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