print(""" 
    Conjuntos(sets):  é uma coleção não ordenada e não indexada de itens únicos. Não permite duplicatas, são definidos usando chaves {}. 
    São úteis quando você precisa garantir que todos os elementos sejam únicos.
""")

numeros = {1, 2, 3, 4, 5}
print(numeros)

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

print("Operações de conjunto União (union() ou |), Interseção (intersection() ou &), Diferença (difference() ou -).")

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# União (union() ou |)
print(set1 | set2)

#  Interseção (intersection() ou &)
print(set1 & set2)

# Diferença (difference() ou -)

# Diferença: elementos presentes em set1, mas não em set2
print(set1 - set2) 

# Diferença: elementos presentes em set2, mas não em set1
print(set2 - set1)  