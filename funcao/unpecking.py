def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numero):
    print(type(numero))
    soma = 0
    for n in numero:
        soma += n
    return soma

if __name__ == '__main__':
        print(soma_2(2, 3))
        print(soma_3(2, 4, 6))

        # packing
        print(soma_n(1))
        print(soma_n(1, 1))
        print(soma_n(1, 1, 1, 1, 1, 1, 1))


        #unpacking
        tuple_nums = (1, 2, 3)
        print(soma_3(*tuple_nums))
        lista_nums = [1, 2, 3]
        print(soma_3(*lista_nums))