print("""
    Tuplas: é similar a uma lista, mas é imutável, o que significa que não pode ser alterada após sua criação e são definidas usando parênteses. 
    Podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgulas de parenteses.
      
    Conclusão:
   --> Use a vírgula para criar tuplas com um único elemento para evitar problemas de interpretação.
   --> Em tuplas com múltiplos elementos, não é necessário colocar a vírgula no final, a menos que haja uma razão específica.
   --> Use tuplas para garantir imutabilidade, e listas para dados que serão alterados com frequência.
   --> Menor uso de memória: Tuplas tendem a usar menos memória que listas, sendo mais eficientes quando você só precisa armazenar dados sem modificá-los.
   --> Usadas como chaves em dicionários: Como as tuplas são imutáveis, podem ser usadas como chaves em dicionários, algo que não é possível com listas.
""")

# usando palavra reservada
palavra_reservada = tuple("TUPLAS")
print(palavra_reservada) 

# usando parenteses
minha_tupla = (1, 2, 3,)
print(minha_tupla)

# criar uma tupla a partir de uma lista
num = tuple([1, 2, 3, 4, 5])
print(num)

# sem parenteses
tupla_sem_parent = 3, 4, 5, 6
print(tupla_sem_parent)

#tupla vazia
tupla_vazia = ()
print(tupla_vazia)

# Com um único elemento (é necessário uma vírgula)
tupla_com_um_elemento = (42,)
print(tupla_com_um_elemento)

print("Acessando elemento usando índice")

cores = ("vermelho", "verde", "azul",)
print(cores[0])  

# index negativos
print(cores[-2])
print(cores[-1])

print("Tuplas aninhadas: Tuplas que armazenam outras tuplas, com pode ser criado etruturas bidmensionais(tabelas), e acessar informando os índices de linha de coluna.") 

tupla_aninhada = ((1, 2), (3, 4), (5, 6))
print(tupla_aninhada[0])  
print(tupla_aninhada[0][1])  

print("Exemplo de matriz")
# Definindo uma matriz (Tuplas aninhada) com três Tuplas internas
matriz = (
    (1, "a", 2),  
    ("b", 3, 4),   
    (6, 5, "c")    
)

# Imprimindo a matriz completa
print(matriz)  

# Acessando a primeira Tuplas (índice 0)
print(matriz[0])

# Acessando o primeiro elemento da primeira Tuplas (índice 0 da Tuplas de índice 0)
print(matriz[0][0]) 

# Acessando o último elemento da primeira Tuplas (índice -1 da Tuplas de índice 0)
print(matriz[0][-1]) 

# Acessando o último elemento da última Tuplas (índice -1 da última Tuplas, índice -1 da matriz)
print(matriz[-1][-1])

print("Fatiamento")
python = ("PYTHON",)

print(python[1:])  
print(python[:3]) 
print(python[1:3]) 
print(python[0:3:2]) 
print(python[::]) 
print(python[::-3]) 


print("Desempacotamento de Tuplas: O desempacotamento permite atribuir os valores de uma tupla a variáveis individuais de maneira simples.") 

tupla = (1, 2, 3)
a, b, c = tupla  # Atribui 1 a 'a', 2 a 'b', e 3 a 'c'
print(a, b, c)  # Saída: 1 2 3

print("Métodos associados")

# count(): Retorna o número de vezes que um valor aparece na tupla.
tupla_count = (1, 2, 3, 2, 2)
print(tupla_count.count(2))  

# index(): Retorna o índice da primeira ocorrência de um valor.
tupla_index = (10, 20, 30)
print(tupla_index.index(20))  

# Len: Determinar quantos itens estão armazenados em uma tupla, já que ela pode conter diferentes tipos de dados e não pode ser modificada.
tupla_len = (9, 0, 33, 8,)
print(tupla_len)
print(len(tupla_len))

print("Conversão entre listas e tuplas, usando as funções list() e tuple().")

# Converter uma tupla para lista
tupla_convertida = (1, 2, 3)
lista = list(tupla_convertida)
print(lista) 

# Converter uma lista para tupla
lista_convertida = [1, 2, 3]
tupla = tuple(lista_convertida)
print(tupla)  

print("Aplicação prática: Retornos múltiplos de funções: Funções podem retornar várias informações usando tuplas.")
# Aplicação 1
def coordenadas():
    return 10, 20

x, y = coordenadas()  # Desempacota a tupla retornada
print(x, y)  # Saída: 10 20

# Aplicação 2
print("Agrupamento de dados heterogêneos: Tuplas são úteis para representar coleções de dados diferentes que pertencem ao mesmo registro, como um ponto em um gráfico 3D ((x, y, z)).")
