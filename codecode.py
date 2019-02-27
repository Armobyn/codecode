#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
 -------------------------------------------------------------------------
| Autor: Eder Hernández Guzmán                                            |
| Alias: Amonion                                                          |
| Objetivo: Encriptar un texto                                            |
| Funcion: escribimos un texto el programa lo encripta, de igual manera   |
| lo desencripta en caso de haber sido encriptado                         |
 -------------------------------------------------------------------------
"""
import os#para importar eventos del sistema

#definiendo un diccionario
abecedario = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'ñ':15,'o':16,'p':17,'q':18,'r':19,'s':20,'t':21,'u':22,'v':23,'w':24,'x':25,'y':26,'z':27,' ':28}

#definiendo una lista
abc=[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',' ']

ciclo = 1
while ciclo == 1:

	os.system('clear')#manadando la instruccion de clear de mi sistema
	#pedimos al usuario ingresar una cadena
	x = str(input("ingresa una cadena , por favor:"))

	#a modo de prueba mostramos la cadena ingresada
	#print("la cadena ingresada es: ",x)

	#definims a el tamaño de la cadena com o "tam"
	tam = len(x)
	#imprimimos la longitud de la cadena
	#print("el tamaño de la cadena es: ",tam,"\n\n")

	#codificando
	#comenzamos el bucle que terminara cuando "range" sea igual al tamaño "tam" de la cadena"x"
	for i in range(tam):
		#la siguiente linea toma el valor del indice de la cadena "x",
		#con esto vuelve a tomar el siguinete valor que es el del diccionario "abecedario"
		#y se lo asignamos a la variable "valor"

		valor = int(abecedario[(x[i])])

		#hacemos una condicion : si el valor dentro del diccionario es menor o igual que 14
		if valor<=14:
			result = valor + (14)
			#la letra_final se toma de la lista "abc" con respecto al valor de "result"
			letra_final = abc[result]

		elif valor>14:
			result = valor - (14)
			letra_final = abc[result]

		print(letra_final, end="")
	ciclo = int(input("\n\ndesea salir del programa?\nSi(2)\nNo(1)\n"))
