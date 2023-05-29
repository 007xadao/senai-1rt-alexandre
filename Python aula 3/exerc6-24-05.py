velocidade = float(input("Digite a velocidadedo carro em Km/h: "))

limite_velocidade = 80
valor_multa_por_kM = 7.00

if velocidade > limite_velocidade: 
   velocidade_excedida = velocidade - limite_velocidade
   valor_da_multa = velocidade_excedida * valor_multa_por_kM
   print("Voce foi multado!")
   print("Velocidade excedida: {:.2f} Km/h".format(velocidade_excedida))
   print("Valor da multa: R$ {:.2f}".format(valor_da_multa))
else:
   print("Voce esta dentro do limite de velocidade. ")

    