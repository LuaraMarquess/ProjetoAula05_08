def menor():
    print("Eis, os programas ideias para você: ")
    print("Teletubies, Tom e Jerri,Show da Xuxa...")
    print("Se passar das 10h, vai dormir!!!")
    return
def maior():
    print("Eis, boas opções de carro para comprar:")
    print("Fiat 147, Vw Fusca, Chevette...")
    print("Se beber, nao dirija...")
    return
print ("Digite a sua idade: ")
idade = int(input())

if idade <18:
    menor()
else:
    maior()