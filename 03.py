numEleitor = int(input("Digite o numero de eleitor\n"))
candidato1 = 0
candidato2 = 0
candidato3 = 0

for i in range(0, numEleitor):
    voto = int(input(f"Digite o voto do {i+1}° eleitor\n"))
    
    if voto ==1:
    
         candidato1 = candidato1 + 1
    
    elif voto == 2:
        
          candidato2 = candidato2 + 1
    else :
        candidato3 = candidato3 +1
    
    if candidato1 > candidato2 and candidato1 > candidato3:

        print(f'Ganhou o candidato 1 com {candidato1} votos')

    elif candidato2 > candidato1 and candidato2 > candidato3 :

        print(f'Ganhou o candidato 2 com {candidato2} votos')

    else:
        print(f'Ganhou o candidato 3 com {candidato3} votos')