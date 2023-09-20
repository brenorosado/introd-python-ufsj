if __name__ == "__main__":

    def concWords(*args):
        for word in args:
            print(word, end=" ")

    def printUserInfo(**data):
        for key, value in data.items():
            print("{} é {}".format(key, value))
    
    def calcula_preco_final(valor, **kwargs):
        imposto = kwargs.get('imposto')
        desconto = kwargs.get('desconto')
        valorFinal = valor

        if(imposto != None):
            if((type(imposto) == int) | (type(imposto) == float)):
                valorFinal += imposto
            else:
                print("Tipo do argumento 'imposto' invalido. Utilize int ou float")

        if(desconto != None):
            if((type(desconto) == int) | (type(desconto) == float)):
                valorFinal -= desconto
            else:
                print("Tipo do argumento 'desconto' invalido. Utilize int ou float")

        print("Valor final: ", valorFinal)
            



# concWords("Escrevendo", "código", "python")

# printUserInfo(PrimeiroNome = "Breno", Sobrenome= "Rosado", Idade = 22, Telefone="+55 (33) 998100776")
# printUserInfo(PrimeiroNome = "José", Sobrenome = "Ribeiro", Idade = 23, Curso = "Engenharia Mecatrônica", Email = "jose@gmail.com")

# calcula_preco_final(6500)

# calcula_preco_final(6500, imposto="absd")
# calcula_preco_final(6500, imposto=1500)

# calcula_preco_final(6500, desconto="desconto")
# calcula_preco_final(6500, desconto=1500)

# calcula_preco_final(6500, imposto="750", desconto=1500)
# calcula_preco_final(6500, imposto=750, desconto="1500")
calcula_preco_final(6500, imposto=750, desconto=1500)
