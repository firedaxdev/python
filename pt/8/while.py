#Bucles While

inicio =  0
final = 10

while (inicio < final):
	print(inicio)
	inicio = inicio + 1
while(inicio < final):
	print(inicio)
	inicio = inicio + 1
else:
	print(inicio, "ya no es menor que", final)

start = 0
end = 10
while(start < end):
	print(start)
	if(start == 5): break
	start += 1

index = {1:'Armando', 2:'Roberto', 3:'Rocio', 4:'Priscila'}
contador = 1
while(contador <= 4):
	print(index[contador])
	contador += 1
print("-" * 20)
lista = ['Arturo', 'Gerardo', 'Cecilia', 'Pedro']
contador = 0
while(contador < len(lista)):
	print(lista[contador])
	contador += 1
