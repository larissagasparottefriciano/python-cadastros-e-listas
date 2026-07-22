livros = []

while True:
    dados = int(input('\n1. Adicionar leitura | 2. Acessar biblioteca | 3. Sair: '))
    
    if dados == 1:
        adicionar = input('Digite o nome do livro: ').strip()
        if adicionar == "":
            print('Nome inválido! Digite o nome de um livro.')
        else:
            livros.append(adicionar)  # Adiciona na lista aqui!
            print('Livro adicionado com sucesso!')
        
    elif dados == 2:
        if len(livros) == 0:
            print('Nenhum livro adicionado à biblioteca.')
        else:
            print('Livros cadastrados:', ", ".join(livros))
            
    elif dados == 3:
        print('Deslogando!')
        break
    else:
        print('Opção inválida!')
