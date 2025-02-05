from utils import clean_string
from page_functions import get_product_list


# Teste de correspondência de produto
def product_match_test(product_name):
    product_list = get_product_list(product_name)

    sub_words = clean_string(product_name).split(" ")

    incongruities = []
    for p in product_list:
        temp_name = clean_string(p["name"])
        if not any(word in temp_name for word in sub_words):
            incongruities.append(p)

    tam = len(incongruities)

    print("Teste de Correspondência: ", end='')
    if tam <= 0:
        print('Passou')
    else:
        print('Falhou')
        print(f'\t{tam} {"incongruências encontradas." if tam > 1 else "incongruência encontrada."}')
        for i in incongruities:
            print(f'\t\tNome: {i["name"]} \n\t\t\tPreço: {i["preco"]} \n\t\t\tLink: {i["link"]}')

    return incongruities, product_list


# Filtro de preço
def price_filter_test(product_name, min_price, max_price):
    product_list = get_product_list(product_name, min_price, max_price)

    incongruities = []
    for p in product_list:
        if p["preco"] < min_price:
            incongruities.append(p)
        elif p["preco"] > max_price:
            incongruities.append(p)

    tam = len(incongruities)

    print("Teste de Filtro de Preço: ", end='')
    if tam <= 0:
        print('Passou')
    else:
        print('Falhou')
        print(f'\t{tam} {"incongruências encontradas." if tam > 1 else "incongruência encontrada."}')
        for i in incongruities:
            print(f'\t\tNome: {i["name"]} \n\t\t\tPreço: {i["preco"]} \n\t\t\tLink: {i["link"]}')
    return incongruities, product_list
