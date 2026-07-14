"""
Questão 5 — Transformação com lambda (map)

Uma loja está aplicando 10% de desconto em todos os produtos.

Implemente a função `aplicar_desconto`, que recebe uma lista de preços
e retorna uma nova lista com os preços após o desconto de 10%,
arredondados para 2 casas decimais.

OBRIGATÓRIO: use a função map() com uma lambda.

Exemplo:
    aplicar_desconto([100.0, 59.90, 10.0]) -> [90.0, 53.91, 9.0]
"""


def aplicar_desconto(precos):
    return list(map(lambda preco: round(preco * 0.9, 2), precos))
    
