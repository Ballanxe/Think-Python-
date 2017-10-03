import string 



def open_file(file,n,n1=0):
	""" file =  nombre del archivo que se va a abrir
		n = cantidad de lineas que voy a omitir
		n1 = numero de lineas que deseo imprimir"""
	fin = open(file)
	book_lines = []
	count = 0
	for line in fin:
		word = line.strip()
		count += 1
		if count > n:
			book_lines.append(word)
	return book_lines

	
a = open_file('war.txt',190)

def dividir(l):
	""" extrae las palabras de una lista de oraciones 
	l = list """

	a = []
	for i in range(len(l)):
		a += l[i].split(' ')
	return a[:100]

b = dividir(a)
# print b

words = ['Yo,','Somos:', 'Especial!','creamos(','nose', 'Alberto']

def sucia(l,m):
	if l not in m:
		return True

def clean(l):
	lista = []
	for word in l:
 		for simbol in string.punctuation:
			if sucia(simbol,word):
				lista.append(word)

	print lista


def limpiador(l):
	cleaned = []
	clean = []

 	for word in l:
 		for simbol in string.punctuation:
			if simbol in word: 
				clean_word = word.replace(simbol, "")			
				cleaned.append(clean_word)
	print cleaned
		
			

print clean(words)



	


# l = [ 'Hola yo me llamo Alberto', 'Tengo mucha hambre', 'Quiero ser feliz', 'Hola yo me llamo Pedro']
# delimiters = ['\n', ' ', ',', '.', '?', '!', ':', 'and_what_else_you_need']





# f = open_file('war.txt',190,5)
# print f


# def words(l):
# 	words = dict()
# 	for i in l:



# def histogram(s):
# 	d = dict()
# 	for c in s:
# 		if c not in d:
# 			d[c] = 1
# 		else:
# 		d[c] += 1
# 	return d







