# Entrada de informações do cliente
while (True):
    print ('Digite suas informações de cadastro: \n')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    salario_at = float(input('Salário atual: '))
    print (f'informações: \nNome: {nome} \nIdade: {idade} \nSalário Atual: {salario_at}')
# Confirmação de dados do cliente
    confirm = input('Suas informações estão corretas? (S ou N)')
    if confirm == 'sim' or confirm == 'Sim':
        break
    elif confirm == 'nao' or confirm == 'Nao':
        continue
# Previsão do salário por 10 anos
aumento = float (0.015)
ano = 2024
# Calcular o aumento salarial do ano
for i in range (1,11):
    # Calcular quanto aumenta cada ano
    ano += 1
    salario_at += salario_at * aumento
    aumento *=2
    # Imprimir salário e ano
    print (f'Ano: {ano}\n Salário: R${salario_at:.2f}')



        

