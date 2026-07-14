# Teste Técnico Python — Estágio / Desenvolvedor(a) Júnior

Resoluções do teste técnico de Python com foco em **funções simples** e **expressões lambda**.

> **Resultado:** 14/14 testes passando (todas as questões + bônus)

---

## Estrutura do Projeto

```
codigo_base/
├── desafios/
│   ├── q1_media.py        # Média aritmética
│   ├── q2_saudacao.py     # Saudação com parâmetro padrão
│   ├── q3_ordenacao.py    # Ordenação com sorted() + lambda
│   ├── q4_filtro.py       # Filtragem com filter() + lambda
│   ├── q5_desconto.py     # Transformação com map() + lambda
│   └── q6_bonus.py        # Relatório de vendas (bônus)
├── rodar_testes.py         # Script de verificação automática
└── README.md
```

---

## Questões e Soluções

### Q1 — Média de notas (2 pts)
Função `calcular_media(notas)` que retorna a média arredondada para 2 casas decimais. Retorna `0.0` para lista vazia.

### Q2 — Saudação com parâmetro padrão (2 pts)
Função `saudar(nome, idioma="pt")` que retorna a saudação no idioma pedido (`pt`, `en`, `es`). Idiomas desconhecidos usam o padrão português.

### Q3 — Ordenação com lambda (2 pts)
Função `ordenar_por_idade(pessoas)` que ordena tuplas `(nome, idade)` da mais nova para a mais velha usando `sorted()` com `lambda`.

### Q4 — Filtragem com lambda (2 pts)
Função `apenas_pares(numeros)` que filtra apenas os números pares usando `filter()` com `lambda`.

### Q5 — Transformação com lambda (2 pts)
Função `aplicar_desconto(precos)` que aplica 10% de desconto usando `map()` com `lambda`, arredondando para 2 casas decimais.

### Q6 — Relatório de vendas — Bônus (+1 pt)
Função `total_acima_de(vendas, minimo)` que soma os valores das vendas estritamente acima do mínimo informado.

---

## Como rodar os testes

```bash
python rodar_testes.py
```

---

## Requisitos

- Python 3.x
- Nenhuma biblioteca externa — apenas a biblioteca padrão do Python
