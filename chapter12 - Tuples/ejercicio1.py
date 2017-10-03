def sum_all(*arg):
	l = list(arg)
	print sum(l)

sum_all(1,3,4,20,30,200)

def sum_all(*arg):
	x = 0
	for i in range(len(arg)):
		x += arg[i]
	return x

#recorriendo un diccionario

for key, val in d.items():
	print val, key

#recorriendo una secuencia

for index, element in enumerate('abcde'):
	print index, element

#recorriendo una tupla 

for letter, number in t:
	print number, letter

def most_frequent(s):
	def letter(s):
		for i in s:
			if 

hola = dict(nombre='Alberto', apellido='Rincones', edad=28)

def make_tuple(dicc,lista=[]):

    for key, val in dicc.items():
        lista == lista.append([key,val])
    return lista

print make_tuple(hola)