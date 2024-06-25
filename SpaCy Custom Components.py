import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("Britain is a place. Mary is a doctor")

for ent in doc.ents:
    print(ent.text, ent.label_)

'''in this code, our goal is to remove all entities flagged as GPE, or flag them as any other label
we do this by the means of custom components in SpaCy'''

from spacy.language import Language

@Language.component('remove_gpe')
def remove_gpe(doc):
    original_ents = list(doc.ents)
    for ent in doc.ents:
        if ent.label_ == 'GPE':
            original_ents.remove(ent)

    doc.ents = original_ents
    return (doc)

nlp.add_pipe('remove_gpe')
#print(nlp.analyze_pipes())

doc = nlp("Britain is a place. Mary is a doctor")

for ent in doc.ents:
    print(ent.text, ent.label_)

# we have added a custom pipe to our pipeline, which deletes entities that are marked as GPE

