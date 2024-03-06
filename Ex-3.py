p = float(input('Peso: '))

if p > 50:
    e = p - 50
    m= e * 4

else:
    e = m = 0

print(f'Excesso: {e: .2f}Kg')
print(f'Multa: R${m: .2f} ')
