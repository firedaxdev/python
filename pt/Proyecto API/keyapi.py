#Programa para realizar tokens basico
import random
import textwrap
#cada key consta de 10 caracteres
keys = [
"ASggA",
"Sqgas",
"gasgA",
"gkkQ1",
"jhGlo",
"4Ert0",
"jhytV",
"GmG09",
"ga3ga",
"1Agg4",
"poL02",
"AdgA1",
"agXaa",
"Q1gas",
"qwGa1",
"aGa11",
"QwtTT",
"12AXz",
"jjkAs",
"qqSX1"
]
#los datos que introduzca el usuario al menos deben de ser de 2 caracteres xD
nombres = input("Como te llamas? ") #a
apellidos = input("Cuales son tus apellidos? ") #b
edad =  input("Cual es tu edad? ") #c
ciudad = input("Cual es tu ciudad? ") #d
estado = input("En que estado naciste? ") #e
dia_n = input("Dia en que naciste? ") #f
mes_n = input("Mes en que naciste? ") #g
anio_n = input("Año en que naciste? ") #h
#cortando los datos a 2 caracteres de cada dato que introduzca
s_edad, s_dia_n, s_mes_n, s_anio_n  = str(edad), str(dia_n), str(mes_n), str(anio_n)
a,b,c,d,e,f,g,h = nombres[0:2], apellidos[0:2], s_edad[0:2], ciudad[0:2], estado[0:2], s_dia_n[0:2], s_mes_n[0:2], s_anio_n[0:2]
#generando aleatoriamente los keys
p1 = random.choice(keys)
p2 = random.choice(keys)
p3 = random.choice(keys)
p4 = random.choice(keys)
p5 = random.choice(keys)
p6 = random.choice(keys)
p7 = random.choice(keys)
#Formulando token
token = a + p1 + b + p2 + c + p3 + d + p4 + e + p5 + f + p6 + g + p7 +h
print("Tu token es:", token)
