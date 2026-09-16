import nltk 
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
nltk.download('wordnet')
#input text
text="The student are studying and playing games."
#tokenization
words=word_tokenize(text)
#create lemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer_words=[lemmatizer.lemmatize(word)for word in words]
#display result
print("original text:",text)
print("Lemmatized:"," ".join(lemmatizer_words))
