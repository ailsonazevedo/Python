INSS = 0
IRRF = 0
aliquota = 0
deducao = 0

salarBruto = float(input("Informe seu salário bruto: "))
dependentes = int(input("Informe o número de dependen"))
pergPen = input("Voce possui alguma pensão alimenticia desconta diretamente da fonte? (S/N): ")
if pergPen == 'S' or pergPen == 's':
    pensao = float(input("Entre com o valor da pensão alimentícia(R$): "))
else:
    pensao = 0
PAT = float(input("Informe o valor do seu PAT(Programa de Alimentação do Trabalhador): "))
pergPln = input("Possui algum plano de saúde diretamente descontado?(S/N): ")
if pergPln == 'S' or pergPln == 's':
    plnSaude = float(input("Informe o valor do plano de saúde(R$): "))
else:
    plnSaude = 0
pergAdc = input("Possui mais algum desconto adiconal?(S/N): ")
if pergAdc == 'S' or pergAdc == 's':
    desconto = float(input("Informe o valor do desconto(R$): "))
else:
    desconto = 0
if salarBruto <= 1830.29:
    INSS = salarBruto * 8 / 100
if salarBruto > 1830.29 and salarBruto <= 3050.52:
    INSS = salarBruto * 9 / 100
if salarBruto > 3050.52 and salarBruto <= 6101.06:
    INSS = salarBruto * 11 / 100
if salarBruto > 6101.06:
    INSS = 671.12

baseCalc = salarBruto - INSS - pensao * 189.59

if baseCalc <= 1903.98:
    aliquota = 0
    deducao = 0
if baseCalc >= 1903.99 and baseCalc <= 2826.65:
    aliquota = 7.5 / 100.0
    deducao = 142.80
if baseCalc >= 2826.66 and baseCalc <= 3751.05:
    aliquota = 15 / 100.0
    deducao = 354.80
if baseCalc > 3751.06 and baseCalc <= 4664.68:
    aliquota = 22.5 / 100.0
    deducao = 636.13
if baseCalc > 4664.68:
    aliquota = 27.5 / 100.0
    deducao = 869.36

IRRF = baseCalc * aliquota - deducao
salLiq = salarBruto - ((pensao * dependentes) + plnSaude + PAT + desconto + INSS + IRRF)
print("Seu salário Liquído: R$ {:.2f}".format(salLiq))
print("Valor Pago ao INSS: R$ {:.2f}".format(INSS))
print("Valor Pago ao IRRF: R$ {:.2f}".format(IRRF))

