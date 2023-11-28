import sys

print("Número de argumentos: ", len(sys.argv) - 1);

if len(sys.argv) < 2:
    print("Numero incorreto de argumentos. Utilize: python atividade16.py nome-a-ser-impresso")
    sys.exit() # Encerra a execução do programa

nome = sys.argv[1];
print("Olá, ", nome);

# Exemplo 1
# Ocorre um erro ao tentar acessar o segundo argumento, pois ele nao existe

# Exemplo 2
# O programa considera apenas o primeiro nome
