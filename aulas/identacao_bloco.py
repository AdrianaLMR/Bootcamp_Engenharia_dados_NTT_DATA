print("Identação de código")
# É uma forma de manter o código fonte légivel e manutenível, em python a identaçao exerce um segundo papel que seria 
#  definir a estrutura e o agrupamento de blocos de código. Em vez de usar chaves {} para definir blocos, Python usa
#  a identação para agrupar código que deve ser executado junto.

# Identação se refere ao uso de espaços ou tabulações no início de uma linha de código para indicar que ela faz 
# parte de um bloco maior, definindo a hierarquia e o escopo do código. 

# Se a identação estiver incorreta, o Python levantará um erro de IndentationError, indicando que a identação não 
# está consistente ou é inválida.

# Bloco de código são agrupados por identação. Um bloco de código é uma seção de código que pertence a uma estrutura 
# de controle, como funções, loops, ou condicionais.


# Regras para Identação:

# Consistência: É importante ser consistente com o número de espaços ou tabulações. O padrão comum é usar 4 espaços 
# por nível de identação.

# Níveis de Identação: Cada nível de identação indica um novo bloco de código. Por exemplo, o corpo de uma função é 
# um bloco de código indentado.

print("Exemplo de bloco com identação")
def saudacao(nome):
    if nome:  # Começo do bloco do 'if'
        print(f"Olá, {nome}!")  # Este é o corpo do 'if'
    else:  # Começo do bloco 'else'
        print("Olá, Mundo!")  # Este é o corpo do 'else'

saudacao("Ana")

print("Exemplo de bloco aninhado")

for i in range(3):  # Bloco de código do 'for'
    print(f"Loop {i}")  # Corpo do 'for'
    if i % 2 == 0:  # Bloco de código do 'if'
        print(f"{i} é par")  # Corpo do 'if'
    else:
        print(f"{i} é ímpar")  # Corpo do 'else'

# Utilizando espaços
#em python existe uma convenção que define as boas práticas para escrita de cógido na linguagem.
#nesse documento é recomendado utilizar 4 espaços em branco por nível de identação, ou seja, a cada novo bloco adiciona 4 novos espaços em branco.


print("Exemplo de bloco com espaços")
def sacar(self, valor: float) -> None: #Inicio bloco do método

    if self.saldo >= valor:
        self.saldo = valor  
    # Fim bloco do if

def sacar_dinheiro(valor):
    quantia = 300

    if quantia >= valor:
        print("Quantia de dinheiro sacado!")
        print("Retire seu dinheiro na boca do caixa")
    
print("Obrigada por ser nosso cliente")

sacar_dinheiro(300)
sacar_dinheiro(1000)

def depositar(valor):
    saldo = 500
    saldo += valor

sacar_dinheiro(1000)