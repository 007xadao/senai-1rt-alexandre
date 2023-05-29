valor1 = float (input("Digite o primeiro valor: "))
valor2 = float (input("Digite o segundo valor: "))

print("Escolha a operação:")
print("1 - Adiçao")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")

opcao = int(input("Digite o numero da operaçao desejada:"))
if opcao == 1:
    resultado = valor1 + valor2
    operacao = "adiçao"
elif opcao == 2:
    resultado = valor1 - valor2
    operacao = "Subtração"
elif opcao == 3:
    resultado = valor1 / valor2
    operacao = "divisão"
elif opcao == 4:
    resultado = valor1 * valor2
    operacao = "multiplicação"        
else:
    print("Opção invalida.")
    exit()
print("Resultado da {} entre {} e {}: {}".format(operacao, valor1, valor2, resultado))
nota = int(input("Informe a nota do participante: "))
if nota <= 50:
    print("Certificado de Participação")
elif nota <= 60:
    print("Certificado de Menção Honrosa")
elif nota <= 70:
    print("Medalha de Bronze") 
elif nota <= 90:
    print("Medalha de Prata")
else:
    print("Medalha de ouro")   
       