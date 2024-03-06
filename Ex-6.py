g = float(input('Ganho por hora: '))
h = int(input('Carga horária mensal: '))

sb = g * h
ir = (11 / 100) * sb
inss = (8 / 100) * sb
sind = (5 / 100) * sb
sl = sb - ir - inss - sind

print(f'Salário bruto:       R${sb: .2f}')
print(f'Imposto de renda:    R${ir: .2f}')
print(f'INSS:                R${inss: .2f}')
print(f'Sindicato:           R${sind: .2f}')
print(f'Salário Liquído:     R${sl: .2f}')
