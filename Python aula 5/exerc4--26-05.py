def identificador(numero):
    if numero % 2 == 0:
        print("O numero",numero,"e par.")
    else:
        print("O numero",numero,"e impar.")

n = int (input("Digitar um numero:"))
print(identificador(n))         

