#Autor: Lucas SVS
#Data: 25/06/2024 
#Versão 1.0
#Descrição: estudo de dado do tipo array
#=====================================================

aluno_sala = ['Lucas', 'Diego', 'Cavanhas']

aluno_sala.append('Andrey')
print(aluno_sala)

print(aluno_sala[2]) #indice 2 -> Cavanhas

for indice in range(4):
    print(aluno_sala[indice])

for aluno in aluno_sala:
    print(aluno)

print('================================================')

cabecalho = ['nome', 'idade', 'matricula']
dado_um =  ['Pele', 'eterno', '10']

print(dado_um[0])

tabela = [cabecalho, dado_um]
print(tabela[1][0]) #na variavel de cima criamos uma tabela, por isso agr o primeiro valor desse print é a linha e o segundo é a coluna.

'''
      0        1          2
0  'nome',  'idade', 'matricula'
1  'Pele', 'eterno',    '10'

'''

