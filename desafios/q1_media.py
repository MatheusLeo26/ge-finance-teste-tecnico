"""
Questão 1 — Média de notas (função simples)

Implemente a função `calcular_media`, que recebe uma lista de números
(notas) e retorna a média aritmética arredondada para 2 casas decimais.

Se a lista estiver vazia, retorne 0.0.

Exemplos:
    calcular_media([7, 8, 9])      -> 8.0
    calcular_media([10, 5.5])      -> 7.75
    calcular_media([])             -> 0.0
"""


def calcular_media(notas):
    if not notas:
        return 0.0
    return round(sum(notas) / len(notas), 2)
