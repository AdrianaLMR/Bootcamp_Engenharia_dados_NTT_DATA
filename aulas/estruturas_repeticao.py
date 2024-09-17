print("estrutura de repetição")
#  Estruturas de repetição em Python permitem executar um bloco de código várias vezes com base em condições ou em um número específico 
# de iterações. As duas principais estruturas de repetição em Python são o for e o while.

#  Estrutura for
# A estrutura for é usada para iterar sobre uma sequência (como listas, tuplas, dicionários, strings ou intervalos) e executar um bloco de código
#  para cada item na sequência.

# Iterando sobre uma lista
frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)

# Exemplo com range():
# Iterando sobre um intervalo de números
for i in range(5):  # Vai de 0 a 4
    print(i)

# . Estrutura while
# A estrutura while executa um bloco de código enquanto uma condição especificada for True. Se a condição for False, o loop é interrompido.
# Imprimindo números de 0 a 4
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incrementa o contador para evitar um loop infinito


# Controle de Fluxo dentro dos Loops
# break: Encerra o loop imediatamente, independentemente da condição.
for i in range(10):
    if i == 5:
        break  # Interrompe o loop quando i é igual a 5
    print(i)

# continue: Pula a iteração atual e continua com a próxima iteração do loop.
for i in range(10):
    if i % 2 == 0:
        continue  # Pula a impressão de números pares
    print(i)

# else: Um bloco else opcional pode ser adicionado após um loop. Ele será executado quando o loop terminar normalmente (sem break).
for i in range(5):
    print(i)
else:
    print("Loop terminou.")
