arquivo = open('pessoas_csv.py')
for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()