import csv


with open(r'C:\Users\gabri\Downloads\desafio-ibge.csv', 'r', encoding='ISO-8859-1') as arquivo:
    csv_arquivo = csv.reader(arquivo)
    contador = 0
    for linha in csv_arquivo:
        if contador == 4 or contador == 9:
            print('linha selecionada: ',linha)
        else:
            print(f'a linha {contador} nao foi selecionado')
        contador += 1