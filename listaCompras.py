listaCompras = []

while True:
    print("Qual opcao voce deseja selecionar?")
    print("1- Adicionar itens para a lista")
    print("2- Excluir itens da lista")
    print("3- Listar itens da lista")
    print("4- Sair da Lista de Compras")

    selecionar = input("Digite o numero desejado: ")

    if selecionar == "1":
        item = input("Digite o nome do item que você deseja adicionar: ")
        listaCompras.append(item)
        print(f"O item '{item}' foi adicionado para a lista de compras.")

    elif selecionar == "2":
        if len(listaCompras) == 0:
            print("A lista de compras esta vazia!")
        else:
            item = input("Digite o nome do item que você deseja excluir: ")
            if item in listaCompras:
                listaCompras.remove(item)
                print(f"O item '{item}' foi excluido da lista de compras.")
            else:
                print(f"O item '{item}' não está na lista de compras.")
 
    elif selecionar == "3":
        if len(listaCompras) == 0:
            print("A lista de compras esta vazia!")
        else:
            print("Itens na lista de compras: ")
            for item in listaCompras:
                print(f"- {item}")

    elif selecionar == "4":
        print("Voce saiu da Lista de Compras.")
        break

    else:
        print("Sua escolha está inválida! Tente novamente.")