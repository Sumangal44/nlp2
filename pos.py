# perform pos tagging any text data
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

text="The student is studying in the library."

word=nltk.word_tokenize(text)
pos_tag=nltk.pos_tag(word)

print("original text",text )

print("pos tagging",pos_tag)


# """
# NN
# NNS
# VB
# VBG
# VBP
# JJ
# RB
# DT
# PRP
# IN
# CC
# VBD
# NNP    
# """