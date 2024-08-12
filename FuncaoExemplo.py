def Apresentar():
    print("Meu nome é", meunome, ".")
    print("Minha altura é de: ", minhaaltura, "metros")
    print("Minha idade é", minhaidade, "anos")
    return
def Conferir(x):
    if x>=18:
        print("você é maior de idade!")
    else:
        print("Ops, menor de idade nao pode")
    return
meunome = str(input("Digite o seu nome:  "))
minhaaltura = float(input("Digite a sua altura:  "))
minhaidade = int(input("Digite a sua idade:  "))

Apresentar()
Conferir(minhaidade)
