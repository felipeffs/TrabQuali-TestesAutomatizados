from page_functions import get_cep_result
from tests import product_match_test, price_filter_test

# Pesquisar Monitor entre as faixas de preço por preço 430 á 500
# Se pesquisar Battlefield, aparece minecraft no meio OU Battlefield 1943

product_name = "Monitor"
price_min = 430
price_max = 500

(_, product_list) = product_match_test(product_name)
print(f'Quantidade de Produtos no teste: {len(product_list)}')
(_, product_list) = price_filter_test(product_name, price_min, price_max)
print(f'Quantidade de Produtos no teste: {len(product_list)}')

get_cep_result()
