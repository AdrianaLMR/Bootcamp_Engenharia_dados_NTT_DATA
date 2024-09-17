#Conversão de tipos

# Inteiro para float
print("Conversão de Inteiro para float")    
preco = 10
print(preco) 

preco = float(preco)    
print(preco)        

preco = 10 / 2
print(preco)    

# Float para inteiro
print("Conversão de Float para inteiro")    
kilo = 10.5 
print(kilo) 

kilo = int(kilo)    
print(kilo)          

# Conversão por divisão
print("Conversão por divisão")    
unidade = 10
print(unidade) 

unidade = (unidade / 2)    
print(unidade)        

print(unidade // 2) # Retorna um inteiro

# Conversão númerico para string
print("Conversão númerico para string")    
valor_produto = 10
print(valor_produto) 

print(str(valor_produto))

text_concatenado = f"O valor do produto é: {valor_produto}"
print(text_concatenado)

# Conversão de string para número
print("Conversão de string para número")
numero_float = "20.0"
numero_int = "18"
print(int(numero_int))
print(float(numero_float))
