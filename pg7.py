# find synonims and antonyms word("active") using wordnet

from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')
word = "active"
synonyms = set()
antonyms = set()

for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        synonyms.add(lemma.name())
if lemma.antonyms():
    for antonym in lemma.antonyms():
        antonyms.add(antonym.name())

print("word:", word)
print("Synonyms:")
for syn in sorted(synonyms):
    print(syn)
print("Antonyms:")
for ant in sorted(antonyms):    
    print(ant)    

