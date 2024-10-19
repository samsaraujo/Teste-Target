const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function contarA(s) {
    const sLower = s.toLowerCase();
    const contagem = (sLower.match(/a/g) || []).length; // Usando regex para contar 'a'
    return contagem;
}

// Usando readline para entrada do usuário
rl.question("Digite uma string: ", (string) => {
    const contagem = contarA(string);
    console.log(`A letra 'a' ocorre ${contagem} vez(es) na string.`);
    rl.close(); // Fecha a interface após a entrada
});

// PARA RODAR O CODIGO NO TERMINAL: node q2.js