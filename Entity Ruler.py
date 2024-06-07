import spacy

nlp = spacy.load('en_core_web_sm')

text = "West cherstertenfieldville was referenced in Mr. Deeds."

#west cherstertenfieldville will be incorrectly recognized here, we wanna manually add this entity to our model
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)

ruler = nlp.add_pipe('entity_ruler')

print(nlp.analyze_pipes())

patterns= [{'label': 'GPE', 'pattern': 'West cherstertenfieldville'}]

ruler.add_patterns(patterns)

doc2 = nlp(text)

for ent in doc2.ents:
    print(ent.text, ent.label_)

nlp2 = spacy.load('en_core_web_sm')
ruler1 = nlp2.add_pipe('entity_ruler', before = 'ner')

ruler1.add_patterns(patterns)

doc3= nlp2(text)

for ent in doc3.ents:
    print(ent.text, ent.label_)

nlp3 = spacy.load('en_core_web_sm')

ruler = nlp3. add_pipe('entity_ruler', before = 'ner')

patterns= [{'label': 'GPE', 'pattern': 'West cherstertenfieldville'},
           {'label': 'film', 'pattern': 'Mr. Deeds'}
           ]

ruler.add_patterns(patterns)

doc4 = nlp3(text)

for ent in doc4.ents:
    print(ent.text, ent.label_)









