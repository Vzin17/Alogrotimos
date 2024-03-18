###
# Atividade 5
# Aluno: Vitor Josue Antonello Stolfo
# Data: 11/03/2024
###
ValorFab = float(input("Digite o valor de fabrica do carro: "))
ValorX = (ValorFab * 0.12)
print(f"Comissao: {ValorX}")
ValorY = (ValorFab * 0.45)
print(f"Imposto eh de: {ValorY}")
Valor = (ValorFab + ValorX + ValorY)
print(f"Valor_1: {Valor}")
ValorFinal = (ValorFab * 0.12) + (ValorFab * 0.45) 
ValorF = (ValorFab *(0.12 + 0.45))
Resultado = (Valor + ValorFinal + ValorF)
print(f"O custo final do carro eh de: {Resultado}")
