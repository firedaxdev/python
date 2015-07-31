#Excepciones o errores en tiempo de ejecucion
var = False
while (var == False):
	try:
		var = int(input("Escribe un numero entero diferente a 0: "))
		print(var)
	except ValueError as e:
		print("El valor que introduciste no es entero")
