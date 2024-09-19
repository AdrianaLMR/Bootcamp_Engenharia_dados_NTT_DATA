print("Listas: Uma lista é uma coleção ordenada e mutável de itens. Cada item pode ser de qualquer tipo de dado (inteiros, strings, outras listas, etc.). O índice sempre começa no zero(0)")

#Exemplo de listas

frutas = ["Laranja", "Melão", "Uva", "Morango", "Mmeixa",]
print(frutas)

letras = list("python") # Palavra reservada/ construtor
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari",  "F8", 4200000, 2020, 2090, "São Paulo", True]
print(f"Carro: {carro}")

print("Adicionando elementos a lista")

lista = []
print(lista)

print("Métodos da classe list")

# Adicionando elemento no incio da lista insert()
lista.insert(0, "Luva")
print(lista)

# Adicionando elemento no final da lista apend()
lista.append("Bola")
print(lista)    

print("Removendo elementos a lista")
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
print(num)  

# Remmove o primeiro item correspondente remove()
num.remove(4)
print(num)

# Remmove por índice pop()
num.pop(1)
print(num) 

# Remmove todos elementos clear()
num.clear()
print(num)

# extend(iterável) Estende a lista, adicionando todos os elementos do iterável ao final da lista.
print("Adicionando todos os elementos do iterável ao final da lista")
list_iterável = [1, 2, 3]
list_iterável.extend([4, 5])
print(list_iterável)  

# index(x, start=0, end=len(lista))
print("Retorna o índice do primeiro elemento da lista cujo valor seja x. Se start e end forem fornecidos, busca apenas nesse intervalo. Gera um erro se o valor não for encontrado.")
list_index = [1, 2, 3, 2]
indice = list_index.index(2)
print(indice)  

#Count(x)
print("Retorna o número de ocorrências do elemento x na lista")
list_count = [1, 2, 3, 2]
ocorrencias = list_count.count(2)
print(ocorrencias)

#sort(key=None, reverse=False)
print("Ordena a lista em ordem crescente. O parâmetro reverse=True ordena em ordem decrescente. O parâmetro key pode ser uma função que serve como critério de ordenação.")

#sort
list_sort = [3, 1, 4, 2]
list_sort.sort()
print(list_sort)

#key
list_key = ["ab", "a", "abc"]
list_key.sort(key=len)
print(list_key) 

#Reverse()
print("Inverte a ordem dos elementos da lista")
list_reverse = [1, 2, 3]
list_reverse.reverse()
print(list_reverse) 

# copy()
print("Retorna uma cópia superficial da lista.")
list_copy = [1, 2, 3]
copia = list_copy.copy()
print(copia)  

# Len listas, tuplas e conjuntos
print("Len  é utilizado para retornar o número de itens em um objeto. Esse objeto pode ser uma lista, tupla, string, dicionário, conjunto ou qualquer outro tipo de dado que suporte o conceito de comprimento.")
linguagens = ["python", "js", "c", "csharp"]
print(linguagens)

# Len strings
texto = "Olá, mundo!"
print(len(texto))  # Saída: 11 (inclui o espaço e pontuação)

# Len dicionário
dicionario = {"nome": "Ana", "idade": 25}
print(len(dicionario))  # Saída: 2

# sorted()
print("""
    O método sorted() em Python é utilizado para retornar uma nova lista contendo os elementos de um iterável ordenados. 
    Ao contrário do método sort() (que é usado diretamente em listas e modifica a lista original), sorted() funciona com qualquer iterável 
    (como listas, tuplas, strings, etc.) e retorna uma nova lista ordenada, sem modificar o iterável original.
    
    Usando o parâmetro key
    O parâmetro key permite que você forneça uma função que será aplicada a cada elemento do iterável para determinar a ordem. Isso é útil quando você deseja ordenar com base em critérios diferentes, 
    como o comprimento de strings ou o valor absoluto de números.
""")

#inteiros
inteiros = [5, 2, 9, 1, 5, 6]
print(sorted(inteiros))

#inteiros
word = "Buzina"
print(sorted(word))  

# Ordenando em ordem reversa
numeros_reverse = [5, 2, 9, 1, 5, 6]
print(sorted(numeros_reverse, reverse=True)) 

print("sorted() com key()")
# Ordenar por comprimento das strings:
ordem_comprimento = ["banana", "maçã", "uva", "abacaxi"]
print(sorted(ordem_comprimento, key=len))

# Ordenar números por valor absoluto
ordem_absoluto = [-4, 1, -2, 3, -5]
print(sorted(ordem_absoluto, key=abs)) 

# Ordenar objetos por atributos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"{self.nome} ({self.idade} anos)"

pessoas = [Pessoa("Ana", 25), Pessoa("Bruno", 20), Pessoa("Clara", 30)]
print(sorted(pessoas, key=lambda p: p.idade)) 

# Ordenar tuplas de acordo com o segundo elemento
ordenar_tuplas = [(1, 'banana'), (2, 'abacaxi'), (3, 'uva')]
print(sorted(ordenar_tuplas, key=lambda x: x[1]))  

