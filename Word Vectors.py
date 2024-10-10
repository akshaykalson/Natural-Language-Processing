import spacy
import numpy as np
#activate virtual environment first using terminal

nlp = spacy.load('en_core_web_md')
#this time we are working with medium text model, this model has word vectors , the earlier small model did'nt have this functionality
with open('resources/USA.txt', 'r') as f:
    text = f.read()

doc = nlp(text)
sentence1 = list(doc.sents)[0]

# print(sentence1)

your_word = "dog"

ms = nlp.vocab.vectors.most_similar(
    np.asarray([nlp.vocab.vectors[nlp.vocab.strings[your_word]]]), n=10)
words = [nlp.vocab.strings[w] for w in ms[0][0]]
distances = ms[2]
print(words)

doc1 = nlp('I like salty fries and hamburgers.')
doc2 = nlp('Fast food tastes very good')

print(doc1, '<->', doc2, doc1.similarity(doc2))

french_fries = doc1[2:4]
burgers = doc1[5]
print(french_fries, '<->', burgers, french_fries.similarity(burgers))







