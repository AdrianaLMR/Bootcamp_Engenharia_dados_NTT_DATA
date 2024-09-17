print(
    """
    Funções são blocos de código reutilizáveis que realizam uma tarefa específica. 
    Elas permitem que você organize seu código, evite repetições e facilite a manutenção.
    Uma função é definida usando a palavra-chave def, seguida pelo nome da função, parênteses, 
    e um bloco de código indentado. Se necessário, você pode passar argumentos (informações) para a função.
      
    Retornando valores
    Para retornar valores é utlizado a palavra reservada RETURN, toda função retorna um NONE por padrão, diferente de outras linguagens 
    o python pode retornar mais de um valor.
    """)

print("Exemplos de func e python")
#Exemplo de func

def saudacao():
    print("Hello world!")
saudacao()

# Exemplos de func com paramêtros

def comprimento(nome):
    print("Olá, {}!".format(nome))

comprimento("Ana")

# Exemplos de func com paramêtros com atributos, sem atributos é considerado anônimo
def mensagem(nome= "Fulano"):
    print(f"Seja bem vindo {nome}")

mensagem()

# Exemplo de func com retorno

def soma(a, b):
    return a + b

resultado = soma(3, 5)
print(resultado)

# Exemplo de func com mais de um retorno

def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

# Chamada da função
antecessor, sucessor = retorna_antecessor_sucessor(10)
print("Antecessor:", antecessor)
print("Sucessor:", sucessor)

def salvar_carro(marca, modelo, ano, placa):
    #Salva carro banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# Chamada normal da função, passando os argumentos na ordem correta
# Recebe quatro parâmetros: marca, modelo, ano e placa
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# Chamada da função usando argumentos nomeados (permite mudar a ordem dos parâmetros)
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# Chamada da função usando um dicionário e o operador ** para desempacotar os valores como argumentos
salvar_carro(**{"marca": "Fiat", "modelo":"Palio", "ano":1999, "placa":"ABC-1234"})

print("Args e Kwargs")
print(
    """
    são usados em funções para permitir que elas aceitem um número variável de argumentos, oferecendo 
    mais flexibilidade na forma como os parâmetros são passados.
      
    *args permite que você passe uma quantidade indefinida de argumentos posicionais para uma função. 
    Quando você usa *args, os argumentos são agrupados em uma tupla dentro da função.

    **kwargs (Argumentos Nomeados Variáveis)
    **kwargs permite que você passe uma quantidade indefinida de argumentos nomeados (ou seja, pares
    chave-valor) para uma função. Esses argumentos são agrupados em um dicionário dentro da função.
      
    Pode combinar *args e **kwargs na mesma função. Isso permite que a função aceite tanto argumentos 
    posicionais quanto nomeados.
    """)

def exemplo_args(*args):
    # Exibe os argumentos posicionais (*args)
    print("Argumentos *args:")
    for valor in args:
        print(valor)

def exemplo_kwargs(**kwargs):
    # Exibe os argumentos nomeados (**kwargs)
    print("Argumentos **kwargs:")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

def exemplo_args_kwargs(*args, **kwargs):
    # Exibe os argumentos posicionais e nomeados juntos
    print("Argumentos *args e **kwargs juntos:")
    
    print("Argumentos *args:")
    for valor in args:
        print(valor)
    
    print("Argumentos **kwargs:")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Exemplo de uso de *args
exemplo_args(1, 2, 3)

# Exemplo de uso de **kwargs
exemplo_kwargs(nome="Ana", idade=25)

# Exemplo de uso de *args e **kwargs juntos
exemplo_args_kwargs(10, 20, nome="Carlos", profissao="Professor")


#Exemplo aula exibir poema
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]) 
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Sexta-feira, 26 de Agosto de 2022",
    "The Road Not Taken by Robert Frost",
    "Two roads diverged in a yellow wood,",
    "And sorry I could not travel both",
    "And be one traveler, long I stood",
    "And looked down one as far as I could",
    "To where it bent in the undergrowth;",
    "",
    "Then took the other, as just as fair,",
    "And having perhaps the better claim,",
    "Because it was grassy and wanted wear;",
    "Though as for that the passing there",
    "Had worn them really about the same,",
    "",
    "And both that morning equally lay",
    "In leaves no step had trodden black.",
    "Oh, I kept the first for another day!",
    "Yet knowing how way leads on to way,",
    "I doubted if I should ever come back.",
    "",
    "I shall be telling this with a sigh",
    "Somewhere ages and ages hence:",
    "Two roads diverged in a wood, and I—",
    "I took the one less traveled by,",
    "And that has made all the difference.",
    autor="Robert Frost",
    ano=1916
)

