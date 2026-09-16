import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('punkt')
#input text
text="The students are studying and playing games."
#tokenization
words=word_tokenize(text)
#create stemming 
stemmer=PorterStemmer()
#perform stemming
stemmed_words=[stemmer.stem(word)for word in words]
#display results
print("original words:")
print(words)
print("\n After stemming:")
print(stemmed_words)