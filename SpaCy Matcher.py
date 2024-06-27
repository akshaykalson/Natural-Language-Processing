import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Create a Matcher object
matcher = Matcher(nlp.vocab)

# Define the pattern for matching email addresses
pattern = [{'LIKE_EMAIL': True}]
matcher.add('EMAIL_ADDRESS', [pattern])

# Process the text
doc = nlp('This is an email address: wmattingly@aol.com')

# Find matches in the text
matches = matcher(doc)

# # Add matched spans to doc.ents
# new_ents = [Span(doc, start, end, label='EMAIL_ADDRESS') for match_id, start, end in matches]
# doc.ents = list(doc.ents) + new_ents
#
# # Print the entity labels
# for ent in doc.ents:
#     print(ent.text, ent.label_)

# Print the matches
print(matches)

# Print the text of the matched pattern
print(nlp.vocab[matches[0][0]].text)
