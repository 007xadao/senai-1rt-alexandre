distancia = float (input("Digite a distancia da viagem em km: "))

if distancia <= 200:
    preco_passagem = distancia * 0.50 # R$ 0.50 por Km para viagens ate 200 km
else:
    preco_passagem = distancia * 0.45 # R$ 0.45 por Km para vuagens acima de 200 Km

print (f"O preco da passagem e R$ {preco_passagem:.2f}.")
