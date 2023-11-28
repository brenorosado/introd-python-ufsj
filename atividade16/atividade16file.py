
arquivo = open("arquivo.txt", "w");

arquivo.write("banana");
arquivo.write("melancia");

arquivo.close();

##########################################

arquivo = open("arquivo.txt", "a");

arquivo.write("morango\n");
arquivo.write("manga\n");

arquivo.close();

##########################################

arquivoPalavras = open("palavras.txt", "w");

arquivoPalavras.write("open\n");
arquivoPalavras.write("write\n");
arquivoPalavras.write("close\n");
arquivoPalavras.write("open\n");
arquivoPalavras.write("read\n");
arquivoPalavras.write("close\n");

arquivoPalavras.close();

arquivoPalavras = open("palavras.txt", "r");

palavras = [];

for linha in arquivoPalavras:
    linha = linha.strip();
    palavras.append(linha);

print("palavras", palavras);

arquivoPalavras.close();