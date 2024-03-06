l1 = int(input('Lado 1:'))
l2 = int(input('Lado 2:'))
l3 = int(input('Lado 3:'))

if l1 > l2 + l3 or l2 > l1 +l3 or l3 > l1 + l2:
    print('Não é possível formar um triângulo')
elif l1 == l2 == l3:
    print('Equilátero')
elif l1 == l2 or l1 == l3 or l3 == l2:
    print('Isóceles')
else:
    print('Escaleno')

