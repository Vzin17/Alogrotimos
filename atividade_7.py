###
# Atividade 7
# Aluno: Vitor Josue Antonello Stolfo
# Data: 11/03/2024
###
CarrosVendidos = float(input("Digite a quantidade de carros que voce vendeu: "))
ValorCarros = float(input("Digite o valor dos carros: "))
VLR_carros = (CarrosVendidos * 50)
Comissao = (ValorCarros * 0.05)
Salario = (VLR_carros + Comissao + 500)
print(f"O salario dos funcionarios eh de: {Salario}")
