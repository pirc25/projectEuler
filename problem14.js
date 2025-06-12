let numeroActual = 0;
let boleano = true;
for (i = 1; boleano; i++) {
    let multiplos = 2
    numeroActual = numeroActual + i
    for (j=1;j<=Math.sqrt(numeroActual);j++) {
        if(numeroActual%j===0){
            multiplos++
        }
        if(multiplos.length === 500) {
            boleano = false
        }
    }
}
console.log(numeroActual)
