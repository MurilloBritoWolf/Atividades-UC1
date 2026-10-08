temperatura = int(input("Digite a temperatura: "))

if temperatura > 30:
    print("Muito quente")
elif temperatura >= 20:
    print("Agradável")
elif temperatura >= 10:
    print("Frio")
else:
    print("Muito frio")
