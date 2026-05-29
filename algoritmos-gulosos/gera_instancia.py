"""
Gera instâncias aleatórias no formato esperado (triângulo superior).
Uso: python gera_instancia.py <n> <seed> <arquivo_saida>
"""

import sys
import random


def gerar(n, seed, arquivo):
    random.seed(seed)
    with open(arquivo, "w") as f:
        f.write(f"{n}\n")
        for i in range(n - 1):
            linha = [str(random.randint(1, 1000)) for _ in range(i + 1, n)]
            f.write(" ".join(linha) + "\n")
    print(f"Instância gerada: {arquivo} (n={n}, seed={seed})")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python gera_instancia.py <n> <seed> <arquivo_saida>")
        sys.exit(1)
    gerar(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])