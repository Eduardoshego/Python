n = int(input('Digite o número de  sequencias\n'))
cond = 1
soma = 0

for i in range(0,n):
    print(f'{i+1}° sequência')
    while True:
        if cond == 0:
            break
        cond = int(input(f'Digite  número da {i+1}° sequência\n'))
        if cond % 2 == 0:
            soma = soma + cond
    print(f'A soma da  {i+1}° sequência é {soma}')
    print('')
    soma = 0
    cond = 1   