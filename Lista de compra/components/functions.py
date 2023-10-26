import json


def adicionarItem(compras, item, qtd):
    compras[item] = qtd


def removerItem(compras, item):
    if item in compras:
        del compras[item]


def visualizarCompras(compras):
    for item, qtd in compras.items():
        print(f'{item}: {qtd}')
    print()
    print('Pressione enter para continuar')
    input()


def salvarCompras(compras, nomeArquivo):
    with open(nomeArquivo, 'w') as arquivo:
        json.dump(compras, arquivo)


def carregarCompras(nomeArquivo):
    with open(nomeArquivo, 'r') as arquivo:
        return json.load(arquivo)
