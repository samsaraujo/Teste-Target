def proximo_elemento():
    # Sequência a)
    a = [1, 3, 5, 7]
    a.append(a[-1] + 2)
    
    # Sequência b)
    b = [2, 4, 8, 16, 32, 64]
    b.append(b[-1] * 2)
    
    # Sequência c)
    c = [0, 1, 4, 9, 16, 25, 36]
    c.append((len(c))**2)  # Próximo número é o quadrado do próximo inteiro
    
    # Sequência d)
    d = [4, 16, 36, 64]
    d.append((len(d) + 2) ** 2)  # Próximos quadrados de números pares
    
    # Sequência e)
    e = [1, 1, 2, 3, 5, 8]
    e.append(e[-1] + e[-2])  # Sequência de Fibonacci
    
    # Sequência f)
    f = [2, 10, 12, 16, 17, 18, 19]
    f.append(20)  # Segue números sem os múltiplos de 3, exceto 12
    
    # Resultados
    print("Próximo elemento de a:", a[-1])
    print("Próximo elemento de b:", b[-1])
    print("Próximo elemento de c:", c[-1])
    print("Próximo elemento de d:", d[-1])
    print("Próximo elemento de e:", e[-1])
    print("Próximo elemento de f:", f[-1])

proximo_elemento()


#PARA RODAR O CODIGO NO TERMINAL: py q4.py