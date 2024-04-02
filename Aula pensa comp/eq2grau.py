a = float(input('digite o valor do coeficiente a'))
b = float(input('digite o valor do coeficiente b'))
c = float(input('digite o valor do coeficiente c'))
delta = b**2 - 4*a*c
x1 = (-b + delta**(1/2))/2*a
x2 = (-b - delta**(1/2))/2*a

if delta < 0:
    print (f'A equação não possui raízes reais')
elif delta == 0:
    x1 = x2
    print (f'A raíz da equação é x= {x1}')
else:
    print(f'As raízes da equação são x1={x1} e x2={x2}')
print ('delta =', delta)