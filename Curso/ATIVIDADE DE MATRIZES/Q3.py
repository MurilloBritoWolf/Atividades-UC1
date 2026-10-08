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
