compras = []

while True:
    prod = input('Digite o produto: ')
    
    if prod.lower() == 'fim':
        print('Lista finalizada')
        break
    
    compras.append(prod)
    print(compras)
    print('Próximo item')

print('Compras finais:', compras)
