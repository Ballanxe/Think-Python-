
def traverse(string):
	a = len(string)
	index = -1
	while abs(index) < a + 1:
		print string[index],
		index = index - 1

traverse("alberto") 
	
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
	if letter == 'O' or letter == 'Q':
		print letter + 'u' + suffix
		continue
	print letter + suffix

fruit = 'banana'
print fruit[3:3]
	
def find(word,letter,ind):
	index = ind
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1

print find("alberto","a",4)

def counter(word,let):
	count = 0
	for letter in word:
		if letter == let:
			count = count + 1
	print count 

counter("finguirikiki",'i')

def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

 

def is_palindrome(word):
	if word[::-1] == word[0::]:
		return True

print is_palindrome("reconocer")

def any_lowercase4(s):
	flag = False
	for c in s:
		flag = flag or c.islower()
	return flag

print any_lowercase4("CHIRIMOLLA")

def rotate_word(word,num):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for c in word:
		c.

