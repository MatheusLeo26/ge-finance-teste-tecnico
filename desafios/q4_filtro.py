"""
Questão 4 — Filtragem com lambda (filter)

Implemente a função `apenas_pares`, que recebe uma lista de inteiros e
retorna uma lista contendo apenas os números pares, na mesma ordem.

OBRIGATÓRIO: use a função filter() com uma lambda.
Dica: filter() retorna um iterador — converta para lista antes de retornar.

Exemplos:
    apenas_pares([1, 2, 3, 4, 5, 6]) -> [2, 4, 6]
    apenas_pares([1, 3, 5])          -> []
"""


def apenas_pares(numeros):
    return list(filter(lambda x: x % 2 == 0, numeros))
