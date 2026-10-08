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
