# def find_diccio(word, diccio=dict()):
	
# 	def open_dic():
# 		file = open('words.txt')
# 		for line in file:
# 			word = line.strip()
# 			diccio[word] = ''
# 		return diccio
	
# 	open_dic()
# 	if word in diccio:
# 		return True
# 	else:
# 		return False

# print find_diccio('raul')

def histogram(s):
	d = dict()
	for letter in s:
		d[letter] = 1 + d.get(letter, 0)
	return d

h = histogram('fongorokikiki')

def print_hist(h):
	for key in sorted(h.keys()):
		print key, h[key]

print print_hist(h)

def reverse_lookup(d,v):
	li = []
	for key in d:
		if d[key] == v:
			li.append(key)
	return li

	raise ValueError

print reverse_lookup(h,1)

def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse

print invert_dict(h)