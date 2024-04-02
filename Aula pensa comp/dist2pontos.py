xa = int(input('digite a coordenada x do Ponto A'))
ya = int(input('digite a coordenada y do Ponto A'))
xb = int(input('digite a coordenada x do Ponto B'))
yb = int(input('digite a coordenada y do Ponto B'))

dist = ((xa-xb)**2 + (ya-yb)**2)**(1/2)

print (f'A distancia entre os pontos A({xa};{ya}) e B({xb};{yb}) é:')
print (f'{dist} u.m')