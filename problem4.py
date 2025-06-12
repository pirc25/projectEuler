numero1= 999
numero2= 999
valores = []
condicion= True 
while condicion:
  
  mutltiplicado = numero1*numero2
  mutltiplicado_invertido = int(str(mutltiplicado)[::-1])
  if(mutltiplicado == mutltiplicado_invertido):
    valores.append(mutltiplicado)
  if(numero2<100):
    numero1 -=1
    numero2 = 999
  if(numero1<100):
    condicion=False
  numero2 -= 1
valores.sort()
print(valores)