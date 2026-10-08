compra = float(input("digite o valor da sua compra: "))

if compra >= 200: 
    desconto = compra * 0.10
    valortotal = compra - desconto
    print("O valor da sua comprar com o desconto e de: ",valortotal)
else:
    print("O valor da sua compra e de: ",compra)