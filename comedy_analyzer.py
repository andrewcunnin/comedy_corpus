import nltk;
import comedy_corpus;
from nltk.corpus import stopwords

stops = stopwords.words()

men_ns = []
white_men_ns = []
non_white_men_ns = []
white_men_transcripts = [text for text in comedy_corpus.white_men]
non_white_men_transcripts = [text for text in comedy_corpus.non_white_men]

for transcript in white_men_transcripts:
	for word in transcript:
		if(word not in stops):
			white_men_ns.append(word.lower())
			men_ns.append(word.lower())

for transcript in non_white_men_transcripts:
	for word in transcript:
		if(word.lower() not in stops):
			non_white_men_ns.append(word.lower())
			men_ns.append(word.lower())

white_men_fdist = nltk.FreqDist(white_men_ns)
non_white_men_fdist = nltk.FreqDist(non_white_men_ns)
print(white_men_fdist["dick"]/len(white_men_ns))
print(non_white_men_fdist["dick"]/len(non_white_men_ns))
men_fdist = nltk.FreqDist(men_ns)


