import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt_tab")
nltk.download("stopwords")
text = "Natural Language Processing is a branch of Artificial Intelligence"
tokens = word_tokenize(text)
print("original text:")
print(text)
stop_words = set(stopwords.words("english"))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

print("\nFiltered Tokens:")
print(filtered_tokens)
