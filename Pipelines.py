import spacy
import numpy as np
#activate virtual environment first using terminal

'''in this file, we are going to load a blank model, and add just sentencizer to it. This was , we are only including the functionalities that
we require, so that the usage is faster'''


with open('resources/USA.txt', 'r') as f:
    text = f.read()

nlp = spacy.blank('en')
nlp.add_pipe('sentencizer')

doc = nlp(text)
sentence1 = list(doc.sents)[0]

print(sentence1)
print(nlp.analyze_pipes())



