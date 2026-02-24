

try:
    arquivo = open('pessoas_csv.py')

    for registro in arquivo:
       print('Nome: {} Idade: {}'.format(registro.strip().split(',')))

finally:
    print('finally')
    arquivo.close()

    if arquivo.close:
        print('arquivo ja foi fechado')