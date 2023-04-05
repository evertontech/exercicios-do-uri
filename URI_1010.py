# CALCULO SIMPLES
codPeca_01, numPecas_01, valorUnitarioPeca_01 = split(input())
codPeca_02, numPecas_02, valorUnitarioPeca_02 = split(input())

valorTotal = numPecas_01 * valorUnitarioPeca_01 + numPecas_02 * valorUnitarioPeca_02

print("VALOR A PAGAR: R$ {:.2f}".format(valorTotal))