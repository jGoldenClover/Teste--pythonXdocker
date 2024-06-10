import random


# numeroAleatorio = 0
# for i in range (10) :
#     numeroAleatorio += random.randint(0,50)
    
    
# media = numeroAleatorio / 10
    
# print("A media é : " , numeroAleatorio , " ÷ 10 = " , media)


# respostaUsuario = input("Cara ou Coroa? \n")

# resultado = random.randint(0,1)
# if resultado == 0 :
#     resultado = 'cara'
# elif resultado == 1 :
#     resultado = 'coroa'
# numeroDeAcertos = 0
    
# while respostaUsuario.lower() == resultado :
#     respostaUsuario = input("Você acertou! Agora de novo Cara ou Coroa? \n")
#     resultado = random.randint(0,1)
#     if resultado == 0 :
#         resultado = 'cara'
#     elif resultado == 1 :
#         resultado = 'coroa'
#     numeroDeAcertos += 1
    
# print("A quantidade de acertos foi :", numeroDeAcertos)



import math

pedirRespostaAoUsuario = 'sim'

while pedirRespostaAoUsuario.lower() == 'sim' :
    pedirCalculoAoUsuario = int(input("Escolha o calculo desejado : \n 1- Área do triângulo. \n 2- Área do círculo. \n 3- Perímetro do círculo. \n 4- Área do trapézio. \n 5- Área de um quadrilátero. \n 6- Baskara \n"))

    match pedirCalculoAoUsuario :
        case 1 :
            altura = float(input("Digite o valor da altura do triângulo :"))
            base = float(input("Digite o valor da base do triângulo :"))
            print("O resultado é :" , altura , " x " , base , " = " , base*altura)
        case 2 :
            raio = float(input("Digite o valor do raio do círculo :"))
            print("O resultado é :" , raio , " x 3,14 = " , (raio*raio) * 3,14 , " ou " , raio**2 , " x ¬ = " , raio**2 ,"¬")
        case 3 : 
            raio = float(input("Digite o valor do raio do círculo :"))
            print("O resultado é :" , 2*raio *3,14 , " ou " , 2*raio , "¬")
        case 4 :
            baseMaior = float(input("Digite o valor da base maior :"))
            baseMenor = float(input("Digite o valor da base menor :"))
            altura = float(input("Digite o valor da altura :"))
            print("O resultado é :" , ((baseMaior + baseMenor) /2)*altura )
        case 5 :
            lado1 = float(input("Digite o valor de um dos lados : "))
            lado2 = float(input("Digite o valor de um dos lados : "))
            print("O resultado é :" , lado1*lado2)
        case 6 :
            valorA = float(input("Digite o valor de A :"))
            valorB = float(input("Digite o valor de B :"))
            valorC = float(input("Digite o valor de C :"))
            valorDelta = (valorB**2) -4 *valorA *valorC
            valorX1 = -valorB + math.sqrt(valorDelta)
            valorX2 = -valorB - math.sqrt(valorDelta)
            print("Os dois valores de X são : " , valorX1 , " e " , valorX2)
        case _:
            print("Digite um valor válido!")

    pedirRespostaAoUsuario = input("Você deseja repetir o laço ? \n (sim) (não)")