# Função para calcular a sequência de Fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]  # Inicia a sequência com 0 e 1
    while True:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        if next_value > n:  # Para quando o próximo valor exceder n
            break
        fib_sequence.append(next_value)
    return fib_sequence

# Solicita ao usuário um número
try:
    number = int(input("Informe um número: "))  # Converte a entrada para inteiro
except ValueError:
    print("Por favor, insira um número válido.")
    exit()

# Calcula a sequência de Fibonacci até o número informado
fib_sequence = fibonacci(number)

# Verifica se o número está na sequência
if number in fib_sequence:
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")

# Imprime a sequência de Fibonacci calculada
print("Sequência de Fibonacci:", fib_sequence)


#PARA RODAR O CODIGO NO TERMINAL: py q1.py