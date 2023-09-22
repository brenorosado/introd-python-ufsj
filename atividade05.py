
# criando o tipo de exception customizado para erro de formula
class FormulaError(Exception):
    "Raised when formula is invalid."

# declarando funcao
def calcular(formula):
    # iniciando bloco try/exception
    try:
        # separando os componentes da formula, que devem ser 2 numeros e 1 operador
        componentes = formula.split(" ");
        # checando se a formula contem exatamente 3 componentes
        if(len(componentes) != 3):
            # acusando erro de formula invalida caso tenha menos ou mais que 3 componentes
            raise FormulaError();
        
        # obtendo e nomeando os 3 componentes da formula
        [primeiroNum, operador, segundoNum] = componentes;
        # convertendo primeiroNum de string para float
        primeiroNum = float(primeiroNum);
        # convertendo segundoNum de string para float
        segundoNum = float(segundoNum);
    
        # declarando variavel de resultado da operacao
        resultado = 0;
        # declarando switch com match das possiveis operacoes
        match operador:
            # caso a operacao seja soma
            case '+':
                # atribuindo ao resultado a soma dos numeros 
                resultado = primeiroNum + segundoNum;
            # caso a operacao seja subtracao
            case '-':
                # atribuindo ao resultado a subtracao dos numeros 
                resultado = primeiroNum - segundoNum;
            # caso a operacao seja multiplicacao
            case '*':
                # atribuindo ao resultado a multiplicacao dos numeros 
                resultado = primeiroNum * segundoNum;
            # caso a operacao seja divisao
            case '/':
                # atribuindo ao resultado a divisao dos numeros 
                if(segundoNum == 0.0):
                    raise ValueError
                resultado = primeiroNum / segundoNum;
            # caso a operacao seja invalida
            case _:
                # acusando erro de formula invalida
                raise FormulaError();
        # exibindo o resultado para o usuario
        print("Resultado da operacao: ", resultado);
        # retornando o resultado caso essa funcao seja usada para integrar outra parte de codigo
        return resultado;
    # tratando errors do tipo FormulaError
    except FormulaError:
        # exibindo mensagem para FormulaError
        print("Formula invalida, os componentes devem estar separados por 1 espaço e serem respectivamente: numero operacao numero. Operacoes validas: +, -, *, /.");
    # tratando errors do tipo ValueError
    except ValueError:
        # exibindo mensagem para ValueError
        print("O primeiro e terceiro componentes da formula devem ser numeros validos. Caso seja uma divisao, o segundo numero nao pode ser 0.");
    # tratando errors que nao foram previstos
    except:
        # exibindo mensagem para erros nao previstos
        print("Ocorreu um erro.")

# declarando a variaval que recebera a formula do usuario
formulaDoUsuario = '';
# iniciando a esturua de repeticao que execute ate que o usuario digite 'sair'
while(formulaDoUsuario != 'sair'):
    # obtendo a formula do usuario
    formulaDoUsuario = input("Insira uma formula no seguinte formato '4 * 2' ou 'sair':");
    
    # verificando se o usuario deseja continuar realizando operacoes
    if(formulaDoUsuario == 'sair'):
        # parando a estrutura caso o usuario tenha digitado 'sair'
        break;
    
    # chamando a funcao para realizar o calculo com a formula do usuario
    calcular(formulaDoUsuario);

# Abaixo estão os resultados para diferentes entradas do usuario:

# 12 + 4: Resultado da operacao:  16.0
# 12 - 4: Resultado da operacao:  8.0
# 12 * 4: Resultado da operacao:  48.0
# 12 / 4: Resultado da operacao:  3.0
# 12 / 0: O primeiro e terceiro componentes da formula devem ser numeros validos. Caso seja uma divisao, o segundo numero nao pode ser 0.
# 12 / 4 * 3: Formula invalida, os componentes devem estar separados por 1 espaço e serem respectivamente: numero operacao numero. Operacoes validas: +, -, *, /.
# 12 4: Formula invalida, os componentes devem estar separados por 1 espaço e serem respectivamente: numero operacao numero. Operacoes validas: +, -, *, /.
# 12 *: Formula invalida, os componentes devem estar separados por 1 espaço e serem respectivamente: numero operacao numero. Operacoes validas: +, -, *, /.
# 12 * =: O primeiro e terceiro componentes da formula devem ser numeros validos. Caso seja uma divisao, o segundo numero nao pode ser 0.
# 12 / abc: O primeiro e terceiro componentes da formula devem ser numeros validos. Caso seja uma divisao, o segundo numero nao pode ser 0.
# def / 12: O primeiro e terceiro componentes da formula devem ser numeros validos. Caso seja uma divisao, o segundo numero nao pode ser 0.