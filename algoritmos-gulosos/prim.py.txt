import sys
import heapq
import time


def ler_grafo(arquivo):
    with open(arquivo) as f:
        n = int(f.readline())
        adj = [[0] * n for _ in range(n)]
        for i in range(n - 1):
            valores = list(map(int, f.readline().split()))
            for k, j in enumerate(range(i + 1, n)):
                adj[i][j] = valores[k]
                adj[j][i] = valores[k]
    return n, adj


def prim(n, adj):
    INF = float('inf')
    chave = [INF] * n
    pai = [-1] * n
    na_mst = [False] * n

    chave[0] = 0
    heap = [(0, 0)]
    custo = 0
    arvore = []

    while heap:
        w, u = heapq.heappop(heap)

        if na_mst[u]:
            continue
        na_mst[u] = True
        custo += w

        if pai[u] != -1:
            arvore.append((pai[u], u, w))

        for v in range(n):
            if not na_mst[v] and adj[u][v] > 0 and adj[u][v] < chave[v]:
                chave[v] = adj[u][v]
                pai[v] = u
                heapq.heappush(heap, (chave[v], v))

    return custo, arvore


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python prim.py <arquivo_instancia>")
        sys.exit(1)

    arquivo = sys.argv[1]
    n, adj = ler_grafo(arquivo)

    inicio = time.time()
    custo, arvore = prim(n, adj)
    fim = time.time()

    print(f"Instância: {arquivo}")
    print(f"Algoritmo: PRIM")
    print(f"Custo MST: {custo}")
    print(f"Tempo: {(fim - inicio) * 1000:.4f} ms")