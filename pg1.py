import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt_tab")
text = "Natural Language Processing is a branch of Artificial Intelligence ."
tokens = word_tokenize(text)
print("original text:")
print(text)
print("\nTokens:")
print(tokens)
