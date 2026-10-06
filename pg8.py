from collections import Counter

# Training sentences
sentence = [
    "I study NLP",
    "I study Python",
    "I like NLP"
]

# Convert all text to lowercase and split into words
words = " ".join(sentence).lower().split()

# Count each word
word_count = Counter(words)

# Total number of words
total_words = len(words)

# Calculate unigram probabilities
unigram_prob = {}

for word, count in word_count.items():
    unigram_prob[word] = count / total_words

# Display unigram probabilities
print("Unigram Probability")
print("-------------------")

for word, prob in unigram_prob.items():
    print(f"{word}: {prob:.4f}")

# Calculate probability of each sentence
print("\nProbability of the Sentences")
print("----------------------------")

for s in sentence:

    words_in_sentence = s.lower().split()

    prob = 1.0

    for word in words_in_sentence:
        prob *= unigram_prob[word]

    print(f"'{s}': {prob:.8f}")