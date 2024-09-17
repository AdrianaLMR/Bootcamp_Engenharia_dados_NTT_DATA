print("String \n")

curso = "Python"
print(f"Exemplo de uma string: {curso}")

print("\n Métodos com string \n")

# Lower converte todos os caracteres da string para minúsculos
palavra = "Exemplo de TEXTO com LOWER"
print(palavra.lower())

# Upper converte op todos caracteres em maiúsculos
frase = "Exemplo de TEXTO com UPPER"
print(frase.upper())

#Title  Converte a primeira letra de cada palavra em maiúscula e o restante em minúsculas.
texto = "exemplo de TEXTO com TITLE"
print(texto.title())  # Saída: "Exemplo De Texto"

print("\n Removendo espaços nas strings \n")

# strip Remove espaços em branco no início e no final da string.
texto = "   exemplo de TEXTO strip   "
print(texto.strip())  

# strip Remove espaços da esquerda da string.
texto = "   exemplo de TEXTO  lstrip  "
print(texto.lstrip())  

# strip Remove espaços da direita da string.
texto = "   exemplo de TEXTO rstrip   "
print(texto.rstrip())  

# Remover espaços duplicados:  Pode-se usar replace(" ", " ") repetidamente ou uma combinação de split() e join() para remover espaços
#  duplicados entre palavras.
texto = "exemplo   de   TEXTO   com   combinação   de    split()    e    join()"
print(" ".join(texto.split()))  

# Aplicando title() e removendo espaços:
texto = "   exemplo   de   TEXTO    com   combinação   de   title()    e    join()"
texto_formatado = " ".join(texto.split()).title()  # Remove espaços e aplica title()
print(texto_formatado)  # Saída: "Exemplo De Texto"

print("\n Junções e centralizações \n")

#  center() centraliza a string, preenchendo os espaços ao redor com um caractere (por padrão, espaços em branco) até que a string atinja o comprimento especificado.
aula = "STRINGS para método center"
print(aula.center(10, "#")) # preenchimento personalizado

centralizado = aula.center(10)  # Centraliza em um espaço de 10 caracteres
print(centralizado)

# join() é utilizado para juntar elementos de uma sequência (como uma lista de strings) em uma única string, separando-os por um delimitador que você define.
text =  "STRINGS para método join"
print(".".join(text))

palavras = ['STRINGS',  'para', 'método', 'join', 'com', 'array']
paragrafo = " ".join(palavras) 
print(paragrafo)