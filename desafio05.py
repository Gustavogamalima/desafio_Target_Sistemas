# Definindo a string a ser invertida
string = "Olá, mundo!"

# Convertendo a string em uma lista de caracteres
caracteres = list(string)

# Invertendo a ordem dos caracteres na lista
caracteres_invertidos = caracteres[::-1]

# Convertendo a lista de volta para uma string
string_invertida = "".join(caracteres_invertidos)

# Imprimindo a string invertida
print(string_invertida)
