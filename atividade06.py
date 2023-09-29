
# declaracao da funcao do exercicio 1 recebendo a lista de numeros inteiros chamada "numeros"
def calcQuadrados(numbers):
    # declarando a lista que será onde será adicionado os resultados das operações;
    quadrados = [];
    # iniciando a estrutura de repeticao for para iterar em cada numero da lista numeros
    for number in numbers:
        # adicionando a lista de resultados "quadrados" o numero elevado ao quadrado
        quadrados.append(pow(number, 2))
    
    # exibindo os resultados p/ usuario
    print("Quadrados: ", quadrados);
    # retornando os resultados
    return quadrados;

# calcQuadrados([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);

# declarando funcao do exercicio 2 recebndo as duas listas que serão iteradas
def mostrarListas(lista1, lista2):
    # exibindo uma primeira linha só para indicar que a primeira coluna de números
    # são da lsita 1 e a segunda coluna de numeros da lista 2
    print("Lista 1   |   Lista 2");
    # iniciando a estrutura de repeticao for iterando para o tamanho da lista1
    # estou considerando que a lista 1 e a lista 2 terão sempre o mesmo tamanho
    for i in range(len(lista1)):
        # exibindo os numeros de ambas as listas, a lista 1 na ordem fornecida
        # e a lista 2 na ordem inversa
        print(lista1[i], "             ", lista2[len(lista2) -1 -i])

# mostrarListas([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# declarando funcao do exercicio 3 recendo a lista que terá itens removidos
def removerItensDaLista(lista):
    # exibindo a lista recebida
    print(lista);
    # excluindo o segundo item (index 1) da lista com pop
    lista.pop(1);
    # exibindo a lista após excluir o segundo item
    print(lista);
    # exibindo o último item da lista com pop
    lista.pop();
    # exibindo a lista após excluir o último elemento
    print(lista);
    # removendo o item "Luisa" da lista com remove
    lista.remove("Luisa");
    # exibindo a lista após exluir o item "Luisa"
    print(lista);
    # excluindo o primeiro item da lista (index 0) com del
    del lista[0];
    # exibindo a lista apos excluir o primeiro item da lista
    print(lista);

# removerItensDaLista(["Luiz Gama", "Dandara", "Luisa", "Conceição", "João Cândido", "Maria Carolina"]);
