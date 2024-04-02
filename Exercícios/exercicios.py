## Arquivo que contém exercícios que uso para praticar meus conhecimento
## durante os estudos em Python
## O arquivo está dividido em vários exercícios que estão comentados
## para que não interfiram na hora de rodar um exercício específico
## Para testar, é preciso apenas tirar o comentário do exercício desejado
##---------------------------------------------------------------------
# # EXERCICIO 1
# # EXERCICIO 1
# # Faça um programa que receba dois números inteiros e gere 
# # os números inteiros que estão no intervalo compreendido por eles.

# x = int(input('Digite um número:'))
# y = int(input('Digite outro número:'))
# lista = []
# resultado = 0
# for i in range (x, y+1):
#     lista.append(i)
#     resultado += i
# print (lista)
# print (f'A soma dos números de {x} a {y} é {resultado}')
# --------------------------------------------------------------
# #EXERCICIO 2
# # imprima os numero impares de 1 a 50

# lista=[]
# for num in range (1,51):
#     if num %2 != 0:
#        lista.append(num)
# print (f'os numeros impares entre 1 e 50 são: \n {lista}') 
#--------------------------------------------------------------
#EXERCICIO 3
# # calcule a potencia de um numero sem usar função potencia
# base = int (input('Digite o numero da base: '))
# expo = int (input('Digite o numero do expoente: '))

# resultado = 1

# for i in range (expo):
#     resultado *= base

# print (resultado)
# --------------------------------------------------------------
# #EXERCICIO 4
# # Faça um programa que peça 10 números inteiros, calcule e mostre a
# # quantidade de números pares e a quantidade de números impares.
# lista = []
# for i in range (10):
#     x = int(input('Digite um número:'))
#     lista.append(x)
# print (lista)

# par = 0
# impar = 0

# for x in lista:
#     if x % 2 == 0:
#         par += 1
#     else:
#         impar += 1

# print (f' A quantidade de pares é {par}')
# print (f' A quantidade de ímpares é {impar}')
# --------------------------------------------------------
# #EXERCICIO 5
# #Fibonacci
# x = int(input('Digite até qual termo voce quer ver: '))
# fibonacci = [0,1]
# for i in range (2, x):
#     y = fibonacci [-1]+fibonacci[-2]
#     if y > 500:
#         break
#     fibonacci.append(y)
# print (fibonacci)
# --------------------------------------------------------
# # EXERCICIO 6 
# # Fatorial de um número
# x = int(input('Digite um número que deseja saber o fatorial:'))
# fatorial = 1
# if x == 0:
#     print ( 'O fatorial de 0 é 1')
# else:
#     for i in range (1,x+1):
#         fatorial *= i
#     print (f'O fatorial de {x} é {fatorial}')
#---------------------------------------------------------
# #  EXERCICIO 7 
# # Dado um conjunto de N numeros, determine a soma, o maior valor e o menor valor
# # e permita que sejam numeros apenas entre 0 e 1000

# x = int(input('Digite a quantidade de números na lista'))
# numeros = []
# soma = 0
# numvalido = 0

# for i in range (x):
#     while numvalido < x:
#         num = int(input(f'Digite o {numvalido+1}º número (entre 0 e 1000)'))
#         if num>= 0 and num <= 1000:
#             numeros.append(num)
#             numvalido += 1
#             break
#         else: 
#             print ('Número invalido, tente novamente !')

#     soma += num
    
# minimo = min(numeros)
# maximo = max(numeros)
# print (numeros)
# print (f'A soma dos números na lista é {soma}')
# print (f'O menos numero é {minimo}')
# print (f'O maior numero é {maximo}')
# ----------------------------------------------------------
#EXERCICIO 8
# Calcular numero primo

x = int(input('Digite um número'))
if x >1:   
    divisores = []  
    for i in range (2,int(x**0.5)+1):
        if x % i == 0:
            divisores.append(i)
    if len(divisores)==0:
        print(f'{x} é um numero primo')
    else:
        print (f'{x} não é um numero primo')
        print (f'é divisivel por {divisores}')
else: 
    print(f'{x} não é um numero primo')
#------------------------------------------------------------
# # EXERCICIO 9
# # Numa eleição existem três candidatos. Faça um programa que 
# # peça o número total de eleitores. Peça para cada eleitor votar 
# # e ao final mostrar o número de votos de cada candidato.

# votos = []
# numeleito= int(input('Qual o número total de eleitores ? \n'))
# print ("Nessa eleição existem tres candidatos: A, B e C")
# for i in range (1, numeleito+1):
#     resposta = input(f'Eleitor {i}, em qual você deseja votar:')
#     votos.append(resposta)
# print (votos)