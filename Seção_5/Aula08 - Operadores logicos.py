print(7 != 3 and 2)
#
saldo = 1000
salario = 4000
Despesas = 3900

saldo_positivo = saldo > 0
despesas_controladas = salario - Despesas >= 0.2 * salario
meta = saldo_positivo and despesas_controladas
print(meta)
