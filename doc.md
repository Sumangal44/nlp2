
### Line 2

```python
import nltk
```

Imports the **NLTK (Natural Language Toolkit)** library.

NLTK is used for Natural Language Processing tasks in Python.

---

### Line 3

```python
from nltk.corpus import wordnet
```

Imports **WordNet** from the NLTK corpus.

WordNet is a lexical database of English words containing relationships such as:

* Synonyms
* Antonyms
* Different meanings
* Word relationships

---

### Line 4

```python
nltk.download('wordnet')
```

Downloads the **WordNet dataset**.

We need this dataset before we can use:

```python
wordnet.synsets()
```

---

### Line 5

```python
word = "active"
```

Stores the input word in the variable `word`.

Here the word is:

```text
active
```

You can change it to another word, for example:

```python
word = "happy"
```

---

### Line 6

```python
synonyms = set()
```

Creates an empty **set** to store synonyms.

A set is used because the same synonym may appear multiple times, and a set automatically removes duplicates.

---

### Line 7

```python
antonyms = set()
```

Creates an empty set to store antonyms.

---

### Line 8

```python
for syn in wordnet.synsets(word):
```

This is the main loop.

`wordnet.synsets(word)` finds all the different **meanings/synsets** of the word.

For example:

```python
wordnet.synsets("active")
```

may return several meanings of `"active"`.

The variable `syn` represents one synset at a time.

---

### Line 9

```python
for lemma in syn.lemmas():
```

This loop gets all the **lemmas** contained in the current synset.

A lemma represents a word associated with a particular meaning.

So the program checks every word related to each meaning.

---

### Line 10

```python
synonyms.add(lemma.name())
```

Gets the name of the current lemma and adds it to the `synonyms` set.

For example:

```python
lemma.name()
```

might return:

```text
active
```

The word is then stored in:

```python
synonyms
```

---

### Line 11

```python
if lemma.antonyms():
```

Checks whether the current lemma has an antonym in WordNet.

If an antonym exists, the condition becomes `True`.

If there is no antonym, it becomes `False`.

---

### Line 12

```python
for antonym in lemma.antonyms():
```

If an antonym exists, this loop goes through each antonym.

The variable `antonym` represents one antonym.

---

### Line 13

```python
antonyms.add(antonym.name())
```

Gets the name of the antonym and stores it in the `antonyms` set.

For example:

```text
inactive
```

may be added.

---

### Line 14

```python
print("Word:", word)
```

Displays the original word.

Output:

```text
Word: active
```

---

### Line 15

```python
print("\nSynonyms:")
```

Displays the heading **Synonyms**.

`\n` creates a new line before the heading.

---

### Line 16

```python
for syn in sorted(synonyms):
```

Sorts all synonyms alphabetically and loops through them one by one.

`sorted()` makes the output easier to read.

---

### Line 17

```python
print(syn)
```

Prints each synonym.

---

### Line 18

```python
print("\nAntonyms:")
```

Displays the heading **Antonyms**.

---

### Line 19

```python
for ant in sorted(antonyms):
```

Sorts the antonyms alphabetically and loops through them.

---

### Line 20

```python
print(ant)
```

Prints each antonym.

---

