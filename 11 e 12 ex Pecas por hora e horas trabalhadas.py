

''' 
11. A empresa XYZ, possui uma linha de produção de peças para indústria sucro-alcooleira. A 
fim de implementar alguns pilares da Indústria 4.0, como IoT e Computação em Nuvem, 
para visualizar em tempo real sua produção, pretende-se instalar sensores nesta linha, para 
realizar a contagem de peças produzidas em um determinado intervalo de tempo (aquisição 
de dados).


12. Faça um programa que leia a quantidade de peças produzidas por hora e quantidade de 
horas trabalhadas desta máquina. Retorne o total diário de produção '''



qtd_produzida = int(input('Qual foi a quantidade de peças produzidas por hora: '))
tempo = int(input('Qual foi a quantidade de tempo trabalhada em horas: '))
print(f'Hoje foram produzidas {qtd_produzida} peças em um intervalo de {tempo}, parabéns!')
