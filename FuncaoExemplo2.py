def adicao(x,y):
    a = x + y
    return a

def subtracao(x,y):
    return x - y

def  multiplicacao(x,y):
   return x * y

def divisao(x,y):
    return x/y


print("Digite dois valores inteios...")
n1 = int(input("x: "))
n2 = int(input("y:  "))
op =input("Qual operação (+,-, *, /)? ")

if op == "+": 
    z = adicao(n1,n2)
    print("Resultado da soma: ",z)
elif op == "-":
    z = subtracao(n1,n2)
    print("Resultado da subtração: ",z)
elif op == "*":
    z = multiplicacao(n1,n2)
    print("Resultado da multiplicacao: ",z)
elif op == "/":
    z = divisao(n1,n2)
    print("Resultado da divisao: ",z)

else:
    print("Opção digitada inexistente! ")