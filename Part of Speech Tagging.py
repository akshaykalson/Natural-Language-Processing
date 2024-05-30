import spacy
from spacy import displacy
# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Read the text file with the appropriate encoding
with open('resources/USA.txt', 'r', encoding='utf-8') as f:
    text = f.read()   #this will create a text object

doc = nlp(text)  #a doc object is created

sentence1 = list(doc.sents)[0]
print(sentence1)

token= sentence1[12]
print('Token is', token)

text1 = "Mike enjoys playing football"
doc2 = nlp(text1)
for token1 in doc2:
    print(token1.text, token1.pos_, token1.dep_)

# Render and save the visualization to a file
html = displacy.render(doc, style='dep', page=True)
with open("dependency_parse.html", "w", encoding="utf-8") as file:
    file.write(html)

print("Visualization saved as dependency_parse.html")

