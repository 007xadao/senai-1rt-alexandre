salario = float(input("Informe seu salario: "))
if salario > 8250:
    novosalario = salario + (salario *0.10)
else:
    novosalario = salario + (salario * 0.15)    

print("seu novo salario e de:",novosalario)