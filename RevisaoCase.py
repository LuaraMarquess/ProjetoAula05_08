print("O que você achou dos nossos serviços?  ")
print("1. Péssimo, 2.Ruim 3.Razoável, 4.Bom, 5.Ótimo...")
avaliacao = int(input("Digite uma opção:  "))

match avaliacao:
    case 1:
        print("O serviço precisa melhorar muito! ")
        print("Avaliação: Reprovado! ")
    case 2: 
        print("O serviço precisa  melhorar em alguns quesitos...")
        print("Avaliaçao: reprovado.")
    case 3:
        print("Nem bom,nem ruim...")
        print("Avaliação: Aprovado.")
    case 4:
        print("Aceitável no geral,embora possa melhorar.")
        print("Avaliação: Aprovado")
    case 5:
        print("Perfeito,melhor que issso estraga!")
        print("Avaliação: Aprovado! ")
    
    case _:
        print("Opção não correta ")

print("Obrigado pela atenção.")