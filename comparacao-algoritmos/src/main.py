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
        if os.path.isfile(caminho_completo) and nome.endswith(".in"):
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

def selecionar_instancias(arquivos):
    print("\nInstancias disponiveis:")
    for i, caminho in enumerate(arquivos, 1):
        print(f"  {i}. {os.path.basename(caminho)}")

    while True:
        entrada = input("\nDigite os numeros das instancias desejadas separados por espaco (ou 'all' para todas): ").strip()

        if entrada.lower() == "all":
            return arquivos

        try:
            indices = [int(x) for x in entrada.split()]
            if all(1 <= idx <= len(arquivos) for idx in indices) and len(indices) > 0:
                return [arquivos[idx - 1] for idx in indices]
            print(f"Informe numeros entre 1 e {len(arquivos)}.")
        except ValueError:
            print("Entrada invalida. Digite numeros inteiros ou 'all'.")

def selecionar_algoritmos():
    algoritmos_disponiveis = ["selection", "insertion"]

    print("\nAlgoritmos disponiveis:")
    for i, alg in enumerate(algoritmos_disponiveis, 1):
        print(f"  {i}. {alg}")

    while True:
        entrada = input("\nDigite os numeros dos algoritmos desejados separados por espaco (ou 'all' para todos): ").strip()

        if entrada.lower() == "all":
            return algoritmos_disponiveis

        try:
            indices = [int(x) for x in entrada.split()]
            if all(1 <= idx <= len(algoritmos_disponiveis) for idx in indices) and len(indices) > 0:
                return [algoritmos_disponiveis[idx - 1] for idx in indices]
            print(f"Informe numeros entre 1 e {len(algoritmos_disponiveis)}.")
        except ValueError:
            print("Entrada invalida. Digite numeros inteiros ou 'all'.")

def executar_comparison(repeticoes, arquivos_selecionados, algoritmos_selecionados):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    larguras_tabela_1 = imprimir_cabecalho_tabela_1()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    caminho_saida = os.path.join(base_dir, "tests", f"resultados_{timestamp}.txt")

    linhas_saida = []

    for caminho_arquivo in arquivos_selecionados:
        valores = ler_instancia(caminho_arquivo)
        nome_arquivo = os.path.basename(caminho_arquivo)
        n = len(valores)

        for algoritmo in algoritmos_selecionados:
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

                linha = linha_tabela(linha_detalhada, larguras_tabela_1)
                print(linha)
                linhas_saida.append(linha)

    rodape = separador(larguras_tabela_1)
    print(rodape)
    linhas_saida.append(rodape)

    with open(caminho_saida, "w", encoding="utf-8") as arquivo_saida:
        arquivo_saida.write("TABELA 1 - TEMPO DE PROCESSAMENTO POR REPETICAO\n")
        arquivo_saida.write(separador(larguras_tabela_1) + "\n")
        arquivo_saida.write(linha_tabela(["Arquivo", "N", "Algoritmo", "Inicio", "Fim", "Repeticao", "Tempo (s)"], larguras_tabela_1) + "\n")
        arquivo_saida.write(separador(larguras_tabela_1) + "\n")
        for linha in linhas_saida:
            arquivo_saida.write(linha + "\n")

    print(f"\nResultados salvos em: {caminho_saida}")

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
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pasta_instancias = os.path.join(base_dir, "instancias-numericas")
    arquivos = listar_arquivos_instancias(pasta_instancias)

    while True:
        repeticoes = ler_repeticoes()

        if repeticoes == 0:
            print("Encerrando o programa.")
            break

        arquivos_selecionados = selecionar_instancias(arquivos)
        algoritmos_selecionados = selecionar_algoritmos()

        executar_comparison(repeticoes, arquivos_selecionados, algoritmos_selecionados)

if __name__ == "__main__":
    main()
