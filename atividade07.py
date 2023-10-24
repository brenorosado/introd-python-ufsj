
## exercicio 1
def exercicio1():
    # criando uma lista
    minha_lista = [1, 2, 3, 4, 5]
    # criando uma tupla
    minha_tupla = (5, 4, 3, 2, 1)
    # criando um dicionário
    meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}

    # exibindo o tipo de cada coleção
    print("Tipo da lista: ", type(minha_lista))
    print("Tipo da tupla: ", type(minha_tupla))
    print("Tipo do dicionário: ", type(meu_dicionario))


## exercicio 2
def exercicio2():

    # criando um dicionário de países e capitais
    paises_capitais = {
        "Brasil": "Brasilia",
        "Estados Unidos": "Washington",
        "Franca": "Paris",
        "Japao": "Toquio",
        "Australia": "Canberra"
    }
    # imprimindo o comprimento do dicionário
    print("Comprimento do dicionário:", len(paises_capitais))

    # imprimindo as entradas do dicionário usando um loop for
    print("Entradas do dicionário:")
    # iniciando a estrutura de repeticao for
    for pais, capital in paises_capitais.items():
        # exibindo as entradas do dicionario
        print(f"{pais} - {capital}")

    # removendo a entrada 'Australia' do dicionario
    del paises_capitais["Australia"]

    # imprimindo as entradas restantes em forma de tuplas
    print("Entradas do dicionário em forma de tuplas:")
    for entrada in paises_capitais.items():
        print(entrada)

    # usando a função get para obter o valor de uma entrada
    pais_buscado = "Franca"
    capital_franca = paises_capitais.get(pais_buscado, "Pais não encontrado")
    print(f"A capital da {pais_buscado} eh {capital_franca}")


# print(exercicio1())
print(exercicio2())