print(""" 
    Conjuntos(sets):  é uma coleção não ordenada e não indexada de itens únicos. Não permite duplicatas, são definidos usando chaves {}. 
    Eles são úteis para armazenar itens únicos e realizar operações matemáticas como união, interseção e diferença.
    Mutáveis: É possível adicionar ou remover elementos de um conjunto (exceto no caso de frozensets, que são imutáveis).
    Pode criar um conjunto usando a função set() ou com chaves {}.
      
    Set são uma coleção que não possui objetos repetidos, usamos ets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.
    Isso não garante a ordem dos itens. 
""")

#func set()
meu_conjunto = set()
print(meu_conjunto)

print(set([1, 2, 1, 3, 4, 2]))
print(set("Abacaxi"))
print(set(("palio", "gol", "fiat")))

# Com chaves{}print
numeros = {1, 2, 3, 4, 5}
print(numeros)

print("Métodos dos Conjuntos")

print("Acessando dados") 
# Conjuntos não suportam indexação e nem fatiamento, caso queira acessar valores é necessário converter o conjunto para lista.
dados_set = {1, 2, 3, 4, 2, 1}
print(dados_set)
acessando_dados_set = list(dados_set)
print(acessando_dados_set[0])

print("Adicionando elementos")
# Adicionar elementos add()
numeros.add(1)
print(numeros)

print("Removendo elementos")
# Removendo elementos remove() (gera erro se o item não existir) e discard() (não gera erro)
numeros.remove(1)
print(numeros)  

numeros.discard(3)
print(numeros)

print("Limpar conjunto")
numeros.clear()
print(numeros)

print("Len(): Retorna o número de elementos únicos no conjunto. ")
print(len(numeros))

print("In():verifica se um elemento está dentro do conjunto. ")
print( 3 in numeros)

print("""
    Copiar conjunto
    É utilizado para criar uma cópia superficial (shallow copy) de um conjunto (ou de outros objetos mutáveis, como listas e dicionários).
""")
conjunto_original = {1, 2, 3}
copia_conjunto = conjunto_original.copy()

print("Original:", conjunto_original)  # {1, 2, 3}
print("Cópia:", copia_conjunto)        # {1, 2, 3}

copia_conjunto.copy()
print(copia_conjunto)

print("""
    Pop():
    Quando aplicado a conjuntos, remove e retorna um elemento arbitrário do conjunto.
    Como os conjuntos são não ordenados, o método não remove necessariamente o "primeiro" elemento, mas sim qualquer elemento aleatório.
    Se o conjunto estiver vazio, o método pop() gera um erro KeyError.
""")

elemento_removido = numeros.pop()
print("Elemento removido:", elemento_removido)
print("Conjunto após pop:", numeros)

print("Operações de conjunto União (union() ou |), Interseção (intersection() ou &), Diferença (difference() ou -).")

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# União (union() ou |)  Combina todos os elementos de dois conjuntos.
print(set1.union(set2))
print(set1 | set2)

#  Interseção (intersection() ou &) Retorna apenas os elementos que estão em ambos os conjuntos
print(set1.intersection(set2))
print(set1 & set2)

# Diferença (difference() ou -) Retorna os elementos que estão no primeiro conjunto, mas não no segundo.
print(set1 - set2)

# Diferença: elementos presentes em set1, mas não em set2
print(set1 - set2) 
print(set1.difference(set2))


# Diferença: elementos presentes em set2, mas não em set1
print(set2 - set1)  
print(set2.difference(set1))

# Diferença Simétrica (^): Retorna os elementos que estão em um conjunto ou no outro, mas não em ambos.
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# {}.isubset: usado para verificar se todos os elementos de um conjunto (set) estão presentes em outro conjunto. Em outras palavras, ele verifica se um conjunto é um subconjunto de outro.
print(set1.issubset(set2))
print(set2.issubset(set1))

# {}.isuperset: usado para verificar se um conjunto contém todos os elementos de outro conjunto. Em outras palavras, ele verifica se um conjunto é um superconjunto de outro.
print(set1.issuperset(set2))
print(set2.issuperset(set1))

# isdisjoint(): verifica se dois conjuntos são disjuntos, ou seja, se eles não possuem nenhum elemento em comum.
A = {1, 2, 3}
B = {4, 5, 6}
C = {3, 4, 5}

print(A.isdisjoint(B))  # Verificar se A e B são disjuntos / True (não há elementos em comum)

print(A.isdisjoint(C))  # Verificar se A e C são disjuntos / False (o elemento 3 está presente em ambos)

print("Verificação de Subconjuntos e Superconjuntos")
set1 = {1, 2}
set2 = {1, 2, 3}

# issubset(): Verifica se um conjunto é subconjunto de outro.
print(set1.issubset(set2))  

# issuperset(): Verifica se um conjunto é superconjunto de outro
print(set2.issuperset(set1))  

print("Verificação de Elementos")

valores = {1, 2}
print(1 in valores)  # True

print("""
    Conjuntos Imutáveis
    os frozensets, que são conjuntos imutáveis.
    Eles compartilham os mesmos métodos de conjuntos normais, exceto pelos métodos que modificam o conjunto (add, remove, etc.).
    """)

meu_frozenset = frozenset([1, 2, 3])
print(meu_frozenset)
# meu_frozenset.add(4)  # Lançará erro, pois o frozenset é imutável.

print("""
    Iterar conjunto
    No contexto de conjuntos (sets), que são coleções desordenadas e sem elementos duplicados, a iteração percorre os itens do conjunto, 
    mas não garante uma ordem específica, pois conjuntos são estruturalmente não ordenados.
""")

# Iterando sobre o conjunto
carros = {"gol", "fiat", "palio"}
for carro in carros:
    print(carro)

print("""
    Função Enumerate
    É usada em iterações para fornecer, além dos itens do iterável, um índice associado a cada item, para conjuntos, como 
    são coleções desordenadas, o índice atribuído pela função enumerate() não tem uma correspondência lógica com uma "posição" dentro do conjunto, já que os elementos não têm uma ordem fixa.
""")

# Iterando sobre o conjunto com enumerate()
salada_frutas = {"maçã", "banana", "laranja"}
for indice, fruta in enumerate(salada_frutas):
    print(f"Índice {indice}: {fruta}")