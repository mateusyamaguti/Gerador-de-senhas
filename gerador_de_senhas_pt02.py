import random

print('Gerador de senhas')
print('\nSenha mínima de 9 digitos')

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*().,?'

qtd_crt = int(input('\nDigite a quantidade de caracteres: '))

def pegar_caracteres_minisculos():
    caracteres_minisculos = ''
    for minisc in range(qtd_crt//4):
        caracteres_minisculos += random.choice(caracteres[:26])
    return(caracteres_minisculos)

def pegar_caracteres_maiusculo():
    caracteres_maiusculo = ''
    for maius in range(qtd_crt//4):
        caracteres_maiusculo += random.choice(caracteres[26:52])
    return(caracteres_maiusculo)

def pegar_caracteres_numericos():
    caracteres_numericos = ''
    for num in range(qtd_crt//4):
        caracteres_numericos += random.choice(caracteres[52:62])
    return(caracteres_numericos)

def pegar_caracteres_simbolicos():
    caracteres_simbolicos = ''
    for simb in range(qtd_crt//4):
        caracteres_simbolicos += random.choice(caracteres[62:])
    return(caracteres_simbolicos)

senha = ''

if (len(pegar_caracteres_minisculos() + pegar_caracteres_maiusculo() + 
        pegar_caracteres_numericos() + pegar_caracteres_simbolicos())) < (qtd_crt):
    # print('erro')
    senha = pegar_caracteres_minisculos() + pegar_caracteres_maiusculo() + pegar_caracteres_numericos() + pegar_caracteres_simbolicos() + random.choice(caracteres)
    # print(senha)
    # print(len(senha))
    # print(random.sample(senha, len(senha)))
    senha_final = ''
    for caract in random.sample(senha, len(senha)):
        senha_final += caract
else:
    senha = pegar_caracteres_minisculos() + pegar_caracteres_maiusculo() + pegar_caracteres_numericos() + pegar_caracteres_simbolicos()
    # print(senha)
    # print(random.sample(senha, len(senha)))
    senha_final = ''
    for caract in random.sample(senha, len(senha)):
        senha_final += caract

senha = pegar_caracteres_minisculos() + pegar_caracteres_maiusculo() + pegar_caracteres_numericos() + pegar_caracteres_simbolicos()
comprimento_senha = len(senha)

if comprimento_senha < qtd_crt:
    for letra in range(qtd_crt - comprimento_senha):
        senha += random.choice(caracteres)

senha_final = ''
for item in random.sample(senha, len(senha)):
    senha_final += item 


print(f'\nSenha gerado: {senha_final}, tamanho da senha {len(senha)}')