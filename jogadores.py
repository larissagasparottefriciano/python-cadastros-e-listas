jogadores = []
i = 1

while i <= 20:
    nome = input(f'Digite o nome do jogador {i}/20 (ou "fim" para encerrar): ')
    
    if nome.lower() == 'fim':
        print('Cadastro encerrado antes do limite.')
        break
    
    if nome.strip() == '':
        print('Nome inválido, tente novamente.')
        continue
    
    jogadores.append(nome)
    i += 1

print('\n--- CADASTRO FINALIZADO ---')
print(f'Total de jogadores registrados: {len(jogadores)}')
print(f'Lista: {jogadores}')
