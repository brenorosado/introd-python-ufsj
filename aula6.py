
# Exercício 1:
def exercicio1():
    # Declarando variáveis
    y = 'abc';
    x = 25;
    try:
        print(x/y);
        print(z);
    # Tratando erro de variável não declarada. Neste exercício, a variável z não está declarada;
    except NameError:
        print("Variável z não foi definida");
    # Tratando erro de compatibilidade de variáveis ao fazer a divisão. Neste exercício, a variável y
    # não pode ser utilizada para fazer operações numéricas;
    except TypeError:
        print("Erro de execução do comando. Verifique os tipos das variáveis ou zero no denominador");

# exercicio1();

# Exercício 2:
    # (1º) Verdadeiro, o bloco de try-except está correto;
    # (2º) Falso, o bloco 'finally' pode ser utilizado para executar algo ao final, tendo ocorrido ou não algum erro;
    # (3º) Falso, o bloco 'else' pode ser utilizado junto ao 'except' para executar algo caso nenhum erro tenha ocorrido;
    # (4º) Falso, o código na cláusula 'finally' é executado ao final de maneira independente ao ocorrer erros e a 
    # cláusula 'else' só é executada caso não tenha ocorrido erros.

# Exercício 3:
    # (1º) Falso, pois o print será de uma variável booleana já que está verificando se dois números são iguais.
    # E também será printado a palavra 'finally' da cláusula 'finally';
    # (2º) Falso, pois não há nenhuma raise sobre o valor das variáveis utilizadas.
    # (3º) Verdadeiro, pois a verificação se o número 5 e 6 retornará 'False' e o comando print('finally') da cláusula
    # 'finally' será executado;
    # (4º) Falso, não será exibida a mensagem 'ValueError' pois não há nenhuma raise sobre o valor das variáveis utilizadas.]

# Ecercício 4:
    # () mais de uma cláusula, podendo tratar diversos tipos de erros diferentes e também ter uma cláusula para erros não tratados/previstos.
