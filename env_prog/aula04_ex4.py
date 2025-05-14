def abrir_csv(paht_arquivo, separador, comeco = 0, fim_exlusivo = None):
    """Abrir arquivo csv e comverter cada linha em uma tupla, onde cada elemento é um elemento da tupla"""
    lista = []
    arquivo = open(f"{paht_arquivo}", "r")

    for i in arquivo:
        lista.append(tuple(p.strip('"') for p in i.strip().split(f"{separador}")))
    lista_total = lista[comeco:fim_exlusivo]
    print(lista_total)
    
    
    
abrir_csv("/home/fgv/code/env_prog/arc/dados.csv",",",comeco=5)