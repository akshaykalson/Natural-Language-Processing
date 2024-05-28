import spacy

#the worksheet link = https://spacy.pythonhumanities.com/01_02_linguistic_annotations.html
# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Read the text file with the appropriate encoding
with open('resources/USA.txt', 'r', encoding='utf-8') as f:
    text = f.read()   #this will create a text object

# print(text)

doc = nlp(text)  #a doc object is created

print(doc) #when we print doc object , the output is similar but actually it is not same
print(len(text))
print(len(doc))

for token in text[:10]:
    print(token)


for token1 in doc[:10]:
    print(token1)

#we can notice the difference here, when we print first 10 tokens of both objects, we get 10 letters in first case, but we get 10 words
#in second case, this means that doc object is creating tokens out of raw text

for sent in doc.sents:
    print(sent)

sentence1 = doc.sents[0]
print(sentence1)
#if we try to do this, it will create error, because doc object is a generator. it is not iterateable

sentence1 = list(doc.sents)[0]
print(sentence1)

token2= sentence1[12]
print('Token 2 is', token2)

#these below statements will provide us with metadata of tokens
print(token2.right_edge)
print(token2.text)
print(token2.left_edge)
print(token2.ent_type_) #tells the type of entity this word belongs to
print(token2.ent_iob_) #gives information I=inside a larger token/entity, o= outside, b= beginning
print(token2.lemma_) # this will show the lamentized form of this token
print(token2.morph) #this will print morphological analysis of this word
print(token2.pos_) #this will print part of speech, will tell you what kind of word it is

