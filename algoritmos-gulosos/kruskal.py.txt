import sys
import time


def ler_grafo(arquivo)
    with open(arquivo) as f
        n = int(f.readline())
        adj = [[0]  n for _ in range(n)]
        for i in range(n - 1)
            valores = list(map(int, f.readline().split()))
            for k, j in enumerate(range(i + 1, n))
                adj[i][j] = valores[k]
                adj[j][i] = valores[k]
    return n, adj


class UnionFind
    def __init__(self, n)
        self.pai = list(range(n))
        self.rank = [0]  n

    def find(self, x)
        if self.pai[x] != x
            self.pai[x] = self.find(self.pai[x])
        return self.pai[x]

    def union(self, x, y)
        rx, ry = self.find(x), self.find(y)
        if rx == ry
            return False
        if self.rank[rx]  self.rank[ry]
            rx, ry = ry, rx
        self.pai[ry] = rx
        if self.rank[rx] == self.rank[ry]
            self.rank[rx] += 1
        return True


def kruskal(n, adj)
    arestas = []
    for i in range(n)
        for j in range(i + 1, n)
            if adj[i][j]  0
                arestas.append((adj[i][j], i, j))
    arestas.sort()

    uf = UnionFind(n)
    custo = 0
    arvore = []

    for w, u, v in arestas
        if uf.union(u, v)
            custo += w
            arvore.append((u, v, w))
            if len(arvore) == n - 1
                break

    return custo, arvore


if __name__ == __main__
    if len(sys.argv)  2
        print(Uso python kruskal.py arquivo_instancia)
        sys.exit(1)

    arquivo = sys.argv[1]
    n, adj = ler_grafo(arquivo)

    inicio = time.time()
    custo, arvore = kruskal(n, adj)
    fim = time.time()

    print(fInstância {arquivo})
    print(fAlgoritmo Kruskal)
    print(fCusto MST {custo})
    print(fTempo {(fim - inicio)  1000.4f} ms)