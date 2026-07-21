sabores = []
i = 1

while i <= 10:
    escolha = input(f'Digite o sabor {i}/10 de sua escolha (ou FIM para finalizar) : ')
    
    if escolha.lower() == 'fim':
        print('Lista finalizada \n')
        break
    
    if escolha == "":
        print('Sabor inválido, tente novamente \n')
        continue
    
    sabores.append(escolha)
    i+= 1

print('Cadastro de sabores realizado com sucesso! \n')
print(f'Total de sabores escolhidos: {len(sabores)}\n')
print("Sabores escolhidos:", ", ".join(sabores))
print('Bom apetite')
