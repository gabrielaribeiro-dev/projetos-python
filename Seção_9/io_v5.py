

with open('pessoas_csv.py') as arquivo:
    for registro in arquivo:
       print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

if arquivo.close:
        print('arquivo ja foi fechado')