def abrir_csv(paht_arquivo, separador, comeco = 0, fim_exlusivo = None):
    """Abrir arquivo csv e comverter cada linha em uma tupla, onde cada elemento é um elemento da tupla"""

    
    lista = [] #iniciamos a lista vazia que sera preenchida
    arquivo = open(f"{paht_arquivo}", "r") #abrimos o arquivo e o inserimos em uma variavel, apenas como leitura

    for linhas in arquivo:
        #pegamos nossa lista vazia, e adicionamos no final dela uma tupla onde cada elemento é um elemento separador por virgula
        lista.append(tuple(iterador_para_as_linhas.strip('"') for iterador_para_as_linhas in linhas.strip().split(f"{separador}")))
        lista_total = lista[comeco:fim_exlusivo] 

    return lista_total
    
if __name__ == "__main__":
    csv = abrir_csv("/home/fgv/code/env_prog/arc/dados.csv",",",comeco=5)    
    print(csv)
    