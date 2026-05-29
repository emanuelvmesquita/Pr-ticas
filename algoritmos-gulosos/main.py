"""
Executa Kruskal, PRIM e Dijkstra para todas as instâncias e exibe os resultados.
Uso: python main.py
"""

import os
import time
from kruskal import ler_grafo as ler_kruskal, kruskal
from prim import prim
from dijkstra import dijkstra

INSTANCIAS_DIR = os.path.join(os.path.dirname(__file__), "instancias")
INSTANCIAS = ["dij10.in", "dij20.in", "dij40.in", "dij50.in"]


def executar(arquivo):
    n, adj = ler_kruskal(arquivo)

    t0 = time.time()
    custo_k, _ = kruskal(n, adj)
    t_k = (time.time() - t0) * 1000

    t0 = time.time()
    custo_p, _ = prim(n, adj)
    t_p = (time.time() - t0) * 1000

    t0 = time.time()
    dist_d = dijkstra(n, adj, 0, n - 1)
    t_d = (time.time() - t0) * 1000

    return n, custo_k, t_k, custo_p, t_p, dist_d, t_d


def main():
    print("=" * 80)
    print(f"{'Instância':<12} {'n':>4}  "
          f"{'Kruskal(MST)':>14} {'t(ms)':>10}  "
          f"{'PRIM(MST)':>12} {'t(ms)':>10}  "
          f"{'Dijkstra':>10} {'t(ms)':>10}")
    print("=" * 80)

    for nome in INSTANCIAS:
        caminho = os.path.join(INSTANCIAS_DIR, nome)
        if not os.path.exists(caminho):
            print(f"{nome:<12}  arquivo não encontrado: {caminho}")
            continue
        n, ck, tk, cp, tp, dd, td = executar(caminho)
        print(f"{nome:<12} {n:>4}  "
              f"{ck:>14} {tk:>10.4f}  "
              f"{cp:>12} {tp:>10.4f}  "
              f"{dd:>10} {td:>10.4f}")

    print("=" * 80)


if __name__ == "__main__":
    main()