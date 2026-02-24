def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':

    # teste (assertions)
    assert tag_bloco('incluido com sucesso!') == \
           '<div class="sucess">incluido com sucesso!</div>'
    assert tag_bloco('impossivel excluir!', 'error') == \
           '<div class="erro">impossivel excluir!</div>'
    print(tag_bloco('bloco'))
