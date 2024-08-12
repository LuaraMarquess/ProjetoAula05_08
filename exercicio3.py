def verificaCidade(nomePessoa,cid):
    if cid == "Rio de Janeiro":
        print(f"Seja bem-vindo á cidade maravilhosa {nomePessoa}")
    else:
        print(f"Seja bem-vindo á cidade {cid}, {nomePessoa}")
    return 

nome = input("Digite o seu nome:  ")
cidade = input("Digite a sua cidade: ")

verificaCidade(nome,cidade)