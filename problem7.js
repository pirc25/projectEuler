let valorEncontrado = true;
let contadorPrimos = 1; // 2 es el primer primo
let primoActual = 2;
let i = 3; // Comenzamos desde el primer número impar después de 2

while (valorEncontrado) {
  let esPrimo = true;

  // Verificar si el número es primo
  for (let j = 2; j <= Math.sqrt(i); j++) { //// USAR LA Raíz cuadrada.
    if (i % j === 0) {
      esPrimo = false;
      break;
    }
  }

  if (esPrimo) {
    contadorPrimos++;
    primoActual = i;

    if (contadorPrimos === 10001) {
      console.log("Este es el número:", primoActual);
      valorEncontrado = false;
    }
  }

  i += 2; // Solo verificamos números impares
}