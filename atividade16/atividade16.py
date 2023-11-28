# criando arquivo e abrindo-o para escrita
arquivoPalavras = open("atividade16.txt", "w");

# escrevendo linhas no arquivo
arquivoPalavras.write("open\n");
arquivoPalavras.write("write\n");
arquivoPalavras.write("close\n");
arquivoPalavras.write("open\n");
arquivoPalavras.write("read\n");
arquivoPalavras.write("gravar\n")
arquivoPalavras.write("close\n");

# fechando arquivo
arquivoPalavras.close();

# abrindo arquivo para leitura
arquivoPalavras = open("atividade16.txt", "r");

# declarando lista para inserir as palavras lidas
palavras = [];

# lendo linhas do arquivo
for linha in arquivoPalavras:
    # obtendo palavras das linhas
    linha = linha.strip();
    # acrescentando as palavras na lista de palavras lidas
    palavras.append(linha);

# exibindo palavras
print("palavras", palavras);

# fechando arquivo
arquivoPalavras.close();

# abrindo arquivo para leitura
with open("atividade16.txt", "r") as f:
    lines = f.readlines()

# abrindo arquivo para escrita
with open("atividade16.txt", "w") as f:
    for line in lines:
        if line.strip("\n") != "gravar":
            f.write(line)

# abrindo arquivo para leitura
arquivoPalavras = open("atividade16.txt", "r");

# declarando lista para inserir as palavras lidas
palavras = [];

# lendo linhas do arquivo
for linha in arquivoPalavras:
    # obtendo palavras das linhas
    linha = linha.strip();
    # acrescentando as palavras na lista de palavras lidas
    palavras.append(linha);

# exibindo palavras
print("palavras", palavras);