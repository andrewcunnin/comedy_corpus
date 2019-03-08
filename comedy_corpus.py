import nltk;
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import re;

corpus_root = "comedy-corpora"

# filename is <name>_<title>_<year>_<ww or nw>_<mm or nm>.txt
# words in file names separated by '%20' instead of spaces
# fields separated by '_'
# ww: white, nw: non-white, mm: male, nm: non-male

class ComedyCorpus:
	name = ""
	fileid = ""
	text = ""

	def __init__(self, name="", fileid="", text=""):
		self.name = name;
		self.fileid = fileid;
		self.text = text;

	def set_name(self, name): #sets corpus display name
		self.name = name;
	
	def set_fileid(self, fileid): #sets fileid
		self.fileid = fileid;
	
	def set_text(self, text): #sets text field
		self.text = text;

	def __str__(self): # defines the string representation of a text object, so that it prints as "<[name]>"
		return ("<" + self.name + ">")

	def __getitem__(self, key): #allows user to index corpora as they would text
		return self.text[key];

	def __iter__(self): #allows user to iterate through tokens of text
		yield from corpus_tokenize(self.text)

def corpus_tokenize(text): #defines a text token     
	return re.compile(r"[ .?!;:'\",\[\]{}()]*\s*").split(text)

def load_corpus(race_code=None, gender_code=None): #loads corpora into an array based on race and gender

	if(race_code == None): # if none is specified, search all
		race_code = ".." 
	if(gender_code == None):
		gender_code = ".."

	reader = PlaintextCorpusReader(corpus_root, ".*_"+race_code+"-"+gender_code+"\.txt") # uses filename encoding to load specified texts
	corpora = []

	for fileid in reader.fileids(): #creates ComedyCorpus object, populates with fileid and name
		new_corpus = ComedyCorpus()
		new_corpus.set_fileid(fileid)
		new_corpus.set_text(reader.raw(fileid)) #gets word content based on fileid
		fileid = re.sub("_"+race_code+"-"+gender_code+"\.txt", "", fileid); #name is fileid without encoding
		fileid = fileid.replace("-", " ")
		fileid = fileid.replace("_", "; ")
		new_corpus.set_name(fileid)
		corpora.append(new_corpus)

	return corpora;

def list_transcripts(texts):
	for text in texts:
		print(str(text))

def list_corpora():
	print("all_comedy")
	print("non_white_men")
	print("non_white_non_men")
	print("white_men")
	print("white_non_men")
	print("all_non_white")
	print("all_white")
	print("all_men")
	print("all_non_men")



print("loading Comedy Corpora")

print("loading all_comedy")
all_comedy = load_corpus()

print("loading non_white_men")
non_white_men = load_corpus(race_code = "nw", gender_code = "mm")
print("loading non_white_non_men")
non_white_non_men = load_corpus(race_code = "nw", gender_code = "nm")

print("loading white_men")
white_men = load_corpus(race_code = "ww", gender_code = "mm")
print("loading white_non_men")
white_non_men = load_corpus(race_code = "ww", gender_code = "nm")

print("loading all_non_white")
all_non_white = load_corpus("nw", None)
print("loading all_white")
all_white = load_corpus("ww", None)
print("loading all_men")
all_men = load_corpus(None, "mm")
print("loading all_non_men")
all_non_men = load_corpus(None, "nm")

print("use list_transcripts(<array name>) to see a list of which transcripts are within each group")
print("use list_corpora() to see a list of pre-existing categories of comedians")
print("access text of corpora object using <object>.text")




