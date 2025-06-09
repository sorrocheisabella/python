listnome = []
listidade = []
listcategoria = []

while True:
    print("Cadastro de Aluno:")
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    if idade < 18:
        print("Você menor")
    else:
        categoria = input("Digite a categoria desejada (A, B ou AB): ")
        
        if categoria == "A":
            listnome.append(nome)
            listidade.append(idade)
            listcategoria.append(categoria)
        elif categoria == "B":
            listnome.append(nome)
            listidade.append(idade)
            listcategoria.append(categoria)
        else:
            listnome.append(nome)
            listidade.append(idade)
            listcategoria.append(categoria)

    continuar = input("Deseja cadastrar outro aluno? (s/n): ")
    if continuar != "s":
        break

for lista in listnome, listidade, listcategoria:
    print(lista)