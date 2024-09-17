print("Strings Multiplas linhas")

# Strings_Multiplas_linhas = """
# Strings múltiplas linhas são representadas usando aspas triplas, que podem ser simples (''') ou duplas ("""). 
# Essas strings permitem que você inclua quebras de linha e formate o texto de maneira mais flexível do que com 
# strings de uma linha. 

# São úteis para textos longos ou docstrings (strings de documentação), pois permitem que você escreva o texto 
# de forma mais legível e mantenha a formatação original.
# """


print("Aspas tiplas simples(''')")
texto_aspas_simples = '''Este é um exemplo de
uma string com múltiplas linhas
usando aspas triplas simples.'''
print("--" * 10)

print('Aspas tiplas duplas(""")')
texto_aspas_duplas = """ Este é um exemplo de
uma string com múltiplas linhas
usando aspas triplas duplas. """

print("--" * 10)

# As aspas triplas permitem que o texto ocupe várias linhas e quebras de linha sejam preservadas no texto final.

mensagem = """Esta é uma mensagem
que ocupa várias linhas.
Cada nova linha é preservada."""
print(mensagem)

print("Docstring")
#  Quando usadas logo após uma definição de função, classe ou módulo, as aspas triplas são usadas para criar 
# docstrings, que servem como documentação.
def minha_funcao():
    """
    Esta é uma docstring. Ela descreve a função e
    pode ocupar várias linhas.
    """
    pass
