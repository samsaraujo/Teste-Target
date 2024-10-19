def contar_a(s):
    # Convertendo a string para minúscula para verificar 'a' e 'A'
    s_lower = s.lower()
    contagem = s_lower.count('a')
    return contagem

# Você pode definir a string aqui ou usar a entrada do usuário
string = input("Digite uma string: ")  # ou defina: string = "Exemplo de String com A"
contagem = contar_a(string)

print(f"A letra 'a' ocorre {contagem} vez(es) na string.")


#PARA RODAR O CODIGO NO TERMINAL: py q2.py