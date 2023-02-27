# Definindo a string
string = 'Teste'

# Criando uma lista com os caracteres da string
lista_caracteres = list(string)

# Invertendo a ordem dos caracteres na lista
lista_caracteres_reversa = []
for i in range(len(lista_caracteres)-1, -1, -1):
    lista_caracteres_reversa.append(lista_caracteres[i])

# Juntando os caracteres invertidos em uma nova string
string_reversa = ''.join(lista_caracteres_reversa)

# Imprimindo o resultado
print(string_reversa)
