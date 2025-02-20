import csv

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
        Função que le um csv e retorna uma lista de dicionários
    """
    lista = []
    with open(nome_do_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

def filtrar_produtos_entregues(lista: list[dict]) -> list[dict]:
    """
        Função que filtra produtos onde entregue = True
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get('entregue') == 'True':
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    """
    Funcao que soma os valores dos produtos filtrados
    """
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += int(produto.get('price'))
    return valor_total