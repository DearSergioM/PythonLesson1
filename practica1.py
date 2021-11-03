

gen = (i for i in range(100) if i % 2 ==0)

gen2 = (i for i in range(100) if i % 2 !=0)

for x in gen:
    print(x)

for y in gen2:
    print(y)



dic = {'color': 'red', 'size': 123, 'width': 400}

for key in dic:
    print(key)
    print(dic[key])

    if 'color' in dic:
        print(dic['color'])

def multiplicacion(a1, a2):
    return a1 * a2

def mult(a1, a2, i = 0, acc = 0):
    if i < a2:
        return mult(a1, a2, i + 1, a1 + acc)
    else:
        return acc

def mult2(* args):
    res = 1
    for j in args:
        res *= j
    return res

def mult3(**kwargs):
    res = 1
    for key in kwargs:
        print(key)
        res *= kwargs[key]
    return res
        
print'(=============================)'

print(multiplicacion(2,6))

print'(=============================)'

print (mult(2,8))

print'(=============================)'

print(mult2(28, 2, 4 ,5))

print'(=============================)'

print(mult3(num1 = 2, num2 = 6))

print'(=============================)'