# Ordenar com múltiplos critérios
people = [("Ana", 25), ("Bruno", 20), ("Ana", 30)]
print(sorted(people, key=lambda p: (p[0], p[1])))  # Ordena por nome e, em caso de empate, por idade

print("Acessando itens pelo índice")

produtos = ["Leite", "Ovos", "Massa"]
print(produtos)
print(produtos[2])

produto_perecivel = produtos[1]
print(produto_perecivel)

print("Fatiamento: Slicing: acessar uma parte específica de uma lista, string ou outro tipo de sequência. Você pode usar fatiamento para obter uma sublista, uma subsequência de caracteres ou qualquer segmento de uma sequência.")

nome = list("Adriana")

print(nome[2:])
print(nome[:2])
print(nome[1:5])
print(nome[0:5:2])
print(nome[::])
print(nome[::-1])

print(nome[1:3])  # Acessa itens do índice 1 ao 2

# Fatiamento com passo, para obter uma sublista com elementos a cada 2 posições, começando do índice 1 até o final da lista
sublista = nome[1::2]
print(sublista) 

# Fatiamento com índices negativos, pode usar índices negativos para contar a partir do final da lista. Para obter os três últimos elementos
sublista_negativa = nome[-3:]
print(sublista_negativa)  

# Fatiamento Reverso para obter uma lista em ordem reversa
sublista_reversa = lista[::-1]
print(sublista_reversa)  

print("Listas aninhadas:  (ou lista dentro de lista) é uma lista que contém outras listas como elementos. Esse conceito é útil quando você quer organizar dados em múltiplas dimensões, como uma tabela ou matriz.")

lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Acessar o segundo elemento da primeira lista
print(lista_aninhada[0][1]) 

# Modificar o terceiro elemento da segunda lista
lista_aninhada[1][2] = 60
print(lista_aninhada) 

print("Exemplo de matriz")
# Definindo uma matriz (lista aninhada) com três listas internas
matriz = [ 
    [1, "a", 2],  
    ["b", 3, 4],   
    [6, 5, "c"]    
]

# Imprimindo a matriz completa
print(matriz)  

# Acessando a primeira lista (índice 0)
print(matriz[0])

# Acessando o primeiro elemento da primeira lista (índice 0 da lista de índice 0)
print(matriz[0][0]) 

# Acessando o último elemento da primeira lista (índice -1 da lista de índice 0)
print(matriz[0][-1]) 

# Acessando o último elemento da última lista (índice -1 da última lista, índice -1 da matriz)
print(matriz[-1][-1]) 

print("Percorrendo listas com for")

carros = ["gol", "celta", "palio"] 
for carro in carros:
    print(carro)

print("Percorrendo listas com for enumerate")
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

print("""
    Compreensão de Listas:
    Em vez de usar loops e chamadas para funções append ou extend, você pode usar uma única linha de código para gerar uma nova lista.
    É uma técnica muito útil para transformar dados ou gerar listas com base em uma sequência existente.
    
    Acesso direto:
    Como a lista é uma sequência pode ser acessar os seus elementos através de índices. Contamos o índice de determinada sequência a aprtir do zero. 
      
    A sintaxe básica para uma compreensão de lista é: 
        
    nova_lista = [expressã( valor que será adicionado à nova lista)o for item in iterável if condição]

    --> expressão -- O valor que será adicionado à nova lista.
    --> item -- Variável que representa cada elemento do iterável.
    --> iterável -- Qualquer objeto que pode ser iterado, como uma lista, uma string, um range, etc.
    --> condição -- (Opcional) Um teste que filtra os elementos do iterável. Apenas os itens que satisfazem a condição são incluídos na nova lista.
      
    Considerações: 
    Embora as compreensões de listas sejam poderosas e elegantes, é importante usá-las com moderação. Compreensões complexas podem ser difíceis de ler e entender. 
    Se a lógica da compreensão de lista se tornar muito complicada, pode ser melhor usar um loop tradicional para melhorar a clareza do código.
    """)
# Acessar os valores 

# Cria lista de quadrados
quadrados = [x**2 for x in range(10)] 
print(f"Exemplo de lista de quadrados criados \n {quadrados}")

# Filtrar elementos
pares = [x for x  in range(10) if x % 2 == 0]
print(f"Exemplo de Filtrar os elementos \n {pares}")

#  Transformar Strings
cesta_frutas = ["maçã", "banana", "cereja"]
cesta_frutas_maiusculas = [cesta_frutas.upper() for cesta_frutas in cesta_frutas]
print(cesta_frutas_maiusculas)

# Aplicar Transformação e Filtragem Juntas / criar uma lista com o comprimento das strings que têm mais de 3 caracteres
strings = ["a", "abc", "abcd", "abcde"]
comprimentos = [len(s) for s in strings if len(s) > 3]
print(comprimentos)
print("teste")
print( [n**2 if n > 6 else n for n in range(10) if n % 2 == 0])