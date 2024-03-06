a = int(input('Área a ser pintada em metros: '))

if a % 54 == 0:
    l = a / 54

else:
    l = int(a / 54) + 1

p = l * 80

print(f'Quantidade:      {l} Latas')
print(f'Valor final:     R${p: .2f}')
