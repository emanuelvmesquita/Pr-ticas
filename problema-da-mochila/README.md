# Problema da Mochila Inteira — Programação Dinâmica

**Disciplina:** Estrutura de Dados e Complexidade de Algoritmos  
**Instituição:** Universidade Federal da Paraíba — Centro de Informática

---

## Descrição do Problema

Dado um conjunto de objetos $O$, escolher um subconjunto $S \subseteq O$ tal que:

- A soma dos pesos não ultrapasse a capacidade da mochila: $\sum_{i \in S} p_i \leq M$
- O valor total seja máximo: $\max \sum_{i \in S} v_i$

---

## Solução

A solução utiliza **Programação Dinâmica** com array unidimensional (*rolling array*) e uma tabela booleana auxiliar para reconstrução dos itens selecionados.

### Recorrência

$$dp[w] = \max(dp[w],\ dp[w - p_i] + v_i), \quad w = M, M-1, \ldots, p_i$$

A tabela `kept[i][w]` registra se o item $i$ foi incluído na solução ótima com capacidade $w$, permitindo reconstruir quais itens foram escolhidos ao final.

### Complexidade

| | |
|---|---|
| Tempo | $O(n \times M)$ |
| Espaço | $O(n \times M)$ |

---

## Formato de Entrada

```
n M
p1 v1
p2 v2
...
pn vn
```

| Campo | Descrição |
|---|---|
| `n` | Número de itens |
| `M` | Capacidade da mochila |
| `pi` | Peso do item $i$ |
| `vi` | Valor do item $i$ |

---

## Como Executar

**Requisito:** Python 3 com NumPy instalado.

```bash
python mochila_dp.py instancias/<arquivo>.txt
```

**Exemplo:**

```bash
python mochila_dp.py instancias/mochila01.txt
```

**Saída:**

```
Instância : instancias/mochila01.txt
Itens     : 7   Capacidade: 23
Valor ótimo         : 107
Itens selecionados  : 1, 2, 6, 7
Peso total          : 23 / 23
Tempo de execução   : 0.0002s
```

---

## Instâncias de Teste

| Arquivo | Itens (n) | Capacidade (M) | Valor ótimo | Tempo |
|---|---|---|---|---|
| `mochila01.txt` | 7 | 23 | 107 | < 0.001 s |
| `mochila02.txt` | 5 | 10 | 130 | < 0.001 s |
| `mochila1000.txt` | 1000 | 12811 | 4135 | ~0.04 s |
| `mochila2500.txt` | 2500 | 31896 | 37138 | ~0.20 s |
| `mochila5000.txt` | 5000 | 62862 | 71811 | ~0.77 s |

As soluções de `mochila01` e `mochila02` foram verificadas contra o gabarito fornecido.

---

## Estrutura do Projeto

```
problema-da-mochila/
├── mochila_dp.py       # Implementação da solução
└── instancias/
    ├── mochila01.txt
    ├── mochila02.txt
    ├── mochila1000.txt
    ├── mochila2500.txt
    └── mochila5000.txt
```
