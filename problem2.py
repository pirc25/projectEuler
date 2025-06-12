# ENCONTRAR LA SUMA DE LOS NUNMEROS PAR DE FIBONACHI HASTA EL NÜMERO QUE SEA MENOR A 40000000

# Inicializamos el arreglo con los primeros números de Fibonacci
arreglo = [1, 2]
suma = 2  # Inicializamos la suma con el primer número par de Fibonacci
def fibonacci(arreglo, suma):
    while True:
        # Calculamos el siguiente número de Fibonacci
        numero = arreglo[-1] + arreglo[-2]  # Sumamos los dos últimos números de la lista
        
        # Si el número supera 4,000,000, terminamos
        if numero > 4000000:
            break
        
        # Agregamos el nuevo número al arreglo
        arreglo.append(numero)
        
        # Si el número es par, lo añadimos a la suma
        if numero % 2 == 0:
            suma += numero
    return suma
# Llamamos a la función y calculamos la suma
suma_total = fibonacci(arreglo, suma)
# Mostramos el resultado
print("La suma de los números pares de Fibonacci menores a 4,000,000 es:", suma_total)