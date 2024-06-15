import re
import spacy
from spacy.tokens import Span
from spacy.language import Language
from spacy.util import filter_spans

text = "Paul Newman was an American actor, but Paul Hollywood is a British TV Host. The name Paul is quite common."

pattern = r"Paul [A-Z]\w+"

matches = re.finditer(pattern, text)

for match in matches:
    print(match)

nlp = spacy.blank('en')
doc = nlp(text)

# This is how we can inject entities into our doc objects by using regex-based matching
@Language.component('paul_ner')
def paul_ner(doc):
    original_ents = list(doc.ents)
    pattern = r"Paul [A-Z]\w+"
    mwt_ents = []

    for match in re.finditer(pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        if span is not None:
            mwt_ents.append((span.start, span.end, span.text))

    for ent in mwt_ents:
        start, end, name = ent
        par_ent = Span(doc, start, end, label='PERSON')  # We have labelled these regex matched entities as persons
        original_ents.append(par_ent)

    doc.ents = original_ents
    return doc

nlp2 = spacy.blank('en')
nlp2.add_pipe('paul_ner')

doc2 = nlp2(text)
print([(ent.text, ent.label_) for ent in doc2.ents])

@Language.component('cinema_ner')
def cinema_ner(doc):
    original_ents = list(doc.ents)
    pattern = r"Hollywood"
    mwt_ents = []

    for match in re.finditer(pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        if span is not None:
            mwt_ents.append((span.start, span.end, span.text))

    for ent in mwt_ents:
        start, end, name = ent
        par_ent = Span(doc, start, end, label='Cinema')  # We have labelled these regex matched entities as persons
        original_ents.append(par_ent)

    filtered = filter_spans(original_ents)
    doc.ents = filtered
    return doc

nlp3 = spacy.load('en_core_web_sm')
nlp3.add_pipe('cinema_ner')

doc3 = nlp3(text)

for ent in doc3.ents:
    print(ent.text, ent.label_)
