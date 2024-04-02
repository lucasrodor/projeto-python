#entrada de número
x = int(input('digite um número: '))

#escolher quantas tabuadas subsequentes vou querer fazer
for i in range (x,x+4):
    print (f'Tabuada de {i}')
#calcular a tabuada do numero de entrada
    for y in range (1,11): 
        resultado = i*y
#imprimir a tabuada no formato de tabuada
        print (f'{i} x {y} = {resultado}')