print(
    """
    Funções com paramêtros especiais
    Os parâmetros especiais em Python são técnicas que permitem que funções aceitem uma quantidade variável de argumentos ou argumentos nomeados. 
    Eles ajudam a tornar as funções mais flexíveis e adaptáveis. 
    1 - Parâmetros padrão têm valores predefinidos.
    2 - *args aceita uma quantidade variável de argumentos posicionais, armazenando-os em uma tupla.
    3 - **kwargs aceita uma quantidade variável de argumentos nomeados, armazenando-os em um dicionário.
    """)

# Exemplo com Argumentos Apenas Posicionais e Nomeados (keyword and position only)
def saudar(nome, idade, / , cidade, estado, *, pais, telefone):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")
    print(f"estado: {pais}")
    print(f"Pais: {telefone}")

# Passando oargumentos por posição e nome onde permitido
# Argumentos posicionais (nome e idade) são passados por posição, e não podem ser passados por nome.
# Argumentos que podem ser passados por posição ou nome (cidade e estado), pois estão entre / e *.
# Argumentos nomeados (pais e telefone) devem ser passados apenas por nome, pois estão após *.
saudar("Beltrano", 30, "Florianópolis", "SC", pais="Brasil", telefone="123456789" )

#Exemplo de Argumentos Keyword-Onl
print("Para definir argumentos keyword-only, você usa o símbolo * na assinatura da função. Todos os parâmetros que vêm após o * devem ser passados por nome.")
def mensagem_personalizada(nome, *, mensagem="Bem-vindo"):
    print(f"{mensagem}, {nome}!")

# Correto - passando argumento keyword-only
mensagem_personalizada("Ana", mensagem="Olá")

# Correto - usando o valor padrão para 'mensagem'
mensagem_personalizada("Carlos")



#Exemplo de Argumentos Apenas Posicionais
print(
    """"
    Para definir argumentos apenas posicionais em Python, você usa o símbolo / na assinatura da função. 
    Todos os parâmetros à esquerda do / devem ser passados apenas por posição e não podem ser passados por nome.
    """)
def calcular_area(base, altura, /):
    area = base * altura
    print(f"Área: {area}")

# Correto - passando argumentos apenas por posição
calcular_area(10, 5)

# Incorreto - passando argumentos nomeados (vai gerar um erro)
# calcular_area(base=10, altura=5)

print("Escopo Global e local")
print(
    """
    Escopo Global: refere-se ao espaço onde variáveis e funções são acessíveis em todo o programa, fora de funções e classes. Variáveis definidas no escopo global podem 
    ser acessadas de qualquer lugar no código, desde que não sejam sobrescritas por variáveis locais com o mesmo nome.
    """)

variavel_global = "Eu sou global"

def exibir_variavel():
    print(variavel_global)  # Acessando a variável global

exibir_variavel()
print(variavel_global)  # Acessando a variável global fora da função


print(
    """
    Escopo Local: refere-se ao espaço dentro de uma função ou bloco de código onde variáveis e parâmetros são definidos e acessíveis. 
    Essas variáveis são conhecidas apenas dentro da função ou bloco onde são definidas.
    """)

def exemplo_funcao():
    variavel_local = "Eu sou local"
    print(variavel_local)  # Acessando a variável local dentro da função

exemplo_funcao()

# Tentando acessar a variável local fora da função gera um erro
# print(variavel_local)  # Isso vai gerar um erro, pois 'variavel_local' não é acessível fora da função

print(
    """
    Interação Entre Escopos
    Somente Leitura: Dentro de uma função, você pode ler variáveis globais, mas não pode modificá-las diretamente a menos que declare 
    explicitamente que está modificando uma variável global usando a palavra-chave global.
    Modificação de Variáveis Globais exemplo abaixo. 
    """)

variavel_global = "Antes da alteração"

def alterar_global():
    global variavel_global
    variavel_global = "Depois da alteração"

alterar_global()
print(variavel_global)  # Agora mostra "Depois da alteração"
