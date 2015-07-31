#Bucles for

for x in range(0, 9):
	print(x)

tupla = ("Armando", "Ruelas", "Leyva")
lista = ['Armando', 'Humberto','Ruelas', 'Leyva']
for x in tupla:
	print(x)
print("-" * 30)
for x in lista:
	print(x)
else: print("Ha termiando de indexarse los elementos")

elementos =  {1:'A', 2:'B', 3:'C', 4:'D'}
for clave, valor in elementos.items():
	print(clave,valor)
