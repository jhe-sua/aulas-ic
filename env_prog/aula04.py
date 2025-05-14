obj_range = range(1,56,3) 
print(type(obj_range)) #a funcao range nao cria um objeto do tipo lista, mas sim um objeto do range que é iteravel
print(obj_range, end="\n\n")

obj_list = list(obj_range) #a funcao list converte iteraveis em uma lista
print(obj_list)
print(type(obj_list), end="\n\n")

#generator comprenhension
obj_iterador = (i for i in range(10)) #quero que x receba todos os valores i que estao em range(100), isso porque usamos parentesis, logo criamos um objeto gerador
obj_iterador_list = list(obj_iterador)
print(obj_iterador_list)
print(type(obj_iterador),end="\n\n")

#List comprehension
obj_list_compre = [i for i in "abacaxi"]
print(type(obj_list_compre))
print(obj_list_compre, end="\n\n")

#set comprehension
obj_set = {i for i in "abacaxi"}
print(obj_set)
print(type(obj_set), end="\n\n")

#dict comprehension
obj_dict = {k:v for k,v in enumerate("abacaxi")}
print(obj_dict)
print(type(obj_dict), end="\n\n")

obj_dict2 = dict(enumerate("abacaxi"))
print(obj_dict2)
print(type(obj_dict2), end="\n\n")

#objeto zip
#tambem é um objeto iteravel, que junta outros objetos iteraveis na sua ordem
#o primeiro com o primeiro com o primeiro... o segundo com o segundo com o segundo...
#se um objeto iteravel é maior do que o outro, zip os junta ate o tamanho do menor

word = "paralelepipedo"
numeros = [1, 2, 3, 4, 5]
obj_zip = zip(word,numeros) #esse objeto pode ser convertido em uma tupla, lista, diccionario...
print(list(obj_zip))
print(type(obj_zip), end="\n\n")


