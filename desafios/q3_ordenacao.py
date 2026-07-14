"""
Questão 3 — Ordenação com lambda (sorted + key)

Você recebe uma lista de tuplas no formato (nome, idade).

Implemente a função `ordenar_por_idade`, que retorna uma NOVA lista
ordenada da pessoa mais nova para a mais velha.

OBRIGATÓRIO: use a função sorted() com uma lambda no parâmetro `key`.

Exemplo:
    pessoas = [("Bia", 30), ("Caio", 22), ("Ana", 25)]
    ordenar_por_idade(pessoas) -> [("Caio", 22), ("Ana", 25), ("Bia", 30)]
"""


def ordenar_por_idade(pessoas):
    return sorted(pessoas, key=lambda pessoa: pessoa[1])
