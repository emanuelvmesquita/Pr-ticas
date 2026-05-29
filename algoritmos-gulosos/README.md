# Algoritmos Gulosos em Grafos
Projeto acadêmico da disciplina **Estrutura de Dados e Análise de Algoritmos** (Mestrado). Implementa e compara empiricamente três algoritmos gulosos clássicos em grafos ponderados.
***

## Estrutura do projeto

```
algoritmos-gulosos/
├── main.py.txt           — script principal: executa e compara os três algoritmos
├── dijkstra.py.txt       — caminho mínimo entre vértice 0 e vértice n-1
├── kruskal.py.txt        — Árvore Geradora Mínima via Union-Find
├── prim.py.txt           — Árvore Geradora Mínima via heap
├── gera_instancia.py.txt — gerador de instâncias aleatórias
└── instancias/           — arquivos de entrada (.in)
```

## O que o projeto faz

O `main.py` executa os três algoritmos sobre as instâncias em `instancias/` e exibe os resultados em tabela ASCII no terminal:

```
================================================================================
Instância      n    Kruskal(MST)      t(ms)     PRIM(MST)      t(ms)   Dijkstra      t(ms)
================================================================================
dij10.in       10           ...          ...           ...         ...        ...        ...
dij20.in       20           ...          ...           ...         ...        ...        ...
...
================================================================================
```

Colunas exibidas: nome da instância, número de vértices, custo da MST (Kruskal), tempo (ms), custo da MST (Prim), tempo (ms), distância mínima (Dijkstra), tempo (ms).

## Algoritmos implementados

| Algoritmo   | Problema              | Estrutura auxiliar        | Complexidade         |
|-------------|-----------------------|---------------------------|----------------------|
| Kruskal     | Árvore Geradora Mínima | Union-Find (path compression + union by rank) | O(E log E) |
| Prim        | Árvore Geradora Mínima | Min-heap (fila de prioridade) | O(E log V)    |
| Dijkstra    | Caminho Mínimo (0 → n−1) | Min-heap (fila de prioridade) | O((V + E) log V) |

## Formato das instâncias

Os arquivos de entrada usam o **triângulo superior** da matriz de adjacência:

```
n
w[0][1] w[0][2] ... w[0][n-1]
w[1][2] w[1][3] ... w[1][n-1]
...
w[n-2][n-1]
```

Onde `n` é o número de vértices e `w[i][j]` é o peso da aresta entre os vértices `i` e `j`. O grafo é não-direcionado: cada peso é espelhado internamente para formar a matriz completa.

## Como executar

### 1. Gerar instâncias

```bash
python gera_instancia.py.txt <n> <seed> instancias/dij<n>.in
```

Exemplo — instâncias usadas pelo `main.py`:

```bash
python gera_instancia.py.txt 10  1 instancias/dij10.in
python gera_instancia.py.txt 20  2 instancias/dij20.in
python gera_instancia.py.txt 40  3 instancias/dij40.in
python gera_instancia.py.txt 50  4 instancias/dij50.in
```

### 2. Executar o comparativo

```bash
python main.py.txt
```

### 3. Executar algoritmos individualmente

```bash
python dijkstra.py.txt instancias/dij10.in
python prim.py.txt     instancias/dij10.in
python kruskal.py.txt  instancias/dij10.in
```

## Objetivo

Implementar e comparar o desempenho de três algoritmos gulosos sobre grafos:
- **Kruskal** — constrói a MST ordenando arestas por peso e usando Union-Find para evitar ciclos
- **Prim** — constrói a MST crescendo a partir de um vértice inicial via heap mínimo
- **Dijkstra** — encontra o caminho mínimo do vértice `0` ao vértice `n−1` via heap mínimo
