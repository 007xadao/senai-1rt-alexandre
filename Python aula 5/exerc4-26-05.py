def identificador(num):
    if num % 2 == 0 :
        print("O numero", num,"e par.")
    else:
        print("O numero",num,"e impar")   
n = int(input("Digite um numero:"))
print(identificador(n))         