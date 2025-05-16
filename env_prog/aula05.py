import argparse#argparse, e uma analizador de variaveis que vem do terminal

def le_arquivo(nome_arq, delimitador = ',', comeco = 1, fim_exclusivo = None):
    with open(nome_arq, "r") as arquivo: #uma aplicacao do with, é para gerenciar contextos, pois tudo o que foi feino neles quando finaliza é fechado
        # pegamos nosso arquivo, tiramos espacos e aspas duplas,tiramos virgulas no final do arquivo, separamos com um delimitador cada linha do arquivo definida no slice
        linhas = [tuple(linhas.strip().strip('"').rstrip(",").split(delimitador)) for linhas in arquivo.readlines()[comeco:fim_exclusivo]]
    len_cabecalho = len(linhas[0])
    for numero, linha in enumerate(linhas):
        try:
            assert len(linha) == len_cabecalho
        except AssertionError:
            print(f"Na linha {numero + comeco - 1} do arquivo {nome_arq} temos uma quantidade diferente de colunas ({len(linha)}) a do cabecalho ({len_cabecalho})")
    print(f"{numero} linhas processadas do arquivo {nome_arq}") #aqui numero, sera o numero da linha final
            


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ler um arquivo csv")
    parser.add_argument("csv", type=open, help="Arquivo CSV") 
    #print(dir(parser.parse_args()))
    le_arquivo(nome_arq=parser.parse_args().csv.name, delimitador='","', comeco=1)