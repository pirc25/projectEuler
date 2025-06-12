numero_total = 600851475143
lista = []
def factores_primos(numero_total, lista):
    # Comenzamos desde 2 (primer número primo)
    divisor = 2
    
    while numero_total > 1:
        if numero_total % divisor == 0:
            # Si el divisor divide exactamente, lo agregamos a la lista
            lista.append(divisor)
            # Dividimos el número total por el divisor
            numero_total //= divisor
        else:
            # Incrementamos el divisor para buscar el siguiente primo
            divisor += 1
factores_primos(numero_total, lista)
print("Factores primos:", lista)