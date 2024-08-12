def ParImpar(numero1, numero2):
    if (numero1 + numero2) % 2 ==0:
         print("Você venceu! ")
    else:
         print("Você perdeu! ")

    return
num1 = int(input(("Digite um número")))
num2 = 4
ParImpar(num1,num2)