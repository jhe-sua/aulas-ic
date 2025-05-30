# implementando guerra de strings em python, para 2 jogadores

# introdução
uma string é um conjunto de caracteres,no python, cada caracter possui uma representação decimal e cada numero decimal possui uma representação em caracter desde 0 ate 110000
o nosso objetivo é tentar recriar o jogo "guerra" que é feito com cartas, da seguinte forma:

1. cada string possui uma quantidade de caracteres, cada caracter representa uma carta
    aqui iniciaremos com string_total que contem nossa frase

2. cada jogador recebe a mesma quantidade de cartas
    aqui criaremos string_esquerda e string_direita, cada uma delas recebera um caracter de string_total ate string_total ficar com 1 caracter se len(string_total) for impa ou 0 se for par

3. cada string possui um ordem
    depois começa o jogo, pegamos o primeiro elemento de string_direita e o primeiro de string_esquerda, comparamos o valor decimal deles para saber se um é maior do que o outro ou se são iguais, se um for maior do que o outro a string dona desse caracter ganhar, e leva os dois para sua "pilha", entao teremos string_direita_pilha e string_esquerda_pilha

4. a pilha
    a pilha é adicionada ao final de sua respeitiva string (parte da animação), a string em si, não conta os elementos da pilha como dela, quando os elementos da string acabarem, ela pega a pilha, embaralha os elementos que estejam presentes e adiciona eles a si mesma, a pilha é sempre acionada quando a string ficar sem caracteres

5. guerra
    quando comparamos dois caracteres e seu valor decimal é igual, fazemos "guerra", ela funciona assim: 

    criase um ambiente de guerra, onde esses dois caracteres são adicionados, depois cada string adiciona outro caracter, se não tiver acciona a pilha, acontecera a "ultima guerra" se sim tiver caracteres, entao serao adicionados mas eles não participarão da guerra, e depois são colocados os proximos que serao comparados apenas eles, chegando novamente no 