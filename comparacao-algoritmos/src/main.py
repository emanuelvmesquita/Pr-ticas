import os
import time
from datetime import datetime

def ler_instancia(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read().split()
        numeros = [int(valor) for valor in conteudo]

    if len(numeros) > 1 and numeros[0] == len(numeros) - 1:
        return numeros[1:]

    return numeros

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        menor_indice = i
        for j in range(i + 1, n):
            if arr[j] < arr[menor_indice]:
                menor_indice = j
        arr[i], arr[menor_indice] = arr[menor_indice], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = chave

def esta_ordenado(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def formatar_data_hora(data_hora):
    return data_hora.strftime("%d/%m/%Y %H:%M:%S")

def executar_algoritmo(nome_algoritmo, valores):
    copia = valores[:]

    inicio_datahora = datetime.now()
    inicio_perf = time.perf_counter()

    if nome_algoritmo == "selection":
        selection_sort(copia)
    elif nome_algoritmo == "insertion":
        insertion_sort(copia)
    else:
        raise ValueError(f"Algoritmo desconhecido: {nome_algoritmo}")

    fim_perf = time.perf_counter()
    fim_datahora = datetime.now()

    return copia, inicio_datahora, fim_datahora, fim_perf - inicio_perf

def listar_arquivos_instancias(caminho_pasta):
    arquivos = []

    for nome in os.listdir(caminho_pasta):
        caminho_completo = os.path.join(caminho_pasta, nome)
        if os.path.isfile(caminho_completo):
            arquivos.append(caminho_completo)

    arquivos.sort()
    return arquivos

def separador(larguras):
    return "+-" + "-+-".join("-" * largura for largura in larguras) + "-+"

def linha_tabela(valores, larguras):
    colunas = []
    for valor, largura in zip(valores, larguras):
        colunas.append(f"{str(valor):<{largura}}")
    return "| " + " | ".join(colunas) + " |"

def imprimir_cabecalho_tabela_1():
    cabecalho = [
        "Arquivo",
        "N",
        "Algoritmo",
        "Inicio",
        "Fim",
        "Repeticao",
        "Tempo (s)",
    ]
    larguras = [20, 8, 12, 19, 19, 10, 12]

    print()
    print("TABELA 1 - TEMPO DE PROCESSAMENTO POR REPETICAO")
    print(separador(larguras))
    print(linha_tabela(cabecalho, larguras))
    print(separador(larguras))

    return larguras

def executar_benchmark(repeticoes):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pasta_instancias = os.path.join(base_dir, "instancias-numericas")
    algoritmos = ["selection", "insertion"]

    arquivos = listar_arquivos_instancias(pasta_instancias)
    larguras_tabela_1 = imprimir_cabecalho_tabela_1()

    for caminho_arquivo in arquivos:
        valores = ler_instancia(caminho_arquivo)
        nome_arquivo = os.path.basename(caminho_arquivo)
        n = len(valores)

        for algoritmo in algoritmos:
            for repeticao in range(1, repeticoes + 1):
                ordenado, inicio, fim, tempo_execucao = executar_algoritmo(
                    algoritmo, valores
                )

                if not esta_ordenado(ordenado):
                    raise ValueError(
                        f"O algoritmo {algoritmo} nao ordenou corretamente."
                    )

                linha_detalhada = [
                    nome_arquivo,
                    n,
                    algoritmo,
                    formatar_data_hora(inicio),
                    formatar_data_hora(fim),
                    repeticao,
                    f"{tempo_execucao:.6f}",
                ]

                print(linha_tabela(linha_detalhada, larguras_tabela_1))

    print(separador(larguras_tabela_1))

def ler_repeticoes():
    while True:
        entrada = input(
            "\nDigite a quantidade de repeticoes (ou 0 para sair): "
        ).strip()

        try:
            repeticoes = int(entrada)

            if repeticoes < 0:
                print("Informe um numero inteiro maior ou igual a zero.")
                continue

            return repeticoes

        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.")

def main():
    while True:
        repeticoes = ler_repeticoes()

        if repeticoes == 0:
            print("Encerrando o programa.")
            break

        executar_benchmark(repeticoes)

if __name__ == "__main__":
    main()