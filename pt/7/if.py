
a = 1
b = 2
#Operadores comparativos
# ==
# !=
# >
# <
# >=
# <=
# Operadores logicos
# and
# or
# not
#Operador memberchip, nos permitira comparar valores en strings, list y tuples in o not in

if not(a <= b):
	print("Verdad, no es mayor!")
elif(a == b):
	print("Este si es cierto")
else:
	print("Ninguna condicion fue verdadera")

lista = ["Armando", "Gerardo", "Roberto"]
if ("Armaando" in lista):
	print("Cierto, Armando si esta")
elif ("Rober" in lista):
	print("Cierto, Roberto si esta")
elif ("Geraro" in lista):
	print("Cierto, Gerardo si esta")
elif ("Gerardo" not in lista):
	print("Cirto, no esta en la lista")
else:
	print("Ninguna condicion se pudo cumplir")
