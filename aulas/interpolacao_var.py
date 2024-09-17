print("---" * 30)
print('Interpolação de variáveis')
print("---" * 30)

print("Método %")
# Método antigo % (string formatting):
# Esse método, embora ainda seja suportado, é considerado legada. Ele funciona de maneira parecida com o printf de 
# linguagens como C, onde % é usado como um placeholder.
carro = "UNO"
cor = "Preto"
descricao_carro = "Meu carro é um %s da cor %s." % (carro, cor)  # Corrigido %d para %s, pois 'cor' é uma string
print(descricao_carro)
print("---" * 30)

print("Método .format()")

# Este método permite que você insira variáveis em uma string usando placeholders {}. Ele é muito flexível e pode 
# ser utilizado para interpolar múltiplas variáveis.
nome = "Adriana"
idade = 30
profissao = "Estudante"
apresentacao = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(apresentacao)

# Com o .format(), você pode também especificar a ordem dos valores, ou seja, colocar índices dentro das chaves {}.
mensagem = "Eu sou {0}, tenho {1} anos e sou {2}.".format(nome, idade, profissao)
print(mensagem)
print("---" * 30)

print("F-strings (Python 3.6+)")

# As f-strings são uma maneira mais moderna e eficiente de interpolar variáveis em strings. Para usá-las, basta 
# prefixar a string com f e colocar as variáveis entre chaves {} diretamente dentro da string.
produto = "Tomate"
preco = 1.0
nota_fiscal = f"O preço do {produto} é R${preco:.2f}"  # Adicionada precisão de 2 casas decimais
print(nota_fiscal)

# F-strings também permitem expressões complexas dentro das chaves, como cálculos ou chamadas de funções:
peso = 50.0
altura = 1.65
resultado_imc = f"Meu IMC é igual a {peso / (altura ** 2):.2f}"  # Adicionada precisão de 2 casas decimais
print(resultado_imc)
print("---" * 30)

print("Método concatenação simples +")
# Concatenação simples:
# Você pode usar o operador + para concatenar strings e valores de variáveis (convertendo para str quando necessário).
usuario = "Fulano"
senha = 30
notificacao = "Nome de usuário: " + usuario + " e senha de usuário: " + str(senha) + " Incorreto."  # Corrigido 'pssaword' para 'senha' e adicionado espaço
print(notificacao)
print("---" * 30)

print("Formata;aó de string")

PI = 3.14159
print(f"Valor de PI é igual a {PI:.2f}")
print(f"Valor de PI é igual a {PI:10.2f}") # Adiciona espaços antes do resultado de PI