def area (largura, comprimento) :
    area_terreno = largura * comprimento 
    return area_terreno

largura = float(input("Digite a largura do terreno em metros:"))
Comprimento = float(input("Digite o comprimento do terreno em metros"))

resultado = area(largura, Comprimento)
print("A area do terreno e:",resultado,"metros quadrados.")

