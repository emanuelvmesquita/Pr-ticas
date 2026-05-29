"""
Gera instâncias aleatórias no formato esperado (triângulo superior).
Uso: python gera_instancia.py <n> <seed> <arquivo_saida> [w_min] [w_max]
"""

import sys
import random


def gerar(n, seed, arquivo, w_min=1, w_max=9999):
    random.seed(seed)
    with open(arquivo, "w") as f:
        f.write(f"{n}\n")
        for i in range(n - 1):
            linha = [str(random.randint(w_min, w_max)) for _ in range(i + 1, n)]
            f.write(" ".join(linha) + "\n")
    print(f"Instância gerada: {arquivo} (n={n}, seed={seed}, pesos=[{w_min},{w_max}])")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: python gera_instancia.py <n> <seed> <arquivo_saida> [w_min] [w_max]")
        sys.exit(1)
    n    = int(sys.argv[1])
    seed = int(sys.argv[2])
    arq  = sys.argv[3]
    wmin = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    wmax = int(sys.argv[5]) if len(sys.argv) > 5 else 9999
    gerar(n, seed, arq, wmin, wmax)