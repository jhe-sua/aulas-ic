def abrir_csv(paht_arquivo):
    lista = []
    arquivo = open(f"{paht_arquivo}", "r")

    for i in arquivo:
        lista.append(tuple(p.strip('"') for p in i.strip().split(",")))
    lista_total = lista[5:]
    print(lista_total[5])
    
    
    
abrir_csv("/home/fgv/code/env_prog/arc/dados.csv")