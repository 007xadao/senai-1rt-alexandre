from time import sleep
def contagem_rergressiva(nu) :

    while nu > 0:
        nu = nu -1
        print(nu)
        sleep(1)

p = int(input("Declare o valor inicial:"))        

contagem_rergressiva(p)




