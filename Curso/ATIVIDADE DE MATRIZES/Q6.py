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