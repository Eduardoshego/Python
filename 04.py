inicio = int(input('Digite o número inicial da tabuada\n'))
final = int(input('Digite o número final da tabuada\n'))

for i in range(inicio, final +1):
    print(f'Para o {i}')
    for j in range (inicio , final + 1):
        print(f'{i}x{j} = {i*j} ')
    print('')
