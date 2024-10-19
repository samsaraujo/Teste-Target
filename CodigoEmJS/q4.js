function proximoElemento() {
    // Sequência a)
    let a = [1, 3, 5, 7];
    a.push(a[a.length - 1] + 2);
    
    // Sequência b)
    let b = [2, 4, 8, 16, 32, 64];
    b.push(b[b.length - 1] * 2);
    
    // Sequência c)
    let c = [0, 1, 4, 9, 16, 25, 36];
    c.push(c.length * c.length);  // Próximo número é o quadrado do próximo inteiro
    
    // Sequência d)
    let d = [4, 16, 36, 64];
    d.push((d.length + 2) * (d.length + 2));  // Quadrados de números pares
    
    // Sequência e)
    let e = [1, 1, 2, 3, 5, 8];
    e.push(e[e.length - 1] + e[e.length - 2]);  // Sequência de Fibonacci
    
    // Sequência f)
    let f = [2, 10, 12, 16, 17, 18, 19];
    f.push(20);  // Segue números sem os múltiplos de 3, exceto 12
    
    // Resultados
    console.log("Próximo elemento de a:", a[a.length - 1]);
    console.log("Próximo elemento de b:", b[b.length - 1]);
    console.log("Próximo elemento de c:", c[c.length - 1]);
    console.log("Próximo elemento de d:", d[d.length - 1]);
    console.log("Próximo elemento de e:", e[e.length - 1]);
    console.log("Próximo elemento de f:", f[f.length - 1]);
}

proximoElemento();


// PARA RODAR O CODIGO NO TERMINAL: node q4.js