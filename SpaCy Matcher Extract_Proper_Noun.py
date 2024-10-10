import spacy
from spacy.matcher import Matcher

with open('resources/USA.txt', 'r') as f:
    text = f.read()

# print(text)

nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)
pattern = [{'POS': 'PROPN', 'OP': '+'}]    #it will pick up part of speech that is proper noun, and it will take biggest length proper noun

matcher.add('PROPER_NOUN', [pattern], greedy = 'LONGEST' )    #it will pick up pattern from the above list, and assign it key : PROPER_NOUN

doc = nlp(text)

matches = matcher(doc)

print(len(matches))

for match in matches[:10]:                       #this will print out first 10 matches
    print(match, doc[match[1]:match[2]])


