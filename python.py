import random


# numeroAleatorio = 0
# for i in range (10) :
#     numeroAleatorio += random.randint(0,50)
    
    
# media = numeroAleatorio / 10
    
# print("A media é : " , numeroAleatorio , " ÷ 10 = " , media)


respostaUsuario = input("Cara ou Coroa? \n")

resultado = random.randint(0,1)
if resultado == 0 :
    resultado = 'cara'
elif resultado == 1 :
    resultado = 'coroa'
numeroDeAcertos = 0
    
while respostaUsuario.lower() == resultado :
    respostaUsuario = input("Você acertou! Agora de novo Cara ou Coroa? \n")
    resultado = random.randint(0,1)
    if resultado == 0 :
        resultado = 'cara'
    elif resultado == 1 :
        resultado = 'coroa'
    numeroDeAcertos += 1
    
print("A quantidade de acertos foi :", numeroDeAcertos)
