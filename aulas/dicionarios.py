print("Dicionários: São uma coleção de pares chaves{}: valor, onde cada chave é única. Chaves devem ser imutáveis (strings, números, tuplas), enquanto valores podem ser de qualquer tipo.")

aluno = {"nome": "João", "idade": 25, "curso": "Engenharia"}
print(aluno)

print("Operações com dicionários")

# Acessando valores
print(aluno["nome"])  # "João"

# Adicinando ou modificando
aluno["idade"] = 26  # Modifica o valor
aluno["nota"] = 8.5  # Adiciona nova chave-valor

#removendo pares chave-valor:  pop() (remove por chave), clear() (remove todos)
aluno.pop("curso")  # Remove a chave "curso"
aluno.clear()  # Limpa o dicionário
