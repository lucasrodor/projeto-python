
# R= float(input('Digite o valor do raio da esfera: '))
# vol = 4/3*R**3

# print (f'O raio da esfera em que R={R} é {vol}π')

numero = int(input("Digite um número: "))

# Verifica se o número é maior que 1
if numero > 1:
    # Itera de 2 até a raiz quadrada do número + 1
    for i in range(2, int(numero**0.5) + 1):
        # Se o número for divisível por qualquer número dentro do intervalo, ele não é primo
        if numero % i == 0:
            print(numero, "não é um número primo.")
            break
    else:
        print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")
