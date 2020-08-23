a = str(input('Introduce un número: '))

k = 0
n = 0
m = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
for i in a:
    if i == '0':
        k += 1
    elif i == '1':
        n += 1
    elif i == '2':
        m += 1
    elif i == '3':
        p += 1
    elif i == '4':
        q += 1
    elif i == '5':
        r += 1
    elif i == '6':
        s += 1
    elif i == '7':
        t += 1
    elif i == '8':
        u += 1
    elif i == '9':
        v += 1

print('\nCantidad de ceros: ', k)
print('Cantidad de unos: ', n)
print('Cantidad de dos: ', m)
print('Cantidad de tres: ', p)
print('Cantidad de cuatros: ', q)
print('Cantidad de cincos: ', r)
print('Cantidad de seis: ', s)
print('Cantidad de sietes: ', t)
print('Cantidad de ochos: ', u)
print('Cantidad de nueves: ', v)

'mina'.count()