import urllib
import string

zipcode = '02492'

# url = 'http://uszip.com/zip/' + zipcode
# conn = urllib.urlopen(url)

def prompt_zip():
	a = input('inserte el codigo zip')
	return str(a)

def connect():
	url = 'http://listado.mercadolibre.com.ve/camara#D[A:camara]'
	conn = urllib.urlopen(url)
	data = dict()
	db = open('merca.txt', 'w')

	for line in conn.fp:
	    line = line.strip(string.punctuation + string.whitespace + '')
	    db.write(line)
	

	conn.close()

connect()

# def process_line(line, hist):
#     """Adds the words in the line to the histogram.

#     Modifies hist.

#     line: string
#     hist: histogram (map from word to frequency)
#     """
#     # replace hyphens with spaces before splitting
#     line = line.replace('-', ' ')
    
#     for word in line.split():
#         # remove punctuation and convert to lowercase
#         word = word.strip(string.punctuation + string.whitespace)
#         word = word.lower()

#         # update the histogram
#         hist[word] = hist.get(word, 0) + 1

