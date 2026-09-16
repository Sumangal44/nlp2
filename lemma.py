import spacy
nlp=spacy.load("en_core_web_sm")
text="The cats were running much faster than the dogs"
#process the text
doc=nlp(text)
#extract the base lemma for each word
lemmatized_words=[token.lemma_ for token in doc]
print("original text:",text)
print("Lemmatized:"," ".join(lemmatized_words))

