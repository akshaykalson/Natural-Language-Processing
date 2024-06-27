import spacy
from spacy.matcher import Matcher

#in this file, our main task is to identify the quotations, and then determine who is speaking or thinking that particular quotation

with open('resources/alice_in_wonderland.txt', 'r') as f:
    text = f.read()

text = text.replace('`', "'")

# print(text)

nlp = spacy.load('en_core_web_sm')

speak_lemmas = ['think', 'say']


matcher = Matcher(nlp.vocab)
pattern = [{"ORTH": "'"},
           {"IS_ALPHA": True, "OP": "+"},
           {"IS_PUNCT": True, "OP":"*"},
           {"ORTH": "'"},
           {"POS":"VERB", "LEMMA": {"IN":speak_lemmas}},
           {"POS": "PROPN", "OP": "+"}
           ]   #this is a pattern that we have created here to extract quotations out of our text data

#It will pick up parts of the text where, the sentence starts with a quotation mark, has alpha word like 'is' and then also has punctuation ',' and then quotation mark closed

matcher.add('Quoted', [pattern], greedy = 'LONGEST' )    #it will pick up pattern from the above list, and assign it key : PROPER_NOUN

doc = nlp(text)

matches = matcher(doc)

for match in matches[:100]:
    print(match, doc[match[1]:match[2]])

