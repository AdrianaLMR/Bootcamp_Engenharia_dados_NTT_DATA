num_1 = 10
num_2 = 5

print(num_1 + num_2) # soma
print(num_1 - num_2) # subtração
print(num_1 * num_2) # multiplicação
print(num_1 / num_2) # divisão
print(num_1 // num_2) # divisão inteira
print(num_1 % num_2) # resto divisão(Módulo)
print(num_1 ** num_2) # exponenciação

# Ordem de resolução de operadores

# Ordem de resolução de operadores
# 1. Parênteses ()
# 2. Exponenciação **
# 3. Negação (-) ou sinal unário
# 4. Multiplicação *, Divisão /, Divisão inteira //, Módulo %
# 5. Adição + e Subtração -

print("Exemplo de ordem de resolução de operadores")

# 1. Primeiro resolve a multiplicação 5 * 2, depois subtrai de 10
print(10 - 5 * 2)  # Saída: 0

# 2. Primeiro resolve o parênteses (10 - 5), depois multiplica por 2
print((10 - 5) * 2)  # Saída: 10

# 3. Igual ao primeiro exemplo, resolve a multiplicação 5 * 2, depois subtrai de 10
print(10 - 5 * 2)  # Saída: 0

# 4. Primeiro resolve a exponenciação 10 ** 5, depois multiplica por 2
print(10 ** 5 * 2)  # Saída: 2000000

# 5. Primeiro resolve a multiplicação 5 * 2 dentro do parênteses, depois a exponenciação
print(10 ** (5 * 2))  # Saída: 10000000000

# 6. Primeiro resolve a divisão 10 / 5, depois multiplica por 2
print(10 / 5 * 2)  # Saída: 4.0

print("Operadores de comparação")
# Igualdade (==)
print(5 == 5)   # True
print(5 == 3)   # False

# Diferença (!=)
print(5 != 3)   # True
print(5 != 5)   # False

# Maior que (>)
print(5 > 3)    # True
print(3 > 5)    # False

# Menor que (<)
print(3 < 5)    # True
print(5 < 3)    # False

# Maior ou igual (>=)
print(5 >= 5)   # True
print(3 >= 5)   # False

# Menor ou igual (<=)
print(3 <= 5)   # True
print(5 <= 3)   # False

print("Operadores de Atribuição")
# Atribuição simples (=)
x = 5
print(x)  # 5

# Atribuição com adição (+=)
x += 3  # Equivalente a: x = x + 3
print(x)  # 8

# Atribuição com subtração (-=)
x -= 2  # Equivalente a: x = x - 2
print(x)  # 6

# Atribuição com multiplicação (*=)
x *= 4  # Equivalente a: x = x * 4
print(x)  # 24

# Atribuição com divisão (/=)
x /= 3  # Equivalente a: x = x / 3
print(x)  # 8.0

# Atribuição com módulo (%=)
x %= 5  # Equivalente a: x = x % 5
print(x)  # 3.0

# Atribuição com exponenciação (**=)
x **= 2  # Equivalente a: x = x ** 2
print(x)  # 9.0

print("Operadores lógicos")

# Operador AND (e), ambas opções devem ser verdadeiras para ser true
print(True and True)   #True
print(True and False) # False

saldo = 1000
saque = 200
limite = 100
print(saldo >= saque and saque <= limite)

# Operador OR (ou), ambas devem sevem false para retornar false, caso contraio é true
print(True or False)   # True
print(False or False)  # False

# Operador NOT (não), inverte o resultado not true = false
print(not True)        # False
print(not False)       # True

contatos_emergencia = [] # string ou listas sem elementos são falsos
not 1000 > 1500 #True
not contatos_emergencia # True
not "Saque 1500;" #False
not ""  # True

# Precedência com parênteses
print("Precedência com parênteses operadores lógicos")
estudante_aprovado = True
fez_projeto_final = False
atingiu_nota_minima = True

resultado = estudante_aprovado or (fez_projeto_final and atingiu_nota_minima)
print(resultado)  # Saída: True

print("Operadores de identidada")
# Os operadores de identidade são usados para comparar objetos e verificar se ocupam o mesmo espaço na memória. Eles são:

# is: Retorna True se os dois objetos comparados forem o mesmo objeto.
# is not: Retorna True se os dois objetos comparados não forem o mesmo objeto.

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)      # False - a e b têm os mesmos valores, mas não são o mesmo objeto
print(a is c)      # True  - a e c são o mesmo objeto
print(a is not b)  # True  - a e b não são o mesmo objeto

curso = "Curso de Python"
nome_curso = curso
valor , tempo = 200, 200


curso is nome_curso # True
curso is not nome_curso # Falso, pois ambos utilizam a mesma posição na memória
valor is tempo # True

print("Operadores de associação")
# Os operadores de associação são usados para verificar se um valor ou objeto está presente em uma sequência (como listas, strings, tuplas). Eles são:
# Case Sensitive
# in: Retorna True se o valor estiver presente na sequência.
# not in: Retorna True se o valor não estiver presente na sequência.

lista = [1, 2, 3, 4, 5]
texto = "Python"

print(3 in lista)       # True - o valor 3 está na lista
print(6 in lista)       # False - o valor 6 não está na lista
print('P' in texto)     # True - a letra 'P' está presente na string "Python"
print('Java' in texto)  # False - "Java" não está presente na string "Python"

texto not in lista # Verifica se a string está na lista / True
saldo = 500 
saldo += 300
print(saldo)