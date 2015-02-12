import math
#regresa los impares compuestos formados como la suma de un primo y el dobre de un cuadrado
def suma(imparcompuesto,primos):
	s = []
	for e2 in range(len(primos)):
			p =primos[e2]
			for e3 in range(1,imparcompuesto[-1]):
				r=p+2*(e3**2)
				s.append(r)
	return s
#regresa todo los impares compuestos ordenados obtenidos del metodo suma
def conjuntoSol(imparcompuesto,suma):
	lista=[]
	cjto = set()
	for e in range(len(imparcompuesto)):
		for e2 in range(len(suma)):
			if (imparcompuesto[e]==suma[e2]):
				cjto.add(suma[e2])
	lista= list(cjto)

	return sorted(lista)
#comprueba que cada impar compuesto dado esté en el conjunto de imapares compuestos dados por la suma.
def goldbach(iparcompuesto,sol):
	m = []
	print(imparcompuesto)
	print(sol)
	for x in imparcompuesto:
		if x not in sol:
			m.append(x)
	return m
#regresa todo los numero primos menores a 10000
def primos(num):
	lp = []
	for x in range(1,num):
		for y in range(2,x):
				if (x%y==0):
					break#no se ejecula el else
		else: lp.append(x)
	return lp
#regresa los impares compuestos menores a 10000
def imparCompuesto(compuestos):		
	ic=[]
	for e in compuestos:
		if(e%2!=0):
			ic.append(e)
	return ic
#regresa todo los numeros compuetos menor a 10000
def compuestos(num):
	c =[]
	for x in range(1,num):
		for y in range(2,x):
				if (x%y==0):
					c.append(x)
					break#no se ejecula el else
	return c
#regresa el menor impar compuesto que no esta en el conjunto de impares compuestos dados por la suma.
def menor(resultados):
	m = sorted(resultados)	
	return m[0]


compuestos = compuestos(2000)
primos = primos(2000)
imparcompuesto = imparCompuesto(compuestos)
suma = suma(imparcompuesto,primos)
conjuntosol = conjuntoSol(imparcompuesto,suma)
resultados = goldbach(imparcompuesto,conjuntosol)
print(menor(resultados))
