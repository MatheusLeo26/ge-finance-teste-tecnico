"""
Questão Bônus — Relatório de vendas (combinando conceitos)

Você recebe uma lista de dicionários representando vendas:

    vendas = [
        {"produto": "Teclado", "valor": 120.0},
        {"produto": "Mouse", "valor": 45.0},
        {"produto": "Monitor", "valor": 899.0},
    ]

Implemente a função `total_acima_de`, que recebe a lista de vendas e um
valor mínimo, e retorna a SOMA dos valores das vendas que forem
estritamente maiores que esse mínimo.

Sugestão: dá para resolver em uma linha com filter + lambda + sum,
mas qualquer solução correta é aceita.

Exemplo:
    total_acima_de(vendas, 100) -> 1019.0   (120.0 + 899.0)
    total_acima_de(vendas, 1000) -> 0
"""


def total_acima_de(vendas, minimo):
    return sum(venda["valor"] for venda in vendas if venda["valor"] > minimo)
    
