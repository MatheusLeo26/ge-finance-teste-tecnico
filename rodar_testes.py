"""
Script de verificação — rode com: python rodar_testes.py

Ele executa testes simples em cada questão e mostra o resultado.
Você pode rodar quantas vezes quiser enquanto resolve o teste.
"""

import sys

sys.path.insert(0, "desafios")

from q1_media import calcular_media
from q2_saudacao import saudar
from q3_ordenacao import ordenar_por_idade
from q4_filtro import apenas_pares
from q5_desconto import aplicar_desconto
from q6_bonus import total_acima_de

RESULTADOS = []


def verificar(descricao, obtido, esperado):
    ok = obtido == esperado
    RESULTADOS.append(ok)
    status = "OK  " if ok else "ERRO"
    print(f"[{status}] {descricao}")
    if not ok:
        print(f"        esperado: {esperado!r}")
        print(f"        obtido:   {obtido!r}")


print("\n--- Questão 1: calcular_media ---")
verificar("média de [7, 8, 9]", calcular_media([7, 8, 9]), 8.0)
verificar("média de [10, 5.5]", calcular_media([10, 5.5]), 7.75)
verificar("lista vazia", calcular_media([]), 0.0)

print("\n--- Questão 2: saudar ---")
verificar("padrão pt", saudar("Ana"), "Olá, Ana!")
verificar("inglês", saudar("Ana", "en"), "Hello, Ana!")
verificar("espanhol", saudar("Luis", "es"), "Hola, Luis!")
verificar("idioma desconhecido", saudar("Ana", "fr"), "Olá, Ana!")

print("\n--- Questão 3: ordenar_por_idade ---")
pessoas = [("Bia", 30), ("Caio", 22), ("Ana", 25)]
verificar(
    "ordena por idade",
    ordenar_por_idade(pessoas),
    [("Caio", 22), ("Ana", 25), ("Bia", 30)],
)
verificar("não altera a lista original", pessoas, [("Bia", 30), ("Caio", 22), ("Ana", 25)])

print("\n--- Questão 4: apenas_pares ---")
verificar("mistura de pares e ímpares", apenas_pares([1, 2, 3, 4, 5, 6]), [2, 4, 6])
verificar("somente ímpares", apenas_pares([1, 3, 5]), [])

print("\n--- Questão 5: aplicar_desconto ---")
verificar(
    "desconto de 10%",
    aplicar_desconto([100.0, 59.90, 10.0]),
    [90.0, 53.91, 9.0],
)

print("\n--- Questão Bônus: total_acima_de ---")
vendas = [
    {"produto": "Teclado", "valor": 120.0},
    {"produto": "Mouse", "valor": 45.0},
    {"produto": "Monitor", "valor": 899.0},
]
verificar("mínimo 100", total_acima_de(vendas, 100), 1019.0)
verificar("mínimo 1000", total_acima_de(vendas, 1000), 0)

total = len(RESULTADOS)
aprovados = sum(RESULTADOS)
print(f"\nResultado final: {aprovados}/{total} testes passando")
