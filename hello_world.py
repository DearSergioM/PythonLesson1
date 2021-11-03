print 'Hello World'
 
var = 'mundo'
num = 1234
num2 = 5678

flotante = 123.4
flotante2 = 456.31
carac = 'c'
carac2 = 'd'

bol = True
bol2 = False
bol3 = None

print (var)
print (carac+carac2)
print (var+carac)

print (num + num2)
print (flotante + flotante2)

print (not bol)
print (not bol2)
print (bol or bol2)
print (bol and bol2)

if 10 > 5:
        print ('10 es mayor que 5')
elif 10 < 5:
        print ('NOP')

var_rapida = 10


if type (var_rapida) is int:
 print('Es un entero')

if type (var) is str:
 print('Es una cadena')

if type (flotante) is float:
 print('Es un flotante')

if type (flotante) is int:
 print('Es un entero')


arrgelo_num = [0 ,1 ,2 ,3]
arreglo_car = ['c','h','a','d']


print (arreglo_car[0])
print ''
print (arreglo_car[1])
print ''
print (arreglo_car[2])
print ''
print (arreglo_car[3])
print ''
print(len(arreglo_car))
print ''
print(arreglo_car[len(arreglo_car) - 1])

for i in arrgelo_num:
    print(i)

for k in range(5):
    print(var[k])

for j in var:
    print(j)


for numero in range(0, 101):
        if (numero % 2) == 0:
           print(numero)
print '======================================'
for numero2 in range(0, 100):
   if numero2 > 1:
       for i in range(2, numero2):
           if (numero2 % i) == 0:
               break
       else:
           print(numero2)
print '======================================'
for numero3 in range (1, 100 , 2):
    print(numero3)