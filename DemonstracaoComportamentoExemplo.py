#Demonstração do comportamento das listas...
print("Vou almoçar em um restaurante a quilo! ")

original = ["Arroz","Feijão","Batata","Alface","Frango"]
print("Eis,a minha comida: ", original)
#derivada = original
derivada = original[:] #Copiando conteúdo da original e colocoando na derivada


print("Meu amigo irá comer também", derivada)

print("Vou alterar as ações sem ele ver...")
original.remove("Arroz")
original.remove("Feijão")
original.remove("Alface")
original.append("Picanha")
original.append("Linguiça")

print("Amiguinho, me mostre o que você vai comer? ")
print("Claro! Dá uma conferida",derivada)