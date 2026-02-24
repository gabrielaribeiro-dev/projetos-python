from string import Template
nome, idade = 'Ana', 30
print('Nome: %s Idade: %d' % (nome, idade))
print('Nome: {0} Idade: {1}'.format(nome, idade))
print(f'Nome: {nome} Idade: {idade} {2 ** 8 + 1}')
s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))