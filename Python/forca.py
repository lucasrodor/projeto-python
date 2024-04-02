    #exibir uma mensagem dando incio ao jogo
print ('Jogo da Forca \n')

    #preencher a palavra chave
palavra= input('Digite a palavra chave: ')
dica = input('Digite uma dica sobre a palavra: ')
    #preencher a quantidade de vidas
vidas= int(input('Digite a quantidade de vidas para esse jogo:'))
print ('\n'*100)
print ('Tudo pronto, o jogo vai começar')
print (f'Você têm {vidas} vidas')
aux = '*'*len(palavra)
print (f'Palavra: {aux}')
    #iniciar um processo repetitivo de tentativas
letradig = []
while True: 
    #permitir a entrada de uma letra
    print (f'dica: {dica}')
    letra = input('Digite uma letra: \n')
    #verificar se ela ja foi digitada
    if letra in letradig: 
        print (f'Letra {letra} já foi digitada, tente novamente!')
        continue
    else: 
    #inserir a letra na lista
        letradig.append(letra)

    #verificar se ela está na palavra
    if letra in palavra:
        print (f'A letra {letra} está na palavra')
        frase = ''
        for char in palavra:
            if char in letradig:
               aux = char
    #mostrar a palavra com a letra ( se acertada )
            else: 
                aux= '*'
            frase = frase + aux
        print (f'A palavra está assim:{frase}')
    #mostrar se já venceu
        if frase == palavra :
            print ('Parabens, você venceu')
            print (f'A palavra era {palavra}')
            break

    else:
        print (f'A letra {letra} não está na palavra')
        print 
    #verificar se ainda temos vidas
        if vidas > 0:
            vidas = vidas - 1 
        if vidas == 0: 
            print ('Você perdeu o jogo')
            print (f'A palavra era: {palavra}')
            break

    #mostrar a quantidade de vidas restanates
    print (f'Você  têm {vidas} vida(s) restante(s)\n')
    #mostrar as letras digitadas       
    print (f'- Letras usadas: {letradig}\n')
print ('Jogo Finalizado')
    
        

