salario = float(input("Digite o salario do funcionario: "))

if salario > 8250.00:
   aumento = salario * 0.10 # Aumento de 10% para salarios superiores a R$ 8250.00
else: 
   aumento = salario * 0.15 # Aumento de 15% para salarios inferiores a R$ 8250.00

novo_salario = salario + aumento

print(f"O valor do aumento e R$ {aumento:.2f}.")
print(f"O novo salario e R$ {novo_salario:.2f}.")