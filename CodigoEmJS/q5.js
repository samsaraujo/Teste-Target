function verificarLampadas() {
    let interruptores = ["Interruptor 1", "Interruptor 2", "Interruptor 3"];
    let lampadas = [null, null, null];  // null significa que ainda não sabemos qual é qual

    // Ligamos o interruptor 1 e deixamos ligado por alguns minutos (simulação rápida aqui)
    console.log("Ligando o Interruptor 1 por alguns minutos...");
    setTimeout(() => {
        // Desligamos o interruptor 1 e ligamos o interruptor 2
        console.log("Desligando o Interruptor 1 e ligando o Interruptor 2.");

        // Vamos à sala verificar as lâmpadas
        console.log("Indo à sala das lâmpadas verificar...");

        lampadas[1] = "Lâmpada acesa";  // Interruptor 2 controla a lâmpada que está acesa
        lampadas[0] = "Lâmpada quente";  // Interruptor 1 controla a lâmpada quente
        lampadas[2] = "Lâmpada fria";  // Interruptor 3 controla a lâmpada fria

        // Exibe o resultado
        for (let i = 0; i < 3; i++) {
            console.log(`${interruptores[i]} controla a ${lampadas[i]}.`);
        }
    }, 2000);  // Simula o tempo para esquentar a lâmpada
}

verificarLampadas();



// PARA RODAR O CODIGO NO TERMINAL: node q5.js