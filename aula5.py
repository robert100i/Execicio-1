idade = int(input('Digite sua idade:'))

if idade > 15 and idade < 18 or idade > 70:
    print('O voto é opcional')
elif idade < 16:
    print('Você não pode votar')
else:
    print('O voto é obrigatorio')