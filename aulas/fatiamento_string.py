print("Fatiamento de strings") 

print(
    """
    É uma técnica muito útil em Python para acessar partes específicas de uma string. 
    O fatiamento de strings utiliza a notação de colchetes [] para extrair substrings. 
    A sintaxe geral é: string[início:fim:passo]
    """
)
print("--" * 10)

# Var global
texto = "Python é divertido"

print("Fatiamento Silpes")
 # Extrai a substring que começa no índice 0 e vai até o índice 6 (não inclui o caractere no índice 6).
print(texto[0:6]) 
print("--" * 10)

print("Omissão de Índices")

# Se omitir o índice inicial, o fatiamento começa no início da string:
print(texto[:6])  # 'Python'
# Se omitir o índice final, o fatiamento vai até o final da string:
print(texto[7:])  # 'é divertido'
print("--" * 10)

print("Uso do Passo")
# O passo pode ser utilizado para obter substrings com intervalos específicos:  
print(texto[::2])  # retorna todos os caracteres da string, mas apenas aqueles em índices pares.
print("--" * 10)

print("Fatiamento Reverso")
# pode usar um passo negativo para reverter a string:
print(texto[::-1])  # 'odivnuf é nohtyP'
print("--" * 10)

print("Fatiamento Negativo")
# Índices negativos podem ser usados para contar a partir do final da string:
print(texto[-11:-1])  # extrai a substring que começa no índice -11 e vai até o índice -1 (não inclui o caractere no índice -1).
print("--" * 10)
