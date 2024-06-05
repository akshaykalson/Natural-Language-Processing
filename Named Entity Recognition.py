import spacy

'''
Named entity is a part of information extraction from text.
'''

from spacy import displacy

nlp = spacy.load('en_core_web_sm')

# Read the text file with the appropriate encoding
with open('resources/USA.txt', 'r', encoding='utf-8') as f:
    text = f.read()

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)   # it will tell us what each entity inside doc exactly classified as

#current model we're using is a small model, its gonna make mistakes while classifying the entities

# Render and save the visualization to a file
html = displacy.render(doc, style='ent', page=True)
with open("named_entity_recognition.html", "w", encoding="utf-8") as file:
    file.write(html)

print("Visualization saved as named_entity_recognition.html")
