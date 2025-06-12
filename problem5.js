let mayorValor = 20;
let valorEncontrado = true;
let multiplos = [20, 19, 18, 17, 16, 14, 13, 12, 11];
let i = 1; // Inicia desde 1, no 21
let pivot;

while (valorEncontrado) {
  pivot = mayorValor * i; // Calcula el posible número
  let esDivisible = true;

  for (let multiplo of multiplos) {
    if (pivot % multiplo !== 0) {
      esDivisible = false;
      break; // Sale del bucle si no es divisible
    }
  }

  if (esDivisible) {
    console.log("Este es el número:", pivot);
    valorEncontrado = false; // Detiene el ciclo
  }

  i += 1; // Incrementa i
}