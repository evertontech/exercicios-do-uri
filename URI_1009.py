nomeVendedor = str(input())
salarioFixo = float(input())
totalDeVendas = float(input())

total = totalDeVendas * 0.15 + salarioFixo

print("TOTAL = R$ {:.2f}".format(total))