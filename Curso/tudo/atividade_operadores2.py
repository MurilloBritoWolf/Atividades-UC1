nota = float(input("Digite sua nota: "))
nota1 =float(input("Digite sua nota: "))
frequencia = float(input("Digite a sua frequência: "))

media = nota + nota1 /2

if media >= 7 and frequencia >= 75:
    print("Aprovado")
    print("Sua média e: ",media)
else:
    print("Reprovado")
    print("Sua média e: ",media)
