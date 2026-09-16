# demonstrate word embedding using word2vec
from gensim.models import Word2Vec

sentences = [
    ["The", 'cat', 'is', 'sitting', 'on', 'the', 'mat'],
    ["The", 'dog', 'is', 'playing', 'with', 'the', 'ball'],
    ["The", 'bird', 'is', 'flying', 'in', 'the', 'sky'],
    ["The", 'fish', 'is', 'swimming', 'in', 'the', 'water'],
    ["The", 'child', 'is', 'playing', 'in', 'the', 'park']
]
model = Word2Vec(sentences,vector_size=50, window=2, min_count=1,workers=4)
print("original text", sentences)
print("word embedding cat", model.wv['cat'])

print("word similar to cat", model.wv.most_similar('cat',topn=3)) 




