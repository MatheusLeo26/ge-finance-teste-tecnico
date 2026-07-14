"""
Questão 2 — Saudação (parâmetros com valor padrão)

Implemente a função `saudar`, que recebe um nome e um idioma opcional
(padrão "pt") e retorna a saudação correta:

    "pt" -> "Olá, <nome>!"
    "en" -> "Hello, <nome>!"
    "es" -> "Hola, <nome>!"

Se o idioma não for um dos três acima, retorne "Olá, <nome>!" (padrão pt).

Exemplos:
    saudar("Ana")            -> "Olá, Ana!"
    saudar("Ana", "en")      -> "Hello, Ana!"
    saudar("Ana", "fr")      -> "Olá, Ana!"
"""


def saudar(nome, idioma="pt"):
    if idioma == "en":
        return f"Hello, {nome}!"
    elif idioma == "es":
        return f"Hola, {nome}!"
    else:
        return f"Olá, {nome}!"
