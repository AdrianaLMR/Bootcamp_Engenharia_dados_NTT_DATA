print("Estrutras condicionais")

# As estruturas de controle permitem que você direcione o fluxo do seu programa com base em condições ou repetições. 

print("Condicionais (if, elif, else)")

idade = 18
if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você acabou de se tornar adulto.")
else:
    print("Você é adulto.")  

print("Laços de Repetição (for, while)")
for i in range(5):
    print(i)  # Imprime de 0 a 4

print("if aninhados")
def verificar_saldo(saldo: float, valor: float) -> str:
    # Verifica se o saldo é suficiente para realizar a transação
    if saldo >= valor:
        return "Saldo suficiente para realizar a transação."
    else:
        return "Saldo insuficiente."

# Exemplo de uso
saldo_atual = 150.0
valor_da_transacao = 100.0
mensagem = verificar_saldo(saldo_atual, valor_da_transacao)
print(mensagem)


print("while: Repete enquanto a condição for verdadeira.")
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incrementa o contador

print("Controle de Fluxo (break, continue, pass")
print("Break")
for i in range(10):
    if i == 5:
        break
    print(i)  # Imprime 0 a 4

print("Continue")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Imprime apenas números ímpares


print("pass")
for i in range(5):
    if i == 2:
        pass  # Placeholder para lógica futura
    else:
        print(i)


#Essas estruturas permitem que você crie programas mais complexos e ajustem o fluxo de execução conforme necessário. A correta identação e uso 
# dessas estruturas são fundamentais para a escrita de código Python claro e funcional.