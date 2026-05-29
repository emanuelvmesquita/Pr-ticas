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


def dijkstra(n, adj, origem, destino):
    INF = float('inf')
    dist = [INF] * n
    dist[origem] = 0
    heap = [(0, origem)]

    while heap:
        d, u = heapq.heappop(heap)

        if d > dist[u]:
            continue
        if u == destino:
            break

        for v in range(n):
            if adj[u][v] > 0:
                nd = dist[u] + adj[u][v]
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

    return dist[destino]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python dijkstra.py <arquivo_instancia>")
        sys.exit(1)

    arquivo = sys.argv[1]
    n, adj = ler_grafo(arquivo)

    origem = 0
    destino = n - 1

    inicio = time.time()
    menor_caminho = dijkstra(n, adj, origem, destino)
    fim = time.time()

    print(f"Instância: {arquivo}")
    print(f"Algoritmo: Dijkstra")
    print(f"Origem: {origem}, Destino: {destino}")
    print(f"Caminho mínimo: {menor_caminho}")
    print(f"Tempo: {(fim - inicio) * 1000:.4f} ms")