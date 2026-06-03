#!/usr/bin/env python3
"""
Problema da Mochila Inteira - Programação Dinâmica
UFPB - Estrutura de Dados e Complexidade de Algoritmos
"""

import sys
import time
import numpy as np


def mochila_dp(n, M, pesos, valores):
    """
    DP 0/1 com array 1D (rolling) e tabela booleana de rastreamento.

    Recorrência:
        dp[w] = max(dp[w], dp[w - p_i] + v_i)   para w de M até p_i

    Complexidade: O(n * M) tempo, O(n * M) espaço (tabela kept)
    """
    dp = np.zeros(M + 1, dtype=np.int64)
    # kept[i, w] = True se o item i foi escolhido na solução ótima com capacidade w
    kept = np.zeros((n, M + 1), dtype=np.bool_)

    for i in range(n):
        p, v = pesos[i], valores[i]
        if p > M:
            continue
        old_dp = dp.copy()
        # candidates[j] = old_dp[j] + v  →  dp[p+j] se for melhor
        candidates = old_dp[: M + 1 - p] + v
        mask = candidates > old_dp[p:]
        dp[p:] = np.where(mask, candidates, old_dp[p:])
        kept[i, p:] = mask

    # Reconstrução dos itens selecionados (traceback)
    w = M
    selecionados = []
    for i in range(n - 1, -1, -1):
        if w >= pesos[i] and kept[i, w]:
            selecionados.append(i + 1)  # índice 1-based
            w -= pesos[i]

    selecionados.reverse()
    return int(dp[M]), selecionados


def ler_instancia(filename):
    with open(filename, "r") as f:
        n, M = map(int, f.readline().split())
        pesos, valores = [], []
        for _ in range(n):
            p, v = map(int, f.readline().split())
            pesos.append(p)
            valores.append(v)
    return n, M, pesos, valores


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python mochila_dp.py <arquivo_instancia>")
        sys.exit(1)

    arquivo = sys.argv[1]
    n, M, pesos, valores = ler_instancia(arquivo)

    print(f"Instância : {arquivo}")
    print(f"Itens     : {n}   Capacidade: {M}")

    t0 = time.time()
    valor, itens = mochila_dp(n, M, pesos, valores)
    elapsed = time.time() - t0

    peso_total = sum(pesos[i - 1] for i in itens)

    print(f"Valor ótimo         : {valor}")
    print(f"Itens selecionados  : {', '.join(map(str, itens))}")
    print(f"Peso total          : {peso_total} / {M}")
    print(f"Tempo de execução   : {elapsed:.4f}s")
