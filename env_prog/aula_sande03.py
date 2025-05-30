palavra = "walter é maravilhoso"

#ord("d") = 100
#chr(100) = "d"
#valor total de chr = 110000

#guerra con palavras
# 
#quero pegar uma string, se a quantidade de caracteres é impa o caractere impa é o medio e fica invariante
#se for par o medio é o nada
#as duas strings resultantes (da direita e da esquerda)
#os valores das letras das extremidades são comparados, o maior valor ganha, entao se subtraem os dois valores, o maior pelo menor
#isso deixara um valor que sera convertido em caractere e adicionado no string ganhador, assim ate um dos strings ficar sem letras
#se as duas são iguais, a subtração dara 0
#nessa situação o caracter imediatamente depois do seguinte é adicionado a "guerra" e denovo é calculado o valor e assim por diante
#ate uma string "ganhar" a guerra, se ela ganhar, subtrai cada letra 2 a 2, isso deixara uma letra por cada subtração que sera adicionada em sequencia na string ganhadora
#se uma string esta em guerra e ficar sem caracteres a guerra é imediatamente efetuada, 

valor_total = 0
for letra in palavra:
    valor_total += ord(letra)

print(valor_total)
