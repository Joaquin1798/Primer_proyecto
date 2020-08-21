costo = int(input('¿Cúanto vas a pagar? '))
pago = int(input('¿Con cuánto pagas? '))
print()
vuelto = pago - costo

while vuelto>0:
    if (vuelto//20)>0:
        n1 = vuelto//20
        print('Billetes de 20:',n1)
        vuelto = vuelto - (n1*20)

    elif (vuelto//10)>0:
        n2 = vuelto//10
        print('Billetes de 10:', n2)
        vuelto = vuelto - (n2*10)

    elif (vuelto//5)>0:
        n3 = vuelto//5
        print('Monedas de 5:', n3)
        vuelto = vuelto - (n3*5)

    elif (vuelto//2)>0:
        n4 = vuelto//2
        print('Monedas de 2:', n4)
        vuelto = vuelto - (n4*2)

    elif (vuelto//1)>0:
        n5 = vuelto//1
        print('Monedas de 1:', n5)
        vuelto = vuelto - (n5*1)
