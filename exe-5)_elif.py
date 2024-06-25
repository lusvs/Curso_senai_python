#Autor: Lucas SVS
#Data: 28/05/2024
#Versão 1.0
#Descrição: Algoritimo que considera o imput para receber
#           umas das respostas (elif)

#===================================================================

nota = float(input('coloque sua nota:'))

if nota >= 6: 
    print('aluno aprovado')
    print(nota)

elif(nota < 4):
    print('aluno reprovado')
    print(nota)

else:
    print('Aluno recuperação')
    print(nota)