from components.functions import adicionarItem
from components.functions import removerItem
from components.functions import visualizarCompras
from components.functions import salvarCompras
from components.functions import carregarCompras

import time
import os


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1 Criar uma nova lista de compras')
        print('2 Carregar uma lista existente')
        print('3 Sair')
        escolha = input('Escolha uma opcao: ')
        if escolha == '1':
            compras = {}
            gerenciarCompras(compras)
        elif escolha == '2':
            print('Listas disponiveis: ')
            arquivos = [arquivo for arquivo in os.listdir()
                        if arquivo.endswith('.json')]
            if not arquivos:
                print('Nenhuma lista encontrada')
                time.sleep(2)
                continue
            for i, arquivo in enumerate(arquivos, 1):
                print(f'{i} {arquivo}')
            escolha = int(
                input('Escolha uma lista para carregar(0 se nenhuma): '))
            if escolha == 0:
                continue
            if escolha < 0 or escolha > len(arquivos):
                print('Opcao invalida')
            time.sleep(2)
            continue
            nomeArquivos = arquivos[escolha - 1]
            compras = carregarCompras(nomeArquivos)
            gerenciarCompras(compras, nomeArquivos)
        elif escolha == '3':
            break
        else:
            print('Opcao invalida')
            time.sleep(2)


def gerenciarCompras(compras, nomeArquivo=None):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1 Adicionar item')
        print('2 Remover item')
        print('3 Visualizar lista')
        print('4 Salvar e sair')
        print('5 Sair sem salvar')
        escolha = input('Escolha uma opcao: ')
        if escolha == '1':
            item = input('Digite o nome do item: ')
            qtd = float(input('Digite a quantidade: '))
            adicionarItem(compras, item, qtd)
        elif escolha == '2':
            item = input('Digite o nome do item: ')
            removerItem(compras, item)
        elif escolha == '3':
            visualizarCompras(compras)
        elif escolha == '4':
            if nomeArquivo is None:
                nomeArquivo = input('Digite o nome do arquivo para salvar: ')
            if not nomeArquivo.endswith('.json'):
                nomeArquivo += '.json'
            salvarCompras(compras, nomeArquivo)
            break
        elif escolha == '5':
            break
        else:
            print('Opcao invalida')
            time.sleep(2)


if __name__ == '__main__':
    main()
