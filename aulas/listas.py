print("Listas: Uma lista é uma coleção ordenada e mutável de itens. Cada item pode ser de qualquer tipo de dado (inteiros, strings, outras listas, etc.). O índice sempre começa no zero(0)")

#Exemplo de listas

frutas = ["Laranja", "Melão", "Uva", "Morango", "Mmeixa",]
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari",  "F8", 4200000, 2020, 2090, "São Paulo", True]
print(f"Carro: {carro}")

print("Adicionando elementos a lista")

lista = []
print(lista)

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

# Remmovepor índice pop()
num.pop(1)
print(num) 

# Remmove todos elementos clear()
num.clear()
print(num)

print("Acessando itens pelo índice")

produtos = ["Leite", "Ovos", "Massa"]
print(produtos)
print(produtos[2])

produto_perecivel = produtos[1]
print(produto_perecivel)

print("Fatiamento: Slicing: acessar uma parte específica de uma lista, string ou outro tipo de sequência. Você pode usar fatiamento para obter uma sublista, uma subsequência de caracteres ou qualquer segmento de uma sequência.")

nome = list("Adriana")
print(nome[1:3])  # Acessa itens do índice 1 ao 2

# Fatiamento com passo, para obter uma sublista com elementos a cada 2 posições, começando do índice 1 até o final da lista
sublista = nome[1::2]
print(sublista)  # Saída: [20, 40, 60, 80, 100]

# fatiamento com índices negativos, pode usar índices negativos para contar a partir do final da lista. Para obter os três últimos elementos
sublista_negativa = nome[-3:]
print(sublista_negativa)  # Saída: [80, 90, 100]

# Fatiamento Reverso para obter uma lista em ordem reversa
sublista_reversa = lista[::-1]
print(sublista_reversa)  # Saída: [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

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
