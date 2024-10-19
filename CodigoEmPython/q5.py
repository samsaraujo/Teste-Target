import time

def verificar_lampadas():
    interruptores = ["Interruptor 1", "Interruptor 2", "Interruptor 3"]
    lampadas = [None, None, None]  # None significa que ainda não sabemos qual é qual

    # Ligamos o interruptor 1 e deixamos ligado por alguns minutos (simulação rápida aqui)
    print("Ligando o Interruptor 1 por alguns minutos...")
    time.sleep(2)  # Simula o tempo que a lâmpada fica ligada e esquenta
    
    # Desligamos o interruptor 1 e ligamos o interruptor 2
    print("Desligando o Interruptor 1 e ligando o Interruptor 2.")
    
    # Vamos à sala verificar as lâmpadas
    print("Indo à sala das lâmpadas verificar...")

    lampadas[1] = "Lâmpada acesa"  # Interruptor 2 controla a lâmpada que está acesa
    lampadas[0] = "Lâmpada quente"  # Interruptor 1 controla a lâmpada quente
    lampadas[2] = "Lâmpada fria"  # Interruptor 3 controla a lâmpada fria

    # Exibe o resultado
    for i in range(3):
        print(f"{interruptores[i]} controla a {lampadas[i]}.")

verificar_lampadas()


#PARA RODAR O CODIGO NO TERMINAL: py q4.py