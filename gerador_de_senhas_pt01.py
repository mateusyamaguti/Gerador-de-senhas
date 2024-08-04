import random

print('Gerador de senhas')

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*().,?'

qtd_senhas = int(input('\nQuantas senhas você deseja criar? '))

qtd_crt = int(input('As senhas terão quantos caracteres? '))

for c in range(qtd_senhas):
    senhas = ''
    for q in range(qtd_crt):
        senhas += random.choice(caracteres)
    print(senhas)

