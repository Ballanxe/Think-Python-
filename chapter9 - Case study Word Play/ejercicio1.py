fin = open('words.txt')
line = fin.readline()
word = line.strip()

def read(n):
	for line in fin:
		word = line.strip()
		if n in word:
			continue
		 print word

read('a')

def has_no_e(word):
	for letter in word: 
		if letter == 'e':   
			return False
	return True

def avoids(word,forbidden):
	for letter in word: 
		if letter in forbidden:
			return False 
	return True 
 
def read_no_e():
	for line in fin:
		word = line.strip()


def uses_only(word,available):
	for letter in word:
		if letter not in available:
			return False 
	return True    

def uses_all(word,required):
	for letter in required: 
		if letter not in word: 
			return False
	return True 

# Loops con indices

def is_abecedarian(word):
	previous = word[0]
	for c in word:
		if c < previous:
			return False
		previous = c
	return True 

def is_abecedarian2(word):
	if len(w ord) <= 1:
		return True
	if word[0] > word[1]:
		return False
	return is_abecedarian2(word[1:])

def is_abecedarian(word):
	i = 0 
	while i < len(word) -1:
		if word[i+1] < word[i]:
			return False 
		i = i + 1
 