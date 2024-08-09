time = input("Digite o nome do melhor time:  ")
MelhorTime = "Flamengo"

while time != MelhorTime:
    print("Você deve digitar o nome do melhor time corretamente:   ")
    time = input("Digite o nome do melhor time ")
    continue
else:
    print("Parabéns você digitou o time corretamente.")