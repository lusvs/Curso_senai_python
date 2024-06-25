#Autor: Lucas SVS
#Data: 23/05/2024
#Versão 1.0
#Descrição: Algoritimo que recebe o nome do usuário e exibe em uma frase
#           de saudação concatenada com a entrada do usuário
#=======================================================================
#Observação:
#           a)Para fazer um comentario coloque '#'
#           b) No visual code usamos o comando 'ctrl' + ';' para comentar
#              um bloco de codigo
#=======================================================================

nome = input('Qual é seu nome?')
mensagem = 'olá, seja bem vindo!'
frase = mensagem + nome #concatenar a variavel 'nome' com a variavel 'mensagem'
print (frase)
