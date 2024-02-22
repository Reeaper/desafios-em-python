print('Valor da viajem com base na quilometragem')
km = float(input("Quantos Km terá a sua viajem(apenas números)? "))

if km <= 200:
    calc = km * 0.45
    print(f"O valor da sua viajem será de R${calc}")
else:
    calc = km * 0.50
    print(f'O valor da sua viajem será de R${calc}')
