#Demonstração do uso de for/range...
#range gera uma sequencia

print("Digite o valor máximo desejado: ")
numero = int(input())

print("Segue, os numeros desejados:  ")
for x in range(0,numero):
    print(x)


print ("Digite o nome desejado: ")
nome = input()

print("Vamos soletrar cada letra? ")
for x in nome:
    print(x)
