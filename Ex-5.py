n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

if n3 < n1 > n2:
    maior = n1

elif n1 < n3 > n2:
    maior = n3

else:
    maior = n2

if n3 > n1 < n2:
    menor = n1

elif n1 > n3 < n2:
    menor = n3

else:
    menor = n2

print(f'Maior: {maior}')
print(f'Menor: {menor}')
